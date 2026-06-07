#!/usr/bin/env python
# coding: utf-8

# ## Notebook_1
# 
# null

# In[1]:


get_ipython().system('pip install azure-eventhub')


# In[2]:


import json
import random
import time
import uuid
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# ==========================================
# CONFIGURATION: BENGALURU TRAFFIC STREAM
# ==========================================
EVENTSTREAM_CONNECTION_STRING = "Endpoint=sb://esehusw38mwt4mbbodn74e3e.servicebus.windows.net/;SharedAccessKeyName=key_2cbd47b2-ebec-4df0-90bd-b0069d108a7c;SharedAccessKey=i7n4NVQZJMIFNeJk7U/uaAl23l34XceKg+AEhO0UyKY="
EVENTSTREAM_HUB_NAME = "esehusw38mwt4mbbodn74e3e_eh"


# In[6]:


# =========================================================================
# 15 BENGALURU JUNCTIONS WITH DETAILED REALISTIC PROFILES
# =========================================================================
BENGALURU_JUNCTIONS = {
    "Silk Board Junction": {
        "lat": 12.9176, "lon": 77.6244, "base_wait_sec": 180, "max_speed_limit": 30, "bus_ratio": 0.04
    },
    "Hebbal Flyover": {
        "lat": 13.0359, "lon": 77.5978, "base_wait_sec": 120, "max_speed_limit": 45, "bus_ratio": 0.03
    },
    "Sony World Junction": {
        "lat": 12.9348, "lon": 77.6322, "base_wait_sec": 110, "max_speed_limit": 35, "bus_ratio": 0.02
    },
    "Tin Factory": {
        "lat": 12.9961, "lon": 77.6755, "base_wait_sec": 200, "max_speed_limit": 25, "bus_ratio": 0.08
    },
    "Town Hall": {
        "lat": 12.9642, "lon": 77.5816, "base_wait_sec": 140, "max_speed_limit": 30, "bus_ratio": 0.06
    },
    "Marathahalli Bridge": {
        "lat": 12.9524, "lon": 77.6974, "base_wait_sec": 130, "max_speed_limit": 40, "bus_ratio": 0.04
    },
    "Goraguntepalya Junction": {
        "lat": 13.0289, "lon": 77.5398, "base_wait_sec": 160, "max_speed_limit": 30, "bus_ratio": 0.03
    },
    "Dairy Circle Junction": {
        "lat": 12.9429, "lon": 77.5975, "base_wait_sec": 115, "max_speed_limit": 35, "bus_ratio": 0.05
    },
    "JP Nagar 6th Phase": {
        "lat": 12.9105, "lon": 77.5857, "base_wait_sec": 100, "max_speed_limit": 35, "bus_ratio": 0.03
    },
    "Kengeri Metro Station": {
        "lat": 12.9082, "lon": 77.4764, "base_wait_sec": 90,  "max_speed_limit": 45, "bus_ratio": 0.07
    },
    "RR Nagar Arch": {
        "lat": 12.9352, "lon": 77.5137, "base_wait_sec": 110, "max_speed_limit": 35, "bus_ratio": 0.04
    },
    "Rajajinagar 10th Cross": {
        "lat": 12.9892, "lon": 77.5532, "base_wait_sec": 130, "max_speed_limit": 30, "bus_ratio": 0.03
    },
    "Yeshwanthpur Metro": {
        "lat": 13.0236, "lon": 77.5501, "base_wait_sec": 150, "max_speed_limit": 35, "bus_ratio": 0.05
    },
    "Majestic (KBS)": {
        "lat": 12.9774, "lon": 77.5729, "base_wait_sec": 180, "max_speed_limit": 25, "bus_ratio": 0.18
    },
    "Electronic City Toll": {
        "lat": 12.8488, "lon": 77.6601, "base_wait_sec": 95,  "max_speed_limit": 50, "bus_ratio": 0.04
    }
}


# In[7]:


def get_traffic_severity(hour):
    """
    Returns (traffic_multiplier, rush_hour_flag)
    """
    if 8 <= hour <= 11:      # Morning Peak
        return random.uniform(2.2, 3.2), True
    elif 17 <= hour <= 21:   # Evening Peak
        return random.uniform(2.5, 3.5), True
    elif 0 <= hour <= 5:     # Late Night Empty roads
        return random.uniform(0.2, 0.4), False
    else:                    # Normal daytime congestion
        return random.uniform(1.0, 1.6), False

def generate_traffic_telemetry():
    now = datetime.now()
    hour = now.hour
    multiplier, is_rush_hour = get_traffic_severity(hour)
    
    events = []
    
    for area, specs in BENGALURU_JUNCTIONS.items():
        # 1. Calculate realistic slow speeds
        max_speed = specs["max_speed_limit"]
        
        if is_rush_hour:
            # Drop speeds to bumper-to-bumper levels during rush hour
            avg_speed = round(random.uniform(3.5, 11.5), 1)
        else:
            # Off-peak speeds
            avg_speed = round(max(8.0, random.uniform(0.4, 0.8) * max_speed / multiplier), 1)
            
        avg_speed = min(avg_speed, max_speed)
        
        # 2. Calculate Signal Wait Times
        signal_wait_time = min(300, round(specs["base_wait_sec"] * multiplier + random.uniform(-10, 20), 0))
        signal_wait_time = max(15, int(signal_wait_time))
        
        # 3. Calculate Congestion Index
        speed_factor = (1.0 - (avg_speed / max_speed)) * 50
        wait_factor = (signal_wait_time / 300.0) * 50
        congestion_index = min(100.0, round(speed_factor + wait_factor, 1))
        
        # 4. Total dynamic vehicle rate passing per minute
        vehicles_per_min = round(random.uniform(40, 120) * multiplier, 0)
        vehicles_per_min = max(10, int(vehicles_per_min))
        
        # 5. Vehicle Breakdown distribution
        bus_percentage = specs["bus_ratio"]
        remaining_ratio = 1.0 - bus_percentage
        
        vehicle_breakdown = {
            "Two_Wheeler": round(vehicles_per_min * remaining_ratio * random.uniform(0.50, 0.60)),
            "Auto_Rickshaw": round(vehicles_per_min * remaining_ratio * random.uniform(0.18, 0.25)),
            "Cab_Sedan": round(vehicles_per_min * remaining_ratio * random.uniform(0.12, 0.18)),
            "BMTC_Bus": round(vehicles_per_min * bus_percentage),
            "Truck_Delivery": round(vehicles_per_min * remaining_ratio * random.uniform(0.02, 0.06))
        }
        
        event = {
            "timestamp": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event_id": str(uuid.uuid4()),
            "area": area,
            "latitude": specs["lat"],
            "longitude": specs["lon"],
            "avg_speed_kmh": avg_speed,
            "signal_wait_time_sec": int(signal_wait_time),
            "vehicles_passing_per_min": int(vehicles_per_min),
            "congestion_index": congestion_index,
            "vehicle_mix": vehicle_breakdown
        }
        events.append(event)
        
    return events

def start_simulation():
    print(f"🔄 Starting Bengaluru Traffic Simulator... Connecting to Event Stream...")
    
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENTSTREAM_CONNECTION_STRING, 
            eventhub_name=EVENTSTREAM_HUB_NAME
        )
        print("✅ Successfully initialized Event Hub connection.")
    except Exception as e:
        print(f"❌ Error setting up Event Hub: {e}")
        return

    try:
        while True:
            telemetry_batch = generate_traffic_telemetry()
            
            # Send batch of events
            event_data_batch = producer.create_batch()
            for record in telemetry_batch:
                event_data_batch.add(EventData(json.dumps(record)))
                
            producer.send_batch(event_data_batch)
            print(f"📡 Sent telemetry update for {len(telemetry_batch)} locations at {datetime.now().strftime('%H:%M:%S')}")
            
            # Streams updates every 10 seconds
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n🛑 Simulator stopped by user.")
    finally:
        producer.close()

if __name__ == "__main__":
    start_simulation()


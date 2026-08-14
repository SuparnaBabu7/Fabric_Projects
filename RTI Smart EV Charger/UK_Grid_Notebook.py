#!/usr/bin/env python
# coding: utf-8

# ## UK_Grid_Notebook
# 
# null

# In[1]:


# Install the Azure Event Hubs client library to enable sending and receiving events
get_ipython().system('pip install azure-eventhub')


# In[2]:


# --- STEP 1: IMPORT REQUIRED LIBRARIES ---
import time
import json
import requests
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData


# In[3]:


# --- STEP 2: SET UP CREDENTIALS ---
CONNECTION_STR = "Endpoint=sb://esehusw3mzp7d113wjxzdsop.servicebus.windows.net/;SharedAccessKeyName=key_617ac804-c64b-46a6-827e-697e7a5c0ac4;SharedAccessKey=Usb+ihIvxsoTeRyvFaZqaoaO5mTC76qTC+AEhGrF1kY=;EntityPath=esehusw3mzp7d113wjxzdsop_eh"
EVENT_HUB_NAME = "esehusw3mzp7d113wjxzdsop_eh"


# In[4]:


# --- STEP 3: CREATE FUNCTION TO FETCH API DATA ---
def get_carbon_intensity():
    url = "https://api.carbonintensity.org.uk/intensity"
    headers = {'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()['data'][0]
            payload = {
                "timestamp": data['from'],
                "actual_intensity": data['intensity']['actual'],
                "forecast_intensity": data['intensity']['forecast'],
                "index_rating": data['intensity']['index'],
                "device_id": "EV_CHARGER_HOME_01",
                "simulated_charging_status": "IDLE"
            }
            return payload
    except Exception as e:
        print(f"Error fetching API: {e}")
        return None


# In[5]:


# --- STEP 4: CREATE FUNCTION TO STREAM TO FABRIC ---
def send_to_fabric_eventstream():
    client = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        eventhub_name=EVENT_HUB_NAME
    )
    
    print(" Starting live streaming to Fabric Eventstream...")
    
    with client:
        while True:
            payload = get_carbon_intensity()
            if payload:
                # Convert python dictionary to JSON string
                event_data = EventData(json.dumps(payload))
                
                # Create a batch and send
                event_batch = client.create_batch()
                event_batch.add(event_data)
                client.send_batch(event_batch)
                
                print(f"[{payload['timestamp']}] Successfully sent intensity: {payload['actual_intensity']} gCO2/kWh ({payload['index_rating']})")
            
            # Pause for 60 seconds before next fetch
            time.sleep(60)

# --- RUN THE STREAMER ---
send_to_fabric_eventstream()


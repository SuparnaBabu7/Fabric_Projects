# ⚡ Live Smart EV Charger Optimizer with Microsoft Fabric Real-Time Intelligence

A real-time **Smart EV Charger Optimizer** built using **Microsoft Fabric Real-Time Intelligence (RTI)** and the **UK National Grid Carbon Intensity API**.

The solution continuously monitors electricity-grid carbon intensity and simulates an intelligent EV charging decision:

* 🟢 **Low / Very Low Carbon Intensity** → Start Charging
* 🔴 **High / Very High Carbon Intensity** → Pause Charging

---

## 🏗️ Architecture

![Smart EV Charger Architecture](./smart%20ev%20charger.png)

### End-to-End Architecture Flow

```text
UK National Grid Carbon Intensity API
                │
                ▼
        Python Notebook
       UK_Grid_Notebook
                │
                ▼
       Fabric Eventstream
      es_green_ev_charger
                │
                ▼
        Fabric Eventhouse
         eh_green_ev_uk
                │
                ▼
              KQL
     Carbon Intensity Analysis
                │
                ▼
        Real-Time Alert
                │
        ┌───────┴────────┐
        ▼                ▼
 Low Carbon Intensity  High Carbon Intensity
        │                │
        ▼                ▼
 Start Charging      Pause Charging
        │                │
        └───────┬────────┘
                ▼
    Real-Time Intelligence
           Dashboard
                │
                ▼
       Teams Notifications
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate how **Microsoft Fabric Real-Time Intelligence** can be used to transform live external data into actionable business decisions.

The solution uses the **UK National Grid Carbon Intensity API** to retrieve electricity-grid carbon intensity in `gCO₂/kWh`.

When carbon intensity falls below the configured threshold of **100 gCO₂/kWh**, the system identifies the period as suitable for EV charging.

When carbon intensity becomes high, the system can trigger a notification to pause charging.

---

## 🔄 Solution Workflow

```text
Live API Data
     ↓
Python Data Ingestion
     ↓
Fabric Eventstream
     ↓
Fabric Eventhouse
     ↓
KQL Analysis
     ↓
Alert Rule
     ↓
Real-Time Decision
     ↓
Dashboard + Notification
```

---

## 🧩 Microsoft Fabric Components

| Component                  | Purpose                                                         |
| -------------------------- | --------------------------------------------------------------- |
| **Python Notebook**        | Retrieves data from the UK National Grid API and streams events |
| **Eventstream**            | Ingests real-time streaming data                                |
| **Eventhouse**             | Stores and analyzes incoming event data                         |
| **KQL**                    | Queries and filters carbon-intensity information                |
| **Real-Time Intelligence** | Provides monitoring and visualization                           |
| **Alerts**                 | Detects predefined carbon-intensity conditions                  |
| **Microsoft Teams**        | Receives real-time notifications                                |

---

## ⚙️ Decision Logic

The project uses a simple rule-based approach:

### 🟢 Start Charging

```text
Carbon Intensity < 100 gCO₂/kWh
                ↓
        Start Charging EV
```

### 🔴 Pause Charging

```text
High / Very High Carbon Intensity
                ↓
        Pause Charging EV
```

This demonstrates how streaming data can be converted into automated, real-time decisions.

---

## 🛠️ Technologies Used

* Microsoft Fabric
* Real-Time Intelligence
* Fabric Eventhouse
* Fabric Eventstream
* Python
* Kusto Query Language (KQL)
* UK National Grid Carbon Intensity API
* Real-Time Alerts
* Microsoft Teams

---

## 📁 Project Structure

```text
Fabric_Projects/
│
└── RTI Smart EV Charger/
    │
    ├── smart ev charger.png
    │
    └── README.md
```

> **Note:** The architecture image is referenced from the same project folder as this `README.md`.

---

## 🚀 Key Learning

This project demonstrates an important Real-Time Intelligence pattern:

**Live Data → Stream → Analyze → Detect → Alert → Action**

Instead of simply storing and analyzing historical data, the solution continuously monitors incoming events and responds when a predefined condition occurs.

This architecture can also be extended to use cases such as:

* ⚡ Energy optimization
* 🚗 EV fleet management
* 🏭 Industrial IoT monitoring
* 🏢 Smart buildings
* 🌱 Carbon-aware workloads
* 📡 Real-time operational monitoring

---

## 📌 Project Highlights

✅ Live data ingestion from an external API
✅ Python-based event generation
✅ Fabric Eventstream integration
✅ Fabric Eventhouse analytics
✅ KQL-based real-time analysis
✅ Automated alerting
✅ Real-Time Intelligence dashboard
✅ Teams notifications

---

## 🌱 Final Thoughts

The **Smart EV Charger Optimizer** demonstrates how Microsoft Fabric can bring together **real-time data engineering, analytics, monitoring, and automated decision-making** in a single solution.

The core idea is simple:

> **When the data changes in real time, decisions shouldn't have to wait.**

---

### 🔗 Project

**Project:** Live Smart EV Charger Optimizer
**Platform:** Microsoft Fabric Real-Time Intelligence
**Data Source:** UK National Grid Carbon Intensity API




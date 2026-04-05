# 🚆 Real-Time Indian Railways Dashboard using Microsoft Fabric

An end-to-end **Real-Time Analytics solution** built using Microsoft Fabric to monitor Indian Railways train running status using live public API data.

---

## 📌 Overview

This project demonstrates how to build a **real-time data pipeline** using Microsoft Fabric by:

- Streaming live train data from a public API  
- Processing data using Eventstream & Eventhouse  
- Transforming JSON data using KQL  
- Visualizing insights through a real-time dashboard  

The use case is based on **Konkan Railway train running data**.

---

## 🏗️ Architecture Diagram

![Architecture Diagram](https://github.com/SuparnaBabu7/Fabric_Projects/blob/main/Real-Time%20Intelligence/Indian%20Railways/railway_rti_archertecture.png)

---

## ⚙️ Tech Stack

- Microsoft Fabric  
- Eventstream  
- Eventhouse  
- Kusto Query Language (KQL)  
- REST API (Public Railway Data)  

---

## 🔄 Data Flow

1. **Data Source**  
   - Public API:  
     `https://konkan-railway-api.vercel.app/api/v4/fetchTrains`

2. **Ingestion**  
   - Data is ingested in real-time using **Eventstream (HTTP connector)**  

3. **Storage**  
   - Raw streaming data stored in **Eventhouse table**  

4. **Transformation**  
   - JSON data parsed and transformed using **KQL queries**  
   - Cleaned data stored in structured tables  

5. **Visualization**  
   - Real-time dashboard built with:
     - Live train tracking (Map)
     - KPIs (Total trains, delays)
     - Status distribution
     - Delay analysis  

---

## 📊 Key Features

- 🚆 Real-time train tracking  
- 🗺️ Map-based visualization using GPS coordinates  
- ⏱️ Delay analysis (Top delayed trains, Avg delay)  
- 📈 KPI dashboards for operational insights  
- ⚡ Streaming architecture with low latency  

---

## 📂 Project Structure
Real-Time Intelligence/
└── Indian Railways/
├── railway_rti_archertecture.png
├── KQL Queries/
├── Dashboard Assets/
└── Documentation/

---

## 🚀 Getting Started

### Prerequisites

- Microsoft Fabric (Trial or Capacity)
- Basic knowledge of KQL

---

### Setup Steps

1. Create **Eventhouse**
2. Create **Eventstream**
3. Connect to API using HTTP connector
4. Stream data into Eventhouse
5. Transform data using KQL
6. Build Real-Time Dashboard

---

## 📌 Sample Use Cases

- Railway operations monitoring  
- Real-time analytics learning  
- Streaming data architecture demos  
- Dashboarding with live data  

---

## 📥 Resources

- API Source: Konkan Railway Public API  
- KQL Scripts: (Add your files here)

---

## 🙌 About Me

👨‍💻 **INTURI SUPARNA BABU**  
- Microsoft Fabric Community Super User  
- Data Engineering Specialist  
- Active Blogger & Contributor in Fabric Community 

🔗 **LinkedIn Profile:**  
https://www.linkedin.com/in/inturi-suparna-babu-312b59270/

---

## ⭐ Support

If you like this project:

- ⭐ Star this repository  
- 🍴 Fork and explore  
- 🧑‍💻 Share your feedback  

---

## 📢 Connect & Collaborate

I actively share content on:
- Microsoft Fabric  
- Real-Time Intelligence  
- Data Engineering  

Let’s connect, learn, and grow together 🚀

---

**Happy Learning! 🚀**

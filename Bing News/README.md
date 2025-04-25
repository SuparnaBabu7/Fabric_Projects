
# 📊 Microsoft Fabric End-to-End Data Engineering Project

This project demonstrates a complete **Data Engineering pipeline** using **Microsoft Fabric**, integrating **Bing News API**, **Dataflow Gen2**, **Lakehouse**, **PySpark Notebooks**, **Sentiment Analysis**, and **Power BI** reporting, along with **Data Activator alerts** for real-time notifications.

### 👩‍💻 Author
**Inturi Suparna Babu**  
[LinkedIn](https://www.linkedin.com/in/inturi-suparna-babu-312b59270/) | [GitHub](https://github.com/SuparnaBabu7)

---

## 🛠️ Project Workflow

### 1. **Workspace & Lakehouse Setup**
- Created Fabric workspace and Lakehouse to manage data storage.
  
### 2. **Data Ingestion**
- Ingested data from the Bing News REST API using a pipeline with **Copy Activity**.
- JSON files were stored in the Lakehouse.

### 3. **Data Transformation**
- Used **Notebooks with PySpark** to clean, process, and store data as Delta tables.
- Implemented **Incremental Load** logic to handle daily updates efficiently.

### 4. **Sentiment Analysis**
- Applied machine learning to analyze sentiment of news articles.
- Stored results back into Lakehouse.

### 5. **Semantic Model & Power BI Report**
- Created a Semantic Model directly from the Lakehouse.
- Auto-generated and customized Power BI reports.
- [Power BI Report (.pbix)](https://github.com/SuparnaBabu7/Fabric_Projects/blob/main/Bing%20News/bing-news-report.pbix)

### 6. **Automation with Pipelines**
- Built multiple pipelines to orchestrate ingestion → transformation → ML → reporting.
- Parameterized the news topic for dynamic runs.
- Scheduled daily refresh and ML pipeline execution.

### 7. **Real-time Alerts (Data Activator)**
- Configured **Data Activator** alerts on Power BI visuals for specific triggers.

### 8. **Testing & Validation**
- End-to-end testing performed with different news categories (e.g., "Sports").

---

## 📂 Key Files

- 🔗 [Cleaned Data Notebook](https://github.com/SuparnaBabu7/Fabric_Projects/blob/main/Bing%20News/bing-news-clean.ipynb)  
- 🔗 [Sentiment Analysis Notebook](https://github.com/SuparnaBabu7/Fabric_Projects/blob/main/Bing%20News/news-sentiment-analysis-ds.ipynb)  
- 📊 [Power BI Report](https://github.com/SuparnaBabu7/Fabric_Projects/blob/main/Bing%20News/bing-news-report.pbix)  
- 🗂️ [Complete Project Folder](https://github.com/SuparnaBabu7/Fabric_Projects/tree/main/Bing%20News)

---

## 📅 Features

- ✅ End-to-End Microsoft Fabric implementation
- ✅ Dynamic data pipeline with REST API ingestion
- ✅ Incremental load & ML integration
- ✅ Visualization with Power BI
- ✅ Real-time monitoring via Data Activator

---

## 🙌 Acknowledgment

This project was inspired by hands-on learning from the **Microsoft Fabric - Udemy course** and created to demonstrate real-world implementation for aspiring Data Engineers.

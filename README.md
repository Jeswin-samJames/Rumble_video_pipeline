# ETL Pipeline with PySpark for Datalake Medallion Architecture  

## 📌 Project Overview  
This project implements an **ETL pipeline** using **PySpark** to process a dataset of Rumble videos in **Medallion Architecture** (Bronze → Silver → Gold layers).  
The pipeline demonstrates how to organize, clean, transform, and enrich data for downstream analytics.  

- **Input dataset:** JSON file containing Rumble video details.  
- **Output datasets:** Parquet files across Bronze, Silver, and Gold layers.  
- **Technology stack:** PySpark, Parquet, JSON.  

---

## 🗂 Dataset  
The dataset consists of video metadata and user comments in JSON format.  
---

## 🏗 Medallion Architecture  

### 1. **Bronze Layer**  
- Store raw JSON as **Parquet**.  
- No transformations, just structured storage.  

### 2. **Silver Layer**  
- Flatten JSON and select required fields.  
- Retain only these columns:  
- Store as **5 split Parquet files**.  

### 3. **Gold Layer**  
Transformations applied:  

1. **Exploding Tags**  
 - If a video has multiple `video_tags`, create separate rows for each tag.  

2. **Comment Metrics**  
 - `number_of_comments`: Total comments per video.  
 - `number_of_commented_users`: Distinct users who commented per video.  

3. **Filtered Dataset**  
 - Records where `video_host = "Benny Johnson"` **and** `video_tag = "news"`.  

4. **User Engagement Analysis**  
 - Group by `commented_username_hash`.  
 - Calculate per video:  
   - `number_of_comments`: Total comments made by the user.  
   - `number_of_comments_like`: Total likes received for the user’s comments.  

---

## 📂 Project Structure  
<img width="329" height="532" alt="rumble" src="https://github.com/user-attachments/assets/fd2b656e-9870-4023-be1a-fa50d8a8cc2a" />


## Future Enhancements

  - Integrate with Apache Airflow for orchestration.
  - Store datasets in AWS S3 / Azure Data Lake.
  - Connect with BI tools (Power BI, Tableau, Databricks).

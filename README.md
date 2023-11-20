# 📊 Djinni vacancy scraping project

## 📖 Overview
This project offers a straightforward solution for monitoring the latest trends in various programming languages, combining the capabilities of web scraping and data analysis to offer insights into the most sought-after technologies in the job market.

## ✨ Features
- **Easy setup**: Simply specify your scraping settings in djinni/config.py. 
- **Scraping & Data Analysis**: The project is divided into two parts - scraping and data analysis, following the Single Responsibility Principle (SRP).

## 🚀 Getting Started
1. **Execute the following commands:**
   ```bash
   git clone https://github.com/lgSilay/djinni_vacancy_scraping
   djinni_vacancy_scraping
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate in Windows
   pip install -r requirements.txt
   scrapy crawl vacancies -O {file_name}.csv #create your own dataset or you can test on vacancies.csv
   ```

2. **Update config.py with your settings** in /djinni/config.py
   
3. **Run data_analysis.py** to visualize your data.

## 📊 Sample Results
![python_vacancy.JPG](examples%2Fpython_vacancy.JPG)

![java_vacancy.JPG](examples%2Fjava_vacancy.JPG)

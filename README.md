# E-Commerce Sales Analysis (Pandas Project)

## Project Overview

This project analyzes an e-commerce sales dataset using **Python and Pandas** to identify business insights such as monthly sales trends, top-selling products, and high-revenue cities.

The goal of the project is to demonstrate **data cleaning, data analysis, and business insight generation**, which are key skills for a **Data Analyst role**.

---

## Tools & Technologies

* Python
* Pandas
* Jupyter Notebook

---

## Dataset

The dataset contains information about customer orders.

Columns used in the analysis:

* Order ID
* Product
* Quantity Ordered
* Price Each
* Order Date
* Purchase Address

---

## Data Cleaning Steps

The following data preprocessing steps were performed:

* Removed missing values
* Converted numeric columns using `pd.to_numeric()`
* Converted `Order Date` to datetime format
* Created a new **Revenue column**

Revenue formula:

Revenue = Quantity Ordered × Price Each

---

## Analysis Performed

### 1. Monthly Sales Analysis

Calculated total revenue generated in each month using **groupby()**.

Goal:
Identify which month had the highest sales.

---

### 2. Top Selling Products

Analyzed which products were sold the most using total quantity ordered.

Goal:
Understand customer demand.

---

### 3. Sales by City

Extracted city information from purchase addresses and calculated total revenue by city.

Goal:
Identify cities generating the highest revenue.

---

### 4. Sales by Hour

Extracted the hour from order time to analyze peak shopping hours.

Goal:
Understand when customers buy the most products.

---

## Key Insights

* Certain months generate significantly higher revenue.
* Some products dominate total sales volume.
* A few cities contribute the majority of revenue.
* Sales peak during specific hours of the day.

These insights help businesses improve **inventory planning, marketing strategy, and sales optimization**.

---

## Project Structure

sales_analysis
│
├── sales_analysis.ipynb
├── sales_data.csv
├── cleaned_sales_data.csv
└── README.md

---

## Skills Demonstrated

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Business Insight Generation
* Pandas Data Manipulation

---

## Future Improvements

* Add advanced visualizations
* Perform product bundling analysis
* Build a sales prediction model

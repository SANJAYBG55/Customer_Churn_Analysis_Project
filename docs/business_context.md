# Business Context & Dataset Scoping

**Project:** Customer Churn Analysis (Telecom / SaaS)  
**Stage:** 1 - Business Context & Dataset Scoping  
**Date:** January 6, 2026

---

## 1. Business Problem Statement

### What is Customer Churn?
Customer churn occurs when customers stop doing business with a company. In the telecom industry, this means customers cancel their phone/internet service and switch to a competitor.

### Why Does Churn Matter?
- **Revenue Loss:** Each churned customer represents lost monthly recurring revenue
- **Acquisition Cost:** Getting a new customer costs 5-7x more than retaining an existing one
- **Market Competition:** Telecom is highly competitive with many providers fighting for customers
- **Profitability:** Long-term customers are more profitable (higher lifetime value)

### Business Goal
Identify customers who are likely to churn so the company can:
- Offer targeted retention incentives (discounts, upgrades)
- Improve service quality for at-risk customers
- Understand root causes of churn
- Reduce overall churn rate and increase customer lifetime value

---

## 2. Dataset Overview

### Dataset Name
**IBM Telco Customer Churn Dataset**

### Source
Kaggle - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Dataset Description
This dataset contains customer information for a fictional telecom company. It tracks customers who left (churned), stayed, or signed up for services including phone, internet, streaming, and security.

### Time Period
- Dataset represents a **snapshot** of customers at a specific point in time
- Includes historical data about customer tenure (how long they've been customers)
- No explicit date range, but tenure ranges from 0 to 72 months (6 years)

### Dataset Size
- **Rows:** 7,043 customers
- **Columns:** 21 features/attributes

---

## 3. Row Grain (Granularity)

### What Does One Row Represent?
**One row = One unique customer**

### Key Points
- This is a **customer-level dataset**, not transaction-level
- Each customer appears exactly once
- Data represents customer status at a single point in time (snapshot)
- This is NOT a time-series dataset

### Implication for Analysis
- We analyze customer **characteristics** to understand churn
- We cannot track customer behavior over time (no historical changes)
- Analysis will be cross-sectional (comparing churned vs non-churned customers)

---

## 4. Business Entities Identified

### Primary Entity: CUSTOMERS
Each row represents a customer with their attributes.

### Secondary Entities (Attributes)
Based on column analysis, the dataset includes:

#### 4.1 Customer Demographics
- Gender
- Age status (Senior Citizen)
- Family status (Partner, Dependents)

#### 4.2 Service Information
- Phone Service (Yes/No)
- Multiple Lines (Yes/No/No phone service)
- Internet Service (DSL, Fiber optic, No)
- Online Security (Yes/No/No internet service)
- Online Backup (Yes/No/No internet service)
- Device Protection (Yes/No/No internet service)
- Tech Support (Yes/No/No internet service)
- Streaming TV (Yes/No/No internet service)
- Streaming Movies (Yes/No/No internet service)

#### 4.3 Account/Contract Information
- Customer Tenure (months with company)
- Contract Type (Month-to-month, One year, Two year)
- Paperless Billing (Yes/No)
- Payment Method (Electronic check, Mailed check, Bank transfer, Credit card)

#### 4.4 Financial Information
- Monthly Charges (amount billed per month)
- Total Charges (total amount billed to customer)

#### 4.5 Target Variable
- **Churn** (Yes/No) - Whether customer left the company

---

## 5. Business Questions This Dataset Can Answer

### Descriptive Questions (What happened?)
- What is the overall churn rate?
- Which customer segments have highest churn?
- What is the average tenure of churned vs non-churned customers?

### Diagnostic Questions (Why did it happen?)
- Do customers with month-to-month contracts churn more?
- Does internet service type affect churn?
- Are customers with higher monthly charges more likely to churn?
- Do customers without tech support churn more often?

### Prescriptive Questions (What should we do?)
- Which customers should we prioritize for retention campaigns?
- What service improvements would reduce churn?
- Should we change pricing or contract structures?

---

## 6. Expected Analysis Workflow

Based on this dataset, our analysis will follow these stages:

1. ✅ **Stage 1 (Current):** Understand the dataset and business context
2. **Stage 2:** Integrate this dataset with additional data sources (customer, payment, service tables)
3. **Stage 3:** Validate data quality (check for missing values, errors)
4. **Stage 4:** Clean and prepare data for analysis
5. **Stage 5:** Explore patterns through visualizations and statistics
6. **Stage 6:** Create business metrics (churn rate, customer lifetime value, etc.)
7. **Stage 7:** Analyze churn drivers and develop rule-based risk indicators
8. **Stage 8:** Build dashboard to present findings
9. **Stage 9:** Automate and document the entire workflow

---

## 7. Key Assumptions

- Dataset is accurate and representative of real telecom customers
- Churn labels are correct (customers marked as "Yes" actually churned)
- All customers in dataset had the opportunity to churn
- Missing values will be addressed in Stage 4 (Data Cleaning)
- Currency is USD (not explicitly stated in dataset)

---

## 8. Success Criteria for This Project

### Analytics Success
- Identify top 3-5 churn drivers
- Segment customers into risk categories (high/medium/low)
- Provide 5+ actionable business recommendations

### Technical Success
- Clean, reproducible code
- Clear visualizations understandable by non-technical stakeholders
- Interactive dashboard for exploring results

### Portfolio Success
- Demonstrates end-to-end analytics skills
- Shows business thinking, not just technical skills
- Suitable for presenting to recruiters/interviewers

---

## 9. Next Steps

- ✅ Dataset downloaded and profiled
- ✅ Business context documented
- ⏳ Proceed to Stage 2: Data Centralization & Integration

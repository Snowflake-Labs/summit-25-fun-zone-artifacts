# ❄️ Snowflake Cortex + dbt Challenge Series

---

## 🔹 Challenge 001: Classify Invoice Line Items

**Goal**: Classify each free-text service description into a standardized category using Snowflake Cortex `CLASSIFY_TEXT()`.

### 🧾 Inputs

- `invoice_line_items`  
  Raw descriptions like “Deployment of Snowflake project”

- `service_categories`  
  Labels like:
  - "Snowflake Deployment"
  - "ETL Pipeline Engineering"
  - "dbt Modeling"
  - "Performance Tuning & Support"
  - and others

### ⚙️ Task

Build a dbt model that:

- Loads all labels from `service_categories`
- Applies `CLASSIFY_TEXT()` to predict the category for each line item
- Outputs:
  - `line_item_id`
  - `service_description`
  - `predicted_category`

### ✅ Example Output

| line_item_id | service_description                          | predicted_category           |
|--------------|----------------------------------------------|------------------------------|
| 1            | Deployment of Snowflake project - Phase 1    | Snowflake Deployment         |
| 4            | Initial dbt model refactoring                | dbt Modeling                 |
| 6            | Consulting for ML pipeline testing           | Machine Learning Support     |

---

## 🔹 Challenge 002: Sentiment by Review Category

**Goal**: Extract sentiment per hotel review category using Snowflake Cortex `LABEL_SENTIMENT()`.

### 🧾 Inputs

- `hotel_reviews`  
  Customer-written reviews of their stay

- `review_categories`  
  Supplied labels (same for every row):
  - "Staff"
  - "Comfort"
  - "Free WiFi"
  - "Facilities"
  - "Value for money"
  - "Cleanliness"
  - "Location"

### ⚙️ Task

Build **two** dbt models:

1. **`classified_sentiments`**  
   - Uses `LABEL_SENTIMENT()` on each review
   - Returns JSON array of category-level sentiments

2. **`parsed_entity_sentiments`**  
   - Flattens JSON array into rows
   - Final columns:
     - `review_id`
     - `review_text`
     - `entity` (category)
     - `sentiment` (positive/neutral/negative)
     - `confidence` (float)

### ✅ Example Output

| review_id | entity         | sentiment | confidence |
|-----------|----------------|-----------|------------|
| 42        | Free WiFi      | positive  | 0.91       |
| 42        | Comfort        | positive  | 0.86       |
| 42        | Location       | positive  | 0.88       |

---

### 🧰 Provided

- `seeds/hotel_reviews.csv`
- `seeds/review_categories.csv`
- Pre-configured `dbt_project.yml` and source setup

---

## 🔹 Challenge 003: Multi-Language Feedback Summary

**Goal**: Translate multilingual customer reviews to English and generate concise summaries using Cortex `TRANSLATE` and `SUMMARIZE`.

### 🧾 Inputs

- Five separate tables with customer reviews:
  - `customer_feedback_en`
  - `customer_feedback_es`
  - `customer_feedback_fr`
  - `customer_feedback_de`
  - `customer_feedback_ja`
- Each table has:
  - `review_id`
  - `review_text` (≥5 sentences)

### ⚙️ Task

2. Translate the full review text into English
3. Summarize the translated review using Cortex

WITH category_array AS (
  SELECT ARRAY_AGG(category_name) AS classes
  FROM mikedroog.challenge_001_setup.service_categories
),
classified AS (
  SELECT
    i.line_item_id,
    i.service_description AS input,
    category_array.classes,
    SNOWFLAKE.CORTEX.CLASSIFY_TEXT(i.service_description, category_array.classes)['label'] AS predicted_category
FROM {{ ref('invoice_line_items') }} i,
       category_array
)
SELECT * FROM classified
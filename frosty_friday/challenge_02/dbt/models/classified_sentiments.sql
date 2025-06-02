WITH category_array AS (
  SELECT ARRAY_AGG(category_name) AS categories
  FROM {{ref('hotel_review_categories')}}
),
classified AS (
  SELECT
    r.review_id,
    r.review_text,
    category_array.categories,
    SNOWFLAKE.CORTEX.ENTITY_SENTIMENT(r.review_text, category_array.categories) AS entity_sentiments
  FROM {{ref('hotel_reviews_with_entities')}} r,
       category_array
)
SELECT * FROM classified
-- models/parsed_entity_sentiments.sql

WITH base AS (
  SELECT
    review_id,
    review_text,
    entity_sentiments
  FROM {{ ref('classified_sentiments') }}
),

flattened AS (
  SELECT
    review_id,
    review_text,
    value:name::string AS entity,
    value:sentiment::string AS sentiment
  FROM base,
       LATERAL FLATTEN(input => entity_sentiments:categories)
)


SELECT * FROM flattened
with get_entities as (
    select
        *,
        snowflake.cortex.entity_sentiment(
            review_text,
            array_construct(target_entity)
        ):"categories" as entities_extracted
    from
        hotel_reviews_with_entities
),
extract_both as (
    select
        review_id,
        hotel_id,
        review_text,
        entities_extracted[0]:"sentiment"::string as overall_sentiment,
        target_entity,
        entities_extracted[1]:"sentiment"::string as target_sentiment
    from
        get_entities
)

select
    *
from
    extract_both

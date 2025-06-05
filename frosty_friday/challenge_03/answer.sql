-- create or replace table answer as
select
    ai_summarize_agg(
        snowflake.cortex.translate(review_text, '', 'EN')
    ) as english_summary
from
    customer_feedback_combined

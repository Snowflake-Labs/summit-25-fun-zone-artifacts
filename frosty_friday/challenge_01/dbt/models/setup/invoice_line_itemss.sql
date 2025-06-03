-- models/challenge_001_setup/invoice_line_items.sql

select *
from {{ source('challenge_001_setup', 'invoice_line_items') }}
-- models/challenge_001_setup/service_categories.sql

select *
from {{ source('challenge_001_setup', 'service_categories') }}
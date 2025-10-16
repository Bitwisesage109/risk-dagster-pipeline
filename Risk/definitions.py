# Risk/definitions.py
from dagster import Definitions, load_assets_from_modules
from Risk import assets
from Risk.assets import ssis_daily_schedule,ssis_import_job 
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[ssis_import_job],
    schedules=[ssis_daily_schedule],
)

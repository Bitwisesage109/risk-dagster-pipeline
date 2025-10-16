from dagster import asset, job, ScheduleDefinition, define_asset_job
import subprocess, os

@asset
def run_ssis_package(context):
    dtexec_path = r"D:\Program Files (x86)\Microsoft SQL Server\140\DTS\Binn\DTExec.exe"
    package_path = r"\SSISDB\Risk\ETL\Perfomatics_PM.dtsx"
    server_name = "IDCIRISDEV01NYE"
    env_reference = "3"
    sync_option = r'"$ServerOption::SYNCHRONIZED(Boolean)";True'

    cmd = [
        dtexec_path,
        "/ISSERVER", package_path,
        "/SERVER", server_name,
        "/ENVREFERENCE", env_reference,
        "/Par", sync_option,
    ]

    context.log.info(f"Running SSIS: {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    context.log.info("STDOUT:\n" + result.stdout)
    if result.returncode != 0:
        context.log.error("STDERR:\n" + result.stderr)
        raise Exception(f"SSIS package failed: {result.returncode}")

    context.log.info("SSIS package executed successfully.")
    return "Success"

ssis_import_job = define_asset_job(
    name="ssis_import_job",
    selection=[run_ssis_package],
)

# Run daily at 8:00 PM
ssis_daily_schedule = ScheduleDefinition(
    job=ssis_import_job,
    cron_schedule="0 20 * * *",  # 8 PM
)

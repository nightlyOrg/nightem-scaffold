"""
This provider is responsible for running the database migrations.

Read about the migration provider in the wiki on our Github:
https://github.com/NightlyOrg/Nightem-scaffold/wiki
"""
from service_providers.functions import run_tasks


async def run_migrations():
    """
    Runs the migration tasks
    """
    await run_tasks("migrations", "Migration", "Schema")

"""
This provider is responsible for running the seeders that'll fill the database.

Read about the seeding provider in the wiki on our Github:
https://github.com/NightlyOrg/Nightem-scaffold/wiki
"""


from service_providers.functions import run_tasks


async def run_seeders():
    """
    Runs the seeder tasks
    """
    await run_tasks("seeders", "Seeder", "Seeder")

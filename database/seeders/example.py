"""
Seeders are responsible for filling the database schemas.
The bot will run these upon start-up if enabled in config/app.py.

The bot provides seeding commands to run these Seeders manually,
but it is not recommended to use these commands unless you know what
you are doing.

If you are self-hosting this bot for public use, we recommend you
establish a privacy policy, and refrain from touching these commands
while in production. The Nightly organization and Nightem Software
Foundation are not responsible for any data loss or corruption as
a result of using these commands in any wrong or untimely manner.
"""


class Seeder:
    table = "users"
    columns = [
        {"user_id": "1"},
        {"name": "example user"},
        {"rights_level": "1"}
    ]

    def getTable(self):
        return self.table

    def getColumns(self):
        return self.columns

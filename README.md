# Nightem scaffold
The Nightem scaffold is a scaffold for discord bots based on a provision model.
The principle is to use a structured manner of data management through seeding 
and migrations, allowing for a more organized and maintainable codebase.

---

## Usage
To use the scaffold, you need to have the following installed:
- Python 3.8 or higher
- mariaDB or mysql with a database
- the python package manager (pip)

To use the scaffold, you can use the following command:
```bash
git clone https://github.com/NightlyOrg/nightem-scaffold.git
```

After cloning the repository, you can install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

Before proceeding, you should change the git remote from our scaffold to your own project:
```bash
git remote set-url origin <url>
```

After executing these commands, you can start development. Make your config file
in the `config` directory (vault.py), you can use `cp example-vault.py vault.py`
` to copy the example file. After that, you can run the following command to start the bot:
```bash
python main.py
# We recommend using pm2 to manage your bots
pm2 start main.py --interpreter python --name <name> --watch
```

If you followed along correctly, the bot should run.
Questions about things in the scaffold? Check the Github wiki.

https://github.com/NightlyOrg/nightem-scaffold/wiki
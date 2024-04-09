class Schema:
    name = "users"
    columns = [
        "user_id VARCHAR(20) PRIMARY KEY",
        "name VARCHAR(255)",
        "rights_level INT",
    ]

    def getName(self):
        return self.name

    def getColumns(self):
        return self.columns

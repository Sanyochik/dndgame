class DB:
    def __init__(self, psycopg):
        self.psycopg = psycopg
    def connect(self):
        connection = self.psycopg.connect(
            host="localhost",
            dbname="dnd_project_db",
            user="postgres",
            password="pass"
        )

        return connection
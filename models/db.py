class DB:
    def __init__(self, psycopg,os):
        self.psycopg = psycopg
        self.os = os
    def connect(self):
        connection = self.psycopg.connect(
            host=self.os.getenv('DB_HOST'),
            dbname=self.os.getenv('DB_NAME'),
            user=self.os.getenv('DB_USER'),
            password=self.os.getenv('DB_PASSWORD')
        )

        return connection
class Events():
    def __init__(self, db):
        self.db = db

    def getevents(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute("SELECT * FROM events")
        rows = request.fetchall()
        connection.close()

        return rows
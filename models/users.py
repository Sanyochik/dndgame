class Users():
    def __init__(self,db):
        self.db = db

    def getusers(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute("SELECT * FROM users")
        rows = request.fetchall()
        connection.close()

        return rows

    def adduser(self,username,str,chr,vit):
        connection = self.db.connect()
        connection.execute(f"INSERT INTO users (username,str,chr,vit) VALUES ('{username}',{str},{chr},{vit})")
        connection.commit()
        connection.close()
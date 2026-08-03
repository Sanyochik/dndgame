class Journey():
    def __init__(self, db):
        self.db = db

    def getjourneys(self,user_id):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT * FROM journey WHERE ID={user_id}")
        rows = request.fetchall()
        connection.close()

        return rows

    def addjourney(self,id_event,id_user,current_hp,enemy_hp,status):
        connection = self.db.connect()
        connection.execute(f"INSERT INTO journey (id_event,id_user,current_hp,enemy_hp,status) VALUES ('{id_event}','{id_user}','{current_hp}',{enemy_hp},'active')")
        connection.commit()
        connection.close()

    def updatejourney(self,journey_id,current_hp,enemy_hp,status):
        connection = self.db.connect()
        connection.execute(f"UPDATE journey SET current_hp={current_hp}, enemy_hp={enemy_hp}, status={status} WHERE id={journey_id}")
        connection.commit()
        connection.close()


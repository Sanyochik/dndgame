class Journey():
    def __init__(self, db):
        self.db = db

    def getactivejourney(self,userinfo,event_info):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT * FROM journey WHERE id_user={userinfo[0][0]} AND status=1")
        rows = request.fetchall()
        if not rows:
            rows = []
        connection.close()

        return rows

    def getcomplitejourney(self,userinfo,event_info):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT * FROM journey WHERE id_user={userinfo[0][0]} AND status=0")
        rows = request.fetchall()
        if not rows:
            rows = []
        connection.close()

        return rows

    def addjourney(self,user_data,event_data):
        connection = self.db.connect()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO journey (id_event,id_user,current_hp,enemy_hp,status) VALUES ('{event_data[0][0]}','{user_data[0][0]}','{user_data[0][4]}',{event_data[0][6]},1) RETURNING *")
        new_journey = cursor.fetchone()
        connection.commit()
        connection.close()
        return new_journey

    def updatejourney(self,journey_id,current_hp,enemy_hp,status):
        connection = self.db.connect()
        connection.execute(f"UPDATE journey SET current_hp={current_hp}, enemy_hp={enemy_hp}, status={status} WHERE id={journey_id}")
        connection.commit()
        connection.close()


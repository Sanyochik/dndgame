class Events():
    def __init__(self, db,random,users):
        self.db = db
        self.random = random
        self.users = users

    def getevents(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT * FROM events")
        rows = request.fetchall()
        connection.close()

        return rows

    def getcurrentevent(self,event_id):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT * FROM events WHERE id={event_id}")
        rows = request.fetchall()
        connection.close()

        return rows

    def getrandomevents(self,completed):
        ids = [row[0] for row in self.getevents()]
        notcomplitedid = [x for x in ids if x not in completed]
        random_id = self.random.choice(notcomplitedid)
        result = self.getcurrentevent(random_id)

        return result

    def addevent(self,title,discr,img,str_dif,chr_dif,vit_dif,str_ans,chr_ans,dmg):
        connection = self.db.connect()
        connection.execute(f"INSERT INTO events (title,description,img_url,str_dif,chr_dif,vit_dif,str_ans,chr_ans,dmg) VALUES ('{title}','{discr}','{img}',{str_dif},{chr_dif},{vit_dif},'{str_ans}','{chr_ans}',{dmg})")
        connection.commit()
        connection.close()


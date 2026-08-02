class Events():
    def __init__(self, db,random,users):
        self.db = db
        self.random = random
        self.users = users

    def geteventsid(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute(f"SELECT id FROM events")
        rows = request.fetchall()
        rows = [row[0] for row in rows]
        connection.close()

        return rows

    def getrandomevents(self):
        print(self.random.choice(self.geteventsid()))

    def addevent(self,title,discr,img,str_dif,chr_dif,vit_dif,str_ans,chr_ans,dmg):
        connection = self.db.connect()
        connection.execute(f"INSERT INTO events (title,description,img_url,str_dif,chr_dif,vit_dif,str_ans,chr_ans,dmg) VALUES ('{title}','{discr}','{img}',{str_dif},{chr_dif},{vit_dif},'{str_ans}','{chr_ans}',{dmg})")
        connection.commit()
        connection.close()


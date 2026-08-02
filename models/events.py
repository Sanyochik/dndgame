class Events():
    def __init__(self, db,random,users):
        self.db = db
        self.random = random
        self.users = users

    def getevents(self):
        connection = self.db.connect()
        cursor = connection.cursor()
        request = cursor.execute("SELECT * FROM events")
        rows = request.fetchall()
        connection.close()

        return rows
    def pulldice(self):
        result = self.random.randint(1,20)

        return result

    def diceresult(self):
        dice = self.pulldice()
        result = []
        match dice:
            case 1:
                result+=(dice,f'Выпало значение: {dice} Критический провал')
            case 20:
                result+=(dice,f'Выпало значение: {dice} Критический успех')
            case _:
                statdice=self.getatribute(dice,self.users.getusers())
                result+=(f'{dice}+{statdice}', f'Выпало значение: {dice}')


        return result
    def getatribute(self,dice_value,user):
        print(user[0][2])

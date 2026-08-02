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

    def diceresult(self,dicevalue,diceattribute):
        match dicevalue:
            case 1:
                result=(diceattribute,f'Выпало значение: {dicevalue} Критический провал')
            case 20:
                result=(diceattribute,f'Выпало значение: {dicevalue} Критический успех')
            case _:
                result=(diceattribute, f'Выпало значение: {dicevalue}')

        return result
    def getattribute(self,dice_value,user):
        match dice_value:
            case 1:
                result=int(dice_value)
            case 20:
                result = int(dice_value) + int(user[0][2])
            case _:
                result = int(dice_value) + int(user[0][2])
        return result

class Dice():
    def __init__(self,random):
        self.random = random

    def pulldice(self):
        result = self.random.randint(1, 20)

        return result

    def diceresult(self, dicevalue, diceattribute):
        match dicevalue:
            case 1:
                result = (1, f'Выпало значение: {dicevalue} Критический провал')
            case 20:
                result = (round(dicevalue+diceattribute*1.2), f'Выпало значение: {dicevalue} Критический успех')
            case _:
                result = (dicevalue+diceattribute, f'Выпало значение: {dicevalue}')

        return result
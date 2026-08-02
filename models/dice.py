class Dice():
    def __init__(self,random):
        self.random = random

    def pulldice(self):
        result = self.random.randint(1, 20)

        return result

    def diceresult(self, dicevalue, diceattribute):
        match dicevalue:
            case 1:
                result = (diceattribute, f'Выпало значение: {dicevalue} Критический провал')
            case 20:
                result = (diceattribute, f'Выпало значение: {dicevalue} Критический успех')
            case _:
                result = (diceattribute, f'Выпало значение: {dicevalue}')

        return result
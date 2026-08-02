class Attribute:
    def __init__(self):
        ...

    def add(self,curent_label,freestats_value):
        curent_label = int(curent_label)
        freestats_value = int(freestats_value)
        if (freestats_value > 0):
            curent_label += 1
            freestats_value -=1
        else:
            ...

        return curent_label, freestats_value

    def reduce(self,curent_label,freestats_value):
        curent_label = int(curent_label)
        freestats_value = int(freestats_value)
        if (curent_label > 1):
            curent_label -= 1
            freestats_value += 1
        else:
            ...

        return curent_label, freestats_value

    def getattribute(self,dice_value,user):
        match dice_value:
            case 1:
                result=int(dice_value)
            case 20:
                result = int(dice_value) + int(user[0][2])
            case _:
                result = int(dice_value) + int(user[0][2])
        return result


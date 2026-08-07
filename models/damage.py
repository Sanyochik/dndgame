class Damage:
    def __init__(self):
        ...
    def makedmg(self,current_hp,dmg_value,def_value):
        if dmg_value > def_value:
            current_hp -= dmg_value
        if current_hp <= 0:
            current_hp = 0

        return current_hp
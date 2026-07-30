def add(curent_label,freestats_value):
    curent_label = int(curent_label)
    freestats_value = int(freestats_value)
    if (freestats_value > 0):
        curent_label += 1
        freestats_value -=1
        result = [curent_label, freestats_value]
    else:
        result = [curent_label,freestats_value]

    return result

def reduce(curent_label,freestats_value):
    curent_label = int(curent_label)
    freestats_value = int(freestats_value)
    if (curent_label > 1):
        curent_label -= 1
        freestats_value += 1
        result = [curent_label,freestats_value]
    else:
        result = [curent_label,freestats_value]

    return result


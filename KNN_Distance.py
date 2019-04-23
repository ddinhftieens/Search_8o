import math

def Dictance(nitem,item):
    total = 0
    for i in item.keys():
        total += math.pow(nitem[i]-item[i],2)
    return math.sqrt(total)
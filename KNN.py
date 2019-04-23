import random
import KNN_Distance

def readfile(file):
    read = open(file,"r")
    lines = read.read().splitlines()
    read.close()
    featurn = lines[0].split(',')[:-1]
    item =[]
    for i in range(1,len(lines)):
        line = lines[i].split(',')
        itemfeaturn = {'Class':line[-1]}
        for j in range(len(line)-1):
            itemfeaturn[featurn[j]] = float(line[j])
        item.append(itemfeaturn)
    print(item)
    random.shuffle(item)
    return item

def Classsify(nitem,item,k):
    dict = []
    for i in nitem:
        distance = KNN_Distance.Dictance(i,item)
        dict = Update(dict,k,distance,i)
    print(dict)
    count = Calculate(dict)
    return Findmax(count)


def Update(dict,k,distance,nitem):
    if(len(dict)<k):
        dict.append([distance,nitem['Class']])
        dict = sorted(dict)
    else:
        if dict[-1][0] > distance:
            dict[-1] = [distance,nitem['Class']]
            dict = sorted(dict)
    return dict

def Calculate(dict):
    count = {}
    for i in dict:
        if i[1] not in count.keys():
            count[i[1]] = 1
        else:
            count[i[1]] = count[i[1]] + 1
    return count

def Findmax(dict):
    value = 0
    name = ''
    for i in dict.keys():
        if(dict[i]>value):
            value = dict[i]
            name = i
    return(name, value)

def main():
    file = readfile("dataKNN.txt")
    item = {'Height': 1.75, 'Weight': 68.0, 'Age': 28.0}
    print(Classsify(file,item,3))
if __name__ == '__main__':
    main()
import collections
import math

class BaiToan8o(object):

    def __init__(self, trangthai, n, nutcha=None, hanhdong="Start", cost = 0):

        if n*n != len(trangthai) or n<2:
            raise Exception("Khong hop le")
        self.trangthai = trangthai
        self.nutcha = nutcha
        self.n = n
        self.cost = cost
        self.hanhdong = hanhdong
        self.nutcon = []
        for vitri,giatri in enumerate(self.trangthai):
            if giatri == 0:
                self.hang = int(vitri/self.n)
                self.cot = int(vitri%self.n)
                break

    def show(self):
        for i in range(self.n):
            line = []
            k = i*self.n
            for j in range(self.n):
                line.append(self.trangthai[k+j])
            print(line)

    def sangtrai(self):
        if self.cot != 0:
            x = self.hang*self.n + self.cot
            y = x - 1
            trangthai_moi = list(self.trangthai)
            trangthai_moi[x], trangthai_moi[y] = trangthai_moi[y], trangthai_moi[x]
            return BaiToan8o(tuple(trangthai_moi), self.n, nutcha=self, hanhdong="Trai", cost=self.cost+1)
        else:
            return None

    def sangphai(self):
        if self.cot != self.n-1:
            x = self.hang*self.n + self.cot
            y = x + 1
            trangthai_moi = list(self.trangthai)
            trangthai_moi[x], trangthai_moi[y] = trangthai_moi[y], trangthai_moi[x]
            return BaiToan8o(tuple(trangthai_moi), self.n, nutcha=self, hanhdong="Phai", cost=self.cost+1)
        else:
            return None

    def llen(self):
        if self.hang != 0:
            x = self.hang*self.n+self.cot
            y = (self.hang - 1)*self.n + self.cot # y = x - self.n
            trangthai_moi = list(self.trangthai)
            trangthai_moi[x], trangthai_moi[y] = trangthai_moi[y], trangthai_moi[x]
            return BaiToan8o(tuple(trangthai_moi), self.n, nutcha=self, hanhdong="Len", cost=self.cost+1)
        else:
            return None

    def xuong(self):
        if self.hang != self.n-1:
            x = self.hang*self.n+self.cot
            y = (self.hang+1)*self.n + self.cot # y = x+self.n
            trangthai_moi = list(self.trangthai)
            trangthai_moi[x], trangthai_moi[y] = trangthai_moi[y], trangthai_moi[x]
            return BaiToan8o(tuple(trangthai_moi), self.n, nutcha=self, hanhdong="Xuong", cost=self.cost+1)
        else:
            return None

    def Thucthi(self):
        if len(self.nutcon) == 0:
            upp = self.llen()
            if upp is not None:
                self.nutcon.append(upp)
            downn = self.xuong()
            if downn is not None:
                self.nutcon.append(downn)
            leftt = self.sangtrai()
            if leftt is not None:
                self.nutcon.append(leftt)
            rightt = self.sangphai()
            if rightt is not None:
                self.nutcon.append(rightt)
        return self.nutcon

def check(x, queue):
    for i in queue:
        if x.trangthai == i.trangthai:
            return False
    return True

def add(tapnut, queue, list, dich, nguon): #them k neu dung A_DFS
    # tapnut.reverse()
    nut = iter(tapnut)
    while True:
        try:
            x = nut.__next__()
            if x.trangthai == dich:
                print("Chi phi: ",x.cost)
                action = []
                while x != nguon:
                    action.append(x.hanhdong)
                    x = x.nutcha
                action.reverse()
                print("Buoc: ",action)
                return queue,True
            if x.trangthai not in list and check(x,queue): # BFS vs DFS
            # if x.cost < k and check(x,queue):
                queue.append(x)
        except:
            break
    return queue, False

def DFS(nguon,dich):
    list = []
    stack = collections.deque([])
    stack.append(nguon)
    OK = False
    k = 0
    while not OK:
        first = stack.pop()
        print(first.cost)
        list.append(first.trangthai)
        k = k + 1
        tapcacnutcon = first.Thucthi()
        stack, OK = add(tapcacnutcon, stack, list, dich, nguon)
    return k

def BFS(nguon, dich):
    list = []
    queue = collections.deque([])
    queue.append(nguon)
    OK = False
    k = 0
    while not OK:
        frist = queue.popleft()
        print(frist.cost)
        k = k+1
        list.append(frist.trangthai)
        tapcacnutcon = frist.Thucthi()
        queue,OK = add(tapcacnutcon,queue,list,dich,nguon)
    return k

def IDS(nguon,dich):
    n = 0
    k = 1
    OK = False
    while not OK:
        print(k)
        list = []
        stact = collections.deque([])
        stact.append(nguon)
        while not OK:
            if len(stact)==0:
                break
            frist = stact.pop()
            n = n+1
            list.append(frist.trangthai)
            tapcacnutcon = frist.Thucthi()
            stact, OK = add(tapcacnutcon,stact,list,dich,nguon,k)
        k = k + 1
    return n

def main():
    data = (1,2,5,3,4,0,6,7,8)
    dich = (0,1,2,3,4,5,6,7,8)
    nguon = BaiToan8o(data,int(math.sqrt(len(data))))
    # print("Nodes expanded: ",DFS(nguon,dich))
    print("Nodes expanded: ",BFS(nguon,dich))
    # print("Nodes expanded: ",IDS(nguon,dich))

if __name__ == '__main__':
    main()

# python driver.py dfs 6,1,8,4,0,2,7,3,5
#
# path_to_goal: ['Up', 'Left', 'Down', ... , 'Up', 'Left', 'Up', 'Left']
# cost_of_path: 46142
# nodes_expanded: 51015
# search_depth: 46142
# max_search_depth: 46142
#
# python driver.py bfs 6,1,8,4,0,2,7,3,5
#
# path_to_goal: ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up']
# cost_of_path: 20
# nodes_expanded: 54094
# search_depth: 20
# max_search_depth: 21
#
# python driver.py ast 6,1,8,4,0,2,7,3,5
#
# path_to_goal: ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up']
# cost_of_path: 20
# nodes_expanded: 696
# search_depth: 20
# max_search_depth: 20
#
# python driver.py dfs 8,6,4,2,1,3,5,7,0
#
# path_to_goal: ['Up', 'Up', 'Left', ..., , 'Up', 'Up', 'Left']
# cost_of_path: 9612
# nodes_expanded: 9869
# search_depth: 9612
# max_search_depth: 9612
#
#
# python driver.py bfs 8,6,4,2,1,3,5,7,0
#
# path_to_goal: ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left']
# cost_of_path: 26
# nodes_expanded: 166786
# search_depth: 26
# max_search_depth: 27
#
# python driver.py ast 8,6,4,2,1,3,5,7,0
#
# path_to_goal: ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left']
# cost_of_path: 26
# nodes_expanded: 1585
# search_depth: 26
# max_search_depth: 26

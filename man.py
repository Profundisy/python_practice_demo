import random
import time

class Man():

    def __init__(self,name,tili=100,money=300,cangku=[]):
        self.name = name
        self.tili = tili
        self.money = money
        self.cangku = cangku 

    def haoshi(self,time_1=5):
        self.time_1 = time_1
        x = random.randint(1,self.time_1)
        time.sleep(x)
        print('| >>>>> 耗时%d秒 ⏳             |'%x)     
        
    def dig(self,baoku):
        print('*********正在挖宝中⛏...*********')
        print("|    -按Ctrl+C可退出游戏-      |")
        self.haoshi()
        self.baoku = baoku
        num = random.randint(0,len(baoku)-1)
        #print(num)
        self.jianding(self.baoku[num])
        #print(f"-----{self.tili}------")
        self.cangku.append(baoku[num])
        if self.baoku[num] =='石头':
            self.cangku.remove('石头')
        print('|当前保存的东西为:             |')
        print(f"|>> {self.cangku}")
        del self.baoku[num]
        #print(len(self.baoku))
        print("|                              |")
        print('*********挖宝结束了💦..*********')
        self.tili -= 10
        return [self.cangku,self.tili]

    def jianding(self,baowuming):
        '''鉴定宝物的种类'''
        print('|       -开始鉴定🔍物品-       |')
        self.baowuming = baowuming
        if self.baowuming == "石头":
            self.haoshi(2)
            print('|        >无价值的石头<        |')
        if self.baowuming == "铜":
            self.haoshi(3)
            print('|        >--铜 ➕ 1--<         |')
        if self.baowuming == "铁":
            self.haoshi(5)
            print('|        >--铁 ➕ 1--<         |')
        if self.baowuming == "银":
            self.haoshi(7)
            print('|        >--银 ➕ 1--<         |')    
        if self.baowuming == "金":
            self.haoshi(10)
            print('|        >--金 ➕ 1-🤑-<       |')
        print('|        -结束鉴定物品-        |')
        print("             -👇-              ")
    
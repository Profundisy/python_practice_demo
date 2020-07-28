from settings import flush_str

class Q_Error(ValueError):
    pass

class Shop():

    def __init__(self,tilidrug=100):
        #初始化商店药水#
        self.tilidrug = tilidrug   
        
    def man_buy(self,money,tili):
        self.money = money
        self.tili = tili
        choice_drug = input('请输入购买药水的种类：\
            s小型药水🍼【可恢复10点体力,10元】\
                m中型药水🍺【可恢复50点体力，40元】\
                    l大型药水🥃【可恢复100点体力，70元】')
        if choice_drug == 's':
            self.money-=10
            self.tili+=10
        elif choice_drug == 'm':
            self.money-=40
            self.tili+=50
        elif choice_drug == 'l':
            self.money-=70
            self.tili+=100
        print('当前🙋‍♂️体力为%d'%self.tili)
        print('当前💰余额为%d'%self.money)
        return [self.tili , self.money]

    def man_sale(self,cangku,money):
        self.money = money
        self.cangku = cangku
        sale_while = True
        while sale_while:
            try: 
                flush_str('| 请输入想要卖掉的物品名',0.02)   
                self.baowuming = input('(铜，铁，银，金,all一键卖出),输入q退出:\n')
                if self.baowuming == '铜' :
                    self.money += 5
                    self.cangku.remove(self.baowuming)
                elif self.baowuming == '铁':
                    self.money += 10
                    self.cangku.remove(self.baowuming)
                elif self.baowuming == '银':
                    self.money += 30
                    self.cangku.remove(self.baowuming)
                elif self.baowuming == '金':   
                    self.money += 50
                    self.cangku.remove(self.baowuming)
                elif self.baowuming  in  ["q","Q"]:
                    raise Q_Error  
                # self.cangku.remove(self.baowuming)
                elif self.baowuming == "a":
                    while self.cangku:
                        if self.cangku[0] == '铜' :
                            self.money += 5
                        elif self.cangku[0] == '铁':
                            self.money += 10
                        elif self.cangku[0] == '银':
                            self.money += 30
                        elif self.cangku[0] == '金':   
                            self.money += 50
                        self.cangku = self.cangku[1:]
                print(self.cangku)
                if self.baowuming != 'a':
                    flush_str("%s出售成功✔"%self.baowuming,0.03)
                else:
                    flush_str("一键出售成功✔",0.03)
                flush_str('当前💰余额为%d'%self.money,0.03)
                if self.cangku == []:
                    print("仓库的宝物出售完毕")
                    raise Q_Error
            #自定义的Q_Error的范围小于VuleError 所以应该在上面
            except Q_Error:
                flush_str("|------ ---退出商店🙋‍♂--- -----|",0.08)
                break

            except ValueError:
                flush_str('你的仓库里没有%s🤷‍♂，请检查后重新输入'%self.baowuming,0.02)

        return [self.cangku ,self.money]
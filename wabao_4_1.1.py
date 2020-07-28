# 设计一个挖宝游戏 tip: random
import os

from settings import *
from man import Man
from shopping import Shop
from baocangku import Baoku


class Wabao_chushihua():

    def __init__(self,player_name,baoku_name):
        self.player_name = player_name
        self.baoku_name = baoku_name

        # 创建一个game用户
        self.player = Man(self.player_name)

        # 创建一个宝库
        self.baoku = Baoku(self.baoku_name)
        self.baoku_list = []

        # 填充宝库
        self.baoku_list = self.baoku.baoku_tianchong()

        # 创建一个商店
        self.shangdian = Shop()
        self.cjks = Cj(self.player.money)
        str_ = '%s开启了%s之旅'%(self.player_name,self.baoku_name)
        flush_str(str_,0.02)

    def game_main(self):
        '''游戏主程序'''
        try :
            while True:
                # 挖宝主体程序
                time.sleep(0.8)
                os.system('cls')

                # ctrl + c
                f = self.player.dig(self.baoku_list)

                # 如果宝库空了，游戏推出
                if len(self.baoku_list) == 0:
                    print('宝库被你挖空了')
                    break

                self.player.cangku = f[0]
                self.player.tili = f[1]

                print("|>> 当前剩余体力为%d"%self.player.tili)

                # 是否出售宝物   
                if len(self.player.cangku) > 0:
                    choice_baowu = input('|是否出售物件：(y/n)')

                    if choice_baowu == 'y':
                        c = self.shangdian.man_sale(self.player.cangku,self.player.money)
                        self.player.money = c[1]
                        self.player.cangku = c[0] 

                    else:
                        print('下次再来')

                # 是否购买体力
                if self.player.money>=10 and self.player.tili <= 20:
                    choice_tili = input('|是否购买体力？(y/n)')

                    if choice_tili == 'y':
                        d = self.shangdian.man_buy(self.player.money,self.player.tili)
                        self.player.money = d[1]
                        self.player.tili = d[0]

                    else :
                        print('你的余额不足，再见')

                # 如果体力为空，游戏结束
                if self.player.tili == 0:
                    print('体力耗尽，游戏结束了')
                    break
                
                # 是否抽奖
                if self.player.money >=5:
                    self.player.money = self.cjks.begin_cj()

        except KeyboardInterrupt:
            self.save_gamedate()


    def save_gamedate(self):
        '''存档'''
        Now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        game_data = json.dumps({"player":[self.player_name,self.player.tili,self.player.money,self.player.cangku],
                "baoku":[self.baoku_name,self.baoku_list],"time":Now_time})
        game_data_addr = ".\\game_data\\"+self.player_name+".json"

        with open(game_data_addr, 'a', encoding='utf-8') as f:
            f.write(game_data)
            f.write("\n")
            flush_str('\n|       --正在存档中🛀--       |',0.1)

        print("*---游戏结束，正在退出。。。---*")
        time.sleep(1)
        print('>>>下次再来>>>')

    def load_cundang(self,player_info,baoku_info):
        
        self.player_info = player_info
        self.baoku_info = baoku_info
        self.player_name = self.player_info[0]
        self.player.tili = self.player_info[1]
        self.player.money = self.player_info[2]
        self.player.cangku = self.player_info[3]
        self.baoku_list = self.baoku_info[1]

        return self.player_name

                
# 创建一个游戏
print("----------welcome----------")
try:
    # 捕获keyboardError
    player_name = input("| 请输入您的游戏id‍：")

    # 游戏初始化
    if not os.path.exists("game_data"):
        os.mkdir("game_data")

    player_data_name = log_in(player_name)
    flush_str(">>>>正在登录游戏中‍。。。",0.08)

    # 读档
    game_data_addr = ".\\game_data\\"+player_data_name

    try:

        with open(game_data_addr,'r') as f:
            yuanshi_game_data_all = f.readlines()
            game_date_time_list = []
            geshihua_game_data_all = []

            for game_data_line in yuanshi_game_data_all:
                # 删除每一行的\n
                game_data_line = game_data_line.strip("\n")

                # 将每行的字符型字典转换成字典
                game_data_line = eval(game_data_line)

                temp = game_data_line["time"]
                game_date_time_list.append(temp)
                geshihua_game_data_all.append(game_data_line)

            print("|  -以下是您之前的游戏存档↓↓↓-  |")

            for i in game_date_time_list:
                print(f"#  ---{i}---   #")

            choice_gamedata_time = input("|    --选哪个档- ？")

            if choice_gamedata_time in game_date_time_list:
                for i in geshihua_game_data_all:
                    if choice_gamedata_time == i["time"]:
                        game_data_choice = i
                        player_info = game_data_choice['player']
                        baoku_info = game_data_choice['baoku']
                        # cangku_info = game_data_choice

            else:
                print("您输入的存档有误")
                raise FileNotFoundError

        if player_name == player_info[0]:
            time.sleep(1)
            wabao_game = Wabao_chushihua(player_name,"王之财宝")
            print('|  -正在读档中。。。')
            wabao_game.load_cundang(player_info,baoku_info)

        # 游戏运行   
            wabao_game.game_main()

        else :
            wabao_game = Wabao_chushihua(player_name,"王之财宝")
            print('新游戏载入中。。。')
            
        # 游戏运行   
            wabao_game.game_main()

    # 开新档
    except FileNotFoundError :
        choice_quit = input("进行新游戏/y；退出游戏/n")

        if choice_quit in ["Y","y"]:
            wabao_game = Wabao_chushihua(player_name,"王之财宝")
            # 游戏运行   
            wabao_game.game_main()

        if choice_quit in ["N","n"]:
            print("正在退出游戏")
            time.sleep(0.5)
            print("再见")

except KeyboardInterrupt :
    print("\n正在退出游戏")
    time.sleep(0.5)
    print("再见")
    

    

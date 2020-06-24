import time
import json
import random


def flush_str(str_,time_len=0.05):
    for i in str_:
        print(i,end = '',flush = True)
        time.sleep(time_len)
    print("\r")
    time.sleep(0.5)

def log_in(player_name):
    game_data_addr = ".\\game_data\\player_list.json"
    try:
        with open(game_data_addr,"r") as f:
            player_name_data = json.load(f)
            #print(player_name_list)
            if player_name in player_name_data["player_name"]:
                pass
            else:
                print("| -是新用户，正在为你开启游戏...")
                player_name_data["player_name"].append(player_name)
                with open(game_data_addr,"w") as f:
                    json.dump(player_name_data,f)

    except FileNotFoundError:
        print("| -您是新用户，正在为你开启游戏...")
        with open(game_data_addr,"w") as f:
            player_name_data = {"player_name":[player_name]}
            json.dump(player_name_data,f)

    player_data_name = player_name+".json"
    return player_data_name


class Cj():
    def __init__(self,player_money):
        self.player_money = player_money
        self.jc = list(range(100))
    def begin_cj(self):
        flush_str("*********欢迎来抽奖.。..*********",0.05)
        jc = input('|-------奖池1，5🟡/次；        |\n|-------奖池2，20🟡/次；       |\n|-------奖池3，50🟡/次。       |\n|——>请选择奖池(1,2,3): ')
        print("   |")
        if jc == '1':
            #60%概率抽到5金币
            x = random.randint(0,99)
            self.player_money-=5
            print('抽奖-5🟡')
            if x in self.jc[:60]:
                self.player_money+=5
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，💴+5')
            elif x in self.jc[60:70]:
                self.player_money+=20
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，💴+20')
            else:
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('很遗憾啊🙄，你没中奖')

        elif jc == '2':
            #50%概率抽到10金币
            x = random.randint(0,99)
            self.player_money-=20
            print('抽奖-20🟡')
            if x in self.jc[:50]:
                self.player_money+=10
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+10')
            elif x in self.jc[50:70]:
                self.player_money+=30
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+30')
            elif x in self.jc[70:75]:
                self.player_money+=50
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+50')
            else:
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('很遗憾啊🙄，你没中奖')

        elif jc == '3':
            #60%概率抽到5金币
            x = random.randint(0,99)
            self.player_money-=20
            print('抽奖-50金币')
            if x in self.jc[:50]:
                self.player_money+=30
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+30')
            elif x in self.jc[50:75]:
                self.player_money+=50
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+50')
            elif x in self.jc[75:85]:
                self.player_money+=100
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+100')
            elif x in self.jc[85:90]:
                self.player_money+=200
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('恭喜中奖，金币+200')
            else:
                self.player_money+=10
                flush_str(">>>>>>>>>正在抽奖中....>>>>>>>>>",0.05)
                print('很遗憾，安慰奖啊🤨，金币+10')
        return self.player_money
                
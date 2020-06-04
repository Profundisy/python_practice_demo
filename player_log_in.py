import json
import time

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
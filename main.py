import requests
import json
import sys
import os
import time
from pystyle import Colors, Colorate # type: ignore
from datetime import datetime


os.system("cls" if os.name == "nt" else "clear")

def get_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time
def get_chr():
    time_now = get_time()
    chr_value = input("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[?] Enter chr value : "))
    if chr_value == '':
        get_chr()
    else:
        return chr_value
def get_init_data():
    time_now = get_time()
    init_data = input("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[?] Enter init_data value : "))
    if init_data == '':
        get_init_data()
    else:
        return init_data
def get_content_id():
    time_now = get_time()
    content_id = input("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[?] Enter Content-id value : "))
    if content_id == '':
        get_content_id()
    else:
        return content_id
def get_timestamp():
    time_now = get_time()
    timestamp = input("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[?] Enter time value : "))
    if timestamp == '':
        get_timestamp()
    else:
        return timestamp
    
def welcome():
    print(Colorate.Horizontal(Colors.red_to_blue, """
████████╗███████╗              ██████╗  ██████╗ ████████╗
╚══██╔══╝██╔════╝              ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ███████╗    █████╗    ██████╔╝██║   ██║   ██║   
   ██║   ╚════██║    ╚════╝    ██╔══██╗██║   ██║   ██║   
   ██║   ███████║              ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚══════╝              ╚═════╝  ╚═════╝    ╚═╝   
github.com/dimxz
                                                             
"""))
    try:
        chr_value = get_chr()
        init_data = get_init_data()

        content_id = get_content_id()
        time_stamp = get_timestamp()
        return chr_value, init_data, content_id, time_stamp

    except KeyboardInterrupt:
            time_now = get_time()
            print("\n[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[!] CTRL + C pressed, script stopped"))
            sys.exit(0)



def send_taps(access_token, content_id, time_stamp, amount):
        taps_url = "https://api.tapswap.ai/api/player/submit_taps"

        taps_headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"Bearer {access_token}",
            "Connection": "keep-alive",
            "Content-Id": content_id,
            "Content-Type": "application/json",
            "Origin": "https://app.tapswap.club",
            "Referer": "https://app.tapswap.club/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "x-app": "tapswap_server",
            "x-bot": "no",
            "x-cv": "608",
        }

        taps_count = int(amount)
        taps_payload = {"taps": taps_count, "time": int(time_stamp)}
        #print(taps_payload)
        try:
            send_tapss = requests.post(taps_url, headers=taps_headers, json=taps_payload)
            if send_tapss.status_code == 201:
                time_now = get_time()
                stp = send_tapss.json()
                coin_now = stp['player']['shares']
                delay = 30
                charge_level = stp['player']['charge_level']
                tap_level = stp['player']['tap_level']
                amount_now = int(charge_level)*delay/int(tap_level)
                print("\n[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[+] Successfully send {taps_count} taps, total coins : {coin_now}"))
                for detik in range(60, 0, -1):
                    time_now = get_time()
                    print("\r[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue,f"[~] Wait {detik} secs..."), end='')
                    time.sleep(1)
                send_taps(access_token, content_id, time_stamp, amount_now)

            else:
                time_now = get_time()
                print(send_tapss.text)
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[+] Error while sending taps : {send_tapss.status_code}"))
                sys.exit(0)
        except KeyboardInterrupt:
            time_now = get_time()
            print("\n[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[!] CTRL + C pressed, script stopped"))
            sys.exit(0)
def login(chr_value, init_data):
    
    login_url = "https://api.tapswap.ai/api/account/login"
    login_headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Origin": "https://app.tapswap.club",
        "Referer": "https://app.tapswap.club/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "x-app": "tapswap_server",
        "x-cv": "621",
        "x-bot": "no",
    } 
    
    login_payload = {
        "init_data": init_data,
        "referrer": "",
        "chr" : int(chr_value),
        "bot_key": "app_bot_1"
    }
    try:
        login_req = requests.post(login_url, headers=login_headers, data=json.dumps(login_payload))

        if login_req.status_code == 201:
            login_data = login_req.json()
            if 'access_token' in login_data:
                access_token = login_data['access_token']
                name = login_data['player']['full_name']
                coin = login_data['player']['shares']
                energy = login_data['player']['energy']
                energy_level = login_data['player']['energy_level']
                charge_level = login_data['player']['charge_level']
                tap_level = login_data['player']['tap_level']
                boosts = login_data['player']['boost']
                energy_boost = next((b for b in boosts if b["type"] == "energy"), None)
                turbo_boost = next((b for b in boosts if b["type"] == "turbo"), None)
                boost_ready = turbo_boost['cnt']
                energy_ready = energy_boost['cnt']

                time_now = get_time()
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[~] ======================================="))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Name : {name}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Coin : {coin}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Energy : {energy}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Tap Level : {tap_level}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Energy Level : {energy_level}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[~] Charge Level : {charge_level}"))
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[~] ======================================="))
                
                return access_token, tap_level, energy
            else:
                time_now = get_time()
                print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[!] Access Token not found"))
                return None, None, None, None
        elif login_req.status_code == 408:
            time_now = get_time()
            print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, "[!] Request timed out"))
        else:
            time_now = get_time()
            print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[1] Failed getting access token : {login_req.status_code}"))
    except Exception as e:
        time_now = get_time()
        print("[{}] ".format(time_now) + Colorate.Horizontal(Colors.red_to_blue, f"[!] Error : {e}"))
        sys.exit(0)
        

def main():
    w = welcome()
    l = login(w[0], w[1])
    a = l[2]/l[1]
    s = send_taps(l[0],w[2],w[3],a)
main()
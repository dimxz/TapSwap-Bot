# TapSwap Bot
This script automates the clicking process in the TapSwap game, allowing you to maximize your earnings by running continuously 24/7. Unlike the manual tapping required in the game, this script ensures every second is utilized efficiently.

Join TapSwap : [TapswapBot](https://t.me/tapswap_bot)

## Prerequisites
 - Python
 - pip
 - Telegram(Android)
 - Python server
## Installation
1. Clone the repositories
```sh
git clone https://github.com/dimxz/TapSwap-Bot
cd TapSwap-Bot
```
2. Install required modules
```sh
pip install -r requirements.txt
```
## Usage 
```sh
python main.py
```

## How to get chr, init_data, content-id, and time value 

 - Open Telegram on your Android device, navigate to the TapSwapBot, and click the "Start" button.
 - Turn off your mobile data or Wi-Fi connection. Next, click the three dots in the upper-right corner of the screen and select "Reload Page." Once the page reloads, copy the full URL that appears

 - #### chr & init_data
1. Activate developer mode on your desktop device, then open the link you got earlier
2. Go to the "Network" tab, then look for a request called "login"
3. Then open the request payload section, take the contents of "chr" and "init_data"

 - #### content-id & time
1. Activate developer mode on your desktop device, then open the link you got earlier
2. Tap on the coin image on your screen
3. In developer mode, open the network tab then look for a request named "submit_taps"
4. for Content-id, open the "Headers" section then look for "Content-id" in "Request Headers"
5. for the contents of "time", open the "Request" section then take the contents of "time"

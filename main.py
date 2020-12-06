# Author : TheHackersBrain [Gaurav Raj]
# Website : https://thehackersbrain.pythonanywhere.com/
# Note : Don't Forget to Give Credit before commiting any changes.

import argparse
import pyfiglet
from termcolor import colored
import requests
import datetime
from sys import argv


def banner():
    banner = colored(pyfiglet.figlet_format(' Dir Hunter', font='slant'), 'green')
    author = f"Author : {colored('TheHackersBrain [Gaurav Raj]', 'green')}"
    print(f"{banner}\n\t{author}\n")

def arguments():
    args = argparse.ArgumentParser()
    args.add_argument("-u", "--url", help="Target URL")
    args.add_argument("-w", "--wordlist", help="Wordlist File")
    arg = args.parse_args()

def help():
    print(""" Usage :
         python3 main.py -u <target_url> -w <wordlist>\n
    ex : python3 main.py https://www.google.com/ -w /path/to/wordlist
    """)

def bruteforce(wordlist):
    h = arg.url
    if not h.endswith('/'):
        h = h+"/"
    x = datetime.datetime.now()
    st_dt = x.strftime("%Y/%m/%d")
    st_tm = x.strftime("%H:%M:%S")
    print(f"""===============================================================
DirHunter v1.0
by {colored('TheHackersBrain [Gaurav Raj]', 'green')}
===============================================================
[+] URL:           {h}
[+] Wordlists:     {wordlist}
[+] Status Code:   200, 302, 404
[+] Timeout :      10s
===============================================================
{st_dt} {st_tm} Starting DirHunter
===============================================================""")
    with open(wordlist, 'rt') as wordlists:
        word = wordlists.readlines()
        for i in word:
            host = h+i.strip("\n")
            r = requests.get(host)
            if r.status_code == 200:
                print(f"[{colored('+', 'green')}] {host} \t{colored(r.status_code, 'green')}")
            elif r.status_code == 302:
                print(f"[{colored('*', 'yellow')}] {host} \t{colored(r.status_code, 'yellow')}")
            else:
                pass
        x = datetime.datetime.now()
        end_dt = x.strftime("%Y/%m/%d")
        end_tm = x.strftime("%H:%M:%S")
        print(f"""===============================================================
{end_dt} {end_tm} Finished
===============================================================""")

args = argparse.ArgumentParser()
args.add_argument("-u", "--url", help="Target URL")
args.add_argument("-w", "--wordlist", help="Wordlist File")
arg = args.parse_args()

if len(argv) != 5:
    banner()
    help()
    exit()

if __name__ == "__main__":
    try:
        banner()
        bruteforce(wordlist=arg.wordlist)
    except Exception as e:
        x = datetime.datetime.now()
        end_dt = x.strftime("%Y/%m/%d")
        end_tm = x.strftime("%H:%M:%S")
        print(f"""[!] Timeout Exceeded.
===============================================================
{end_dt} {end_tm} Finished
===============================================================
""")
    except KeyboardInterrupt as keyerr:
        x = datetime.datetime.now()
        end_dt = x.strftime("%Y/%m/%d")
        end_tm = x.strftime("%H:%M:%S")
        print(f"""[!] Keyboard interrupt detected, terminating.
===============================================================
{end_dt} {end_tm} Finished
===============================================================
""")
    except EOFError as endoffile:
        print()

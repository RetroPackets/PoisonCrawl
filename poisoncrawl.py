
import requests
from colorama import Fore,Style
import os
import re
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


os.system("clear")
print("Loading...")


os.system("clear")

print(f"""{Fore.WHITE}
     ___________________________________________________________
     ___________________________¶___¶___________________________
     __________________________¶_____¶__________________________
     _________________________¶_______¶_________________________
     ________________________¶_________¶________________________
     ________________________¶_________¶________________________
     _______________________¶¶_________¶¶_______¶_______________
     _______________¶_______¶___________¶_______¶_______________
     _______________¶______¶¶___________¶¶______¶_______________
     _______________¶¶_____¶¶___________¶¶_____¶¶_______________
     _________¶_____¶¶_____¶¶___________¶¶_____¶¶_____¶_________
     _________¶¶_____¶_____¶¶___________¶¶_____¶¶_____¶_________
     _________¶¶_____¶¶____¶¶___________¶¶____¶¶_____¶¶_________
     __________¶¶____¶¶¶___¶¶¶_________¶¶¶___¶¶¶____¶¶__________
     ___________¶¶¶___¶¶¶__¶¶¶_________¶¶¶__¶¶¶____¶¶___________
     ____________¶¶¶___¶¶¶__¶¶¶_______¶¶¶¶_¶¶¶___¶¶¶____________
     _____________¶¶¶¶¶_¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶_¶¶¶¶¶_____________
     _______________¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶______________
     _______________¶¶¶¶¶___¶¶¶¶¶_¶_¶¶¶¶¶¶___¶¶¶¶¶_______________
     ______________¶¶¶¶________¶¶¶¶¶¶¶________¶¶¶¶______________
     ______________¶¶¶_____¶____¶¶¶¶¶____¶_____¶¶¶______________
     _____________T¶¶________¶___¶¶¶___¶________¶¶¶_____________
     _____________¶¶¶________¶¶___¶___¶¶________¶¶¶_____________
     ______________¶¶¶_______¶¶¶_____¶¶¶_______¶¶¶______________
     _______________¶¶¶_____¶¶¶¶¶___¶¶¶¶¶_____¶¶¶¶______________
     ________________¶¶¶¶¶¶¶¶¶_¶¶___¶¶_¶¶¶¶¶¶¶¶¶________________
     __________________¶¶¶¶¶___¶¶___¶¶___¶¶¶¶¶__________________
     __________________________¶¶___¶¶__________________________
     __________________________¶¶___¶¶__________________________
     __________________________¶_____¶__________________________
     _________________________¶¶_____¶¶_________________________
     _________________________¶_______¶_________________________
     ________________________¶_________¶________________________
     ______________________¶_____________¶______________________
     ___________________________________________________________
          
{Fore.GREEN}███████████████████████████████████████████████████████████████████████
{Fore.WHITE}█▄─▄▄─█─▄▄─█▄─▄█─▄▄▄▄█─▄▄─█▄─▀█▄─▄███─▄▄▄─█▄─▄▄▀██▀▄─██▄─█▀▀▀█─▄█▄─▄███
{Fore.WHITE}██─▄▄▄█─██─██─██▄▄▄▄─█─██─██─█▄▀─████─███▀██─▄─▄██─▀─███─█─█─█─███─██▀█
{Fore.GREEN}▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀

            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            |  {Fore.MAGENTA} Coded By:{Fore.WHITE} RetroPackets           {Fore.GREEN}         |
            |   {Fore.MAGENTA} Github :{Fore.WHITE} https://github.com/RetroPackets {Fore.GREEN}|
            |{Fore.MAGENTA} Instagram :{Fore.WHITE} retropacketz              {Fore.GREEN}      |
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     {Fore.RED}Enter URL Without {Fore.MAGENTA}[{Fore.BLUE}https://{Fore.MAGENTA}]""")
print(f"{Fore.CYAN}")
crawl1 = input(f"Enter Website : {Fore.GREEN}")

for _ in tqdm (range (1000), 
               desc=f"{Fore.MAGENTA}Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)




print(f"""
{Fore.WHITE}[*] Extracting Links From {Fore.GREEN}{crawl1}""")
print("")
os.system(f"python3 src/linkscrape.py -d https://{crawl1}")

print(f"""
{Fore.WHITE}[*] RUNNING SUBDOMAIN SCAN ON WEBSITE{Fore.MAGENTA}

    Please Be Patient {Fore.BLUE}[PoisonCrawl]{Fore.MAGENTA}
    Is Scanning 20,000 Subdomains
    From File {Fore.BLUE}[subdomains.txt]{Fore.WHITE}
""")
os.system(f"python3 src/subs.py https://{crawl1}")

print(
    f"""
{Fore.WHITE}[*] CONFIRMING SUBDOMAIN RESULTS FOR{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"python3 src/subs2.py -d https://{crawl1}")

print(
    f"""
{Fore.WHITE}[*] CHECKING FOR OPEN PORTS FOR{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"nmap {crawl1}")

print(
    f"""
{Fore.WHITE}[*] EXTRACTING NAME SERVERS FROM{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"host -t ns {crawl1}")

print(
    f"""
{Fore.WHITE}[*] EXTRACTING IP ADDRESSES FROM{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"host -t a {crawl1}")

print(
    f"""
{Fore.WHITE}[*] EXTRACTING AAAA RECORD FROM{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"host -t aaaa {crawl1}")

print(f"""
{Fore.WHITE}[*] RUNNING MX SCAN FOR{Fore.GREEN} {crawl1}""")
print(f"{Fore.YELLOW}")
os.system(f"host -t mx {crawl1}")

print(
    f"""
{Fore.WHITE}[*] EXTRACTING SOA RECORD FROM{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"host -t soa {crawl1}")

print(
    f"""
{Fore.WHITE}[*] RUNNING TRACEROUTE SCAN FOR{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"nmap -Pn -T4 --traceroute www.{crawl1}")

print(
    f"""
{Fore.WHITE}[*] CHECKING FOR DOS VULNS FOR{Fore.GREEN} {crawl1}"""
)
print(f"{Fore.YELLOW}")
os.system(f"nmap -v --script dos {crawl1}")


print(f"""
{Fore.WHITE}[*] EXTRACTING EMAILS FROM{Fore.GREEN} {crawl1}""")
print(f"{Fore.YELLOW}")


starting_url = f'http://{crawl1}/'

unprocessed_urls = deque([starting_url])
emails = set()

processed_urls = set()
while len(unprocessed_urls):

    url = unprocessed_urls.popleft()
    processed_urls.add(url)

    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    print(f"[*] Crawling URL {url}")
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
    print(emails)
    soup = BeautifulSoup(response.text, 'lxml')


    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link

        if link not in unprocessed_urls and link not in processed_urls:
            unprocessed_urls.append(link)


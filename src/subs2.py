import os
from colorama import Fore,Style
import requests
import time
import urllib3
import sys




def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True, help='Target Domain.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output to file.')
    return parser.parse_args()


def banner():
    global version
    print(' ')

    time.sleep(1)

def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print(f'{Fore.RED}[*] Invalid domain, try again..')
    return host

def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')
        


def main():
    banner()
    args = parse_args()
    target = parse_url(args.domain)
    output = args.output

    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

    if req.status_code != 200:
        print(f'{Fore.RED}[*] Information Not Available!')


    subdomains = [value['name_value'] for value in req.json()]
    subs = sorted(set(subdomains))

    for s in subs:
        print(f'{s}\n')
        if output is not None:
            write_subs_to_file(s, output)



if __name__=='__main__':
    main()

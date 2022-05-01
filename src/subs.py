import requests
import sys
from datetime import datetime
from colorama import Fore,Style

def subdomain_finder(domain):
    with open("src/subdomains/subdomains20k.txt","r") as f:
        for i in f:
            sub_domain = i.strip()
            new_url = sub_domain + "." + domain
            try:
                res = requests.get(new_url)
                print ("[*] Discovered Subdomain :",new_url)
            except:
                pass
        
if len (sys.argv) < 2:
    print(f"{Fore.LIGHTMAGENTA_EX}*"*50)


else:
    domain = sys.argv[1]
    
    s = datetime.now()
    print("    Script Started At :",s)
    subdomain_finder(domain)
    print("    Total Time taken :",datetime.now()-s)


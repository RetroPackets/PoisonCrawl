
from datetime import datetime
from termcolor import colored
import requests
import sys
from bs4 import BeautifulSoup
import os

foundLinks = []
foundInternal = []
foundExternal = []


#def welcome_message():  
    


def print_help(): 
    print("HELP :\n"
          "     -h | --help | Prints this message.\n"
          "     -d | --domain [Domain to test] | Start crawling a domain.\n"
          "     -o | --ofile [File path or name] | Write the output to a file.\n")


def print_error():  
    print(colored("ERROR: Wrong input !\n", "red"))
    print_help()


def showStats(nbrInternalFound, nbrExternalFound, startTime): 
    totalNbr = len(foundLinks)
    time_elapsed = datetime.now() - startTime
    print(
        colored(
            (
                "    Link Extraction Finished !\n"
                "    PoisonCrawl found "
                + str(len(nbrInternalFound))
                + " Internal link(s) and "
                + str(len(nbrExternalFound))
                + f" External link(s),\n    Time elapsed {time_elapsed}:".split(
                    '.'
                )[
                    0
                ]
            )
        )
    )


def read_args():  
    global domain
    global domainHTML
    global output_path
    if len(sys.argv) == 1:
        print_help()
        exit()
    elif len(sys.argv) == 2:
        if sys.argv[1] in ['', '-h', '--help']:
            print_help()
            exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-d', '--domain']:
            domain = sys.argv[2]
            domainHTML = str(BeautifulSoup(requests.get(domain).content, "html.parser"))
    elif len(sys.argv) == 4:
        if sys.argv[1] == '-d' or sys.argv[1] == '--domain' and sys.argv[3] == '-o' or sys.argv[3] == '--ofile':
            domain = sys.argv[2]
            domainHTML = str(BeautifulSoup(requests.get(domain).content, "html.parser"))
            output_path = sys.argv[4]
    else:
        print_error()


def crawl(domainHTML):  
    href = domainHTML.find("a href")
    if href == -1:
        return None, 0
    openQuote = domainHTML.find('"', href)
    closeQuote = domainHTML.find('"', openQuote + 1)
    domain = domainHTML[openQuote + 1: closeQuote]
    return domain, closeQuote


def main(): 
    global domainHTML
    global foundLinks
    #welcome_message()
    read_args()
    start = datetime.now()
    crawl(domainHTML)
    while True:
        domain, n = crawl(domainHTML)
        domainHTML = domainHTML[n:]
        if domain:
            internalOrExternal(domain)
            foundLinks.append(domain)
        else:
            break
    showStats(foundInternal, foundExternal, start)
    if len(foundExternal) > 0:
        moreCrawl()
    else:
        exit()


def internalOrExternal(link):  
    if domain in link:
        print(colored(f"Found external link: {link}", "green"))
        foundExternal.append(link)
    elif link != "":
        print(colored(f"Found internal link: {link}", "yellow"))
        foundInternal.append(link)


def moreCrawl(): 
    global domain
    choice = input(
        colored("""
[*] PoisonCrawl Found """ + str(len(foundExternal)) + " link(s) would you like to crawl them too ? [Y/n] "))
    if choice in ["", "Y", "y"]:
        domain = foundExternal[0]
        foundExternal.clear()
        foundInternal.clear()
        foundLinks.clear()
        main()
    elif choice in ["n", "N"]:
        print("")
        exit()
    else:
        print(colored("Wrong input !", "red"))
        moreCrawl()


if __name__ == "__main__":
    main()

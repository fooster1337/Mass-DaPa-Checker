import requests, re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from bs4 import BeautifulSoup as soap
from colorama import Fore, init
init()
reset = Fore.RESET
yellow = Fore.YELLOW

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def fdom(url):
    if '://' in url:
        dom = url
    else:
        dom = 'http://'+dom
    return urlparse(dom).scheme + '://' + urlparse(dom).netloc

def checker(url):
    try:
        dom = fdom(url)
        data = {
            'domain': dom,
            'submit': 'Get+Website+Metrics'
        }
        req = soap(requests.post('https://www.countingcharacters.com/website-authority-checker', headers=headers, data=data).text, 'html.parser').find_all('span', {'style':'color:#2d3436'})
        if req:
            da, pa = req[0].get_text(), req[1].get_text()
            if (da, pa):
                print(f"{dom} DA : {yellow}{da}{reset} PA : {yellow}{pa}{reset}")
                open('result.txt', 'a+').write(f'{dom} DA : {da} PA : {pa}'+'\n')
            else:
                print(f"{dom} DA : {yellow}1{reset} PA : {yellow}1{reset}")
                open('result.txt', 'a+').write(f'{dom} DA : 1 PA : 1'+'\n')
        else:
            print(req)
            print(f"{dom} {Fore.RED}Error{reset}")
    except Exception as e: print(e)
    #print(req)
    #print(a)

def main():
    banner = """
    Mass Dapa Checker by @GrazzMean
    Don't Buy. Its Free Tools!
    """
    print(banner)
    doml = open(input("Domain List : "), 'r').read().splitlines()
    for dom in doml:
        checker(dom)

if __name__ == '__main__':
    #checker('http://fooster1337.net')
    main()

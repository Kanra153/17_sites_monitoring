import sys
import os
import whois
import datetime
import requests


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as file_handler:
        urls = file_handler.read().split()
    return urls


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code


def get_domain_expiration_date(url):
    try:
        return whois.whois(url)['expiration_date'][0]
    except TypeError:
        return whois.whois(url)['expiration_date']


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('File is not found!')
    path = sys.argv[1]
    urls = load_urls4check(path)
    now = datetime.datetime.now()
    for url in urls:
        print(url)
        print('The server response code is: ', 
              is_server_respond_with_200(url))
        days_until_expiration = get_domain_expiration_date(url)-now
        print('Days until expiration: ',
              days_until_expiration.days, '\n')

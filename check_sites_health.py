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
    status_code = response.status_code
    return True if status_code == 200 else False


def get_domain_expiration_date(url):
    if isinstance(whois.whois(url)['expiration_date'], list):
        return whois.whois(url)['expiration_date'][0]
    return whois.whois(url)['expiration_date']


def output_results_to_console(urls, now):
    for url in urls:
        print(url)
        print('Is server respond with 200?: ',
              is_server_respond_with_200(url))
        days_until_expiration = get_domain_expiration_date(url)-now
        print('Days until expiration: ',
              days_until_expiration.days, '\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('File is not found!')
    path = sys.argv[1]
    urls = load_urls4check(path)
    now = datetime.datetime.now()
    output_results_to_console(urls, now)

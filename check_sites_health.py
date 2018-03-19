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
    if response.status_code == requests.codes.ok:
        return True if status_code == 200 else False
    else:
        return None


def get_domain_expiration_date(url):
    date = whois.whois(url)['expiration_date']
    if isinstance(date, list):
        return date[0]
    return date


def is_domen_name_paid(date, now):
    days_until_expiration = date-now
    if (days_until_expiration.days > 28):
        date_answer = True
    else:
        date_answer = False
    return date_answer


def output_results_to_console(server_answer, date_answer):
    print(url)
    print('Is server respond with 200?: ', server_answer)
    if date == None:
        print('Expiration date is not stated', '\n')
    else:
        print('Is domen name paid for a next month?: ',
              date_answer, '\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Input filepath!')
    path = sys.argv[1]
    urls = load_urls4check(path)
    now = datetime.datetime.now()
    for url in urls:
        date = get_domain_expiration_date(url)
        output_results_to_console(
            is_server_respond_with_200(url),
            is_domen_name_paid(date, now)
        )

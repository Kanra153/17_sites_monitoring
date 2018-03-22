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


def is_server_respond_ok(url):
    response = requests.get(url)
    return response.status_code == requests.codes.ok


def get_domain_expiration_date(url):
    expiration_date = whois.whois(url)['expiration_date']
    if isinstance(expiration_date, list):
        return expiration_date[0]
    return expiration_date


def is_domen_name_paid(expiration_date, now, days_in_month = 28):
    days_until_expiration = expiration_date-now
    return days_until_expiration.days > days_in_month


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
    now = datetime.datetime.today()
    for url in urls:
        date = get_domain_expiration_date(url)
        output_results_to_console(
            is_server_respond_ok(url),
            is_domen_name_paid(date, now)
        )

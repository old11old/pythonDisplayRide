#!/bin/env python

import requests
import time
import urllib
# from lxml import html

EMAIL = 'flurry@displayride.com'
PASSWORD = 'displayflurry246'
PROJECT_ID =1

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8,de;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "dev.flurry.com",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
}


def get_session(email, password):
    session = requests.session()
    session.headers = HEADERS
    params = {
        'loginEmail': email,
        'loginPassword': password
    }
    url = 'https://dev.flurry.com/secure/loginAction.do'
    response = session.post(url, data=params)
    response.raise_for_status()
    tree = html.fromstring(response.text)
    struts_token = tree.xpath('//input[@name="token"]')[0]
    return session, struts_token.value


# def get_csv(session, struts_token):
#     params = {
#         "projectID": str(PROJECT_ID),
#         "versionCut": "versionsAll",
#         "intervalCut": "30Days",
#         "childProjectId": "0",
#         "stream": "true",
#         "direction": "1",
#         "offset": "0",
#         # "struts.token.name": struts_token,
#     }
#     url = 'https://dev.flurry.com/eventsLogCsv.do?' + urllib.urlencode(params)
#     response = None
#     while response is None:
#         response = session.get(url)
#         if response.status_code == 302:
#             location = response.headers['location']
#             if location == 'https://dev.flurry.com/secure/login.do':
#                 raise Exception('Invalid email/password')
#             if location == 'http://www.flurry.com/rateLimit.html':
#                 print
#                 'Throttled. Sleeping.'
#                 time.sleep(60)
#             response = None
#
#     f = open('flurry.csv', 'w')
#     f.write(response.content)
#     f.close()
#

session, struts_token = get_session(EMAIL, PASSWORD)
print('session:{} struts_token:{}'.format(session,struts_token) )
# get_csv(session, struts_token)
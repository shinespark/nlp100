# -*- coding: UTF-8 -*-

from urllib import request, parse
import collections
import json
import sys

argvs = sys.argv
argc = len(argvs)

if argc < 3:
    print('Usage: python test.py token search_word')
    sys.exit()

token = argvs[1]
search_word = parse.quote(argvs[2])
url = 'https://slack.com/api/search.messages?token=' + token + '&query=' + search_word + '&count=1000'
print(url)

res = request.urlopen(url).read()
matches = json.loads(res.decode('utf-8'))['messages']['matches']

count_dict = collections.Counter()
for post in matches:
    if post['type'] == 'message' and post['user'] != '':
        count_dict[post['username']] += 1

for l in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
    print(l)

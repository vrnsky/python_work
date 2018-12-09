﻿import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print('Status code:', response.status_code)

submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
	urlSub = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
	submission_r = requests.get(urlSub)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	submission_dict = {
		'title':response_dict['title'],
		'link':'https://news.ycombinator.com/item?id=' + str(submission_id),
		'comments': response_dict.get('descendants', 0)
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
	print("\nTitle:", str(submission_dict['title']).encode('utf-8'))
	print("Discussion link:", submission_dict['link'])
	print("Comments:", 	submission_dict['comments'])

﻿import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

response = requests.get(url)
print('Status code: ' + str(response.status_code))

response_dict = response.json()
print('Total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []

for repo_dict in repo_dicts:
	description = repo_dict['description']
	names.append(repo_dict['name'])

	if not description:
		description = 'No description provided'
	plot_dict = {
		'value' : repo_dict['stargazers_count'],
		'label' : description,
		'xlink' : repo_dict['html_url']
	}
	plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style = LCS)
my_style.title_font_size = 24
my_style.lbale_font_size = 18
my_style.major_label_fron_size = 18
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names


chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
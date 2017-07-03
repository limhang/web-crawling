from pprint import pprint
from goose import Goose
from goose.text import StopWordsChinese
import re
source_file = open('url_list.md','r')
source_data = source_file.read()
source_array = re.split('--', source_data)

def getUrl(item):
	url_name = re.split('&&', item)
	url = url_name[1]
	name = url_name[0]
	print url

	print name

	html_name = name + '.html'
	print html_name
	g = Goose({'stopwords_class': StopWordsChinese})
	article = g.extract(url=url)
	# print article.raw_html
	f = open(html_name,'a')
	f.write(article.raw_html)
# f.write(article.cleaned_text.encode('utf-8'))
	f.close()
# pprint (vars(article))

for item in source_array:
	getUrl(item)


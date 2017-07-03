from pprint import pprint
from goose import Goose
from goose.text import StopWordsChinese
import re
import os
source_file = open('source.md','r')
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
	currentDir = os.getcwd() + '/' + 'pages' + '/' + name
	if not os.path.exists(currentDir):
		os.makedirs(currentDir)
	f = open(currentDir + '/' +html_name,'a')
	f.write(article.raw_html)
	f.close()
	#print article.title

	f_md = open(currentDir + '/' + name + '.md' ,'a')
	f_md.write(article.cleaned_text.encode('utf-8'))
	f_md.close()
# pprint (vars(article))

for item in source_array:
	getUrl(item)




# url = 'http://42.96.209.98:44719/index.php'
# g = Goose({'stopwords_class': StopWordsChinese})
# article = g.extract(url=url)
# print article.cleaned_text
# # print article.raw_html
# f = open('xxx.html','a')
# f.write(article.raw_html)
# # f.write(article.cleaned_text.encode('utf-8'))
# f.close()
# # pprint (vars(article))


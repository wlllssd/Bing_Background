import urllib.request
url = 'https://cn.bing.com'
def get_pic_address(html):
	global url
	s = ['id="bgLink"','href="','.jpg']
	content = html.partition(s[0])[2]
	content = content.partition(s[1])[2]
	content = content.partition(s[2])[0]
	return url+content+s[2]

def get_pic_info(html):
	global url
	s = ['class="sc_light"','title="','"']
	info = {}
	content = html.partition(s[0])[2]
	content = content.partition(s[1])[2]
	content = content.partition(s[2])[0]
	pic_name = content.partition('，')[0]
	pic_pos = content.partition('，')[2].partition(' (')[0]
	author = content.partition('(')[2].partition(')')[0]
	info = {'name':pic_name,'position':pic_pos,'author':author}
	return info

def gethtml(url):
	page = urllib.request.urlopen(url)
	html = page.read() # type(html) is 'bytes'
	html = html.decode('utf-8') # type(html) is 'str'
	return html

def save_img(pic_url,pic_info):
	byte = urllib.request.urlopen(pic_url)
	with open('imags/{name}.jpg'.format(**pic_info),'ab+') as f:
		f.write(byte.read())
		f.flush()

def run():
	global url
	html = gethtml(url)
	pic_url = get_pic_address(html)
	pic_info = get_pic_info(html)
	save_img(pic_url, pic_info)

run()



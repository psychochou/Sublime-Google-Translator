# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import urllib, json
import ssl
import codecs
from urllib.parse import quote

url_str_google_1="https://translate.google.cn/translate_a/single?client=gtx&sl=zh&tl="
url_str_google_2="&dt=t&dt=bd&ie=UTF-8&oe=UTF-8&dj=1&source=icon&q="
context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.options |= ssl.OP_NO_SSLv2
context.options |= ssl.OP_NO_SSLv3
context.options |= ssl.OP_NO_TLSv1
https_sslv3_handler = urllib.request.HTTPSHandler(context)
opener = urllib.request.build_opener(https_sslv3_handler)
urllib.request.install_opener(opener)

class GoogleTranslateEnglishToChinese(sublime_plugin.TextCommand):
	def run(self, edit):
		query=self.view.substr(self.view.sel()[0])
		print(query)
		query=str(query.encode('utf8').decode())
		url=url_str_google_1+"en"+url_str_google_2+quote(query)
		#print(url)
		q=urllib.request.Request(url);
		q.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
		response=opener.open(q)
		#charset = response.info().get_param('charset', 'utf8')
		#reader = codecs.getreader("utf-8")
		decoded = json.loads(response.read().decode('utf8'))

		#print(b'\xe6\x88\x91\xe4\xbb\xac'.decode('utf-8'))
		
		# print(decoded)
		value=''
		for trans in decoded['sentences']:
			value=value+trans['trans']
		#print(value)
		#print(decoded['sentences'][0]['trans'])
		
		self.view.insert(edit, self.view.sel()[0].end(), value)



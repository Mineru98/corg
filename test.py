from konlpy.tag import Hannanum
from newspaper import Article

url = 'http://v.media.daum.net/v/20170604205121164'
a = Article(url, language='ko')
a.download()
a.parse()

hannanum = Hannanum()
text = hannanum.nouns(a.text)

print(text)

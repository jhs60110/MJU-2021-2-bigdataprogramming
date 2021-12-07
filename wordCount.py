from konlpy.tag import Okt
from collections import Counter

okt = Okt()

file = open('newslist.txt', "r", encoding='UTF-8')
text = file.read()
#명사만 추출
nouns = okt.nouns(text)
# 한글자 제거
text = [x for x in nouns if len(x) > 1]

#불용어 정의
korean_stopwords_path = "C:/Users/jhs60/korean_stopwords.txt"
with open(korean_stopwords_path, encoding='utf-8') as f:
	stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]

# 불용어 제거
text = [x for x in text if x not in stopwords]

count = Counter(text).most_common()

print(count[0:100])
#text = pd.DataFrame(text, columns=['word', 'count'])
#folder_path = os.getcwd()

#text.to_csv('most_word.txt')
#os.startfile(folder_path)

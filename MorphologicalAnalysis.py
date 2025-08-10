from fugashi import Tagger

tagger = Tagger()
text = "形態素解析したい任意の文章を入力"

for word in tagger(text):
    print(word.surface, word.feature)


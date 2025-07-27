from fugashi import Tagger

tagger = Tagger()
text = "彼はそれを見て笑ったが、私は少し怖かった。"

for word in tagger(text):
    print(word.surface, word.feature)


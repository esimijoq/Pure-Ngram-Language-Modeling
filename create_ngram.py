import requests


texts = ["What a truly wonderful day! The sun is shining, birds are singing, and everything feels absolutely perfect. I'm filled with immense joy and gratitude. Life is beautiful.", "This new restaurant is simply fantastic! The food was delicious, the service impeccable, and the atmosphere delightful. I highly recommend it; a truly enjoyable experience overall.", "Today has been utterly miserable. The rain poured incessantly, my internet kept crashing, and I felt completely overwhelmed. A truly frustrating and disappointing day.", "I'm so incredibly upset with this product. It broke almost immediately, the support was unhelpful, and I feel completely ripped off. A terrible purchase, I regret it."]

texts_new = []
for text in texts:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","")
  texts_new.append(text_new)


with open("/content/drive/MyDrive/Colab Notebooks/texts.txt", 'r') as file:
  f = file.read()
  text_txt = f.split("\n\n")

texts_from_txt = []
for text in text_txt:
  text_new = text.replace(".", "").replace("!","").replace(",","").replace("'","").replace(";", "").replace("\n", "")
  texts_from_txt.append(text_new)

for text in texts_from_txt:
  texts_new.append(text)

texts_new_split = []
for text in texts_new:
  txt = text.split(" ")
  texts_new_split.append(txt)

print(texts_new_split)

bigrams = {}
for text in texts_new_split:
  for i in range(len(text)-1):
    word1 = text[i]
    word2 = text[i+1]
    t = (word1, word2)

    if not t in bigrams:
      bigrams[t] = 1
    else:
      bigrams[t] += 1
print(bigrams)

trigrams = {}
for text in texts_new_split:
  for i in range(len(text)-2):
    word1 = text[i]
    word2 = text[i+1]
    word3 = text[i+1+1]
    t = (word1, word2, word3)

    if not t in trigrams:
      trigrams[t] = 1
    else:
      trigrams[t] += 1
print(trigrams)


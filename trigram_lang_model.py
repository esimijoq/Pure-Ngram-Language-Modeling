import requests

with open("/content/drive/MyDrive/Colab Notebooks/the_stories_eng.txt",'r') as file:
  f = file.read()
  texts = f.split("\n\n")

txt = []
for text in texts:
  text_1 = text.replace(".", "").replace("!","").replace(",","").replace("'","").replace(";", "").replace("\n", " ").replace("\n\n", "")
  txt.append(text_1)

text_split = []
for text in txt:
  txt = text.split(" ")
  text_split.append(txt)

print(text_split)

trigrams = {}
for text in text_split:
  for i in range(len(text)-2):
    word1 = text[i]
    word2 = text[i+1]
    word3 = text[i+1+1]

    if not word1 in trigrams:
      trigrams[word1] = {}

    if not word2 in trigrams[word1]:
      trigrams[word1][word2] = {}

    if not word3 in trigrams[word1][word2]:
      trigrams[word1][word2][word3] = 1
    else:
      trigrams[word1][word2][word3] += 1

print(trigrams)

def next_word(word1, word2):
  if word1 in trigrams:
    if word2 in trigrams[word1]:
      next_word = trigrams[word1][word2]
      most_probable = max(next_word, key=next_word.get)
    return most_probable

print(next_word('I', 'am'))

def sentence_new(word1, word2):
  sentence = [word1,word2]
  for i in range(10):
    word3 = next_word(word1, word2)
    word1 = word2
    word2 = word3
    sentence.append(word3)
  return sentence

print(sentence_new('For', 'there'))

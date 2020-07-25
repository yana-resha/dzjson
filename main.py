import json

with open("newsafr.json", encoding = "utf-8") as f:
  json_data = json.load(f)
#print(json_data)
news_list = json_data["rss"]["channel"]["items"]
#print(news_list)

word_list = []

for news in news_list:
  news2 = news["description"]
  #print(news2)
  n_list = news2.split(" ")
  #print(n_list)
  for w in n_list:
    if len(w) >= 6:
      word_list.append(w)
      #print(word_list)

from collections import Counter
long_words = Counter(word_list).most_common(10)
for k in long_words:
  print(k) 



  
    





    




 



%pip install googletrans==3.1.0a0 

import json
from googletrans import Translator

# 파일 경로는 /en_us.json
with open("/en_us.json", "r") as json_file:
    data = json.load(json_file)

en_us = []
ko_kr = []

imsi = ""
for a in data:
  for b in data[a]:
    imsi = imsi + b
  en_us.append(imsi)
  imsi = ""

for en in en_us:
  # src='en' 부분이 원문, dest='ko'부분이 번역문, src 부분을 바꾸거나 지우면 그 언어로 가능.
  if en != "":
    ko = Translator().translate(en, src='en', dest='ko').text
  else:
    ko = ""
  ko_kr.append(ko)

i = 0
for key in data:
  data[key] = ko_kr[i]
  i = i + 1
done = json.dumps(data, indent="\t", ensure_ascii=False)
# print(done)

# 파일 경로는 /ko_kr.json
with open("/ko_kr.json", "w") as file:
    file.write(done)
print("\n\ndone.")

import json
import gzip
from random import shuffle

json_string = None

with gzip.open('dict_en_US.bookmarks', 'rb') as f:
    file_content = f.read()
    json_string = file_content.splitlines()[2]
    
js = json.loads(json_string)

bookmarks_list = js['bookmarks']

for entry in bookmarks_list:
  word = entry.split('|')[1]
  print(word)

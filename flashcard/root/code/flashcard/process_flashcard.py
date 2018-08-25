#!/usr/bin/env python3
from flask import render_template
from random import shuffle


synonyms_content_lines = []
word_list_name = ""
word_list_size = -1
word_list = []
current_word = ""
current_word_cursor = -1

#data_dir = "/home/AnmolSinghJaggi/root/data/flashcard/"
data_dir = "data/flashcard/"

def load_file():
    global word_list_name
    global word_list
    global current_word_cursor
    global current_word
    global word_list_size
    word_list_file_content = open(data_dir + word_list_name + ".txt").read()
    lines = word_list_file_content.splitlines()
    word_list = []
    for line in lines:
      words = line.split()
      for word in words:
        if len(word) > 1:
          word_list.append(word)
    shuffle(word_list)
    word_list_size = len(word_list)
    current_word_cursor = 0
    current_word = word_list[current_word_cursor]


def handle_GET():
    global word_list_name
    global current_word_cursor
    global current_word
    global word_list_size
    word_list_name = "synonyms"
    if len(word_list) == 0:
        load_file()
    template_content = render_template("index_flashcard.html", word_list_name=word_list_name, word_list_size=word_list_size, current_word=current_word, current_word_cursor=current_word_cursor)
    return template_content


def handle_next_word():
    global word_list_name
    global current_word_cursor
    global current_word
    global word_list_size
    current_word_cursor = current_word_cursor + 1
    if current_word_cursor >= word_list_size:
        current_word = 'Out of words!!'
    else:
        current_word = word_list[current_word_cursor]
    template_content = render_template("index_flashcard.html", word_list_name=word_list_name, word_list_size=word_list_size, current_word=current_word, current_word_cursor=current_word_cursor)
    return template_content


def show_synonyms():
    result = ""
    global synonyms_content_lines
    lines = []
    if len(synonyms_content_lines) == 0:
        synonyms_content = open(data_dir + 'synonyms.txt').read()
        synonyms_content_lines = synonyms_content.splitlines()
    global current_word
    for line in synonyms_content_lines:
        if current_word in line.split():
          result += line + "\n"
    return result


def handle_synonyms():
    synonyms = show_synonyms()
    template_content = render_template("index_flashcard.html", word_list_name=word_list_name, word_list_size=word_list_size, current_word=current_word, current_word_cursor=current_word_cursor, synonyms = synonyms)
    return template_content


def handle_change_list(request):
    global word_list_name
    word_list_name = request.form['change_list']
    print(word_list_name)
    load_file()
    template_content = render_template("index_flashcard.html", word_list_name=word_list_name, word_list_size=word_list_size, current_word=current_word, current_word_cursor=current_word_cursor)
    return template_content
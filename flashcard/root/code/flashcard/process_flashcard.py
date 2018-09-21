#!/usr/bin/env python3
from flask import render_template
from random import shuffle


word_list_names = []
word_list_names.append('synonyms.txt')
word_list_names.append('bookmarks.txt')
word_list_names.append('bookmarks_difficult.txt')


synonyms = {}
synonyms_content_lines = []

word_list_name = "synonyms"
word_list_size = -1
word_list = []
current_word = ""
current_word_cursor = -1

#data_dir = "/home/AnmolSinghJaggi/root/data/flashcard/"
data_dir = "data/flashcard/"


def preload_synonyms():
    global synonyms
    global synonyms_content_lines
    if len(synonyms_content_lines) > 0:
        return
    synonyms_file_content = open(data_dir + "synonyms.txt").read()
    synonyms_content_lines = synonyms_file_content.splitlines()
    line_num = -1
    for line in synonyms_content_lines:
        words_in_line = line.split()
        line_num = line_num + 1
        for word in words_in_line:
            if len(word) > 1 and word not in synonyms:
                synonyms[word] = []
            synonyms[word].append(line_num)


def get_synonyms(word):
    result = ""
    if word in synonyms:
        for line_num in synonyms[word]:
            result += synonyms_content_lines[line_num] + "\n"
    else:
        result = "NA"
    return result


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


def get_template_params():
    template_params = {}
    template_params['word_list_name'] = word_list_name
    template_params['word_list_size'] = word_list_size
    template_params['current_word'] = current_word
    template_params['current_word_cursor'] = current_word_cursor
    #template_params['synonyms'] = get_synonyms(current_word)
    return template_params

def handle_GET():
    preload_synonyms()
    global word_list_name
    if len(word_list) == 0:
        load_file()
    template_content = render_template("index_flashcard.html", **get_template_params())
    return template_content


def handle_next_word():
    global current_word_cursor
    global current_word
    current_word_cursor = current_word_cursor + 1
    if current_word_cursor >= word_list_size:
        current_word = 'Out of words!!'
    else:
        current_word = word_list[current_word_cursor]
    template_content = render_template("index_flashcard.html", **get_template_params())
    return template_content


def handle_change_list(request):
    global word_list_name
    word_list_name = request.form['change_list']
    load_file()
    template_content = render_template("index_flashcard.html", **get_template_params())
    return template_content

def handle_synonyms_GET():
    template_content = render_template("synonyms.html")
    return template_content

def handle_synonyms_POST(request):
    word = request.form['word']
    template_params = {}
    template_params['synonyms'] = get_synonyms(word)
    template_params['word'] = word
    template_content = render_template("synonyms.html", **template_params)
    return template_content

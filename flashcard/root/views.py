#!/usr/bin/env python3
from flask import Flask, render_template, request
from code.grocery import process_grocery
from code.flashcard import process_flashcard


app = Flask(__name__)

# Uncomment to make the server refresh the website
# as soon as there is a change in the source code.
#app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
        
        
@app.route("/grocery", methods=["GET", "POST"])
def grocery_index():
    if request.method == "POST":
        return process_grocery.handle_POST(request)
    else:
        return process_grocery.handle_GET()
    

@app.route("/flashcard", methods=["GET"])
def flashcard_index():
    return process_flashcard.handle_GET()



@app.route("/flashcard/next_word", methods=["POST"])
def flashcard_next_word():
    return process_flashcard.handle_next_word()


@app.route("/flashcard/change_list", methods=["POST"])
def flashcard_change_list():
    return process_flashcard.handle_change_list(request)


@app.route("/flashcard/synonyms", methods=["GET", "POST"])
def flashcard_synonyms():
    if request.method == "POST":
        return process_flashcard.handle_synonyms_POST(request)
    else:
        return process_flashcard.handle_synonyms_GET()
    return 


if __name__ == "__main__":
    app.run()

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
def index_grocery():
    if request.method == "POST":
        return process_grocery.handle_POST(request)
    else:
        return process_grocery.handle_GET()
    

@app.route("/flashcard", methods=["GET"])
def index_flashcard():
    return process_flashcard.handle_GET()



@app.route("/flashcard/next_word", methods=["POST"])
def index_flashcard_next_word():
    return process_flashcard.handle_next_word()



@app.route("/flashcard/synonyms", methods=["POST"])
def index_flashcard_synonyms():
    return process_flashcard.handle_synonyms()


@app.route("/flashcard/change_list", methods=["POST"])
def index_flashcard_change_list():
    return process_flashcard.handle_change_list(request)


if __name__ == "__main__":
    app.run()

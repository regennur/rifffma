from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import gunicorn

app = Flask(__name__, template_folder="templates")
app.debug = True


@app.route('/')
def hello_world():
    response = requests.get('https://rifmu.ru/'+"кот")
    contents_html = response.content

    soup = BeautifulSoup(contents_html, 'lxml')
    text_arr = []

    for child in soup.ul.recursiveChildGenerator():

        if child.name == 'a':

            text_arr.append(child.text)

    return jsonify({"data": text_arr})


@app.route('/w/<word>')
def show_word(word):
    response = requests.get('https://rifmu.ru/'+word)
    contents_html = response.content

    soup = BeautifulSoup(contents_html, 'lxml')
    text_arr = []

    for child in soup.ul.recursiveChildGenerator():

        if child.name == 'a':

            text_arr.append(child.text)

    return jsonify({"data": text_arr})

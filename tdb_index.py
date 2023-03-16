#!/usr/bin/python3

# Indexer for OpenTDB
# used for scrapping pancake's questions and answers

import requests
from html import unescape
from bs4 import BeautifulSoup
import sqlite3

class tdb_index:
    @staticmethod
    def get_api_sample() -> dict:
        # Note we can navigate through each element with get_api_sample(10, "hard")["results"][0]
        # Only part of the program that uses the API, documentation at https://opentdb.com/api_config.php
        API = "https://opentdb.com/api.php?amount=50&token=YOURTOKENHERE"
        data = requests.get(API).json()
        return data
    
    @staticmethod
    def get_questions_json(json_data:list) -> list[str]:
        ques = []
        for request in json_data:
            results = request["results"]
            for question in results:
                ques.append(unescape(question["question"]))
        return ques

    @staticmethod
    def get_correct_answer_json(json_data) -> list[str]:
        ques = []
        for request in json_data:
            results = request["results"]
            for question in results:
                ques.append(unescape(question["correct_answer"]))
        return ques

questions = list()
temp = tdb_index.get_api_sample()
while temp["response_code"] != 4:
    questions.append(temp)
    temp = tdb_index.get_api_sample()
questions.append(temp)
result = (tuple(zip(tdb_index.get_questions_json(questions), tdb_index.get_correct_answer_json(questions))))
conn = sqlite3.connect('tdb.db')
for entry in result:
    question = entry[0]
    answer = entry[1]
    finalq = ""
    finala = ""
    for letter in question:
        finalq += letter
        if letter == '"':
            finalq += letter
    for letter in answer:
        finala += letter
        if letter == '"':
            finala += letter
    cursor = conn.execute(f'insert into trivia(question, answer) values("{finalq}", "{finala}");')
conn.commit()
conn.close()
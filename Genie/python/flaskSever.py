# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://localhost:8080'}})

# Load ChatBotRep.csv
file_path = 'ChatBotRep2.csv'
patterns = pd.read_csv(file_path, sep='|')

# Initialize Okt for Korean morphological analysis
okt = Okt()

# Tokenize texts into morphemes
tokens = [okt.morphs(text) for text in patterns['Q']]
texts = [' '.join(token) for token in tokens]

# Calculate TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get most similar answer
def get_most_similar_answer(question):
    question_tokenized = okt.morphs(question)
    question_text = ' '.join(question_tokenized)
    question_tfidf = vectorizer.transform([question_text])
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)
    most_similar_index = similarity.argmax()
    most_similar_answer = patterns.loc[most_similar_index, 'A']
    return most_similar_answer

# Function to get random answer if there are multiple matches
# def get_random_answer(question):
#     matched_indices = []
#     for idx, pattern in enumerate(patterns['Q']):
#         if question in pattern:
#             matched_indices.append(idx)
    
#     if matched_indices:  # If there are matched indices
#         random_index = random.choice(matched_indices)
#         return patterns.loc[random_index, 'A']
#     else:
#         return "죄송해요, 잘 이해하지 못했어요"

# Main route
@app.route('/')
def index():
    msg = request.args["msg"]
    ans = get_answer(msg)
    print(msg, ans)
    return {"msg": ans}

# Function to get answer from patterns
def get_answer(question):
    matched_indices = []
    for idx, pattern in enumerate(patterns['Q']):
        if question in pattern:
            matched_indices.append(idx)

    if matched_indices:  
        random_index = random.choice(matched_indices)
        return patterns.loc[random_index, 'A']
    else:
        return "죄송해요, 잘 이해하지 못했어요"

# API endpoint to get answer
@app.route('/get_answer', methods=['POST'])
def get_answer_api():
    question = request.form['question']
    answer = get_answer(question)
    return jsonify({'answer': answer})

# API endpoint to get most similar answer
@app.route('/get_similar_answer', methods=['POST'])
def get_similar_answer_api():
    question = request.form['question']
    answer = get_most_similar_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

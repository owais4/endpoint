from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
#from flask_ngrok import run_with_ngrok 


app = Flask(__name__)
#run_with_ngrok(app)


@app.route('/comment', methods=['GET','POST'])
def get_comment():
    if (request.method == 'POST'):
        some_json = request.get_json()
        print(some_json)
        # with open("processed_comment.json", "a") as outfile:
        #     json.dump(some_json, outfile)
        #     outfile.write('\n')
        # outfile.close()
    return jsonify({'Response': 'Received'}),201

@app.route('/post', methods=['GET','POST'])
def get_post():
    if (request.method == 'POST'):
        some_json = request.get_json()
        print(some_json)
        # with open("processed_post.json", "a") as outfile:
        #     json.dump(some_json, outfile)
        #     outfile.write('\n')
        # outfile.close()
    return jsonify({'Response': 'Received'}),201

if __name__ == '__main__':
    #process = NLP
    app.run()

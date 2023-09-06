"""
Main Flask app for
"""
import flask
import time
import json
import os
import shortuuid
import urllib.request
from datetime import datetime
from datetime import timedelta


"""Declare and Initialize Classes and Config"""
app = flask.Flask(__name__)
app.secret_key = "123E8369FA329DD1A182D94C31BF8"


@app.route('/', methods=['GET', 'POST'])
def show_index():

    

    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'current_time': current_time,
    }
    return flask.render_template("index.html", **context)


@app.route('/try/', methods=['GET', 'POST'])
def show_try():

    # SET DEFAULT SUGGESTIONS TO EMPTY
    suggestions_text = ''

    # HANDLES TRY REQUESTS
    if flask.request.method == "POST":

        # FETCH ENTERED TEXT
        songs_text = flask.request.form["songs"]

        '''
        ####################################
        BEGIN CUSTOM CODE TO GET RECOMMENDATION
        ####################################
        '''

        print('sample calling functions with:', songs_text)

        # placeholder suggestions
        suggestions_text = 'Based on your preferences, we think that you would enjoy August, Mirroball, and Champaign Problems'

        '''
        ####################################
        END CUSTOM CODE TO GET RECOMMENDATION
        ####################################
        '''        


    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'suggestions_text': suggestions_text,
    }
    return flask.render_template("try.html", **context)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
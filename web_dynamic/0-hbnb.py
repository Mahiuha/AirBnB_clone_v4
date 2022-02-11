#!/bin/bash/python3
"""
This is a flask app that integrates with airbnbn static html template.
"""
from flask import Flask, render_template, url_for


# setup for flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

if __name__ == "__main__":
    app.run()


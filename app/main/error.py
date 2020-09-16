from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    render_template('fourOwFour.html'),404
from flask import Flask, Blueprint, render_template, request, url_for, redirect, session
from model.model import addFilme, listaFilmes

blueprint01 = Blueprint("blueprint01", __name__)

@app.route("/")
def main_page():
    return render_template("index.html")
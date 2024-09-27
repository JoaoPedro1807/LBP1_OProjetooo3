from flask import Flask, Blueprint, render_template, request, url_for, redirect
from model import addfilme, listaFilmes

blueprint01 = Blueprint("blueprint01", __name__)
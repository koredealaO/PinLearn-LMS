from flask import render_template

from . import core_bp


@core_bp.route("/")
def home():
    return render_template("index.html")
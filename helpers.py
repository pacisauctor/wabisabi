import csv
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("-----------------loginrequired used------------------")
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def filtrarFerias(ferias, idemprendimiento):
    fferias = []
    for feria in ferias:
        if feria['id_emprendimiento'] == idemprendimiento:
            fferias.append(feria)
    return fferias


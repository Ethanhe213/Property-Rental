from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import property


@app.route('/create_pr')
def index_property():
    return render_template('PR_form.html')
@app.route('/create',methods=['POST'])
def create():
    valid=property.Property.save_pr(request.form)
    if not valid:
        return redirect('/create_pr')
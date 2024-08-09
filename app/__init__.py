from flask import Flask, render_template, redirect, session
from app.config import Config
from app.forms.sample_form import SampleForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/home')
def root():
    return '<h1>Hello from Flask!</h1>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    # return f"""<p>This is the form page</p>
    # <p>How's It going</p>"""
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')

    return render_template('form.html', form=form)

@app.route('/visits_counter')
def visits():
    if 'visits' in session:
        # reading and updating session data
        session['visits'] = session.get('visits') + 1
    else:
        # setting session data
        session['visits'] = 1
    return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/', methods=["POST"])
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'

@app.route('/ice-cream/<flavor>')
def ice_cream(flavor):
    session['ice-cream'] = flavor
    return f"Flavor = {session.get('ice-cream')}"
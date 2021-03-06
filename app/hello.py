from flask import abort, redirect, url_for, Flask
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.errorhandler(401)
def unauthorized(error):
    return render_template('hello.html'), 401

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
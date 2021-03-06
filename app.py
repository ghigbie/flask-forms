from flask import Flask, render_template, request
app = Flask(__name__)

title = "Flask Forms"

@app.route('/')
def index():
    return render_template('home.html', title=title)

@app.route('/signup')
def signup():
    return render_template('signup.html', title=title)

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html', title=title, first=first, last=last)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e), 404

if __name__ == '__main__':
    app.run(debug=True)

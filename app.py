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
    return render_template('thankyou.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)

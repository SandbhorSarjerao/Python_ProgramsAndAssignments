from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home():                              # Keep all .html files in "Templates" folder
    return render_template('index.html')    # Keep all .css, .js & image files in "Static" folder

@app.route('/about')
def about():
    return render_template('about.html')



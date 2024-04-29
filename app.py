from flask import Flask , render_template

app = Flask('__name__')

@app.route('/homepage')
def home():
    return render_template('index.html')


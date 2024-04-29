from flask import Flask , render_template

app = Flask('__name__')

<<<<<<< HEAD
@app.route('/homepage')
=======
@app.route('/')
>>>>>>> b6604abfe3a85afa7c5fafc7a2dba4a53a740d3f
def home():
    return render_template('index.html')


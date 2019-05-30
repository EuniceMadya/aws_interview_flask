from flask import Flask, render_template, url_for
import os
app = Flask(__name__)




posts = [
    {
        'author': 'ah',
        'title': 'sample',
        'content': 'first post content'
    },
    {
        'author': '???',
        'title': 'sample second',
        'content': 'second post content'
    }


]

@app.route('/')
def hello():
    return '<h1>Hello !<h1>'

@app.route('/Home')
def home():
    return render_template('home.html', posts=posts, title='home')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/ec2_status_new')
def ec2():
    KEY_aws = os.environ["KEY_aws"]
    secretAccessKey = os.environ["SECRETE_KEY"]
    python_data = {
    'KEY_aws': KEY_aws,
    'secretAccessKey': secretAccessKey
}

    return render_template('ec2_status.html', python_data=python_data)

if __name__ == '__main__':
    app.run(debug=True)

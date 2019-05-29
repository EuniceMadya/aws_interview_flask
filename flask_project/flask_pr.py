from flask import Flask, render_template, url_for
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

@app.route('/ec2_status')
def ec2():
    return render_template('ec2_status.html')

if __name__ == '__main__':
    app.run(debug=True)

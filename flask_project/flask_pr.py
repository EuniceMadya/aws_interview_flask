from flask import Flask, render_template, Response, request, redirect, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL

import os
from werkzeug.utils import secure_filename

import upload_multi_s3

app = Flask(__name__)
UPLOAD_FOLDER = '/Users/madya/Documents/GitHub/aws_interview_flask/flask_project/upload_simulation'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

KEY_aws = os.environ["KEY_aws"]
secretAccessKey = os.environ["SECRETE_KEY"]

filenames =[]
app.config['filenames'] = filenames

@app.route('/')
def hello():
    return render_template('home.html', title='home')

@app.route('/Home')
def home():
    return render_template('forloop.html', posts=posts, title='home')

@app.route('/about')
def about():
    return render_template('home.html')

@app.route('/ec2_status_new')
def ec2():
    python_data = {
        'KEY_aws': KEY_aws,
        'secretAccessKey': secretAccessKey
    }
    return render_template('ec2_status.html', python_data=python_data, title ='ec2_snapshot')


@app.route('/download', methods=['GET', 'POST'])
def download():
    print("\n\n\n\n\n", request.form)
    key = request.form['key']

    upload_multi_s3.download(key)
    # filename = "s"
    return render_template("progress.html", filename=key);

@app.route('/s3_upload')
def s3_upload():

    return render_template('s3_upload.html', title='s3 upload', filenames=filenames, filename="", information="",python_data="")

@app.route('/s3_info', methods=['GET', 'POST'])
def s3_info():
    filename=""
    information="please upload a file"
    python_data = {
        'KEY_aws': KEY_aws,
        'secretAccessKey': secretAccessKey
    }
    if request.method == 'POST':

        if 'file' not in request.files:
            # flash('No file part')
            # return redirect(request.url)
            return render_template('s3_upload.html', title='s3 upload',filenames=filenames, filename=filename, information=information,python_data=python_data)

        file = request.files['file']
        print(file)
        print(request.files)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
        print("filename     " , file.filename)
        path = os.path.abspath(file.filename)
        filename = secure_filename(file.filename)
        if(filenames != None):
            if (filename not in filenames):
                filenames.append(filename)
        print(filenames)

        print(path)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        information = upload_multi_s3.upload_to_s3(filename, app.config['UPLOAD_FOLDER']+"/"+filename)

    return render_template('s3_upload.html', title='s3 upload',filenames=filenames, filename=filename, information=information,python_data=python_data)





if __name__ == '__main__':
     app.run(host='0.0.0.0', debug = True)

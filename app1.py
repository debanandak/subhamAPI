import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'
@app.route('/')
def upload():
    return render_template("upload1.html")

@app.route('/done',methods=['POST'])
def doUpload():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
        return render_template('done.html',name=f.filename)

if __name__=='__main__':
    app.run(debug=True)

    

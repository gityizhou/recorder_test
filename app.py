from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL




app = Flask(__name__)

files = UploadSet('files', ALL)
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'

configure_uploads(app, files)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'media' in request.files:
        filename = files.save(request.files['media'])
        url = files.url(filename)
    return render_template('upload.html')


@app.route('/recorder', methods=['GET', 'POST'])
def upload2():
    if request.method == 'POST':
        filename = files.save(request.files['media'])
        url = files.url(filename)
    return render_template('recordertest.html')



if __name__ == '__main__':
    app.run()

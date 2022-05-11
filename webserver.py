import os
import datetime
from flask import Flask, redirect, request, url_for, render_template, send_from_directory
from waitress import serve
from colorizer import colorize

app = Flask(__name__)
DIRECTORY_IN = "input_images"
DIRECTORY_OUT = "result_images"


def allowed_file(filename):
    for allow in ['.png', '.jpg', '.jpeg']:
        if filename.endswith(allow):
            return True, allow
    return False, ""


def get_time_str():
    dt = datetime.timedelta(hours=3)
    tz = datetime.timezone(dt)
    now = datetime.datetime.now(tz)
    return str(datetime.datetime.strftime(now, '%Y-%m-%d-%H-%M-%S'))


def get_save_path(filename):
    if filename != '':
        allow, ftype = allowed_file(filename)
        if allow:
            filepath = os.path.join(DIRECTORY_IN, get_time_str() + "_" + filename)
            return filepath
    return False


@app.route('/', methods=['POST'])
def upload_file():
    try:
        uploading_file = request.files['file']

        if not os.path.exists(DIRECTORY_IN):
            os.makedirs(DIRECTORY_IN)

        path = get_save_path(uploading_file.filename)
        if path is not False:
            uploading_file.save(path)
            out_path = colorize(path)

            s = str(out_path).replace(DIRECTORY_OUT, "").replace('/', '').replace('\\', '')
            r_url = url_for('uploaded_file', filename=s)
        else:
            return redirect(url_for('error'))
    except Exception as err:
        print('Error', err)
        return redirect(url_for('error'))

    return redirect(r_url)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/<filename>')
def uploaded_file(filename):
    return render_template('image.html', filename=filename)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(DIRECTORY_OUT, filename)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=1024)
    serve(app, host='0.0.0.0', port=1024)

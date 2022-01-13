from flask import render_template, redirect, session, url_for, flash, request, send_from_directory
from . import main
from .forms import NameForm, FindSimiliarText, DivideForm, DivideFormResult
from .learnText2.SimilarUtil import findMostSimilarText
from werkzeug.utils import secure_filename
import os
import json

ALLOWED_EXTENSIONS = {'txt'}
UPLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments'
DOWNLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\jsonFolader'
nameNum = 1

@main.route('/', methods=['GET', 'POST'])
def index():
    newForm = FindSimiliarText()
    form = NameForm()
    if form.validate_on_submit():
        newForm.text.data = form.text.data
        newForm.similiarText.data = findMostSimilarText(newForm.text.data)
        return render_template('index.html', form=newForm)
    return render_template('index.html', form=form)


@main.route('/divide', methods=['GET', 'POST'])
def divide():
    form = DivideForm()
    newForm = DivideFormResult()
    if form.validate_on_submit():
        result = {}
        result["姓名"] = newForm.name.data
        result["民族"] = newForm.nation.data
        result["性别"] = newForm.sex.data
        result["出生地"] = newForm.birthplace.data
        result["案由"] = newForm.excuse.data
        result["相关法院"] = newForm.relativeCourt.data
        result["发生时间"] = newForm.time.data
        jsonDownload(nameNum, result)
        nameNumAdd()
        flash("保存成功")
        return render_template('divide.html', form=DivideForm())
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            text = readAFile(os.path.join(UPLOAD_FOLDER, filename))
            # form.text.data = text
            form = DivideFormResult()
            form.text.data = text
            return render_template('divideResult.html', form=form)
    return render_template('divide.html', form=form)


@main.route('/divideResult', methods=['GET', 'POST'])
def storeFile(form):
    return render_template('divideResult.html', form=form)


@main.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def readAFile(str):
    with open(str, 'r', encoding='utf-8') as f:
        return f.read()

def jsonDownload(namenum, result):
    name = "jsonFile{}".format(namenum)
    address = os.path.join(DOWNLOAD_FOLDER, name)
    with open(address, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def nameNumAdd():
    global nameNum
    nameNum += 1
from flask import render_template, redirect, session, url_for, flash, request, send_from_directory
from . import main
from .forms import NameForm, FindSimiliarText, DivideForm, DivideFormResult
from .learnText2.SimilarUtil import useJsonFind
from .learnText2.Util import divideText
import os
import json

ALLOWED_EXTENSIONS = {'txt'}
UPLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments'
DOWNLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\jsonFolader'
nameNum = 1


@main.route('/', methods=['GET'])
def index():
    return render_template('main.html')



@main.route('/similar', methods=['GET', 'POST'])
def similar():
    newForm = FindSimiliarText()
    form = NameForm()
    if form.text.data is None:
        form.text.data = ""
    if form.validate_on_submit():
            newForm.text.data = form.text.data
            newForm.fileLabel.data = form.fileLabel.data
            pattern = ""
            if form.birthNeed.data:
                pattern+="b"
            if form.nameNeed.data:
                pattern+="c"
            if form.nationNeed.data:
                pattern+="n"
            if form.relaNeed.data:
                pattern+="r"
            if form.timeNeed.data:
                pattern+="t"
            if form.sexNeed.data:
                pattern+="s"
            if  form.excuseNeed.data:
                pattern+="e"
            findResult = useJsonFind(form.text.data, pattern)
            newForm.similarText.data = findResult["文本"]
            docujson = findResult["json"]
            newForm.textGuess.data = findResult["guess"]
            newForm.similarname.data = docujson["当事人"]
            newForm.similarsex.data = docujson["性别"]
            newForm.similarexcuse.data = docujson["案由"]
            newForm.similarbirthplace.data = docujson["出生地"]
            newForm.similarnation.data = docujson["民族"]
            newForm.similarrelativeCourt.data = docujson["相关法院"]
            try:
                newForm.similartime.data = docujson["案件日期"]
            except KeyError:
                newForm.similartime.data = docujson["日期"]
            return render_template('similarResult.html', form=newForm)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            text = readAFile(os.path.join(UPLOAD_FOLDER, filename))
            form=NameForm()
            form.text.data = text
            form.fileLabel.data = filename
            return render_template('similar.html', form=form)
    return render_template('similar.html', form=form)


@main.route('/divide', methods=['GET', 'POST'])
def divide():
    form = DivideForm()
    newForm = DivideFormResult()
    if form.text.data is None:
        form.text.data = ""
    if form.validate_on_submit():
        result = {}
        if newForm.nameReplace.data != "":
            result["姓名"] = newForm.nameReplace.data
        else:
            result["姓名"] = newForm.name.data
        if newForm.nationReplace.data != "":
            result["民族"] = newForm.nationReplace.data
        else:
            result["民族"] = newForm.nation.data

        result["性别"] = newForm.sex.data
        if newForm.birthplaceReplace.data != "":
            result["出生地"] = newForm.birthplaceReplace.data
        else:
            result["出生地"] = newForm.birthplace.data
        if newForm.excuseReplace.data != "":
            result["案由"] = newForm.excuseReplace.data
        else:
            result["案由"] = newForm.excuse.data
        if newForm.relativeCourtReplace.data != "":
            result["相关法院"] = newForm.relativeCourtReplace.data
        else:
            result["相关法院"] = newForm.relativeCourt.data
        if newForm.timeReplace.data != "":
            result["发生时间"] = newForm.timeReplace.data
        else:
            str = newForm.time.data
            str = str.replace('年', '.')
            str = str.replace('月', '.')
            str = str.replace('日', '')
            result["发生时间"] = str
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
            filename = file.filename
            text = readAFile(os.path.join(UPLOAD_FOLDER, filename))
            form = DivideFormResult()
            form.fileLabel.data = filename
            divideResult = divideText(text)
            form.sex.choices = divideResult['性别']
            form.relativeCourt.choices = divideResult["相关法院"]
            form.birthplace.choices = divideResult["出生地"]
            form.name.choices = divideResult["姓名"]
            form.nation.choices = divideResult["民族"]
            form.time.choices = divideResult['案件日期']
            form.excuse.choices = divideResult['案由']
            form.text.data = text
            return render_template('divideResult.html', form=form)
    return render_template('divide.html', form=form)


# @main.route('/divideResult', methods=['GET', 'POST'])
# def storeFile(form):
#     return render_template('divideResult.html', form=form)


@main.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def readAFile(str):
    try:
        with open(str, 'r', encoding='utf-8') as file:
            data = file.read()
    except UnicodeDecodeError:
        with open(str, 'r', encoding='gbk') as file:
            data = file.read()
        return data

def jsonDownload(namenum, result):
    name = "jsonFile{}".format(namenum)
    address = os.path.join(DOWNLOAD_FOLDER, name)
    with open(address, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def nameNumAdd():
    global nameNum
    nameNum += 1


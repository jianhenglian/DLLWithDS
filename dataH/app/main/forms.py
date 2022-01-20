from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField, FileField, StringField, HiddenField, SelectField, BooleanField, validators


# After an exploration,
# we found that this class is the real base of our homework.
# we can modify this class to get what we want to dispaly.
"""Though the form in views.py, we can get information in the frontier, 
so we can do something with these data."""
"""接下来我们扩展一下相似案例分析的功能，分析后，会形成左右两块，左边是原文件
右边是相似度最高的文件，同时显示相似度最高文件的相应json文件"""


class NameForm(FlaskForm):
    text = HiddenField("输些东西进来试一试")
    fileLabel = HiddenField("文件附带的")
    nameNeed = BooleanField("姓名")
    nationNeed = BooleanField("民族")
    birthNeed = BooleanField("出生地")
    relaNeed = BooleanField("相关法院")
    timeNeed = BooleanField("案发时间")
    sexNeed = BooleanField("性别")
    excuseNeed = BooleanField("案由")
    submit = SubmitField('查找最相似文本')



class FindSimiliarText(FlaskForm):
     text = HiddenField("")
     fileLabel = HiddenField("文件附带的")
     textGuess = HiddenField("猜的")
     similarText = HiddenField('')
     similarname = HiddenField('名字')
     similarsex = HiddenField("性别  ")
     similarnation = HiddenField("民族  ")
     similarbirthplace = HiddenField("出生地  ")
     similarrelativeCourt = HiddenField("相关法院")
     similarexcuse = HiddenField("案由  ")
     similartime = HiddenField("案件年份")
     submit = SubmitField('查找最相似文本')


class DivideForm(FlaskForm):
    text = TextAreaField("")
    fileLabel = HiddenField("文件附带的")


class DivideFormResult(FlaskForm):
    text = HiddenField("")
    fileLabel = HiddenField("文件附带的")
    name = SelectField("姓名  ")
    nameReplace = StringField("自定义姓名")
    sex = SelectField("性别  ")
    nation = SelectField("民族  ")
    nationReplace = StringField("自定义民族")
    birthplace = SelectField("出生地  ")
    birthplaceReplace = StringField("自定义出生地")
    relativeCourt = SelectField("相关法院")
    relativeCourtReplace = StringField("自定义法院")
    time = SelectField("案件年份")
    timeReplace = StringField("自定义案件年份")
    excuse = SelectField("案由  ")
    excuseReplace = StringField("自定义案由")
    store = SubmitField("保存案件到本地")

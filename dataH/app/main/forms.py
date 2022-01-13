from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField, FileField, StringField, HiddenField
from wtforms.validators import DataRequired


# After an exploration,
# we found that this class is the real base of our homework.
# we can modify this class to get what we want to dispaly.
"""Though the form in views.py, we can get information in the frontier, 
so we can do something with these data."""


class NameForm(FlaskForm):
    text = TextAreaField("输些东西进来试一试", validators=[DataRequired()])
    submit = SubmitField('查找最相似文本')


class FindSimiliarText(FlaskForm):
     text = TextAreaField("", validators=[DataRequired()])
     similiarText = TextAreaField('')
     submit = SubmitField('查找最相似文本')


class DivideForm(FlaskForm):
    text = TextAreaField("")


class DivideFormResult(FlaskForm):
    text = HiddenField("")
    name = StringField("姓名  ")
    sex = StringField("性别  ")
    nation = StringField("民族  ")
    birthplace = StringField("出生地  ")
    excuse = StringField("案由  ")
    relativeCourt = StringField("相关法院")
    time = StringField("案件年份")
    store = SubmitField("保存案件到本地")

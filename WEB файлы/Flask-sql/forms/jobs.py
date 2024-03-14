from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddJobs(FlaskForm):
    title = StringField('Наименование работы', validators=[DataRequired()])
    content = StringField('Наименование работы', validators=[DataRequired()])
    submit = SubmitField('Создать')

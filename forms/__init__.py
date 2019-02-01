from flask_wtf import FlaskForm
from wtforms.fields import FileField
from wtforms.validators import DataRequired

class UploadTrainForm(FlaskForm):
    dataset = FileField('dataset', validators=[DataRequired()])
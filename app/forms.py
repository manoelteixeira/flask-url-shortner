from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    url = URLField(label="URL",
                   validators=[DataRequired(message="You need to provide an url.")])
    submit = SubmitField(label="Create")
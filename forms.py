from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PredictorForm(FlaskForm):
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)],render_kw={"placeholder": "Enter Country"})
    forest = StringField('Forest', validators=[DataRequired(), Length(min=2,max=35)],render_kw={"placeholder": "Enter Forest"})
    submit = SubmitField('Submit')

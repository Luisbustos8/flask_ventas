from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

#Que campos tienen, tipo y forma

class ProdutForm(FlaskForm):
    tipo_producto = StringField("Tipo de Producto", validators=[DataRequired(), Length(min=3, message="Debe tener al menos tres caracteres")])
    precio_unitario = FloatField("Precio U.", validators=[DataRequired(message="Dime algo, tete")])
    coste_unitario = FloatField("Coste U.", validators=[DataRequired()])

    submit = SubmitField("Aceptar")
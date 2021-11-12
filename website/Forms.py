from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.widgets import TextArea

class AddToDBForm(FlaskForm):

    category = SelectField(label='Категория', choices=('Рабочая станция оператора', 'Видеооборудование', 'Аудиооборудование',
                                                       'Фурнитура'))
    type = StringField('Тип')
    name = StringField('Наименование')
    description = StringField('Описание ТЗ', widget=TextArea())
    description2 = StringField('Описание заявка', widget=TextArea())

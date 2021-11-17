from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.widgets import TextArea

class AddToDBForm(FlaskForm):

    category = SelectField('Категория', choices=('Рабочая станция оператора',
                                                 'Видеооборудование',
                                                 'Аудиооборудование',
                                                 'Фурнитура'))
    type = SelectField('Тип', choices=())
    name = StringField();
    #name = SelectField('Наименоваание', choices=())
    description = StringField('Описание ТЗ', widget=TextArea())
    description2 = StringField('Описание заявка', widget=TextArea())

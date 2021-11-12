from flask import Blueprint,render_template, request, url_for, flash
from . import Forms
from . import Database

db_edit = Blueprint('db_edit', __name__)


@db_edit.route('/', methods=['GET', 'POST'])

def add_to_db_form():

    add_to_db_form = Forms.AddToDBForm()

    if add_to_db_form.validate_on_submit():

        category = add_to_db_form.category.data
        type = add_to_db_form.type.data
        name = add_to_db_form.name.data
        description = add_to_db_form.description.data
        description2 = add_to_db_form.description2.data

        print(description)

        Database.append_database(category, type, name, description,description2)

        flash('Устройство добавлено', category='ok')

    else:
        flash("""Пояснение:
        Категория - имеется в виду к чему относится устройство (прим. видеокарта относится к компу)
        Тип - тип устройства (прим.: видеокарта, стойка, камера и т.д.
        Наименование - полное название устройства как их писал разработчик
        Описание - просто вставляешь текст из ТЗ""")




    return render_template('database_edit.html', add_to_db_form=add_to_db_form)


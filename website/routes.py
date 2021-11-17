from flask import Blueprint,render_template, request, url_for, flash, jsonify
from . import Forms
from . import Database

db_edit = Blueprint('db_edit', __name__)

cat_to_type = {
    'Рабочая станция оператора': ['Компьютер', 'Звуковая система'],
    'Видеооборудование': ['Камера'],
    'Аудиооборудование': ['Микрофон', 'Колонки'],
    'Фурнитура': ['Стулья', 'Столы']
}

""" type_to_name = {
    'Компьютер': ['n1', 'n2'],
    'Звуковая система': ['n3', 'n4'],
    'Камера': ['n5', 'n6'],
    'Микрофон': ['n7', 'n8'],
    'Колонки': ['n9', 'n10'],
    'Стулья': ['n11', 'n12'],
    'Столы': ['n13', 'n14']
} """

@db_edit.route('/', methods=['GET', 'POST'])

def add_to_db_form():

    add_to_db_form = Forms.AddToDBForm()
    add_to_db_form.type.choices = cat_to_type['Рабочая станция оператора']
    """ add_to_db_form.name.choices = type_to_name['Компьютер'] """

    if add_to_db_form.validate_on_submit():

        category = add_to_db_form.category.data
        type = add_to_db_form.type.data
        name = add_to_db_form.name.data
        description = add_to_db_form.description.data
        description2 = add_to_db_form.description2.data

        print(description)

        Database.append_database(category, type, name, description, description2)

        flash('Устройство добавлено', category='ok')

    else:
        flash("""Пояснение:
        Категория - имеется в виду к чему относится устройство (прим. видеокарта относится к компу)
        Тип - тип устройства (прим.: видеокарта, стойка, камера и т.д.
        Наименование - полное название устройства как их писал разработчик
        Описание - просто вставляешь текст из ТЗ""")




    return render_template('database_edit.html', add_to_db_form=add_to_db_form)

@db_edit.route('/type/<category>')

def get_type(category):
    types_names = cat_to_type[category]                     # создаем список с типами относящимися к данной категории
                                                            # (сейчас через временный список сверху, позже - со специальной ДБ)
    types = [{'name': name} for name in types_names]        # приводим список с типами в формат JSON
    return jsonify({'types': types})


""" 
@db_edit.route('/type/name/<type>')
def get_name(type):
    name_names = type_to_name[type]                         # создаем список с именами относящимися к данному типу
                                                            # (сейчас через временный список сверху, позже - со специальной ДБ)
    names = [{'name': name} for name in name_names]        # приводим список с именами в формат JSON
    return jsonify({'names': names})
 """


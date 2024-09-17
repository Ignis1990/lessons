# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def user_info(firstname, lastname, year, city, email, phone):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'year': year,
        'city': city,
        'email': email,
        'phone': phone
    }


a = user_info(firstname='Anton', lastname='Stepanyuk', year='1990', city='Magadan', email='fff@fff.fff', phone='88005553535')
print(a)
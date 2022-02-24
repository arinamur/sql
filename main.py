from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    dict = {'surname': ['Scott', 'Pirson', 'Ivanov'],
            'name': ['Ridley', 'Mikky', 'Ivan'],
            'age': [21, 33, 14],
            'position': 'capitan',
            'speciality': ['research engineer', 'farmer', 'teacher'],
            'address': ['module_1', 'module_2', 'module_3'],
            'email': ['scott_chief', 'mikky_pirson', 'ivan_crutoy']}
    for i in range(3):
        user = User()
        user.surname = dict['surname'][i]
        user.name = dict['name'][i]
        user.age = dict['age'][i]
        user.position = 'captain'
        user.speciality = dict['speciality'][i]
        user.address = dict['address'][i]
        user.email = f'{dict["email"][i]}@mars.org'
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()

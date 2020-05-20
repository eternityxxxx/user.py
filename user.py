
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Строка подключения
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# Базовый класс БД
Base = declarative_base()

class User(Base):
    """
        Описывает структуру таблицы user для хранения записей данных пользователей
    """

    # Название таблицы
    __tablename__ = "user"

    # Идентификатор
    id = sa.Column(sa.INTEGER, primary_key = True)
    # Имя
    first_name = sa.Column(sa.TEXT)
    # Фамилия
    last_name = sa.Column(sa.TEXT)
    # Пол
    gender = sa.Column(sa.TEXT)
    # Адрес электронной почты
    email = sa.Column(sa.TEXT)
    # Дата рождения
    birthdate = sa.Column(sa.TEXT)
    # Рост
    height = sa.Column(sa.REAL)

def connect_db():
    """
        Устанавливает соединение к базе данных и возвращает объект сессии
    """

    # Создаем соединение с БД
    engine = sa.create_engine(DB_PATH)
    # Создаем фабрику сессию
    session = sessionmaker(engine)

    # Возвращаем объект сессию
    return session()

def register_user():
    """
        Запрашивает у пользователя данные и возвращает созданный объект
    """

    # Запрашиваем данные
    first_name = input("Введи свое имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Укажи свой пол: ")
    email = input("Также укажи адрес электронной почты: ")
    birthdate = input("Введи дату рождения: ")
    height = input("И накане, укажи свой рост: ")

    # Возвращаем созданного пользвоателя
    return User(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email=email,
                birthdate=birthdate,
                height=height
               )

def main():
    user = register_user()
    session = connect_db()
    session.add(user)
    session.commit()


if __name__ == "__main__":
    main()

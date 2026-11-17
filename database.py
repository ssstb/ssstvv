from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Адрес нашей базы данных в Docker.
# Обрати внимание: мы используем имя сервиса 'db', а не 'localhost'!
# Логин (postgres), пароль (secretpassword) и имя базы (app_db) — такие же, как в docker-compose.yml
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:secretpassword@db:5432/app_db"
)

# Создаем «движок», который будет управлять соединениями
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Фабрика сессий (наш инструмент для открытия/закрытия дверей холодильника)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для наших будущих таблиц
Base = declarative_base()


# Функция-зависимость, которая открывает сессию на время запроса и закрывает её после
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
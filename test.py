from sqlalchemy import inspect
from models import engine  # Переконайтесь, що engine правильно налаштований

inspector = inspect(engine)
tables = inspector.get_table_names()

if tables:
    print("Список таблиць:")
    for table in tables:
        print(table)
else:
    print("Таблиці не знайдено.")

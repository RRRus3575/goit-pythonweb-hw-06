import psycopg2

# Параметры подключения
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432",
    options="-c client_encoding=UTF8" 
)

# Проверяем подключение
print("Подключение успешно!")
conn.close()

FROM postgres:latest

# Установить пароль для пользователя postgres
ENV POSTGRES_PASSWORD=mysecretpassword

# Указать имя создаваемой базы данных
ENV POSTGRES_DB=mydatabase

# Указать имя пользователя
ENV POSTGRES_USER=postgres

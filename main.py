from models import Base, engine

if __name__ == "__main__":
    # Створення всіх таблиць
    Base.metadata.create_all(engine)
    print("Таблиці створено!")

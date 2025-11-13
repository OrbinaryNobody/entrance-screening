Это скелет базы данных в которой есть две таблицы:
1) Accounts - таблица для сохраниния аккаунтов пользователей
    id_accounts SERIAL PRIMARY KEY,
    familiya TEXT,
    name TEXT,
    otchestvo TEXT,
    adress TEXT,
    years INT,
    email TEXT UNIQUE,
    user_number INTEGER UNIQUE,
    password VARCHAR(255),
    user_like INTEGER
2) Goods - таблица для хранения информации о товаре
    id_goods SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    description TEXT,
    image TEXT
Целью данной программы являлась практика в написании баз данных, а так же эта программа представляет собой черновик для реализации настоящего сервиса.
  Для запуска программы в Docker необходимо ввести в терминале:
  docker compose up --build

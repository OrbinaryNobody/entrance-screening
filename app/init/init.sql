CREATE TABLE IF NOT EXISTS goods (
    id_goods SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    description TEXT,
    image TEXT
);

CREATE TABLE IF NOT EXISTS accounts (
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
);

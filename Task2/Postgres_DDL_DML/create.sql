CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    token VARCHAR(150),
);

CREATE TABLE group_chats (
    chat_id SERIAL PRIMARY KEY,
    chat_name VARCHAR(100) NOT NULL
);

CREATE TABLE group_chat_members (
    chat_id INTEGER REFERENCES group_chats(chat_id),
    user_id INTEGER REFERENCES users(user_id),
    PRIMARY KEY (chat_id, user_id)
);

CREATE TABLE group_chat_messages (
    message_id SERIAL PRIMARY KEY,
    chat_id INTEGER REFERENCES group_chats(chat_id),
    user_id INTEGER REFERENCES users(user_id),
    message_text TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE ptp_chats (
    chat_id SERIAL PRIMARY KEY
);

CREATE TABLE ptp_chat_members (
    chat_id INTEGER REFERENCES ptp_chats(chat_id),
    user_id INTEGER REFERENCES users(user_id),
    PRIMARY KEY (chat_id, user_id)
);

CREATE TABLE ptp_chat_messages (
    message_id SERIAL PRIMARY KEY,
    chat_id INTEGER REFERENCES ptp_chats(chat_id),
    sender_id INTEGER REFERENCES users(user_id),
    receiver_id INTEGER REFERENCES users(user_id),
    message_text TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- Таблица учебных групп/классов
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    group_id INTEGER REFERENCES groups(id),
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица категорий вопросов
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Таблица вопросов
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(id),
    question_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица вариантов ответов
CREATE TABLE question_options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    option_text VARCHAR(255) NOT NULL,
    is_correct BOOLEAN NOT NULL DEFAULT FALSE
);

-- Таблица результатов тестирования
CREATE TABLE quiz_results (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER NOT NULL,
    time_spent INTEGER DEFAULT 0, -- в секундах
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица детальных ответов пользователей
CREATE TABLE user_answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id),
    selected_option_id INTEGER REFERENCES question_options(id)
);

-- Вставка данных групп
INSERT INTO groups (name, description) VALUES
('10-А', '10 класс, группа А'),
('10-Б', '10 класс, группа Б'),
('11-А', '11 класс, группа А'),
('11-Б', '11 класс, группа Б'),
('Студенты 1 курс', 'Первый курс университета');

-- Вставка категорий
INSERT INTO categories (name, description) VALUES
('Математика', 'Вопросы по математике'),
('История', 'Вопросы по истории'),
('География', 'Вопросы по географии'),
('Биология', 'Вопросы по биологии'),
('Литература', 'Вопросы по литературе'),
('Физика', 'Вопросы по физике'),
('Химия', 'Вопросы по химии'),
('Информатика', 'Вопросы по информатике');

-- Вставка вопросов
INSERT INTO questions (category_id, question_text) VALUES
-- Математика
(1, 'Чему равно число π с точностью до двух знаков после запятой?'),
(2, 'В каком году началась Вторая мировая война?'),
(3, 'Какая река является самой длинной в мире?'),
(4, 'Сколько хромосом у здорового человека?'),
(5, 'Кто написал роман "Преступление и наказание"?'),
(6, 'Какова скорость света в вакууме?'),
(7, 'Какой химический элемент обозначается символом Au?'),
(8, 'Что означает аббревиатура HTML?'),
-- Математика
(1, 'Чему равен квадратный корень из 144?'),
-- География
(3, 'Какая страна имеет наибольшую площадь территории?');

-- Вставка вариантов ответов для всех вопросов
-- Вопрос 1
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(1, '3.14', TRUE),
(1, '3.16', FALSE),
(1, '3.12', FALSE),
(1, '3.18', FALSE);

-- Вопрос 2
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(2, '1937', FALSE),
(2, '1939', TRUE),
(2, '1941', FALSE),
(2, '1945', FALSE);

-- Вопрос 3
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(3, 'Амазонка', TRUE),
(3, 'Нил', FALSE),
(3, 'Янцзы', FALSE),
(3, 'Миссисипи', FALSE);

-- Вопрос 4
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(4, '23', FALSE),
(4, '46', TRUE),
(4, '48', FALSE),
(4, '52', FALSE);

-- Вопрос 5
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(5, 'Лев Толстой', FALSE),
(5, 'Фёдор Достоевский', TRUE),
(5, 'Антон Чехов', FALSE),
(5, 'Иван Тургенев', FALSE);

-- Вопрос 6
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(6, '300 000 км/с', TRUE),
(6, '150 000 км/с', FALSE),
(6, '450 000 км/с', FALSE),
(6, '600 000 км/с', FALSE);

-- Вопрос 7
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(7, 'Серебро', FALSE),
(7, 'Железо', FALSE),
(7, 'Алюминий', FALSE),
(7, 'Золото', TRUE);

-- Вопрос 8
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(8, 'Hyper Text Markup Language', TRUE),
(8, 'High Tech Modern Language', FALSE),
(8, 'Hyper Transfer Markup Language', FALSE),
(8, 'Home Tool Markup Language', FALSE);

-- Вопрос 9
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(9, '11', FALSE),
(9, '12', TRUE),
(9, '13', FALSE),
(9, '14', FALSE);

-- Вопрос 10
INSERT INTO question_options (question_id, option_text, is_correct) VALUES
(10, 'Канада', FALSE),
(10, 'США', FALSE),
(10, 'Китай', FALSE),
(10, 'Россия', TRUE);

-- Вставка тестового администратора
INSERT INTO users (username, email, password_hash, group_id, is_admin) VALUES
('admin', 'admin@quiz.site', '$2b$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', NULL, TRUE),
-- Пароль: password

-- Тестовые пользователи
('student1', 'student1@school.edu', '$2b$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 1, FALSE),
('student2', 'student2@school.edu', '$2b$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, FALSE),
('student3', 'student3@school.edu', '$2b$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 1, FALSE);


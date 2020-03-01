CREATE TABLE app_user
(
    id        SERIAL PRIMARY KEY,
    nick_name VARCHAR(60) NOT NULL UNIQUE,
    email     VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE questions
(
    id          SERIAL PRIMARY KEY,
    question    TEXT NOT NULL,
    true_answer SMALLINT  NOT NULL
);

CREATE TABLE answers
(
    answer       SMALLINT NOT NULL,
    user_id      INTEGER references app_user (id),
    questions_id INTEGER references questions (id),
    PRIMARY KEY (user_id, questions_id)
);

INSERT INTO app_user(nick_name, email)
VALUES ('angry_birds', 'angry_birds@gmail.com'),
       ('qwerty', 'qwerty@mail.ru'),
       ('sergio_95', 'sergio_95@gmail.com');

INSERT INTO questions(question, true_answer)
VALUES ('Какое растение существует на самом деле?\n1. Лох чилийский' ||
        '\n2.Лох индийский\n3. Лох греческий\4. Лох русский', 2),
       ('Что за место, попав в которое, человек делает селфи на кухне, ' ||
        'которую не может себе позволить?\n1. Лондон\n2. Париж\n3. Рим' ||
        '\n4. Икеа', 4),
       ('Что проводит боксер, наносящий удар противнику снизу?\n1. Свинг' ||
        '\n2. Хук\n3. Апперкот\n4. Джэб', 3),
       ('Как называется ближайшая к Земле звезда?\n1. Проксиома Центавра' ||
        '\n2. Солнце\n3. Полярная\n4. Сириус', 2),
       ('Что помогает запомнить мнемоническое правило «Это я знаю и помню ' ||
        'прекрасно»?\n1. Число Пи\n2. Ряд активности металлов' ||
        '\n3. Цвета радуги\n4. Порядок падежей', 1),
       ('Какую площадь имеет клетка стандартной школьной тетради?' ||
        '\n1. 0.25 кв.см\n2. 1 кв.см\n3. 0.5 кв.см\n4. 1.25 кв. см', 1),
       ('Как назывались старинные русские пушки-гаубицы?\n1. Кентавр' ||
        '\n2. Грифон\n3. Василиск\n4. Единорог', 4);

INSERT INTO answers(answer, user_id, questions_id)
VALUES (1, 1, 1),
       (3, 1, 2),
       (2, 1, 3),
       (2, 1, 4),
       (4, 1, 5),
       (1, 1, 6),
       (3, 1, 7),
       (2, 2, 1),
       (2, 2, 2),
       (2, 2, 3),
       (2, 2, 4),
       (2, 2, 5),
       (2, 2, 6),
       (2, 2, 7),
       (1, 3, 1),
       (2, 3, 2),
       (3, 3, 3),
       (4, 3, 4),
       (1, 3, 5),
       (2, 3, 6),
       (3, 3, 7);

--tests
--error duplicate key
INSERT INTO answers(answer, user_id, questions_id)
VALUES (3, 3, 7);

--output correct answers from users
SELECT nick_name, questions_id, answer FROM answers, questions, app_user
WHERE answer = true_answer AND
      questions_id = questions.id AND
      user_id = app_user.id;

--sum of correct responses from users
SELECT nick_name, count(nick_name) AS sum_true_answer
FROM answers, questions, app_user
WHERE answer = true_answer AND
      questions_id = questions.id AND
      user_id = app_user.id
GROUP BY nick_name;

CREATE TABLE app_user
(
    id        SERIAL PRIMARY KEY,
    nick_name VARCHAR(60) NOT NULL UNIQUE,
    email     VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE questions
(
    id          SERIAL PRIMARY KEY,
    question    VARCHAR(200) NOT NULL
);

CREATE TABLE answers
(
    id           SERIAL PRIMARY KEY,
    answer       VARCHAR(100) NOT NULL,
    true_answer  BOOLEAN  NOT NULL,
    questions_id INTEGER REFERENCES questions (id)
);

CREATE TABLE answers_user
(
    answer       INTEGER REFERENCES answers (id),
    user_id      INTEGER REFERENCES app_user (id),
    questions_id INTEGER REFERENCES questions (id),
    PRIMARY KEY (user_id, questions_id)
);

INSERT INTO app_user(nick_name, email)
VALUES ('angry_birds', 'angry_birds@gmail.com'),
       ('qwerty', 'qwerty@mail.ru'),
       ('sergio_95', 'sergio_95@gmail.com');

INSERT INTO questions(question)
VALUES ('Какое растение существует на самом деле?'),
       ('Что за место, попав в которое, человек делает селфи на кухне, ' ||
        'которую не может себе позволить?'),
       ('Что проводит боксер, наносящий удар противнику снизу?'),
       ('Как называется ближайшая к Земле звезда?'),
       ('Что помогает запомнить мнемоническое правило «Это я знаю и помню ' ||
        'прекрасно»?'),
       ('Какую площадь имеет клетка стандартной школьной тетради?'),
       ('Как назывались старинные русские пушки-гаубицы?');

INSERT INTO answers(answer, true_answer, questions_id)
VALUES ('1. Лох чилийский', false, 1),
       ('2. Лох индийский', true, 1),
       ('3. Лох греческий', false, 1),
       ('4. Лох русский', false, 1),
       ('1. Лондон', false, 2),
       ('2. Париж', false, 2),
       ('3. Рим', false,2),
       ('4. Икеа', true, 2),
       ('1. Свинг', false, 3),
       ('2. Хук', false, 3),
       ('3. Апперкот', true, 3),
       ('4. Джэб', false, 3),
       ('1. Проксиома Центавра', false, 4),
       ('2. Солнце', true, 4),
       ('3. Полярная', false, 4),
       ('4. Сириус', false, 4),
       ('1. Число Пи', true, 5),
       ('2. Ряд активности металлов', false, 5),
       ('3. Цвета радуги', false, 5),
       ('4. Порядок падежей', false, 5),
       ('1. 0.25 кв.см', true, 6),
       ('2. 1 кв.см', false, 6),
       ('3. 0.5 кв.см', false, 6),
       ('4. 1.25 кв. см', false, 6),
       ('1. Кентавр', false, 7),
       ('2. Грифон', false, 7),
       ('3. Василиск', false, 7),
       ('4. Единорог', true, 7);

INSERT INTO answers_user(answer, user_id, questions_id)
VALUES (1, 1, 1),
       (7, 1, 2),
       (10, 1, 3),
       (14, 1, 4),
       (20, 1, 5),
       (21, 1, 6),
       (27, 1, 7),
       (2, 2, 1),
       (6, 2, 2),
       (10, 2, 3),
       (14, 2, 4),
       (18, 2, 5),
       (22, 2, 6),
       (26, 2, 7),
       (1, 3, 1),
       (6, 3, 2),
       (11, 3, 3),
       (16, 3, 4),
       (17, 3, 5),
       (22, 3, 6),
       (27, 3, 7);

--tests
--error duplicate key
INSERT INTO answers_user(answer, user_id, questions_id)
VALUES (25, 3, 7);

--output correct answers from users
SELECT nick_name, answers_user.answer
FROM answers, answers_user, app_user
WHERE answers_user.questions_id = answers.questions_id AND
      answers_user.answer = answers.id AND
      true_answer = TRUE AND
      user_id = app_user.id;

--sum of correct responses from users
SELECT nick_name, count(nick_name) AS sum_true_answer
FROM answers, answers_user, app_user
WHERE answers_user.questions_id = answers.questions_id AND
      answers_user.answer = answers.id AND
      true_answer = TRUE AND
      user_id = app_user.id
GROUP BY nick_name;

SELECT * FROM answers_user
    JOIN answers ON answers_user.questions_id = answers.questions_id AND
                    answers_user.answer = answers.id AND
                    true_answer = TRUE;

UPDATE answers_user
SET answer = 2
WHERE
    user_id = 1 AND
    questions_id = 1;

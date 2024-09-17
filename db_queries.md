Создание таблицы Regions:

CREATE TABLE "Regions" (
	id serial PRIMARY KEY,
	name varchar
);


Создание таблицы Locations:

CREATE TABLE "Locations" (
	id serial PRIMARY KEY,
	address varchar,
	region_id int REFERENCES "Regions"(id)
);


Создание таблицы Departments:

CREATE TABLE "Departments" (
  id serial PRIMARY KEY,
  name varchar,
  location_id int REFERENCES "Locations"(id),
  manager_id int
);


Создание таблицы Employees:

CREATE TABLE "Employees" (
  id serial PRIMARY KEY,
  name varchar,
  last_name varchar,
  hire_date date,
  salary int,
  email varchar,
  manager_id int REFERENCES "Employees"(id),
  department_id int REFERENCES "Departments"(id)
);


Добавление в таблицу Departments ограничения (внешний ключ по полю manager_id):

ALTER TABLE "Departments"
ADD CONSTRAINT fk_manager_id
FOREIGN KEY (manager_id) REFERENCES "Employees"(id);


Показать работников, у которых нет почты или почта не в корпоративном домене (домен dualbootpartners.com):

SELECT * FROM "Employees"
WHERE email IS NULL 
   OR email NOT LIKE '%dualbootpartners.com';


Получить список работников, нанятых в последние 30 дней:

SELECT * FROM "Employees"
WHERE hire_date >= CURDATE - INTERVAL '30 days';


Найти максимальную и минимальную зарплату по каждому департаменту:

SELECT d.name AS department_name,
       MAX(e.salary) AS max_salary,
       MIN(e.salary) AS min_salary
FROM "Employees" e
JOIN "Departments" d ON e.department_id = d.id
GROUP BY d.name;


Посчитать количество работников в каждом регионе:

SELECT r.name AS region_name,
       COUNT(e.id) AS employee_count
FROM "Employees" e
JOIN "Departments" d ON e.department_id = d.id
JOIN "Locations" l ON d.location_id = l.id
JOIN "Regions" r ON l.region_id = r.id
GROUP BY r.name


Показать сотрудников, у которых фамилия длинее 10 символов:

SELECT * FROM "Employees"
WHERE LENGTH(last_name) > 10;


Показать сотрудников с зарплатой выше средней по всей компании:

SELECT * FROM "Employees"
WHERE salary > (SELECT AVG(salary) FROM "Employees");

# Blog Website Backend (Flask API)
This repository contains Python backend files for a blog website built using Flask, SQLite, REST API and Data Structures. 

* Tools Used: DB Browser for SQLite, Postman, Visual Studio Code, Github Desktop
* Libraries used: flask, sqlite3, flask_sqlalchemy, sqlalchemy
* Data Structures Used: Linked List, Binary Search Tree, Stack, Queue, Hash Table

1. DB Browser for SQLite: Allows the users to view the database via a graphical user interface. It is used to create, design, and edit database files compatible with SQLite. 
2. Postman: An API platform for building and using APIs.
3. Flask: Micro web framework for creating APIs in Python. It is a middleware that is between the python application and the server.
4. SQLite3: file-based SQL database used to integrate the SQLite database with Python.
5. SQLAlchemy: Facilitates the communication between Python programs and databases.
6. Flask-SQLAlchemy: Flask extension that makes using SQLAlchemy with Flask easier, providing you tools and methods to interact with your database in your Flask applications through SQLAlchemy.
7. Object-Relational Mapping (ORM): Technique that lets you query and manipulate data from a database using an object-oriented paradigm.

## Installation
1. A virtual environment "venv" is created by the following command:
> python3 -m venv venv
2. The "venv" virtual environment is activated by the command (macOS):
>. venv/bin/activate
3. To install Flask:
>pip install flask
4. To install flask_sqlalchemy:
>pip install flask_sqlalchemy
5. To install sqlite3:
>pip install pysqlite3 
 
 In the command line, to generate the database
1. python
2. from server import db,app
3. app.app_context().push()
4. db.create_all()
5. exit()

## Output of the application

1. User Table Values:

<img width="390" alt="image" src="https://user-images.githubusercontent.com/89472841/197842836-53f40183-2d70-489e-a11c-7e8514ad08bd.png">
2. Blog Post Table values:

<img width="704" alt="image" src="https://user-images.githubusercontent.com/89472841/197843007-ad50128a-a8bb-47c4-8942-8da77eef5e13.png">

### Output of REST API functions:

1. POST - Create User <br/>
User: {
    "name":"Barack Obama",
    "email":"obamabarack@gmail.com",
    "address":"Washington D.C",
    "phone":"7777666688"
}

<img width="440" alt="image" src="https://user-images.githubusercontent.com/89472841/197843437-ee9b68da-67ed-43d6-88e6-2cc928e8004a.png">

2. GET - get_users_descending_order

<img width="322" alt="image" src="https://user-images.githubusercontent.com/89472841/197843705-38943bc1-cfc9-4bbc-9915-6c535ddedc22.png">

3. GET - get_users_ascending_order

<img width="291" alt="image" src="https://user-images.githubusercontent.com/89472841/197843864-a5a045c5-5855-4e76-b749-418fd4992e83.png">

4. GET - get_one_user

User ID: 1

<img width="173" alt="image" src="https://user-images.githubusercontent.com/89472841/197844051-880eb961-825f-4939-8edc-18502d5d37d4.png">

User ID: 6

<img width="250" alt="image" src="https://user-images.githubusercontent.com/89472841/197844173-a84abb78-c04d-4432-8fc1-2c1d36cbc33b.png">

5. DELETE - delete_user_id

<img width="550" alt="image" src="https://user-images.githubusercontent.com/89472841/197844625-72400897-833d-493b-9f05-d1cf49e79bb3.png">

<img width="433" alt="image" src="https://user-images.githubusercontent.com/89472841/197844698-60758ec6-516f-437d-94b0-093d04bf10c0.png">

6. POST - Add Blog

{
    "title":"My Summer as a Software Engineering Intern at Pinterest Toronto!",
    "body":"This summer, I had the incredible opportunity to intern at the one and only Pinterest from the new engineering hub in Toronto!",
    "user_id":13
}

<img width="703" alt="image" src="https://user-images.githubusercontent.com/89472841/197846957-5b0e4954-39fd-4bac-858a-858b065dde22.png">


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

1. Author Table Values:

<img width="307" alt="image" src="https://user-images.githubusercontent.com/89472841/197905583-1991c83c-419b-4ead-90b8-fbebf19a931d.png">

2. Book Table values:

<img width="868" alt="image" src="https://user-images.githubusercontent.com/89472841/197909708-550a35bd-fd96-46ee-9130-3c3b91648370.png">


### Output of REST API functions:

1. POST - Create Author <br/>
{
    "fname":"Joanne",
    "lname":"Rowling",
    "country":"United Kingdom"
}

<img width="323" alt="image" src="https://user-images.githubusercontent.com/89472841/197909928-b9ea4411-ca29-481e-a73a-19c7c1d0006d.png">

2. GET - get_authors_descending_order

<img width="280" alt="image" src="https://user-images.githubusercontent.com/89472841/197910031-59518a39-589e-455b-b3a4-6464e2dab186.png">

3. GET - get_users_ascending_order

<img width="293" alt="image" src="https://user-images.githubusercontent.com/89472841/197910178-b5e82e23-4c59-44a7-91a0-918d95f18ad4.png">

4. GET - get_one_user

User ID: 11

<img width="201" alt="image" src="https://user-images.githubusercontent.com/89472841/197910663-bd489db7-c890-4cf4-be31-36c26778de0f.png">

User ID: 22

<img width="91" alt="image" src="https://user-images.githubusercontent.com/89472841/197910708-51882304-4463-4924-b266-f8c3e2a764f5.png">

5. DELETE - delete_author_id

User ID: 10

<img width="602" alt="image" src="https://user-images.githubusercontent.com/89472841/197911121-06b20fe7-015c-4c84-9c40-715d067afe85.png">
<img width="313" alt="image" src="https://user-images.githubusercontent.com/89472841/197911158-dbe63d9b-ad99-451c-ad3e-9168de8bba82.png">

User ID: 22

<img width="405" alt="image" src="https://user-images.githubusercontent.com/89472841/197911217-67c49d9a-b2f2-4a21-a95f-1c44cd3045f2.png">

6. POST - Add Blog

{
    "title":"My Summer as a Software Engineering Intern at Pinterest Toronto!",
    "body":"This summer, I had the incredible opportunity to intern at the one and only Pinterest from the new engineering hub in Toronto!",
    "user_id":13
}

<img width="703" alt="image" src="https://user-images.githubusercontent.com/89472841/197846957-5b0e4954-39fd-4bac-858a-858b065dde22.png">


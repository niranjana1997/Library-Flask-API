# Flask API
To view schema and tables, Sqlite3 DB Browser will allow users to view the database via a graphical user interface. 
## Installation
SQLAlchemy is a library that facilitates the communication between Python programs and databases.
<br/>
Flask-SQLAlchemy is a Flask extension that makes using SQLAlchemy with Flask easier, providing you tools and methods to interact with your database in your Flask applications through SQLAlchemy.
<br/>
Python SQLite3 module is used to integrate the SQLite database with Python.
<br/>
SQLite DB Browser is an open-source visual tool used to create, design, and edit database files compatible with SQLite. 

1. A virtual environment "venv" is created by the following command:
>>> python3 -m venv venv
2. The virtual environment is activated by the command (macOS):
>>>. venv/bin/activate
3. To install Flask:<br/>
   Flask is a framework used for building complex web applications. It is a middleware that is between the python application and the server.
>>>pip install flask
4. To install flask_sqlalchemy:
>>>pip install flask_sqlalchemy
5. To install sqlite3:
>>>pip install pysqlite3 
 
 In the command line, to generate the database
>>> python
>>> from server import db,app
>>> app.app_context().push()
>>> db.create_all()
>>> exit()

Object-Relational Mapping (ORM) is a technique that lets you query and manipulate data from a database using an object-oriented paradigm.

## Output of the application

1. User Table Values:
<img width="390" alt="image" src="https://user-images.githubusercontent.com/89472841/197842836-53f40183-2d70-489e-a11c-7e8514ad08bd.png">
2. Blog Post Table values:
<img width="704" alt="image" src="https://user-images.githubusercontent.com/89472841/197843007-ad50128a-a8bb-47c4-8942-8da77eef5e13.png">

### Output of REST API functions:

1. POST - Create User
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


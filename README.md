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

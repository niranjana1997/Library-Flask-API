# Library Flask API 
This repository contains Python backend files for a library website built using Flask, SQLite, REST API and Data Structures. 

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

1. POST - Add Author to Database <br/>
{
    "fname":"Joanne",
    "lname":"Rowling",
    "country":"United Kingdom"
}

<img width="323" alt="image" src="https://user-images.githubusercontent.com/89472841/197909928-b9ea4411-ca29-481e-a73a-19c7c1d0006d.png">

2. GET - Get Authors in Descending Order (Data Structure Used: Linked List)

<img width="280" alt="image" src="https://user-images.githubusercontent.com/89472841/197910031-59518a39-589e-455b-b3a4-6464e2dab186.png">

3. GET - Get Authors in Ascending Order (Data Structure Used: Linked List)

<img width="293" alt="image" src="https://user-images.githubusercontent.com/89472841/197910178-b5e82e23-4c59-44a7-91a0-918d95f18ad4.png">

4. GET - Get One Author by ID (Data Structure Used: Linked List)

User ID: 11

<img width="201" alt="image" src="https://user-images.githubusercontent.com/89472841/197910663-bd489db7-c890-4cf4-be31-36c26778de0f.png">

User ID: 22

<img width="91" alt="image" src="https://user-images.githubusercontent.com/89472841/197910708-51882304-4463-4924-b266-f8c3e2a764f5.png">

5. DELETE - Delete Author by ID

User ID: 10

<img width="602" alt="image" src="https://user-images.githubusercontent.com/89472841/197911121-06b20fe7-015c-4c84-9c40-715d067afe85.png">
<img width="313" alt="image" src="https://user-images.githubusercontent.com/89472841/197911158-dbe63d9b-ad99-451c-ad3e-9168de8bba82.png">

User ID: 22

<img width="405" alt="image" src="https://user-images.githubusercontent.com/89472841/197911217-67c49d9a-b2f2-4a21-a95f-1c44cd3045f2.png">

6. GET - Get One Book by ID (Data Structure Used: Tree - Binary Search Tree Algorithm)

Book ID: 1

<img width="990" alt="image" src="https://user-images.githubusercontent.com/89472841/197911802-b8cf11b0-8094-4f7a-891c-e8b77a9f3252.png">

Book ID: 10

<img width="242" alt="image" src="https://user-images.githubusercontent.com/89472841/197911846-1254604f-5fde-4d6e-b20b-62b2356d63f4.png">

7. GET - Get Book's Preface's ASCII value (Data Structure Used: Queue)

<img width="994" alt="image" src="https://user-images.githubusercontent.com/89472841/197912894-3aefdd65-ee56-4982-a9da-5da3bd25b13a.png">

8. POST - Add Book to Database <br/>
{
    "title":"Harry Potter and the Deathly Hallows",
    "total_pages": 759,
    "rating": 4.62,
    "isbn": "9788893814560",
    "published_date": "2007-07-21",
    "preface": "Harry has been burdened with a dark, dangerous and seemingly impossible task: that of locating and destroying Voldemort's remaining Horcruxes. Never has Harry felt so alone, or faced a future so full of shadows. But Harry must somehow find within himself the strength to complete the task he has been given. He must leave the warmth, safety and companionship of The Burrow and follow without fear or hesitation the inexorable path laid out for him..."
}

<img width="867" alt="image" src="https://user-images.githubusercontent.com/89472841/197913339-2d4cfc19-a207-49b4-9d18-48d2287db9e3.png">

9. DELETE - Delete last 5 Books (Data Structure Used: Stack)

Test Case 1: When 9 Books are present in the Database:

<img width="414" alt="image" src="https://user-images.githubusercontent.com/89472841/197913561-129eba19-38ae-42cc-9b60-61cd91ecef14.png">

<img width="875" alt="image" src="https://user-images.githubusercontent.com/89472841/197913607-d44aa907-1dfe-4464-ab1a-3ddd076907c0.png">

Test Case 2: When 4 Books are present in the Database

<img width="481" alt="image" src="https://user-images.githubusercontent.com/89472841/197913679-b854a105-6e38-4f57-b33c-7585a2b45a1d.png">

<img width="863" alt="image" src="https://user-images.githubusercontent.com/89472841/197913722-c35c9ab4-2cf9-4477-93a4-912b65709cd9.png">

Test Case 3: When the Book Database is empty

<img width="380" alt="image" src="https://user-images.githubusercontent.com/89472841/197913798-a5e134bc-3acf-4bc9-ae19-3a428a8a0d1a.png">

<img width="863" alt="image" src="https://user-images.githubusercontent.com/89472841/197913722-c35c9ab4-2cf9-4477-93a4-912b65709cd9.png">


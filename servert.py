from flask import jsonify, request, Flask
# Python SQLite3 module is used to integrate the SQLite database with Python.
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
# This library adds Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application
from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy is a library that facilitates the communication between Python programs and databases.
from sqlalchemy import event
from sqlalchemy.engine import Engine
import LinkedList as ll
import HashTable as ht
import BinarySearchTree as bst
import random as rand
import Queue as q
import Stack as s
from datetime import datetime

app = Flask(__name__)

# database configuration

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///author_book.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# Allowing to configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

# creating instance of the database by passing app into SQLAlchemy class
# This class is used to control the SQL alchemy integration to one or more flask applications
# connecting ORM with flask application
db = SQLAlchemy(app)
# this is used to update date values while updating tables
current_time = datetime.now()

# orm tool translates python classes to tables on relational databases and 
# automatically converts function calls to SQL statements

# class Author represents a table in the database
class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    country = db.Column(db.String(50))
    # this is a foreign key with another table "Book"
    # cascade = "all, delete" will reflect delete changes in Book table too
    book = db.relationship("Book", cascade="all, delete")

# class Book represents a table in the database
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    total_pages = db.Column(db.Integer)
    rating = db.Column(db.Numeric)
    isbn = db.Column(db.String(20))
    published_date = db.Column(db.Date)
    preface = db.Column(db.String(200))
    date_created = db.Column(db.Date)
    # this is a foreign key with another table "Author"
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

# in order to create a function that corresponds to a route, app.route decorator is used
@app.route("/author", methods=["POST"])
def create_new_author():
    # requests will store the values as dict in data variable
    data = request.get_json()
    new_author = Author(
        fname=data["fname"],
        lname=data["lname"],
        country=data["country"],
    )
    # adds new author to the db
    db.session.add(new_author)
    db.session.commit()
    # returns a success message
    return jsonify({"message": "New Author Added to the Database"}), 200

# books are added
@app.route("/book/<input_author_id>", methods=["POST"])
def add_new_book(input_author_id):
    # requests will store the values as dict in data variable
    data = request.get_json()
    check_author = Author.query.filter_by(id=input_author_id).first()
    if not check_author:
        return jsonify({"message": "Author does not exist"}), 400
    published_date = data["published_date"].split("-")
    formatted_date = datetime(int(published_date[0]), int(published_date[1]), int(published_date[2]))
    print("pp", published_date)
    print(formatted_date)
    hashTable = ht.HashTable(10)

    hashTable.add_key_value_to_hash_table("title", data["title"])
    hashTable.add_key_value_to_hash_table("total_pages", data["total_pages"])
    hashTable.add_key_value_to_hash_table("rating", data["rating"])
    hashTable.add_key_value_to_hash_table("isbn", data["isbn"])
    hashTable.add_key_value_to_hash_table("published_date", formatted_date)
    hashTable.add_key_value_to_hash_table("date_created", current_time)
    hashTable.add_key_value_to_hash_table("preface", data["preface"])
    hashTable.add_key_value_to_hash_table("author_id", input_author_id)

    new_book = Book(
        title = hashTable.get_value_by_key("title"),
        total_pages = hashTable.get_value_by_key("total_pages"),
        rating = hashTable.get_value_by_key("rating"),
        isbn = hashTable.get_value_by_key("isbn"),
        published_date = hashTable.get_value_by_key("published_date"),
        preface = hashTable.get_value_by_key("preface"),
        date_created = hashTable.get_value_by_key("date_created"),
        author_id = hashTable.get_value_by_key("author_id"),
    )

    # adds new author to the db
    db.session.add(new_book)
    db.session.commit()
    # returns a success message
    return jsonify({"message": "New Book Added to the Database"}), 200


# displays author in descending order of adding
@app.route("/author/author_descending_order", methods=["GET"])
def get_author_descending_order():
    # getting all authors from db
    all_authors = Author.query.all()
    # creates a linked list
    ll_all_authors = ll.LinkedList()
    # iterating each value in all_authors and adding it to beginning of linked list 
    for eachAuthor in all_authors:
        ll_all_authors.beginning_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    # returns the json by converting the linked list to list
    return jsonify(ll_all_authors.convert_ll_to_list()), 200

# get authors in ascending order
@app.route("/author/authors_ascending_order", methods=["GET"])
def get_all_authors_ascending():
    # getting all authors from db
    all_authors = Author.query.all()
    # creates a linked list
    ll_all_authors = ll.LinkedList()
    # iterating each value in all_authors and adding it to end of linked list 
    for eachAuthor in all_authors:
        ll_all_authors.end_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    # returns the json by converting the linked list to list
    return jsonify(ll_all_authors.convert_ll_to_list()), 200


@app.route("/author/<input_author_id>", methods=["GET"])
def get_one_author(input_author_id):
    # getting all authors from db
    all_authors = Author.query.all()
    # creates a linked list
    ll_all_authors = ll.LinkedList()
    for eachAuthor in all_authors:
        ll_all_authors.beginning_insert(
            {
                "id": eachAuthor.id,
                "fname": eachAuthor.fname,
                "lname": eachAuthor.lname,
                "country": eachAuthor.country,
            }
        )
    output_details = ll_all_authors.get_author_by_id(input_author_id)
    return jsonify(output_details), 200

# query the database to delete the author
@app.route("/author/<input_author_id>", methods=["DELETE"])
def delete_author_id(input_author_id):
    author = Author.query.filter_by(id = input_author_id).first()
    if not author:
        return jsonify({"message": "Author ID (" + str(input_author_id) + ") does not exist"}), 400
    # when trying to delete a author that has a id in the book table, 
    # and since a foreign key constraint is added to the author id column of the book table
    # we need to cascade the deletion of author id in book table too
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author ID (" + str(input_author_id) + ") with Name (" + author.fname + " " + author.lname +") deleted successfully"}), 200


@app.route("/book/<book_id>", methods=["GET"])
def get_one_book(book_id):
    # query all books by query.all()
    all_books = Book.query.all()
    # in order to avoid inserting into binary node in ascending order, it is shuffled
    rand.shuffle(all_books)

    # binary search tree is used to insert all_books
    # and search for 'book_id and retrieve it
    binary_search_tree = bst.BinarySearchTree()

    # iterates through each book in all_books and inserting each value
    for eachBook in all_books:
        binary_search_tree.insert({
            "id" : eachBook.id,
            "title" : eachBook.title,
            "total_pages" : eachBook.total_pages,
            "rating" : eachBook.rating,
            "isbn" : eachBook.isbn,
            "published_date" : eachBook.published_date,
            "date_created" : eachBook.date_created,
            "preface" : eachBook.preface,
            "author_id" : eachBook.author_id,
        })
    # search method is called to search for book_id
    book = binary_search_tree.search(book_id)
    # if book is not available, error message is sent
    if not book:
        return jsonify({"message": "Book not found"})
    # else, message is sent
    else:
        return jsonify(book)

# finds the ascii total of preface of the book
@app.route("/book/numeric_preface", methods=["GET"])
def get_numeric_of_book_preface():
    # getting all book from db
    all_books = Book.query.all()
    # queue object is created
    queue = q.Queue()
    # iterating through each book in all_books
    for eachBook in all_books:
        # adding element (eachBook) to the queue
        queue.enqueue(eachBook)
    # output list is declared and initialized
    output = []
    # iterating through each element in all_books
    for i in range(len(all_books)):
        # dequeued element is set as popped_element
        popped_element = queue.dequeue()
        # counter parameter is set and intialized
        counter = 0
        # iterating through each character in preface
        for character in popped_element.data.preface:
            # adding ascii value of the character to 
            counter += ord(character)
        # returning details in json format
        output.append(
            {
                "id": popped_element.data.id,
                "title" : popped_element.data.title,
                "preface_ascii" : counter,
                "preface": popped_element.data.preface,
            }
        )
    return jsonify(output)

@app.route("/book/delete_last_5", methods=["DELETE"])
def delete_last_5():
    # getting all books from db
    all_books = Book.query.all()
    # creating the stack object
    stack = s.Stack()
    # itertaing through all_books and adding each book to stack
    for eachBook in all_books:
        stack.push(eachBook)
    # iterating 5 times to remove 5 elements
    for i in range(5):
        # top element is popped and removed from db
        popped_element = stack.pop()
        if popped_element is None:
            if i == 0:
                return jsonify({"message" : "Database is empty"})
            else:
                return jsonify({"message" : "Database is empty. Few elements were removed"})

        db.session.delete(popped_element.data)
        db.session.commit()
    # success message is returned
    return jsonify({"message" : "All Elements deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
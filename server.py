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

app = Flask(__name__)

# database configuration

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
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

# class User represents a table in the database
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    # this is a foreign key with another table "BlogPost"
    # cascade = "all, delete" will reflect delete changes in BlogPost table too
    posts = db.relationship("BlogPost", cascade="all, delete")

# class BlogPost represents a table in the database
class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    # this is a foreign key with another table "User"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# in order to create a function that corresponds to a route, app.route decorator is used
@app.route("/user", methods=["POST"])
def create_new_user():
    # requests will store the values as dict in data variable
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )
    # adds new user to the db
    db.session.add(new_user)
    db.session.commit()
    # returns a success message
    return jsonify({"message": "New User Added to the Database"}), 200

# blogs are added
@app.route("/blog/<input_user_id>", methods=["POST"])
def add_new_blog(input_user_id):
    # requests will store the values as dict in data variable
    data = request.get_json()
    check_user = User.query.filter_by(id=input_user_id).first()
    if not check_user:
        return jsonify({"message": "User does not exist"}), 400
    hashTable = ht.HashTable(10)

    hashTable.add_key_value_to_hash_table("title", data["title"])
    hashTable.add_key_value_to_hash_table("body", data["body"])
    hashTable.add_key_value_to_hash_table("date", current_time)
    hashTable.add_key_value_to_hash_table("user_id", input_user_id)

    new_blog_post = BlogPost(
        title = hashTable.get_value_by_key("title"),
        body = hashTable.get_value_by_key("body"),
        date = hashTable.get_value_by_key("date"),
        user_id = hashTable.get_value_by_key("user_id"),
    )

    # adds new user to the db
    db.session.add(new_blog_post)
    db.session.commit()
    # returns a success message
    return jsonify({"message": "New Blog Added to the Database"}), 200


# displays user in descending order of adding
@app.route("/user/user_descending_order", methods=["GET"])
def get_users_descending_order():
    # getting all users from db
    all_users = User.query.all()
    # creates a linked list
    ll_all_users = ll.LinkedList()
    # iterating each value in all_users and adding it to beginning of linked list 
    for eachUser in all_users:
        ll_all_users.beginning_insert(
            {
                "id": eachUser.id,
                "name": eachUser.name,
                "email": eachUser.email,
                "address": eachUser.address,
                "phone": eachUser.phone,
            }
        )
    # returns the json by converting the linked list to list
    return jsonify(ll_all_users.convert_ll_to_list()), 200

# get users in ascending order
@app.route("/user/user_ascending_order", methods=["GET"])
def get_all_users_ascending():
    # getting all users from db
    all_users = User.query.all()
    # creates a linked list
    ll_all_users = ll.LinkedList()
    # iterating each value in all_users and adding it to end of linked list 
    for eachUser in all_users:
        ll_all_users.end_insert(
            {
                "id": eachUser.id,
                "name": eachUser.name,
                "email": eachUser.email,
                "address": eachUser.address,
                "phone": eachUser.phone,
            }
        )
    # returns the json by converting the linked list to list
    return jsonify(ll_all_users.convert_ll_to_list()), 200


@app.route("/user/<input_user_id>", methods=["GET"])
def get_one_user(input_user_id):
    # getting all users from db
    all_users = User.query.all()
    # creates a linked list
    ll_all_users = ll.LinkedList()
    for eachUser in all_users:
        ll_all_users.beginning_insert(
            {
                "id": eachUser.id,
                "name": eachUser.name,
                "email": eachUser.email,
                "address": eachUser.address,
                "phone": eachUser.phone,
            }
        )
    output_details = ll_all_users.get_user_by_id(input_user_id)
    return jsonify(output_details), 200

# query the database to delete the user
@app.route("/user/<input_user_id>", methods=["DELETE"])
def delete_user_id(input_user_id):
    user = User.query.filter_by(id = input_user_id).first()
    # when trying to delete a user that has a id in the blog post table, 
    # and since a foreign key constraint is added to the user id column of the blog post table
    # we need to cascade the deletion of user id in blog post table too
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User ID (" + str(input_user_id) + ") with Name (" + user.name + ") deleted successfully"}), 200


@app.route("/blog/<blog_id>", methods=["GET"])
def get_one_blog_post(blog_id):
    # query all blog posts by query.all()
    all_blogs = BlogPost.query.all()
    # in order to avoid inserting into binary node in ascending order, it is shuffled
    rand.shuffle(all_blogs)

    # binary search tree is used to insert all_blogs
    # and search for 'blog_id and retrieve it
    binary_search_tree = bst.BinarySearchTree()

    # iterates through each blog in all_blogs and inserting each value
    for eachBlog in all_blogs:
        binary_search_tree.insert({
            "id" : eachBlog.id,
            "title" : eachBlog.title,
            "body" : eachBlog.body,
            "user_id" : eachBlog.user_id,
        })
    # search method is called to search for blog_id
    post = binary_search_tree.search(blog_id)
    # if post is not available, error message is sent
    if not post:
        return jsonify({"message": "Blog not found"})
    # else, post message is sent
    else:
        return jsonify(post)

# finds the ascii total of body of the blogpost
@app.route("/blog/numeric_body", methods=["GET"])
def get_numeric_of_blog_body():
    # getting all blog posts from db
    all_posts = BlogPost.query.all()
    # queue object is created
    queue = q.Queue()
    # iterating through each post in all_posts
    for eachPost in all_posts:
        # adding element (eachPost) to the queue
        queue.enqueue(eachPost)
    # output list is declared and initialized
    output = []
    # iterating through each element in all_posts
    for i in range(len(all_posts)):
        # dequeued element is set as popped_element
        popped_element = queue.dequeue()
        # counter parameter is set and intialized
        counter = 0
        # iterating through each character in body
        for character in popped_element.data.body:
            # adding ascii value of the character to 
            counter += ord(character)
        # returning details in json format
        output.append(
            {
                "id": popped_element.data.id,
                "title" : popped_element.data.title,
                "body" : counter,
                "user_id" : popped_element.data.user_id,
            }
        )
    return jsonify(output)

@app.route("/blog/delete_last_5", methods=["DELETE"])
def delete_last_5():
    # getting all blog posts from db
    all_posts = BlogPost.query.all()
    # creating the stack object
    stack = s.Stack()
    # itertaing through all_posts and adding each post to stack
    for eachPost in all_posts:
        stack.push(eachPost)
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
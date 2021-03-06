
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv, find_dotenv
from os import getenv
from functools import wraps
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
load_dotenv()

# ---- CONFIG ----- #

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.getenv(
    'MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv(
    'MONGO_URI')
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY')
mongo = PyMongo(app)

# ---- VARIABLES ----- #

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

# ---- USER ----- #

# throws users that are not logged in to Login page if they try to access certain pages


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check first if user already exists
        if existing_user:
            flash("Username already exists! Please try again.")
            return redirect(url_for("signup"))

        signup = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))}
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("Welcome!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("users/signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check if user already exists
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back!")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))
        flash("Incorrect Username and/or Password!")
    return render_template("users/login.html")


@app.route('/profile/<username>', methods=["GET", "POST"])
@login_required
def profile(username):
    if session["user"]:
        # allows admin to access  all recipes
        if session["user"] == "admin":
            recipe = mongo.db.recipe.find()
        else:
            recipe = mongo.db.recipe.find({"username": username})
        return render_template("users/profile.html", recipe=recipe, username=username)
    return render_template("users/login.html")


@ app.route('/logout')
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))

# ---- RECIPE PAGES ----- #


@ app.route('/recipes/<category>')
def get_all(category):
    if category == "all":
        category = "All recipes"
        recipe = mongo.db.recipe.find()
    # specifically filters Other because MongoDB find() does not return certain words
    elif category == "other":
        recipe = mongo.db.recipe.find({"category_name": "Other"})
    else:
        recipe = mongo.db.recipe.find({"$text": {"$search": category}})
    return render_template("recipes.html", recipe=recipe, page_title=category)


@ app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    # only user that posted recipe or admin has access to edit/delete buttons
    user = ""
    if session.get("user"):
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    username = recipe.get("username")
    return render_template("recipe.html", recipe=recipe, user=user, username=username)


@ app.route('/add_recipe')
@login_required
def add_recipe():
    categories = mongo.db.categories.find()
    return render_template("recipe_form.html", categories=categories, the_recipe={}, page_title="Add Recipe")


@ app.route('/send_recipe', methods=['POST'])
@login_required
def send_recipe():
    recipe = mongo.db.recipe
    return_data = request.form.to_dict()
    # adds date and username that posted recipe
    return_data["date_added"] = dt_string
    return_data["username"] = username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipe.insert_one(return_data)
    return redirect(url_for('thank_you'))


@ app.route('/thank_you')
@login_required
def thank_you():
    return render_template("thank_you.html")


@ app.route('/edit_recipe/<recipe_id>')
@login_required
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', the_recipe=the_recipe)


@ app.route('/delete_recipe/<recipe_id>')
@login_required
def delete_recipe(recipe_id):
    the_recipe = mongo.db.recipe.delete_one({"_id": ObjectId(recipe_id)})
    return render_template('index.html', the_recipe=the_recipe)


@ app.route('/update_recipe/<recipe_id>', methods=['POST'])
@login_required
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    categories_cursor = mongo.db.categories.find()
    # updates only fields that have been changed
    recipe.update_one({"_id": ObjectId(recipe_id)},
                      {'$set': {
                          'title': request.form.get('title'),
                          'category_name': request.form.get('category_name'),
                          'description': request.form.get('description'),
                          'image_url': request.form.get('image_url'),
                          'ingredients': request.form.get('ingredients'),
                          'serves': request.form.get('serves'),
                          'prep': request.form.get('prep'),
                          'cooks': request.form.get('cooks'),
                          'difficulty': request.form.get('difficulty'),
                          'instructions': request.form.get('instructions'),
                          'tips': request.form.get('tips'),
                      }})
    return redirect(url_for('thank_you'))


@ app.route('/shop')
def shop():
    return render_template("shop.html")


@ app.route('/terms')
def terms():
    return render_template("users/terms.html")

# ---- NEWSLETTER SUBSCRIPTION FORM ----- #


@ app.route('/sub', methods=['POST'])
def sub():
    sub = mongo.db.subscribers
    return_data = request.form.to_dict()
    sub.insert_one(return_data)
    flash("Sucessfully Subscribed")
    return redirect(request.referrer)

# ---- SEARCH ----- #


@ app.route('/search', methods=["GET", "POST"])
def search():
    mongo.db.recipe.create_index([('$**', 'text')])
    query = request.form.get("query")
    # limits to search results to 10 recipes because there is no pagination yet
    result = mongo.db.recipe.find({"$text": {"$search": query}}).limit(10)
    result_num = mongo.db.recipe.find({"$text": {"$search": query}}).count()
    if result_num > 0:
        return render_template("search_results.html", result=result, query=query)
    else:
        return render_template("search_results.html", result=result, query=query, message="No results found. Please try again")

# ---- ERRORS ----- #


@ app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), debug=False)

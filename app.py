from flask import Flask, render_template, request, jsonify
import random
import requests

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")



@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
    """Process form data and return lucky number and facts."""
    data = request.json

    # Input validation
    errors = {}
    name = data.get("name")
    email = data.get("email")
    year = data.get("year")
    color = data.get("color")

    # If conditional statements to validate the errors
    if not name:
        errors["name"] = ["This field is required."]
    if not email:
        errors["email"] = ["This field is required"]
    if not year or not (1900 <= int(year) <= 2000):
        errors["year"] = ["Must be a number between 1900 and 2000."]
    if color not in ["red", "green", "orange", "blue"]:
        errors["color"] = ["Invalid value, must be one of: red, green , orange, blue"]

    # Return error if validation fails
    if errors:
        return jsonify({"errors": errors}), 400

    # Generate random lucky number
    lucky_num = random.randint(1, 100)

    # Fetch facts from NumbersAPI
    num_fact = requests.get(f"http://numbersapi.com/{lucky_num}").text
    year_fact = requests.get(f"http://numbersapi.com/{year}/year").text

    # Return json response
    return jsonify({
        "num": {"num": lucky_num, "message": num_fact},
        "year": {"year": year, "message": year_fact}
    })

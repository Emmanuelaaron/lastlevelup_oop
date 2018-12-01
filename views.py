from package_controller import PackageController
from flask import Flask, jsonify

app = Flask(__name__)

my_pack = PackageController()
@app.route("/")
def index():
    return jsonify (my_pack.get_package_by_location())

@app.route("/packages", methods=["POST"])
def add_package():
    return my_pack.create_package()
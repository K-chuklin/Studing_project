from flask import Flask, send_from_directory
from skypro.lesson_12_3.main.views import main_blueprint
from skypro.lesson_12_3.loader.views import loader_blueprint


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/list")
def page_tag():
    pass

@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass

@app.route("/post", methods=["POST"])
def page_post_upload():
    pass

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

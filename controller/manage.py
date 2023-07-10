from flask import Blueprint, render_template, request, jsonify

from service.image.flower_classifier import FlowerClassifier

manage = Blueprint("manage", __name__, url_prefix="/manage")
flower_classifier: FlowerClassifier = None


@manage.route("/", methods=["GET"])
def index():
    """
    home page screen
    :return:
    """
    return render_template("manage/index.html")


@manage.route("/image/flower_classify", methods=["GET"])
def manage_flower_classification():
    """
    show Flower Classification screen
    """

    return render_template("manage/image/flower_classify.html")


@manage.route("/image/flower_classify", methods=["POST"])
def predict_flower():
    """
    predict flower type based on saved flower model
    """
    if "flower" not in request.files or not flower_classifier.is_allowed_file(request.files["flower"].filename):
        return jsonify({"error_message": "Flower image (JPG, JPEG, PNG) is required."}), 400
    return jsonify({
        "flower_type": flower_classifier.predict_flower(request.files["flower"])
    })


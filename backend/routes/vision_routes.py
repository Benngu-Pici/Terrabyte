from flask import Blueprint, request, jsonify
from flask_cors import CORS
from services.vision_service import handle_vision_chat

vision_bp = Blueprint("vision", __name__, url_prefix="/api/vision")
CORS(vision_bp)

@vision_bp.route("/chat", methods=["POST"])
def chat():
    # LẤY TEXT
    message = request.form.get("message", "")

    # LẤY FILE
    image_file = request.files.get("image")

    reply = handle_vision_chat(message, image_file)
    return jsonify({"reply": reply})

# app.py
from flask import Flask
from flask_cors import CORS
from routes.vision_routes import vision_bp

app = Flask(__name__)
CORS(app)  # gắn CORS cho app chính (khỏi lỗi OPTIONS nếu có route khác)

app.register_blueprint(vision_bp, url_prefix="/api/vision")

if __name__ == "__main__":
    app.run(debug=True)

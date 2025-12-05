from flask import Flask, jsonify
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app, supports_credentials=True)

    # Register routes
    from routes.auth_routes import auth_bp
    from routes.book_routes import book_bp
    from routes.review_routes import review_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(book_bp, url_prefix="/api/books")
    app.register_blueprint(review_bp, url_prefix="/api/reviews")

    @app.route("/api/health")
    def health():
        return jsonify({"status":"ok"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

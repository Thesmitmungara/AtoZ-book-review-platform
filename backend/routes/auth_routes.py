from flask import Blueprint, request, jsonify, current_app
from models import db, User
from auth import hash_password, verify_password, create_token, decode_token
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not username or not email or not password:
        return jsonify({"msg":"Missing fields"}), 400
    user = User(username=username, email=email, password_hash=hash_password(password))
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"msg":"User/email already exists"}), 409
    token = create_token(user.id)
    return jsonify({"token": token, "user": {"id": user.id, "username": user.username, "email": user.email}}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    identifier = data.get("username") or data.get("email")
    password = data.get("password")
    if not identifier or not password:
        return jsonify({"msg":"Missing credentials"}), 400
    user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()
    if not user or not verify_password(password, user.password_hash):
        return jsonify({"msg":"Invalid credentials"}), 401
    token = create_token(user.id)
    return jsonify({"token": token, "user": {"id": user.id, "username": user.username, "email": user.email}}), 200

# Optional: refresh token, logout (handled on client by deleting token)

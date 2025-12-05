from functools import wraps
from flask import request, jsonify
from auth import decode_token
from models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)
        if not auth_header:
            return jsonify({"msg":"Missing Authorization header"}), 401
        parts = auth_header.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            return jsonify({"msg":"Invalid Authorization header"}), 401
        token = parts[1]
        try:
            payload = decode_token(token)
            user_id = payload.get("sub")
            user = User.query.get(user_id)
            if not user:
                return jsonify({"msg":"User not found"}), 401
            request.current_user = user
        except Exception as e:
            return jsonify({"msg":"Invalid or expired token"}), 401
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not getattr(request, "current_user", None):
            return jsonify({"msg":"Authentication required"}), 401
        if not request.current_user.is_admin:
            return jsonify({"msg":"Admin privileges required"}), 403
        return f(*args, **kwargs)
    return decorated

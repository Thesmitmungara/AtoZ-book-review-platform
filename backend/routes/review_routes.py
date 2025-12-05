from flask import Blueprint, request, jsonify
from models import db, Book, Review
from routes.helpers import token_required

review_bp = Blueprint('reviews', __name__)

@review_bp.route("/<int:book_id>", methods=["POST"])
@token_required
def add_review(book_id):
    data = request.json
    rating = int(data.get("rating",0))
    comment = data.get("comment")
    if rating < 1 or rating > 5:
        return jsonify({"msg":"Rating must be 1-5"}), 400
    book = Book.query.get_or_404(book_id)
    # prevent duplicate review by same user (optional)
    existing = Review.query.filter_by(book_id=book.id, user_id=request.current_user.id).first()
    if existing:
        return jsonify({"msg":"You have already reviewed this book"}), 409
    review = Review(rating=rating, comment=comment, user_id=request.current_user.id, book_id=book.id)
    db.session.add(review)
    db.session.commit()
    return jsonify({"id": review.id, "rating": review.rating}), 201

@review_bp.route("/<int:review_id>", methods=["PUT"])
@token_required
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.user_id != request.current_user.id:
        return jsonify({"msg":"Forbidden"}), 403
    data = request.json
    review.rating = int(data.get("rating", review.rating))
    review.comment = data.get("comment", review.comment)
    db.session.commit()
    return jsonify({"msg":"updated"})

@review_bp.route("/<int:review_id>", methods=["DELETE"])
@token_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    if review.user_id != request.current_user.id and not request.current_user.is_admin:
        return jsonify({"msg":"Forbidden"}), 403
    db.session.delete(review)
    db.session.commit()
    return jsonify({"msg":"deleted"})

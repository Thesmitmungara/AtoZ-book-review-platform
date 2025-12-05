from flask import Blueprint, request, jsonify
from models import db, Book, Review
from routes.helpers import token_required, admin_required

book_bp = Blueprint('books', __name__)

@book_bp.route("/", methods=["GET"])
def list_books():
    page = int(request.args.get("page",1))
    per_page = int(request.args.get("per_page", 10))
    q = request.args.get("q")
    query = Book.query
    if q:
        query = query.filter(Book.title.ilike(f"%{q}%"))
    pag = query.order_by(Book.created_at.desc()).paginate(page, per_page, False)
    items = []
    for book in pag.items:
        avg_rating = None
        if book.reviews:
            avg_rating = sum([r.rating for r in book.reviews]) / len(book.reviews)
        items.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "avg_rating": avg_rating,
            "description": book.description
        })
    return jsonify({"items": items, "total": pag.total})

@book_bp.route("/", methods=["POST"])
@token_required
@admin_required
def create_book():
    data = request.json
    book = Book(
        title=data.get("title"),
        author=data.get("author"),
        description=data.get("description"),
        published_year=data.get("published_year")
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({"id": book.id, "title": book.title}), 201

@book_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    reviews = [{
        "id": r.id, "rating": r.rating, "comment": r.comment,
        "user": {"id": r.user.id, "username": r.user.username}, "created_at": r.created_at.isoformat()
    } for r in book.reviews]
    return jsonify({
        "id": book.id, "title": book.title, "author": book.author,
        "description": book.description, "published_year": book.published_year,
        "reviews": reviews
    })
@book_bp.route("/<int:book_id>", methods=["PUT"])
@token_required
@admin_required
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.description = data.get("description", book.description)
    book.published_year = data.get("published_year", book.published_year)
    db.session.commit()
    return jsonify({"msg":"updated"})

@book_bp.route("/<int:book_id>", methods=["DELETE"])
@token_required
@admin_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"msg":"deleted"})

from app import create_app
from models import db, User, Book
from auth import hash_password

app = create_app()
app.app_context().push()

db.create_all()

if not User.query.filter_by(username="admin").first():
    admin = User(username="admin", email="admin@example.com", password_hash=hash_password("adminpass"), is_admin=True)
    db.session.add(admin)

# add sample books
books = [
    Book(title="The Pragmatic Programmer", author="Andrew Hunt", description="...", published_year=1999),
    Book(title="Clean Code", author="Robert C. Martin", description="...", published_year=2008),
]
for b in books:
    if not Book.query.filter_by(title=b.title).first():
        db.session.add(b)

db.session.commit()
print("Seeded DB")

Book Review Platform

A full-stack web application that allows users to browse books, write reviews, and manage authentication using JWT.
The frontend is built using React, and the backend is built using Flask.

Features
User Features

Register and log in securely

Browse all books

View book details and reviews

Add, edit, and delete your reviews

Rate books

Admin Features

Add new books

Update existing books

Delete books

Security

JWT authentication

Password hashing

Role-based access for admin

Tech Stack
Frontend

React

React Router

Axios

Bootstrap

Backend

Flask

SQLAlchemy

PyJWT

Database

SQLite (development)

Project Structure
AtoZ-book-review-platform/
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── config.py
│   ├── models.py
│   ├── seed.py
│   ├── requirements.txt
│   └── routes/
│       ├── auth_routes.py
│       ├── book_routes.py
│       ├── review_routes.py
│       └── helpers.py
│
└── frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js
        ├── api.js
        ├── index.js
        ├── contexts/
        │   └── AuthContext.js
        ├── components/
        │   ├── BookCard.js
        │   ├── ProtectedRoute.js
        │   └── ReviewForm.js
        └── pages/
            ├── Login.js
            ├── Register.js
            ├── BookList.js
            ├── BookDetail.js
            └── AdminDashboard.js

API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/auth/register	Register a new user
POST	/api/auth/login	Login and receive JWT token
Books
Method	Endpoint	Description
GET	/api/books	Get list of all books
POST	/api/books	Create a new book (Admin only)
GET	/api/books/<id>	Get details of a single book
PUT	/api/books/<id>	Update book details (Admin only)
DELETE	/api/books/<id>	Delete a book (Admin only)
Reviews
Method	Endpoint	Description
POST	/api/reviews/<book_id>	Add a review to a book
PUT	/api/reviews/<review_id>	Edit a review (owner only)
DELETE	/api/reviews/<review_id>	Delete a review (owner or admin)
Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Create .env:

SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret
DATABASE_URL=sqlite:///db.sqlite3
JWT_EXP=3600


Initialize the database:

python seed.py


Run backend:

python app.py


Backend will run at:
http://localhost:5000

Frontend Setup
cd frontend
npm install


Create .env:

REACT_APP_API_URL=http://localhost:5000/api


Run React app:

npm start


Frontend will run at:
http://localhost:3000

Future Enhancements

Add book cover image upload

Add search & category filtering

Add user profile page

Deploy backend (Render / Railway)

Deploy frontend (Vercel / Netlify)

Author

Smit Patel
GitHub: https://github.com/Thesmitmungara

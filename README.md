# 📚 Book Review Platform

A full-stack web application for browsing books, writing reviews, and managing authentication using JWT.  
Built with **React**, **Flask**, and **SQLAlchemy**.

---

## ✨ Features

### 👤 User Features
- Register and log in securely  
- Browse list of books  
- View detailed book pages  
- Add reviews & ratings  
- Edit and delete own reviews  

### 🛠️ Admin Features
- Add new books  
- Update book details  
- Delete books  
- Manage catalog  

### 🔐 Security
- Password hashing  
- JWT authentication  
- Protected routes  
- Admin-only access controls  

---

## 🧱 Tech Stack

### 🎨 Frontend
- React  
- React Router  
- Axios  
- Bootstrap  

### ⚙️ Backend
- Flask  
- SQLAlchemy ORM  
- PyJWT  

### 🗄 Database
- SQLite (development)  
- Extendable to PostgreSQL / MySQL  

---

## 📁 Project Structure

```
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
```

---

# 🔗 API Endpoints

## 🔐 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login and receive JWT token |

---

## 📚 Books
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | Get all books |
| POST | `/api/books` | Add new book (Admin only) |
| GET | `/api/books/<id>` | Get book details |
| PUT | `/api/books/<id>` | Update book (Admin only) |
| DELETE | `/api/books/<id>` | Delete book (Admin only) |

---

## ⭐ Reviews
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/reviews/<book_id>` | Add a review |
| PUT | `/api/reviews/<review_id>` | Edit a review |
| DELETE | `/api/reviews/<review_id>` | Delete a review |

---

# 🖥️ Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```
SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret
DATABASE_URL=sqlite:///db.sqlite3
JWT_EXP=3600
```

Initialize database:

```
python seed.py
```

Run backend:

```
python app.py
```

Backend runs at:  
👉 http://localhost:5000

---

# 🎨 Frontend Setup

```
cd frontend
npm install
```

Create `.env`:

```
REACT_APP_API_URL=http://localhost:5000/api
```

Run frontend:

```
npm start
```

Frontend runs at:  
👉 http://localhost:3000

---

## 🚀 Future Enhancements
- Image upload for book covers  
- Search + filter functionality  
- User profile page  
- Deployment (Render + Vercel)  
- Review likes / helpful votes  

---

## 👨‍💻 Author
**Smit Patel**  
GitHub: https://github.com/Thesmitmungara


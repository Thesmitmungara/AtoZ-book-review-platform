import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import BookList from "./pages/BookList";
import BookDetail from "./pages/BookDetail";
import AdminDashboard from "./pages/AdminDashboard";
import { useContext } from "react";
import { AuthContext } from "./contexts/AuthContext";

function App(){
  const { user, logout } = useContext(AuthContext);
  return (
    <div className="container py-4">
      <nav className="d-flex justify-content-between mb-4">
        <div>
          <Link to="/">Home</Link>
        </div>
        <div>
          {user ? (
            <>
              <span className="me-2">Hello, {user.username}</span>
              <button className="btn btn-sm btn-outline-secondary me-2" onClick={logout}>Logout</button>
              {user && user.is_admin && <Link to="/admin" className="btn btn-sm btn-primary">Admin</Link>}
            </>
          ) : (
            <>
              <Link to="/login" className="me-2">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<BookList />} />
        <Route path="/books/:id" element={<BookDetail />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </div>
  );
}

export default App;

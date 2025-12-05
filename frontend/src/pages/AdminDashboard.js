import React, { useState } from "react";
import api from "../api";

export default function AdminDashboard(){
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");

  const createBook = async (e) => {
    e.preventDefault();
    try {
      await api.post('/books', { title, author });
      alert("Created");
      setTitle(""); setAuthor("");
    } catch (err) {
      alert(err.response?.data?.msg || "Failed");
    }
  };

  return (
    <div className="col-md-6">
      <h3>Admin - Create Book</h3>
      <form onSubmit={createBook}>
        <div className="mb-2"><input className="form-control" placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} /></div>
        <div className="mb-2"><input className="form-control" placeholder="Author" value={author} onChange={e=>setAuthor(e.target.value)} /></div>
        <button className="btn btn-primary">Create</button>
      </form>
    </div>
  );
}

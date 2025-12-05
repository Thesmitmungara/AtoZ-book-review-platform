import React, { useEffect, useState, useContext } from "react";
import { useParams } from "react-router-dom";
import api from "../api";
import { AuthContext } from "../contexts/AuthContext";

export default function BookDetail(){
  const { id } = useParams();
  const [book, setBook] = useState(null);
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");
  const { user } = useContext(AuthContext);

  useEffect(()=>{
    api.get(`/books/${id}`).then(res => setBook(res.data)).catch(console.error);
  },[id]);

  const submitReview = async (e) => {
    e.preventDefault();
    if(!user) return alert("Login to post review");
    try {
      await api.post(`/reviews/${id}`, { rating, comment });
      const res = await api.get(`/books/${id}`);
      setBook(res.data);
      setComment("");
    } catch(err) {
      alert(err.response?.data?.msg || "Failed");
    }
  };

  if(!book) return <div>Loading...</div>;
  return (
    <div>
      <h3>{book.title}</h3>
      <h6>{book.author}</h6>
      <p>{book.description}</p>

      <hr />
      <h5>Reviews</h5>
      {book.reviews.length === 0 && <p>No reviews yet</p>}
      {book.reviews.map(r => (
        <div key={r.id} className="border p-2 mb-2">
          <strong>{r.user.username}</strong> — {r.rating}/5
          <div>{r.comment}</div>
          <small>{new Date(r.created_at).toLocaleString()}</small>
        </div>
      ))}

      <hr />
      <h5>Add review</h5>
      <form onSubmit={submitReview}>
        <div className="mb-2">
          <label>Rating</label>
          <select className="form-control" value={rating} onChange={e=>setRating(e.target.value)}>
            {[5,4,3,2,1].map(n => <option key={n} value={n}>{n}</option>)}
          </select>
        </div>
        <div className="mb-2">
          <label>Comment</label>
          <textarea className="form-control" value={comment} onChange={e=>setComment(e.target.value)} />
        </div>
        <button className="btn btn-primary">Submit review</button>
      </form>
    </div>
  );
}

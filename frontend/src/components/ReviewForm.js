import React, { useState } from "react";

export default function ReviewForm({ onSubmit }) {
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ rating, comment });
    setComment(""); // clear after posting
  };

  return (
    <form onSubmit={handleSubmit} className="border p-3 mt-4 rounded">
      <h5>Add a Review</h5>

      <div className="mb-3">
        <label>Rating</label>
        <select
          className="form-control"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
        >
          {[5, 4, 3, 2, 1].map((n) => (
            <option key={n} value={n}>
              {n}
            </option>
          ))}
        </select>
      </div>

      <div className="mb-3">
        <label>Comment</label>
        <textarea
          className="form-control"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
        ></textarea>
      </div>

      <button className="btn btn-success">Submit Review</button>
    </form>
  );
}

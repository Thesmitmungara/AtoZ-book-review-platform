import React from "react";
import { Link } from "react-router-dom";

export default function BookCard({ book }) {
  return (
    <div className="card mb-3 shadow-sm">
      <div className="card-body">
        <h5 className="card-title">{book.title}</h5>
        <h6 className="text-muted">{book.author}</h6>
        <p className="card-text">{book.description?.slice(0, 120)}...</p>

        <Link to={`/books/${book.id}`} className="btn btn-primary btn-sm">
          View Details
        </Link>
      </div>
    </div>
  );
}

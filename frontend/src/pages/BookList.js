import React, { useEffect, useState } from "react";
import api from "../api";
import { Link } from "react-router-dom";

export default function BookList(){
  const [books,setBooks] = useState([]);
  useEffect(()=> {
    api.get('/books').then(res => setBooks(res.data.items)).catch(console.error);
  },[]);
  return (
    <div>
      <h3>Books</h3>
      <div className="row">
        {books.map(b=>(
          <div className="col-md-4" key={b.id}>
            <div className="card mb-3">
              <div className="card-body">
                <h5 className="card-title">{b.title}</h5>
                <h6 className="card-subtitle mb-2 text-muted">{b.author}</h6>
                <p>{b.description?.slice(0,120)}...</p>
                <Link to={`/books/${b.id}`} className="btn btn-sm btn-primary">Open</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

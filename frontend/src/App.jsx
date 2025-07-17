import React, { useState } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const getQuote = async () => {
    setError('');
    setQuote('');
    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/quote'); // or :8001
      const data = await response.json();

      if (response.status === 429) {
        setError(data.detail || 'Too many requests. Try again later.');
      } else {
        setQuote(data.quote);
      }
    } catch (err) {
      setError('Unable to reach the backend.');
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">🚀 Rate-Limited Quote Generator</h1>
        <p className="subtitle">You can request a maximum of 5 quotes per minute</p>

        <button className="btn" onClick={getQuote} disabled={loading}>
          {loading ? 'Loading...' : 'Get a Quote'}
        </button>

        {quote && <div className="quote-box">{quote}</div>}
        {error && <div className="error-box">{error}</div>}
      </div>
    </div>
  );
}

export default App;

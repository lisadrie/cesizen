import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Anecdotes from "./pages/Anecdotes";
import Emotions from "./pages/Emotions";
import Favoris from "./pages/Favoris";
import Respiration from "./pages/Respiration"

export default function App() {
  return (
    <Router>
      <nav style={{ padding: "1rem", background: "#eee" }}>
        <Link to="/" style={{ marginRight: "1rem" }}>Home</Link>
        <Link to="/anecdotes" style={{ marginRight: "1rem" }}>Anecdotes</Link>
        <Link to="/emotions" style={{ marginRight: "1rem" }}>Émotions</Link>
        <Link to="/favoris" style={{ marginRight: "1rem" }}>Favoris</Link>
        <Link to="/respiration" style={{ marginRight: "1rem" }}>Respiration</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/anecdotes" element={<Anecdotes />} />
        <Route path="/emotions" element={<Emotions />} />
        <Route path="/favoris" element={<Favoris />} />
        <Route path="/respiration" element={<Respiration />} />
      </Routes>
    </Router>
  );
}

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FormPage from "./components/FormPage";
import Sukses from "./components/sukses";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/FormPage" Component={<FormPage />} />
        <Route path="/sukses" Component={<Sukses />} />
      </Routes>
    </Router>
  );
};

export default App;

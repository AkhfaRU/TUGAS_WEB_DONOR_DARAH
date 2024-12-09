import React from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import InformasiLayanan from './components/InformasiLayanan';
import './home.css'; //kalau ada css

const HomePage = () => {
    const navigate = useNavigate();

    const handleRegister = () => {
        navigate('/signup');
    };

    const handleInformasiLayanan = () => {
        navigate('/informasi-layanan');
    };

    return (
        <div className="container">
            <header className="header">
                <div className="logo">
                    <h1>Palang Merah Indonesia</h1>
                    <h2>Provinsi Jawa Barat | Kota Bandung</h2>
                </div>
                <nav className="nav">
                    <a href="#home">Home</a>
                    <button className="nav-btn" onClick={handleInformasiLayanan}>
                        Informasi Layanan
                    </button>
                </nav>
            </header>
            <main className="main">
                <h1>#SIDD</h1>
                <h2>Sistem Informasi Donor Darah</h2>
                <p>Palang Merah Indonesia Kota Bandung</p>
                <button className="register-btn" onClick={handleRegister}>
                    Registrasi Donor
                </button>
            </main>
        </div>
    );
};

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/signup" element={<SignupForm />} />
                <Route path="/login" element={<LoginForm />} />
                <Route path="/informasi-layanan" element={<InformasiLayanan />} />
            </Routes>
        </Router>
    );
};

export default home;

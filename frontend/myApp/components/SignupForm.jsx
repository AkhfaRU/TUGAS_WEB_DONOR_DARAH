import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const SignupForm = () => {
    const [formData, setFormData] = useState({ username: '', email: '', password: '' });

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Signup submitted:', formData);
        // Tambahkan untuk signup ke backend di sini
    };

    return (
        <div>
            <h2>Signup</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={formData.username}
                    onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                />
                <button type="submit">Sign Up</button>
            </form>
            <p>
                Already have an account? <Link to="/login">Log in here</Link>
            </p>
        </div>
    );
};

export default SignupForm;

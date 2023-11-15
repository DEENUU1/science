'use client'

import { useState } from 'react';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword]  = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      username,
      password,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/auth/token/', {
        method: 'POST',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(
            `grand_type=&username=${data.username}&password=${data.password}&scope=&client_id=&client_secret=`
        ),
      });

      const json = await response.json();

      if (json.access_token) {
        const token = json.access_token;
        setToken(token);
        console.log("Redirect to home page ")
      } else {
        setError('Incorrect email or password.');
      }
    } catch (error) {
      setError('An error occurred while logging in.');
    }
  };

  const setToken = (token) => {
    localStorage.setItem('token', token);
  };

  return (
    <form onSubmit={handleSubmit}>
        <input
          placeholder='Email'
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type='password'
          placeholder='Password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      {/*{error && <Message error>Error: {error}</Message>}*/}
      <button type='submit'>Login</button>
    </form>
  );
};
'use client'
import { useState } from 'react';

export default function RegisterPage() {
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      first_name,
      last_name,
      email,
      password,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const json = await response.json();
      if (json.message === 'User account has been succesfully created.') {
        console.log("Redirect to login page")
      } else {
        setError('An error occurred while creating the user account.');
      }
    } catch (error) {
      setError('An error occurred while creating the user account.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
        <input
          placeholder='First Name'
          value={first_name}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <input
          placeholder='Last Name'
          value={last_name}
          onChange={(e) => setLastName(e.target.value)}
        />

      <input
        placeholder='Email'
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type='password'
        placeholder='Password'
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type='submit'>Register</button>
    </form>
  );
};

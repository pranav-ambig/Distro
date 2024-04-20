import { useState } from 'react'
import React from 'react';
import { Routes, Route } from 'react-router-dom'
import './App.css'
import './output.css';

import NavBar from './components/NavBar'
import HomePage from './components/HomePage'
import AboutPage from './components/AboutPage'
import ContactPage from './components/ContactPage'
import Health from './components/Health'

function App() {
  const [count, setCount] = useState(0)


  return (
    <div>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/health" element={<Health />} />
      </Routes>
    </div>
  )
}

export default App
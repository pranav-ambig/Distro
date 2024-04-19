import React from 'react'
import { Link } from 'react-router-dom'

const NavBar = () => {
  return (
    <div className="m-0 p-0">
      <Link className="m-0 p-0" to="/">Home</Link>
      <Link className="m-0 p-0" to="/about">About</Link>
      <Link className="m-0 p-0" to="/contact">Contact</Link>
    </div>
  )
}

export default NavBar
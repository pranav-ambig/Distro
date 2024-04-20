import React from 'react';
import { Link } from 'react-router-dom';
import img from '../assets/distro.png';

const NavBar = () => {
  return (
    <div className="top-0 w-full bg-gray-200 text-black p-4 flex items-center fixed left-0">
      <img src={img} alt="Logo" className="h-20 w-20 ml-10 mr-10 " />
      <Link to="/" className="text-lg font-bold mr-10">Home</Link>
      <Link to="/about" className="hover:text-gray-700 mr-10 font-bold">Docs</Link>
      <Link to="/contact" className="hover:text-gray-700 mr-10 font-bold">Contact</Link>
      <Link to="/health" className="hover:text-gray-700 mr-10 font-bold">Health</Link>
      {/* <Link to="/status" className="hover:text-gray-700 mr-10 font-bold">Status</Link> */}
    </div>
  );
};

export default NavBar;
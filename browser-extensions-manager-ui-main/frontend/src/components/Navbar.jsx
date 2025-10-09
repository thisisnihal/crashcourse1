import React, { useState } from 'react'
import logo from '../assets/images/logo.svg' 
import SunIcon from '../assets/images/icon-sun.svg'
import MoonIcon from '../assets/images/icon-moon.svg'
import { useStore } from '../store.js';
function Navbar() {

   const {isDarkMode, toggleTheme} = useStore();

   

    return (
        <nav className='"backdrop-blur-lg bg-gray-100/40 shadow-md w-full border-2 p-2 rounded-xl flex justify-between'>
            <span>
              <img src={logo} alt="Extensions Logo" />
            </span>

            <button className='bg-bg w-10 p-1 rounded-xl'
            onClick={toggleTheme}>
                <img src={isDarkMode ? SunIcon : MoonIcon} alt="" className=' h-full' />
            </button>
        </nav>
    )
}

export default Navbar
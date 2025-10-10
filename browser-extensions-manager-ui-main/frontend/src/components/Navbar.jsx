// import logo from "../assets/images/logo.svg";

import SunIcon from "/assets/images/icon-sun.svg";
import MoonIcon from "/assets/images/icon-moon.svg";
import { useStore } from "../store.js";
import { useEffect } from "react";
import Logo from "./Logo.jsx";
function Navbar() {
  const { isDarkMode, toggleTheme } = useStore();

  useEffect(() => {
    const theme = localStorage.getItem("theme") || "light";
    document.documentElement.classList.toggle("dark", theme === "dark");
    document.documentElement.setAttribute("data-theme", theme);
  }, []);

  return (
    <nav className='"backdrop-blur-lg bg-accent/60 shadow-md w-full p-2 rounded-xl flex justify-between'>
      <span>
        {/* could not use image cause we need to invert the text color in svg */}
        {/* <img src={logo}  alt="Extensions Logo" />  */}
        <Logo isDarkMode={isDarkMode} />
      </span>

      <button className="bg-gray-300 dark:bg-accent  w-10 p-1 rounded-xl grid place-content-center cursor-pointer" onClick={toggleTheme}>
        <img src={isDarkMode ? SunIcon : MoonIcon} alt="" className="" />
      </button>
    </nav>
  );
}

export default Navbar;

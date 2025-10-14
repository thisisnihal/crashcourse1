import { useStore } from "./store.js";
import "./App.css";
import Extension from "./components/Extension";

import Navbar from "./components/Navbar";
import { useEffect } from "react";

function App() {

  const initCardData = useStore((state) => state.initCardData);

  useEffect(() => {
    initCardData();
  }, []);

  return (
    <div className="min-w-screen w-full h-full min-h-screen p-8 md:p-16 bg-gradient">
      <Navbar />
      <Extension />
    </div>
  );
}

export default App;

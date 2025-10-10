import React, { useState, useEffect } from "react";
import ExtensionCard from "./ExtensionCard.jsx";
import cardsData from "../data.json";
// const icons = import.meta.glob("../assets/images/*.svg", { eager: true });

function Button({ text, active, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`cursor-pointer rounded-2xl backdrop-blur-lg bg-accent/60 shadow-md px-4 py-1 ${
        active ? "bg-red-500 text-bg" : "text-text"
      }`}
    >
      {text}
    </button>
  );
}

function Extension() {
 
  const [filter, setFilter] = useState("All"); // All | Active | Inactive

  

  return (
    <div className="flex flex-col w-full h-full mt-4 text-text p-1 gap-8">
     
      <div className="flex justify-between flex-wrap">
        <h1 className="text-2xl font-bold">Extensions List</h1>
        <span className="flex w-fit justify-evenly scroll-auto gap-1 md:gap-6">
          <Button text="All" active={filter === "All"} onClick={() => setFilter("All")} />
          <Button text="Active" active={filter === "Active"} onClick={() => setFilter("Active")} />
          <Button text="Inactive" active={filter === "Inactive"} onClick={() => setFilter("Inactive")} />
        </span>
      </div>

    
      <div className="flex flex-wrap gap-2.5 w-full border-0 justify-evenly">
        {cardsData.map((card, index) => ( 
          <ExtensionCard
            key={index}
            icon={card.logo}           
            title={card.name}       
            description={card.description}
            isActive={card.isActive}
  
            
          />
        ))}
      </div>
    </div>
  );
}

export default Extension;

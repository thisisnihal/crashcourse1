import React, { useState } from "react";

function Toggle({ active }) {
  const [on, setOn] = useState(active);

  return (
    <div
      onClick={() => setOn(!on)}
      className={`w-12 h-6 flex items-center rounded-full p-1 cursor-pointer transition
        ${on ? "bg-red-400" : "bg-gray-300"}`}
    >
      <div
        className={`bg-white w-4 h-4 rounded-full shadow-md transform transition
          ${on ? "translate-x-6" : ""}`}
      />
    </div>
  );
}

function ExtensionCard({ icon, title, description, isActive }) {

  return (
    <div className="flex flex-col justify-between cursor-pointer rounded-2xl backdrop-blur-lg bg-accent/60 shadow-md p-5 text-sm text-wrap w-full sm:w-[48%] lg:w-[32%] mb-6">
      <span className="flex justify-between gap-4 items-start">
        <img src={icon} alt="" className="w-12 h-12 object-contain" />
        <span className="flex flex-col">
          <h1 className="font-bold text-2xl">{title}</h1>
          <p>{description}</p>
        </span>
      </span>

      <span className="flex justify-between mt-4">
        <button  className="cursor-pointer hover:bg-red-400 hover:text-accent rounded-2xl backdrop-blur-lg bg-accent/60 border-2 pt-1 pb-1 pr-2.5 pl-2.5">
          Remove
        </button>

        <Toggle active={isActive} />
      </span>
    </div>
  );
}


export default ExtensionCard;

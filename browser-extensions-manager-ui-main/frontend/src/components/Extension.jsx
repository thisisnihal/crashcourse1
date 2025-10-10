import React from "react";
import ExtensionCard from "./ExtensionCard";
import icon from "../assets/images/logo-devlens.svg"


function Button({ text, active = false }) {

  return <button className={`cursor-pointer rounded-2xl backdrop-blur-lg bg-accent/60 shadow-md pr-4 pl-4 pt-0.5 pb-0.5  ${active ? "bg-red-500 text-bg" : "text-text"}`}>
    {text}
  </button>
}

function Extension() {
  return (
    <div className="flex flex-col w-full h-full mt-4 text-text p-1 gap-8 ">
      <div className="flex justify-between">
        <h1 className="text-2xl font-bold ">Extensions List</h1>
        <span className="flex w-fit gap-6 justify-evenly">
          <Button text={"All"} active={true} />
          <Button text={"Active"} />
          <Button text={"InActive"} />
        </span>
      </div>

      <div>
        <ExtensionCard icon={icon} title={"DevLens"} description={"Quickly inspect page layouts and visualize element boundaries."} active={true} />
      </div>
    </div>
  );
}

export default Extension;

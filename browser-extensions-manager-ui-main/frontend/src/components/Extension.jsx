import React, { useState } from "react";
import ExtensionCard from "./ExtensionCard.jsx";
import { useStore } from "../store.js";

// acts like an enum
export const FilterType = Object.freeze({
  ALL: "All",
  ACTIVE: "Active",
  INACTIVE: "Inactive",
});

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
  const [filter, setFilter] = useState(FilterType.ALL);

  const { cardsData } = useStore();

  const filteredCards = cardsData.filter((card) => {
    if (filter === FilterType.ALL) return true;
    if (filter === FilterType.ACTIVE) return card.isActive;
    if (filter === FilterType.INACTIVE) return !card.isActive;
    return true;
  });

  return (
    <div className="flex flex-col w-full h-full mt-4 text-text p-1 gap-8">
      <div className="flex justify-between flex-wrap">
        <h1 className="text-2xl font-bold">Extensions List</h1>
        <span className="flex w-fit justify-evenly scroll-auto gap-1 md:gap-6">
          <Button
            text={FilterType.ALL}
            active={filter === FilterType.ALL}
            onClick={() => setFilter(FilterType.ALL)}
          />
          <Button
            text={FilterType.ACTIVE}
            active={filter === FilterType.ACTIVE}
            onClick={() => setFilter(FilterType.ACTIVE)}
          />
          <Button
            text={FilterType.INACTIVE}
            active={filter === FilterType.INACTIVE}
            onClick={() => setFilter(FilterType.INACTIVE)}
          />
        </span>
      </div>

      <div className="flex flex-wrap gap-2.5 w-full border-0 justify-evenly">
        {filteredCards.map((card) => (
          <ExtensionCard
            key={card.id}
            id={card.id}
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

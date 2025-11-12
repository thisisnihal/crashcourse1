import { useRef, useState } from "react";
import Draggable from "react-draggable";

const Card = ({ title, content, id, sourceList, onDrop }) => {
  const nodeRef = useRef(null);
  const [activeDrags, setActiveDrags] = useState(0);
  const [deltaPosition, setDeltaPosition] = useState({ x: 0, y: 0 });
  const [controlledPosition, setControlledPosition] = useState({ x: 0, y: 0 });

  const onStart = () => {
    setActiveDrags(prev => prev + 1);
  };

  const onStop = (e, ui) => {
    const targetElement = document.elementFromPoint(e.clientX, e.clientY);
    const targetList = targetElement?.closest('.list')?.dataset.listId;
    
    if (targetList && targetList !== sourceList) {
      onDrop(id, sourceList);
      // Only reset position after successful drop
      setControlledPosition({ x: 0, y: 0 });
    } else {
      // Return to original position if not dropped on a valid target
      setControlledPosition({ x: 0, y: 0 });
    }
    setActiveDrags(prev => prev - 1);
  };

  const onDrag = (e, ui) => {
    const { x, y } = ui;
    setDeltaPosition({ x, y });
  };

  const onDropAreaMouseEnter = (e) => {
    if (activeDrags) {
      e.target.classList.add('hovered');
    }
  };

  const onDropAreaMouseLeave = (e) => {
    e.target.classList.remove('hovered');
  };

  const adjustXPos = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setControlledPosition(pos => ({ x: pos.x - 10, y: pos.y }));
  };

  const adjustYPos = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setControlledPosition(pos => ({ x: pos.x, y: pos.y - 10 }));
  };

  // Remove unused controlled position handlers

  return (
    <Draggable 
      nodeRef={nodeRef} 
      position={controlledPosition} 
      onStart={onStart}
      onStop={onStop}
      onDrag={onDrag}
      bounds=".list"
    >
      <div 
        ref={nodeRef} 
        className="flex flex-col cursor-pointer rounded-xl backdrop-blur-lg bg-teal-200/20 shadow-md p-2 text-wrap w-[90%] h-24 mx-auto"
      >
        <div className="header self-center justify-center">{title}</div>
        <hr />
        <div className="content w-full">{content}</div>
      </div>
    </Draggable>
  )
}

export default Card;
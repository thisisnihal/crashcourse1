import { useState } from 'react';
import Column from './Column';

const Board = () => {
  

    return (
        <div className="flex gap-4 w-full h-full p-4">
            <Column
                title="All Tasks"
                tasks={tasks.todo}
                listId="todo"
                onTaskMove={moveTask}
            />
            <Column
                title="Doing Tasks"
                tasks={tasks.doing}
                listId="doing"
                onTaskMove={moveTask}
            />
        </div>
    );
};

export default Board;
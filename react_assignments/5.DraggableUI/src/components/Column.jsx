import Card from './Card.jsx';

const Column = ({ title, tasks, listId, onTaskMove }) => {



    return (
        <div 
            className="list w-1/3 border-2 gap-1 border-teal-200 p-2 min-h-[300px] flex flex-col items-center rounded-xl relative hover:bg-teal-50/10 transition-colors"
            data-list-id={listId}
        >
                <h1 className='text-2xl font-bold text-center underline mb-4'>{title}</h1>
             {tasks.map((task) => {
                {task}
             })}
        </div>
    )
}

export default Column;
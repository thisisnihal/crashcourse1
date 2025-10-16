import React, { useState } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([
    { id: 1, title: 'Learn React', status: 'todo' },
    { id: 2, title: 'Build webpage', status: 'done' },
  ]);
  const [newTaskTitle, setNewTaskTitle] = useState('');

  const handleAddTask = () => {
    if (!newTaskTitle.trim()) return;
    const newTask = {
      id: Date.now(),
      title: newTaskTitle.trim(),
      status: 'todo',
    };
    setTasks([...tasks, newTask]);
    setNewTaskTitle('');
  };

  const handleDragStart = (event, taskId) => {
    event.dataTransfer.setData('text/plain', taskId);
  };

  const handleDrop = (event, newStatus) => {
    event.preventDefault();
    const taskId = event.dataTransfer.getData('text/plain');
    setTasks(prev =>
      prev.map(task =>
        task.id === Number(taskId) ? { ...task, status: newStatus } : task
      )
    );
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const renderColumn = (status) => (
    <div
      className="column"
      onDrop={(e) => handleDrop(e, status)}
      onDragOver={handleDragOver}
    >
      <h2>{status === 'todo' ? 'To Do' : 'Done'}</h2>
      {tasks
        .filter(task => task.status === status)
        .map(task => (
          <div
            key={task.id}
            className="card"
            draggable
            onDragStart={(e) => handleDragStart(e, task.id)}
          >
            {task.title}
          </div>
        ))}
    </div>
  );

  return (
    <div className="app">
      <div className="add-task">
        <input
          type="text"
          value={newTaskTitle}
          onChange={(e) => setNewTaskTitle(e.target.value)}
          placeholder="New task..."
        />
        <button onClick={handleAddTask}>Add</button>
      </div>

      <div className="board">
        {renderColumn('todo')}
        {renderColumn('done')}
      </div>
    </div>
  );
}

export default App;

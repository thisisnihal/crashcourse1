import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import Navbar from './components/Navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
   <div className='w-screen h-screen pt-8 pr-6 pl-6 bg-bg'>
    <Navbar />
   </div>
  )
}

export default App

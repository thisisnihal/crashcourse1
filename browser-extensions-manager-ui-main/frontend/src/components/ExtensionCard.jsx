import React from 'react'

function ExtensionCard({icon, title, description, active}) {
  return (
    <div className='w-1/3 h-48 flex flex-col justify-between cursor-pointer rounded-2xl backdrop-blur-lg bg-accent/60 shadow-md p-5 text-sm text-wrap'>
        <span className='flex justify-between gap-4 item-baseline'>
            <img src={icon} alt="" />
            <span className='flex flex-col '>
                <h1 className='font-bold text-2xl'>{title}</h1>
                <p>{description}</p>
            </span>
        </span>
          
        <span className='flex justify-between'>
    <button className='cursor-pointer hover:bg-red-400 hover:text-accent  rounded-2xl backdrop-blur-lg bg-accent/60 border-2 pt-1 pb-1 pr-2.5 pl-2.5'>
      Remove
    </button>

    
        </span>
    </div>
  )
}

export default ExtensionCard
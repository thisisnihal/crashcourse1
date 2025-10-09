import React from 'react'

function ExtensionCard({icon, title, description, active}) {
  return (
    <div className='w-1/3 h-40 flex flex-col justify-between cursor-pointer rounded-2xl backdrop-blur-lg bg-accent/60 shadow-md pr-1 pl-2.5 pt-0.5 pb-0.5 text-sm text-wrap'>
        <span className='flex justify-between gap-2 item-baseline'>
            <img src={icon} alt="" />
            <span className='flex flex-col '>
                <h1 className='font-bold text-2xl'>{title}</h1>
                <p>{description}</p>
            </span>
        </span>
        <span>

        </span>
    </div>
  )
}

export default ExtensionCard
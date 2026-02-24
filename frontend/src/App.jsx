import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className = "headings">ResuMatch</h1>
      <h2 className="sub-headings"><i>Your AI-Powered job applier</i></h2>
      <button className="get-started">Get Started</button>
    </>
  )
}

export default App

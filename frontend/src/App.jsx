import { useEffect, useState } from "react";
import api from "./api";

const App = () => {

  const [data, setdata] = useState('')

   useEffect(() => {
    api.get("/").then((res) => {
      setdata(res.data);
    })
  })

  return (
    <div>
      <h1>Welcome to FastAPI with React!</h1>
      <p>{data}</p>
    </div>
  )
}

export default App

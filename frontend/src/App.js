import React, { useState, useEffect } from "react";
import Login from "./Login";
import MovieGallery from "./MovieGallery";

function App() {
  const [token, setToken] = useState(() => localStorage.getItem("token"));

  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);
      console.log("Token actual:", token);
    } else {
      localStorage.removeItem("token");
      console.log("Token actual:", token);
    }
  }, [token]);

  return (
    <div className="App">
      {!token ? <Login setToken={setToken} /> : <MovieGallery token={token} />}
      
    </div>
  );
  
}


export default App;

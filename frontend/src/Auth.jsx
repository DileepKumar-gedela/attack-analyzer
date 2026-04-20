import { useState } from "react";
import axios from "axios";

function Auth({ setToken }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const register = async () => {
    await axios.post(
      "http://127.0.0.1:8000/register",
      null,
      { params:{ username, password } }
    );
    alert("User registered");
  };

  const login = async () => {
    const res = await axios.post(
      "http://127.0.0.1:8000/login",
      null,
      { params:{ username, password } }
    );
    setToken(res.data.access_token);
  };

  return (
    <div className="section">
      <h2>Login / Register</h2>

      <input
        placeholder="Username"
        onChange={e=>setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        onChange={e=>setPassword(e.target.value)}
      />

      <br/><br/>

      <button onClick={login}>Login</button>
      <button onClick={register}>Register</button>
    </div>
  );
}

export default Auth;

import { useRef, useState } from "react";
import "./First.css";
import { useNavigate } from "react-router-dom";

function First() {
  const fileRef = useRef();
  const [name, setName] = useState("");
  const [time, setTime] = useState("");
  const [ate, setAte] = useState("");
  const [insight,setInsight]=useState("")
  const navigate=useNavigate()

  const handleClick = () => {
    fileRef.current.click();
  };

  const handleClickDashboard=()=>{
    navigate("/dashboard")
    
  }

  const handleFileChange = () => {
    alert("Image uploaded successfully");
  };

  const handleSubmit = async () => {
    const payload = { name, time, ate };
    await fetch("http://127.0.0.1:8000/data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  };

  return (
    <>
      {/* NAVBAR */}
      <div className="navbar">
        <div className="logo">Nutrition AI</div>
        <div className="nav-links">
          <span>Services</span>
          <span>Contact</span>
          <span>About</span>
        </div>
      </div>

      {/* PAGE CONTENT */}
      <div className="page">
        <div className="center-box">

          {/* INPUTS */}
          <div className="form">
            <input
              className="input"
              placeholder="Your Name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />

            <input
              className="input"
              placeholder="Meal Time (Breakfast / Lunch / Dinner)"
              value={time}
              onChange={(e) => setTime(e.target.value)}
            />

            <input
              className="input"
              placeholder="Food Name"
              value={ate}
              onChange={(e) => setAte(e.target.value)}
            />
          </div>

          {/* FILE UPLOAD */}
          <input
            type="file"
            ref={fileRef}
            accept="image/*"
            style={{ display: "none" }}
            onChange={handleFileChange}
          />

          <button className="action-btn" onClick={handleClick}>
            Upload Food Image
          </button>

          {/* SUBMIT */}
          <button className="action-btn primary" onClick={handleSubmit}>
            Submit Meal
          </button>

          <button onClick={handleClickDashboard}>
            Dashboard
          </button>
          <div className="llm-output-wrapper">
            <div className="llm-output-box">
                <span>AI Insight</span>
                output
            </div>
            </div>

        </div>
      </div>
    </>
  );
}

export default First;

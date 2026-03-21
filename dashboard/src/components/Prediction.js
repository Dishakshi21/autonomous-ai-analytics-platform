import { useState } from "react";
import axios from "axios";

function Prediction() {

  const [prediction, setPrediction] = useState(null);

  const predict = async () => {

    const data = {
      Age: 30,
      Experience: 5,
      PerformanceScore: 4,
      Department_Finance: 0,
      Department_HR: 1,
      Department_IT: 0,
      Department_Management: 0,
      Department_Marketing: 0
    };

    const res = await axios.post(
      "http://127.0.0.1:8000/predict",
      data
    );

    setPrediction(res.data.prediction);

  };

  return (

    <div>

      <h2>Prediction</h2>

      <button onClick={predict}>
        Predict Salary
      </button>

      {prediction && <h3>Prediction: {prediction}</h3>}

    </div>

  );

}

export default Prediction;
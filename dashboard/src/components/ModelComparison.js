import { useEffect, useState } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

function ModelComparison() {

  const [data, setData] = useState([]);

  useEffect(() => {

    axios.get("http://127.0.0.1:8000/model-comparison")
      .then(res => {

        const chartData = Object.entries(res.data.model_comparison)
          .map(([model, score]) => ({
            model,
            score
          }));

        setData(chartData);

      });

  }, []);

  return (

    <div>

      <h2>Model Comparison</h2>

      <BarChart width={600} height={300} data={data}>

        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="model" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="score" fill="#8884d8" />

      </BarChart>

    </div>

  );

}

export default ModelComparison;
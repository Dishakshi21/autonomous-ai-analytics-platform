import { useEffect, useState } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

function FeatureImportance() {

  const [data, setData] = useState([]);

  useEffect(() => {

    axios.get("http://127.0.0.1:8000/feature-importance")
      .then(res => {

        const chartData = Object.entries(res.data.feature_importance)
          .map(([feature, importance]) => ({
            feature,
            importance
          }));

        setData(chartData);

      });

  }, []);

  return (

    <div>

      <h2>Feature Importance</h2>

      <BarChart width={700} height={300} data={data}>

        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="feature" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="importance" fill="#82ca9d" />

      </BarChart>

    </div>

  );

}

export default FeatureImportance;
import UploadDataset from "./components/UploadDataset";
import ModelComparison from "./components/ModelComparison";
import FeatureImportance from "./components/FeatureImportance";
import Prediction from "./components/Prediction";

function App() {

  return (
    <div style={{ padding: "40px" }}>

      <h1>Autonomous AI Analytics Platform</h1>

      <UploadDataset />

      <ModelComparison />

      <FeatureImportance />

      <Prediction />

    </div>
  );

}

export default App;
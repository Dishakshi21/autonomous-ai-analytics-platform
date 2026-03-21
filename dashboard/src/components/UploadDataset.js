import axios from "axios";

function UploadDataset() {

  const uploadFile = async (event) => {

    const file = event.target.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/upload",
      formData
    );

    alert("Dataset Uploaded Successfully");
    console.log(res.data);
  };

  return (

    <div>

      <h2>Upload Dataset</h2>

      <input type="file" onChange={uploadFile} />

    </div>

  );

}

export default UploadDataset;
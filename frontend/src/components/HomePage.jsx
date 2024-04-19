import React, { useState } from 'react';
import axios from 'axios';

function HomePage() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://172.16.129.26:5000/upload-zip', formData);
      console.log('File uploaded successfully');
    } catch (error) {
      console.error('File upload failed', error);
    }
  };

  const handleDownload = () => {
    // Create a temporary anchor element
    const link = document.createElement('a');
    link.href = 'https://drive.google.com/uc?export=download&id=1P9-Qz0AZRgOXWGIbrXjEZWte-yC_jsEt'; // Replace 'path/to/splitter.exe' with the actual path
    link.download = 'splitter.exe';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link); // Clean up
  };

  return (
    <div className="flex flex-col justify-center items-center h-screen mb-500">
      <h1 className="text-6xl font-bold mb-10">DISTRO</h1>
      <input type="file" accept=".zip" className="mt-4" onChange={handleFileChange} />
      <button onClick={handleFileUpload} className="mt-4 p-2 bg-blue-500 text-white">Send</button>
      <button onClick={handleDownload} className="mt-4 p-2 bg-green-500 text-white">Download splitter.exe</button>
    </div>
  );
}

export default HomePage;

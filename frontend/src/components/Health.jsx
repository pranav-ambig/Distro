import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Health() {
  const [numWorkers, setNumWorkers] = useState(null);

  useEffect(() => {
    const getNumWorkers = async () => {
      try {
        const response = await axios.get('http://172.16.129.26:5000/getnumworkers');
        setNumWorkers(response.data);
      } catch (error) {
        console.error('Failed to fetch number of workers', error);
      }
    };

    getNumWorkers();
  }, []);

  return (
    <div className="text-5xl font-bold mt-100">
      <p>Number of workers: {numWorkers}</p>
    </div>
  );
}

export default Health;
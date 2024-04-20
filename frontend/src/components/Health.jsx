import React, { useState, useEffect } from 'react';
import axios from 'axios';



// LineChart.js
import  {   useRef } from 'react';
import Chart from 'chart.js/auto';

const LineChart = () => {
  const chartRef = useRef(null);
  
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://172.16.129.26:5000/getaccuracyarray');
        setData(response.data);
      } catch (error) {
        console.error('Failed to fetch data', error);
      }
    };

    fetchData();
  }, []);

    useEffect(() => {
        const ctx = chartRef.current.getContext('2d');

        // Data for the line chart
        const data = {
            labels: ['.', '.', '.', '.', '.', '.', '.'],
            datasets: [{
                label: 'Accuracy score',
                data: [65, 59, 80, 81, 56, 55, 40],
                fill: false,
                borderColor: 'rgba(75, 192, 192, 1)',
                tension: 0.1
            }]
        };

        // Configuration for the chart
        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: false,
                        text: 'Line Chart Example'
                    }
                }
            }
        };

        // Initialize the chart
        const chart = new Chart(ctx, config);

        return () => {
            // Clean up: Destroy the chart instance when component unmounts
            chart.destroy();
        };
    }, []);

    return (
        <div
            style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                width: '100%',
                height: '300px'
            }}
        >
            <canvas ref={chartRef}></canvas>
        </div>
    );
};

function Health() {
  const [numWorkers, setNumWorkers] = useState(null);

  useEffect(() => {
    const getNumWorkers = async () => {
      try {
        const response = await axios.get('http://10.20.200.150:5000/getnumworkers');
        setNumWorkers(response.data);
      } catch (error) {
        console.error('Failed to fetch number of workers', error);
      }
    };

    getNumWorkers();
  }, []);

  return (
    <div className="text-5xl font-bold mt-10">
      <br />
      <br />
      <br />
      <br />
      <br />


      <p className='p-'>Number of Available workers: {numWorkers}</p>
      <p className='p-'>Accuracy of model :</p>

      <LineChart></LineChart>
    </div>
  );
}

export default Health;
// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import { Line } from 'react-chartjs-2';

// function Status() {
//   const [data, setData] = useState({ labels: [], datasets: [{ label: 'Accuracy', data: [], fill: false, borderColor: 'rgb(75, 192, 192)', tension: 0.1 }] });

//   useEffect(() => {
//     const getStatus = async () => {
//       try {
//         const response = await axios.get('http://172.16.129.26:5000/status');
//         console.log(`Accuracy: ${response.data.Accuracy}, Loss: ${response.data.Loss}`);
//         setData(prevData => ({
//           labels: [...prevData.labels, new Date().toLocaleTimeString()],
//           datasets: [
//             {
//               ...prevData.datasets[0],
//               data: [...prevData.datasets[0].data, response.data.accuracy],
//             },
//           ],
//         }));
//       } catch (error) {
//         console.error('Failed to fetch status', error);
//       }
//     };

//     // Call getStatus every 5 seconds
//     const intervalId = setInterval(getStatus, 5000);

//     // Clear interval on component unmount
//     return () => clearInterval(intervalId);
//   }, []);

//   return (
//     <div>
//       <Line data={data} />
//     </div>
//   );
// }

// export default Status;
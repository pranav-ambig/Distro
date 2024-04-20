import React from 'react'

function AboutPage() {
  return (
    <div>

      <div>
      <h2 className="flex flex-col justify-center items-center h-screen text-center mb-0">master.zip structure</h2>
        <pre className="text-lg font-mono mt-0">
          {`
master.zip
|
|--- model.py
|--- chunks1.csv
|--- chunks2.csv
|    .
|    .
|--- chunksn.csv
|--- requirements.txt
        `}
        </pre>
      </div>

      <div className="flex flex-col justify-center items-center h-screen text-center">
        <h2 className="text-lg">model.py</h2>
        <p className="text-lg font-mono">Python script that contains the model definition and training code</p>
      </div>

      <div className="flex flex-col justify-center items-center h-screen text-center">
        <h2 className="text-lg">chunks*.csv</h2>
        <p className="text-lg font-mono">CSV files containing the data split into chunks</p>
      </div>
    </div>
  )
}

export default AboutPage
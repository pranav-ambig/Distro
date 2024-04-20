import React from 'react'

function AboutPage() {
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <h1 className="text-6xl font-bold">
        Documentation
      </h1>
      <div className="flex flex-col justify-center items-center h-screen">
        <h1>master.zip structure</h1>
        <pre className="text-lg font-mono mt-10">
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

      <div>
        <h1>model.py</h1>
        <p>Python script that contains the model definition and training code</p>
      </div>

      <div>
        <h1>chunks*.csv</h1>
        <p>CSV files containing the data split into chunks</p>
      </div>
    </div>
  )
}

export default AboutPage
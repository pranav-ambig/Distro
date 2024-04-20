import React from 'react'

function AboutPage() {
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <h1 className="text-6xl font-bold">
        Documentation
      </h1>
      <div className="flex flex-row justify-center items-center h-screen">
        <div className="flex flex-col justify-center items-center">
          <h1>master.zip structure</h1>
          <pre className="text-lg font-mono mt-10">
            {`
master.zip
|
|--- model.py
|--- requirements.txt
|--- data/ 
     |--- chunks1.csv
     |--- chunks2.csv
     |    .
     |    .
     |--- chunks*.csv
            `}
          </pre>
        </div>

        <div className="flex flex-col justify-center items-center mx-10">
          <h1>model.py</h1>
          <p>Python script that contains the model definition and training code</p>
        </div>

        <div className="flex flex-col justify-center items-center">
          <h1>chunks*.csv</h1>
          <p>CSV files containing the data split into chunks</p>
        </div>
      </div>
    </div>
  )
}

export default AboutPage
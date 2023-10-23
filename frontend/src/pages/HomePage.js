import React, { useState, useContext } from 'react';
import AuthContext from '../context/AuthContext';
import axios from 'axios';

const HomePage = () => {
  const [businessData, setBusinessData] = useState([]);
  const { authTokens, logoutUser } = useContext(AuthContext);
  const [error, setError] = useState(null); // Define an error state

  const fetchBusinessData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/business/', {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + String(authTokens.access),
        },
      });

      if (response.status === 200) {
        const data = await response.json();
        setBusinessData(data);
        setError(null); // Clear any previous error
      } else if (response.status === 401) {
        logoutUser();
      } else if (response.status === 403) {
        setError("403 Forbidden: Too many requests. Please try again");
        setBusinessData([]); // Clear business data
      } else if (response.status === 429) {
        setError("Too many requests");
        setBusinessData([]); // Clear business data
      } else {
        setError("An error occurred while fetching data.");
        setBusinessData([]); // Clear business data
      }
    } catch (error) {
      console.error(error);
      setError("An error occurred while fetching data.");
      setBusinessData([]); // Clear business data
    }
  };

  return (
    <div>
      <h1>Welcome to the Home Page!</h1>

      <button onClick={fetchBusinessData}>View Data</button>

      {error && <p className="error">{error}</p>}

      {businessData.length > 0 && (
        <>
          <h2>Business Data:</h2>
          <table className="table">
            {/* Table headers */}
            <thead>
              <tr>
                <th>Quarter</th>
                <th>Ser Ref</th>
                <th>Industry Code</th>
                <th>Industry Name</th>
                <th>Filled Jobs</th>
                <th>Filled Jobs Revised</th>
                <th>Filled Jobs Diff</th>
                <th>Filled Jobs Percent Diff</th>
                <th>Total Earnings</th>
                <th>Total Earnings Revised</th>
                <th>Earnings Diff</th>
                <th>Earnings Percent Diff</th>
              </tr>
            </thead>
            {/* Table body */}
            <tbody>
              {businessData.map((dataItem, index) => (
                <tr key={index}>
                  <td>{dataItem.quarter}</td>
                  <td>{dataItem.ser_ref}</td>
                  <td>{dataItem.industry_code}</td>
                  <td>{dataItem.industry_name}</td>
                  <td>{dataItem.filledjobs}</td>
                  <td>{dataItem.filledjobsrevised}</td>
                  <td>{dataItem.filledjobsdiff}</td>
                  <td>{dataItem.filledjobs_diff}</td>
                  <td>{dataItem.total_earnings}</td>
                  <td>{dataItem.totalearningsrevised}</td>
                  <td>{dataItem.earningsdiff}</td>
                  <td>{dataItem.earnings_diff}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
};

export default HomePage;
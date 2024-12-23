import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [category, setCategory] = useState("");
  const [results, setResults] = useState([]);

  const searchProducts = async () => {
    const response = await axios.get("http://localhost:8000/search", {
      params: { category, min_profit: 10 },
    });
    setResults(response.data.results);
  };

  return (
    <div style={{ backgroundColor: "#0d1117", color: "#fff", fontFamily: "Poppins" }}>
      <h1>Prime Arbitrage</h1>
      <input
        type="text"
        placeholder="Enter category"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        style={{ padding: "10px", marginBottom: "10px" }}
      />
      <button onClick={searchProducts} style={{ padding: "10px 20px" }}>
        Search
      </button>
      <div>
        {results.map((product, index) => (
          <div key={index} style={{ margin: "10px 0", padding: "10px", backgroundColor: "#161b22" }}>
            <h2>{product.name}</h2>
            <p>Price: ${product.price}</p>
            <p>Market Price: ${product.market_price}</p>
            <p>Profit: ${product.profit}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;

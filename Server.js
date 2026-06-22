const express = require("express");
const axios = require("axios");
const app = express();

app.use(express.static("public"));

const PAIRS = {
  EURUSD: "EURUSD=X",
  GBPUSD: "GBPUSD=X",
  USDJPY: "JPY=X",
  BTCUSD: "BTC-USD",
  ETHUSD: "ETH-USD"
};

app.get("/api/data", async (req, res) => {
  let results = [];

  for (let name in PAIRS) {
    try {
      const symbol = PAIRS[name];

      const url = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?interval=5m&range=1d`;
      const r = await axios.get(url);

      const price = r.data.chart.result[0].meta.regularMarketPrice;

      results.push({
        name,
        price
      });

    } catch (e) {
      results.push({ name, price: "error" });
    }
  }

  res.json(results);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log("Server running"));

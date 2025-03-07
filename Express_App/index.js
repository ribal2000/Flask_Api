const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post("/analyze-sentiment", async (req, res) => {
    const { text } = req.body;
    if (!text) return res.status(400).json({ error: "Text input is required" });

    try {
        const response = await axios.post("http://flask-app:5000/predict", { text });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});

app.listen(PORT, () => console.log(`Server running at http://127.0.0.1:${PORT}`));

// app/static/js/app.js

// Function to handle the form submission
document.getElementById("analyze-form").onsubmit = async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get the text entered in the form
    const formData = new FormData(event.target);
    const text = formData.get("text");

    // Send a POST request to the Flask server's /analyze endpoint
    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({ text }), // Send the text data
    });

    // Parse the JSON response from the server
    const result = await response.json();

    // Display the result on the page
    if (result.error) {
        document.getElementById("result").innerText = `Error: ${result.error}`;
    } else {
        const predictionText = `Prediction: ${result.prediction} (Confidence: ${(result.probability * 100).toFixed(2)}%)`;
        document.getElementById("result").innerText = predictionText;
    }
};

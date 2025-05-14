document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let userMessage = document.getElementById("user-input").value;
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML += "<p><strong>Bot:</strong> " + data.response + "</p>";
        document.getElementById("user-input").value = "";
    });
}

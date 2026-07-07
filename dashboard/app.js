async function loadStatus() {
    const response = await fetch("http://localhost:8000/health");
    const data = await response.json();

    document.getElementById("status").innerHTML =
        "System Status: " + data.status;
}

loadStatus();

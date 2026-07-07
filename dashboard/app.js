fetch("http://localhost:8000/health")
.then(response => response.json())
.then(data => {
    document.getElementById("status").innerHTML = `
    <h1>🧠 AEON MATRIX LEVEL 3</h1>
    <h2>🟢 ${data.status.toUpperCase()}</h2>
    <p>Mother Brain: READY</p>
    <p>Runtime: ACTIVE</p>
    `;
})
.catch(error => {
    document.getElementById("status").innerHTML = `
    <h2>🔴 API OFFLINE</h2>
    `;
});

async function loadDashboard() {

    try {

        const health = await fetch("http://localhost:8000/health")
            .then(r => r.json());

        const brain = await fetch("http://localhost:8000/brain/status")
            .then(r => r.json());

        const events = await fetch("http://localhost:8000/events")
            .then(r => r.json());


        document.getElementById("system").innerHTML =
            "🟢 " + health.status.toUpperCase();


        document.getElementById("brain").innerHTML =
            "🧠 " + brain.brain + " : " + brain.status;


        document.getElementById("runtime").innerHTML =
            "⚡ " + brain.mode;


        document.getElementById("events").innerHTML =
            "📡 " + events.length + " EVENTS";


    } catch(error) {

        document.getElementById("system").innerHTML =
            "🔴 API OFFLINE";

    }

}


loadDashboard();

async function loadEvents(){

    try {

        const events = await fetch(
            "http://localhost:8000/events"
        ).then(r => r.json());


        document.getElementById("event-list").innerHTML =
        events.length
        ? JSON.stringify(events, null, 2)
        : "No events";


    } catch(e){

        document.getElementById("event-list").innerHTML =
        "Event API Offline";

    }

}


loadEvents();


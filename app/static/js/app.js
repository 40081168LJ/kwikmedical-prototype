// app/static/js/app.js
document.getElementById("emergencyForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const patientId = document.getElementById("patientId").value;
    const condition = document.getElementById("condition").value;
    const location = document.getElementById("location").value;

    const emergencyData = {
        patient_id: parseInt(patientId),
        condition: condition,
        location: location
    };

    fetch("/emergency-call", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(emergencyData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            displayPatientInfo(data.dispatch_details);
        }
    })
    .catch(error => console.error("Error:", error));
});

function displayPatientInfo(dispatchDetails) {
    document.getElementById("patientInfo").innerHTML = `
        <h3>Patient Information</h3>
        <p>Name: ${dispatchDetails.name}</p>
        <p>Condition: ${dispatchDetails.condition}</p>
        <p>Location: ${dispatchDetails.location}</p>
    `;

    document.getElementById("dispatchInfo").innerHTML = `
        <h3>Dispatch Status</h3>
        <p>Status: ${dispatchDetails.status}</p>
        <p>Message: ${dispatchDetails.message}</p>
    `;
}

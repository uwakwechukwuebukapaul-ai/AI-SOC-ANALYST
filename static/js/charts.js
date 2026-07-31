new Chart(document.getElementById("severityChart"), {
    type: "bar",
    data: {
        labels: severityLabels,
        datasets: [{
            label: "Cases",
            data: severityValues
        }]
    }
});

new Chart(document.getElementById("threatChart"), {
    type: "pie",
    data: {
        labels: threatLabels,
        datasets: [{
            data: threatValues
        }]
    }
});

new Chart(document.getElementById("timelineChart"), {
    type: "line",
    data: {
        labels: timelineLabels,
        datasets: [{
            label: "Incidents",
            data: timelineValues
        }]
    }
});
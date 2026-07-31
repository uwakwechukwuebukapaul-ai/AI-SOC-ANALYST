document.addEventListener("DOMContentLoaded", () => {

    // -------------------------
    // Severity Chart
    // -------------------------

    const severityCanvas = document.getElementById("severityChart");

    if (severityCanvas) {

        new Chart(severityCanvas, {

            type: "doughnut",

            data: {

                labels: severityLabels,

                datasets: [{

                    label: "Severity",

                    data: severityValues,

                    backgroundColor: [

                        "#dc3545",
                        "#ffc107",
                        "#198754",
                        "#0d6efd"

                    ],

                    borderWidth: 2

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        });

    }

    // -------------------------
    // Threat Chart
    // -------------------------

    const threatCanvas = document.getElementById("threatChart");

    if (threatCanvas) {

        new Chart(threatCanvas, {

            type: "bar",

            data: {

                labels: threatLabels,

                datasets: [{

                    label: "Threat Count",

                    data: threatValues,

                    backgroundColor: "#0d6efd"

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        });

    }

    // -------------------------
    // Timeline Chart
    // -------------------------

    const timelineCanvas = document.getElementById("timelineChart");

    if (timelineCanvas) {

        new Chart(timelineCanvas, {

            type: "line",

            data: {

                labels: timelineLabels,

                datasets: [{

                    label: "Incidents",

                    data: timelineValues,

                    borderColor: "#dc3545",

                    backgroundColor: "rgba(220,53,69,.2)",

                    fill: true,

                    tension: 0.3

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        });

    }

});
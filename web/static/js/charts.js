/*
Sentinel DNA
SOC Dashboard Charts
*/


// Severity Doughnut Chart

const severityCtx = document.getElementById(
    "severityChart"
);


if (severityCtx) {

    new Chart(severityCtx, {

        type: "doughnut",

        data: {

            labels: severityLabels,

            datasets: [

                {

                    data: severityValues

                }

            ]

        }

    });

}




// Threat Distribution Chart

const threatCtx = document.getElementById(
    "threatChart"
);


if (threatCtx) {

    new Chart(threatCtx, {

        type: "bar",

        data: {

            labels: threatLabels,

            datasets: [

                {

                    label:
                    "Threats",

                    data:
                    threatValues

                }

            ]

        }

    });

}





// Incident Timeline Chart

const timelineCtx = document.getElementById(
    "timelineChart"
);


if (timelineCtx) {

    new Chart(timelineCtx, {

        type: "line",

        data: {

            labels:
            timelineLabels,


            datasets: [

                {

                    label:
                    "Incidents",

                    data:
                    timelineValues

                }

            ]

        }

    });

}
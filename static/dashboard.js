let severityChart = null;
let attackChart = null;



async function updateSOCDashboard(){


    try{


        const response = await fetch("/api/dashboard");


        const data = await response.json();



        document.getElementById("total_incidents").innerText =
            data.total;



        document.getElementById("high_incidents").innerText =
            data.high;



        document.getElementById("open_incidents").innerText =
            data.open;



        document.getElementById("average_risk").innerText =
            data.average_risk;



        document.getElementById("last_update").innerText =
            new Date().toLocaleTimeString();



        drawSeverityChart(
            data.severity_data
        );



        drawAttackChart(
            data.attack_types
        );



    }

    catch(error){

        console.error(
            "Dashboard update error:",
            error
        );

    }


}







function drawSeverityChart(data){



    const canvas =
        document.getElementById(
            "severityChart"
        );



    if(!canvas){

        console.log(
            "Severity chart canvas missing"
        );

        return;

    }



    const ctx =
        canvas.getContext("2d");



    if(severityChart){

        severityChart.destroy();

    }




    severityChart = new Chart(ctx,{


        type:"doughnut",



        data:{


            labels:Object.keys(data),



            datasets:[{

                label:"Severity",


                data:Object.values(data)

            }]


        },



        options:{


            responsive:true,


            maintainAspectRatio:false,


            plugins:{


                legend:{


                    position:"bottom"


                }


            }


        }


    });


}









function drawAttackChart(data){



    const canvas =
        document.getElementById(
            "attackChart"
        );



    if(!canvas){


        console.log(
            "Attack chart canvas missing"
        );


        return;


    }




    const ctx =
        canvas.getContext("2d");





    if(attackChart){


        attackChart.destroy();


    }






    attackChart = new Chart(ctx,{



        type:"bar",



        data:{



            labels:Object.keys(data),



            datasets:[{


                label:"Attack Types",


                data:Object.values(data)


            }]


        },



        options:{



            responsive:true,


            maintainAspectRatio:false,



            scales:{



                y:{


                    beginAtZero:true


                }


            }


        }



    });



}








// Initial load

window.onload = function(){


    updateSOCDashboard();


};




// Auto update every 10 seconds

setInterval(


    updateSOCDashboard,


    10000


);
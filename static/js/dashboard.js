document.addEventListener("DOMContentLoaded", function () {

    const chartCanvas = document.getElementById("atsChart");

    if (!chartCanvas) return;

    new Chart(chartCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Average ATS",
                "Remaining"
            ],

            datasets: [{
                data: [
                    averageATS,
                    100 - averageATS
                ]
            }]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    position: "bottom"
                }

            }

        }

    });

});

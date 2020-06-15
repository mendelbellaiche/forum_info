$(function() {

    $.ajax({
        url: '../data/',
        success: function (data) {

            new Chart(document.getElementById("pie-chart"), {
                type: 'pie',
                data: {
                  labels: ["Number of Tickets", "Number of Comments", "Total"],
                  datasets: [{
                    label: "Number of Item",
                    backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
                    data: [data.number_tickets, data.number_comments, data.number_tickets + data.number_comments]
                  }]
                },
                options: {
                  title: {
                    display: true,
                    text: 'Number of Tickets and Comments'
                  }
                }
            });

        }
    });

});
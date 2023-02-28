/*!
    * Start Bootstrap - SB Admin v7.0.5 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2022 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }


    const dropdownButton = document.getElementById("my-dropdownMenuButton");
    const dropdownMenu = document.querySelector(".my-dropdown-menu");

    dropdownButton.addEventListener("click", function() {
    dropdownMenu.classList.toggle("show");
    });

    dropdownMenu.addEventListener("mouseout", function() {
    dropdownMenu.classList.remove("show");
    });
    dropdownMenu.addEventListener("mouseover", function() {
    dropdownMenu.classList.add("show");
    });


});



$(document).ready(function() {
$('#my-btn').click(function() {
    var id = prompt("Enter item ID:");
    if (id != null && id.trim() != '') {
      $.ajax({
        url: 'http://127.0.0.1:5001/api/v1/tasks/' + id,
        type: 'DELETE',
        success: function(data) {
           console.log(data);
            // Code to save the new table data and display success message
           // Code to save the table data goes here
 
           // Display a success message
           var message = $("<div>");
           message.addClass("flash-message success");
           message.text("data Deleted successfully!");
           $("body").append(message);
 
           // Automatically hide the message after a few seconds
            setTimeout(function() {
            message.hide();
           }, 7000);
         },
        error: function(xhr, Status, error) {
           console.log('Error', Status, error);
           var message = $("<div>");
           message.addClass("flash-message fail");
           message.text("some error occured while Deleting data!" + error);
           $("body").append(message);
           // Automatically hide the message after a few seconds
             setTimeout(function() {
             message.hide();
             }, 7000);
         }
        });
    }
});
});

$(document).ready(function() {
  // Add event listener to update button
  var topicValue, courseValue, reminderValue;
  $(".edit-btn").click(function() {
    // Get table rows and loop through them to add radio buttons
    if ($("#datatablesSimple tbody tr").find("input[name='row-radio']").length > 0) {
      return;
    }

    $("#datatablesSimple tbody tr").each(function() {
      var rowId = $(this).find("td:first").text();
      var radioButton = $("<input type='radio' name='row-radio'>");
      radioButton.val(rowId);
      $(this).find("td:first").prepend(radioButton);
    });

    // Add event listener to radio buttons
    $("input[name='row-radio']").click(function() {
      // Remove any existing text areas
      $("textarea").each(function() {
        var currentValue = $(this).val();
        $(this).closest("td").html(currentValue);
      });
      $("textarea").remove();

      // Get selected row ID and column index
      var rowId = $(this).val();
      var columnIndex = $(this).closest("td").index();

      // If a radio button is selected, create a textarea in the corresponding row
      $(this)
        .closest("tr")
        .find("td:not(:first-child)")
        .each(function(index) {
          if (!$(this).hasClass("Dont")) {
            var currentValue = $(this).text();
            $(this).html("<textarea>" + currentValue + "</textarea>");
          }
        });
      $(this).closest("tr").append("<td><button class='send-btn'>Send</button></td>");

      // Add event listener to text area
      $(".send-btn").click(function() {
        var rows = $('#datatablesSimple tbody tr');
        rows.each(function() {
          var $thisRow = $(this);

          // Get the value of the textarea in the second column
          if ($thisRow.find('td:nth-child(5) textarea').length > 0) {
            topicValue = $thisRow.find('td:nth-child(2) textarea').val();
          }

          if ($thisRow.find('td:nth-child(2) textarea').length > 0) {
            courseValue = $thisRow.find('td:nth-child(3) textarea').val();
          }

          // Get the value of the textarea in the fifth column
          if ($thisRow.find('td:nth-child(7) textarea').length > 0) {
            reminderValue = $thisRow.find('td:nth-child(5) textarea').val();
          }
        });

        var postData = {
          "Topic": topicValue,
          "Course": courseValue,
          "Reminder": reminderValue
        };

        var rowId = $(this).closest("tr").find("input[name='row-radio']").val();
        var num = rowId.trim();
        $.ajax({
          url: 'http://127.0.0.1:5001/api/v1/tasks/' + num,
          type: "PUT",
          data: JSON.stringify(postData),
            contentType: "application/json",
            success: function(response) {
              alert("Value updated successfully!");
            },
            error: function(error) {
              alert("Error updating value: " + error);
            }
          });
        //var currentValue = $('textarea').val();
        //$(this).closest("td").html(currentValue);
        $(this).remove();
        });
      });
    });
  });


/* $(function ShowBox() {
        $("#nav-id").css("background-color", "black")
                    .css("color", "white")

        $("#nav-id").slideUp(10000, function()
	                {
		                $("#nav-id").slideDown(10000);
	                });
                   // .animate({ "left" : "50%" }, 5000);
       // $("#nav-id").animate({ "left" : "0%" }, 500);
    
}); */
function ShowBox() {
    $("#nav-id").css("background-color", "black")
                .css("color", "white");

    $("#nav-id").slideUp(2000, function() {
        $("#nav-id").slideDown(5000);
    });
}

$(document).ready(function() {
    // Get the textarea element
    var textarea = $("#my-chat-input");

    // Attach the focus and blur events
    textarea.on("focus", function() {
        // Slide up the nav element
        $("#nav-id").slideUp();
    }).on("blur", function() {
        // Slide down the nav element
        $("#nav-id").slideDown();
    });

    // Attach the click event to the send button
    $("#chat-submit").on("click", function() {
        // Call the ShowBox function
        ShowBox();
    });
});


function chatlog () {
              var inputMsg = $("#my-chat-input").val();
              var postData = { "text" : inputMsg };
              $("#my-chat-input").val("");
  
              $.ajax({
                  url: 'http://127.0.0.1:5001/api/v1/help/',
                  type: 'POST',
                  headers: {
                          "Content-Type": "application/json",
                              },
                  data: JSON.stringify(postData),
                  success: function(response) {
                      var outputMsg = Object.values(response);
                       var msg = JSON.stringify(outputMsg);
                      console.log(outputMsg);
                      var chatLog = "<div class='sent-message'><p id='sent'>" + inputMsg + "</p></div><div class='replied-message'><p id='received'>" + msg + "</p></div>";
                        $(".chat-conversation").append(chatLog);
                      ouputMsg = {}
                  },
              error: function(jqXHR, textStatus, errorThrown) {
                  console.log('Error', textStatus, errorThrown);
                  var message = $("<div>");
                  message.addClass("flash-message fail");
                  message.text("Bot Server down please help report issue!");
                 $("body").append(message);
               // Automatically hide the message after a few seconds
               setTimeout(function() {
               message.hide();
               }, 7000);
              }
              })
          };



$(document).ready(function() {
  $('#add').click(function() {
    var myDay = $('.Day').val();
    var myCourse = $('.Course').val();
    var myTopic = $('.Topic').val();
    var myReminder = $('.Reminder').val();
    if (myDay && myCourse && myTopic && myReminder) {
      // Add save button
      $('<button/>', {
        text: 'Save',
        class: 'add',
        click: function() {
          // Save the data and remove the save button
          $(this).fadeOut('fast', function() {
            $(this).remove();
          });
        }
      }).appendTo('#card-header');

      var postDate = {
        "Day": myDay,
        "Course": myCourse,
        "Topic": myTopic,
        "Reminder": myReminder
      };
      $('.Day').val('');
      $('.Course').val('');
      $('.Topic').val('');
      $('.Reminder').val('');

      $.ajax({
        url: 'http://127.0.0.1:5001/api/v1/tasks/',
        type: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        data: JSON.stringify(postDate),
        success: function(response) {
          console.log(response);
          // Code to save the new table data and display success message
          // Code to save the table data goes here

          // Display a success message
          var message = $("<div>");
          message.addClass("flash-message success");
          message.text("Table data created successfully!");
          $("body").append(message);

          // Automatically hide the message after a few seconds
          setTimeout(function() {
            message.hide();
          }, 7000);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log('Error', textStatus, errorThrown);
          var message = $("<div>");
          message.addClass("flash-message fail");
          message.text("some error occured while creating table data!");
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


$('#remove-bin').click(function() {
  // Get the data ID from the user
  var Dataid = window.prompt("Please enter the data ID to delete:");
    if ($(this).hasClass('confirm-delete')) {
    // Send delete request to API
        $.ajax({
            url: 'http://127.0.0.1/api/v1/tasks/' + Dataid,
            type: 'DELETE',
            headers: {
                "Content-Type": "application/json",
            },
            success: function(result) {
        // Display success message and remove the deleted item from the page
            alert('Item deleted successfully');
            $('#item-' + dataId).remove();
            },
      error: function(error) {
        // Display error message
        alert('Error deleting item');
      }
    });
  } else {
    // Change button appearance and prompt for confirmation
    $(this).html('<i class="fas fa-check"></i>');
    $(this).addClass('confirm-delete');
    $(this).removeClass('delete-button');
    
    // Set timeout to revert back to original appearance after 5 seconds
    setTimeout(function() {
      $('.confirm-delete[data-id="' + dataId + '"]').html('Delete');
      $('.confirm-delete[data-id="' + dataId + '"]').removeClass('confirm-delete');
      $('.confirm-delete[data-id="' + dataId + '"]').addClass('delete-button');
    }, 5000);
  }
});

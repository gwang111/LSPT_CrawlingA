// Projects page builder for Lab 9
$(document).ready(function () {
  // AJAX call to the labs JSON file that contains all the labs and info for each of them
  $.ajax({
    type: "GET",
    url: "assets/labs.json",
    dataType: "json",
    // On success execute the code to build the projects (labs) page
    success: function (labs) {
      // First, build the list of labs for use by the jQueryUI Tabs widget
      var list = "<ul>";
      $(labs.menuItems).each(function (index) {
        list += "<li><a href=\"#tabs-" + (index + 1) + "\">" + this.name + "</a></li>";
      });
      list += "</ul>";
      $("#labs").append(list);

      // Then, build the individual divs for each of the labs, containing each lab's specific links and data
      $(labs.menuItems).each(function (index) {
        lab_num = index + 1;
        $("#labs").append(
          // The outer div for each lab's tab
          "<div id=\"tabs-" + (index + 1) + "\">" +
            "<h2>" + this.title + "</h2>" +
            "<button id=\"lab-btn-" + lab_num + "\" class=\"ui-button ui-widget ui-corner-all\">Instructions Description</button>" +
            "<a class=\"ui-button ui-widget ui-corner-all\" href=\"" + this.URL + "\">" + this.URLTitle + "</a>" +
            "<div id=\"lab-desc-" + lab_num + "\" class=\"lab-desc\" title=\"Lab " + lab_num + " Instructions\">");

        // Loop to build the contect for each lab's instructions modal
        var modal_content = "<p><ul>";
        $(this.instructions).each(function () {
          modal_content += "<li>" + this + "</li>";
        });
        modal_content += "</ul></p>";
        $("#lab-desc-" + lab_num).append(modal_content);

        // Adding the closing tags for both divs from above
        $("#labs").append("</div></div>");

        // jQueryUI code for setting up the dialog popup and connecting the instructions button to it
        $("#lab-desc-" + lab_num).dialog({
          modal: true,
          width: 600,
          height: 500,
          autoOpen: false,
          buttons: {
            Ok: function () {
              $(this).dialog("close");
            }
          },
        });
      });

      // Linking the buttons for each modal
      /*
       * This cannot be created by a loop, because then the link would be broken and
       * every modal button would just open the modal for the last button in the loop
      */
      $("#lab-btn-1").on("click", function () {
        $("#lab-desc-1").dialog("open");
      });
      $("#lab-btn-2").on("click", function () {
        $("#lab-desc-2").dialog("open");
      });
      $("#lab-btn-3").on("click", function () {
        $("#lab-desc-3").dialog("open");
      });
      $("#lab-btn-4").on("click", function () {
        $("#lab-desc-4").dialog("open");
      });
      $("#lab-btn-5").on("click", function () {
        $("#lab-desc-5").dialog("open");
      });
      $("#lab-btn-6").on("click", function () {
        $("#lab-desc-6").dialog("open");
      });
      $("#lab-btn-7").on("click", function () {
        $("#lab-desc-7").dialog("open");
      });
      $("#lab-btn-8").on("click", function () {
        $("#lab-desc-8").dialog("open");
      });

      // Finally execute the jQueryUI function to turn the parent div into a Tabs widget
      $("#labs").tabs();
    },
    // Execute this code if there was an error
    error: function (msg) {
      alert("Error: " + msg.status + " " + msg.statusText);
    }
  });
});
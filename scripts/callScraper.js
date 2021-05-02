//for fopy pasting with parameters
$.getJSON("link", function (data, textStatus, jqXHR) {
  //I believe we swap data for the search we want
  var results = [];
  $.each(data, function (val) {
    results.push("<li id = 'id'>" + val + "</li>");
  });
  $("<ul/>", { class: "class", html: results.join("") }).appendTo(
    document.body
  ); //document.body can be swapped for some destination I think
});

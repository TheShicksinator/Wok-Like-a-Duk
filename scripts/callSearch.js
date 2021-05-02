//just for copy pasting probably
$.getJSON("/search?terms=x", function (data, textStatus, jqXHR) {
  //I believe we swap data for the search we want
  var results = [];
  $.each(data, function (val) {
    results.push("<li id = 'searchResultTitle'>" + val + "</li>");
  });
  $("<ul/>", { class: "searchResults", html: results.join("") }).appendTo(
    document.body
  ); //document.body can be swapped for some destination I think
});

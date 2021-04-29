$.ajax({
  type: "POST",
  url: "search.py",
  data: { param: searchTerms },
}).done(function (o) {
  // do something
});

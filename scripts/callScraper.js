$.ajax({
  type: "POST",
  url: "scraper.py",
  data: { param: site },
}).done(function (o) {
  // do something
});

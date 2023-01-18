var now = new Date();

var target = document.getElementById("tokei");
var Hour = now.getHours();
var Min = now.getMinutes();

target.innerHTML = "<h1>" + Hour + ":" + Min + "</h1>";



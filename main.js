const url = "zodiac.json";

function formatJSON(json){
	console.log(json);

	let html = "";
	for(let zodiac of json){
		html += "<p>" + zodiac.ja + "/" + zodiac.latin + "</p>";
	}
	document.getElementById("result").innerHTML = html;
}

window.addEventListener("load", ()=>{
	fetch(url)
		.then(response => response.json())
		.then(data => formatJSON(data));
});

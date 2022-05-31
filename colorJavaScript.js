var count = 0;

async function colorInput(){
	

	var shirtValue = document.getElementById("shirtInput").value;
	var bottomValue = document.getElementById("bottomInput").value;
	
	let shirtColor = extractRGB(shirtValue)
	let bottomColor = extractRGB(bottomValue)

	let palette = await completePallete(shirtColor, bottomColor)

	console.log(palette)
	for(let i = 0; i < palette.length; i++){
		let block = document.getElementById(`color${i+1}`)
		let color = palette[i]
		console.log(block)
		console.log(color)
		block.style.backgroundColor = `rgb(${color[0]},${color[1]},${color[2]})`
		console.log(block)

	}
	// var t = document.createTextNode(inputValue);

	// if(inputValue===''){
	// 	alert("You must write something!");
	// }else if(count==1){
	// 	var color = document.createElement("top");
	// 	color.appendChild(t);
	// 	var old = document.getElementById("shirt");
	// 	color.className = "top";
	// 	var parent = old.parentNode;
	// 	parent.replaceChild(color, old);

	// }else if(count==2){
	// 	var color = document.createElement("bottom");
	// 	color.appendChild(t);
	// 	var old = document.getElementById("pants");
	// 	color.className = "bottom";
	// 	var parent = old.parentNode;
	// 	parent.replaceChild(color, old);
		
	// }

	// document.getElementById("myInput").value = "";

	// for(i = 0; i < close.length; i++){
	// 	close[i].onclick = function() {
	// 		var div = this.parentElement;
	// 		div.style.display = "none";
	// 	}
	// }

}

async function completePallete(shirt, bottom){

	var url = "http://colormind.io/api/";
	var data = {
		model : "default",
		input : [shirt,bottom,"N","N","N"]
	}

	let response = await fetch(url, {
		method: "POST",
		body: JSON.stringify(data)
	})
	console.log(response)
	if(response.ok){
		let palette = await response.json()
		return palette.result
	}else{
		console.error(response)
	}

	

	// {"result": [[42, 41, 48], [90, 83, 84], [191, 157, 175], [188, 138, 125], [215, 170, 66]]}
	// note that the input colors have changed as well, by a small amount
}

function extractRGB(hex) {
	if(hex.startsWith("#")){
		hex = hex.substring(1)
	}

  	const r = parseInt(hex.substring(0,2), 16)
  	const g = parseInt(hex.substring(2,4), 16)
  	const b = parseInt(hex.substring(4,6), 16)

  	return [r,g,b]

}

var count = 0;

function colorInput(){
	count++;

	var inputValue = document.getElementById("myInput").value;
	var t = document.createTextNode(inputValue);

	if(inputValue===''){
		alert("You must write something!");
	}else if(count==1){
		var color = document.createElement("top");
		color.appendChild(t);
		var old = document.getElementById("shirt");
		color.className = "top";
		var parent = old.parentNode;
		parent.replaceChild(color, old);

	}else if(count==2){
		var color = document.createElement("bottom");
		color.appendChild(t);
		var old = document.getElementById("pants");
		color.className = "bottom";
		var parent = old.parentNode;
		parent.replaceChild(color, old);
		
	}

	document.getElementById("myInput").value = "";

	for(i = 0; i < close.length; i++){
		close[i].onclick = function() {
			var div = this.parentElement;
			div.style.display = "none";
		}
	}

}
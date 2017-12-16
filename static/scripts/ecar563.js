function upordown(event) {
		  const keyName = event.key;
		  
		  var X = false;
		  
		  if(keyName == "y") X = true;
		  else if(keyName == "u") X = true;
		  else if(keyName == "i") X = true;
		  else if(keyName == "o") X = true;
		  else if(keyName == "p") X = true;
		  
		  if(X) {
			$("#lookingGlass").css("background-color", "red");
		  } else {
			$("#lookingGlass").css("background-color", "white");
		  }	
}

document.onkeyup = function(e) {
	upordown(event);
}

document.onkeydown = function(e) {
	upordown(event);
}

$( "#s1" ).keydown(function(event) {
  upordown(event);
});

$( "#s1" ).keyup(function(event) {
  upordown(event);
});

$( "#s1" ).keypress(function(event) {
  upordown(event);
});

document.addEventListener('keyup', (event) => {
	upordown(event);
}, false);

document.addEventListener('keydown', (event) => {
	upordown(event);
}, false);
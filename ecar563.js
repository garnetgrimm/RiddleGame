document.addEventListener('keydown', (event) => {
	const keyName = event.key;
  
	if(keyName == "z") $("#lookingGlass").html("X")
	else if(keyName == "x") $("#lookingGlass").html("X")
	else if(keyName == "c") $("#lookingGlass").html("X")
	else if(keyName == "v") $("#lookingGlass").html("X")
	else if(keyName == "b") $("#lookingGlass").html("X")
	else $("#lookingGlass").html("O")
}, false);

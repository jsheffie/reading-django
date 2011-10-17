window.onload = initPage;

function initPage() {
	// Currently we find all of the "memoribla" items
	// and we set there "onclick"
	// One important thing to realize here... ( I missed it @ first) 
	// when the user onclick's the image... the javascript code basically
	// makes a "get" to fetch the image. ( this has nothing to do with the
	// request object we are creating in the "createRequest()" function.

	console.log("testtesteeee");
	
	//find the thumbnails on the page
	thumbs = document.getElementById("thumbnailPane").getElementsByTagName("img");

	// set the handler for each image
	for ( var i=0; i < thumbs.length; i++) {
		image = thumbs[i];
		//create the onclick function
		image.onclick = function() {
			// setting up the image "src" url
			detailURL = 'images/' + this.title + '-detail.jpg';
			document.getElementById("itemDetail").src = detailURL;
			console.log("all work and no play makes jack a dull boy");
					getDetails(this.title);
		};
	}
}

// utility function
function createRequest() {
	// here we are going to create a new requestObject... its going to communicate
	// with the server... and send us small chunks of data. -- yippie --
	try {
		request = new XMLHttpRequest();
	} catch (tryMS) {
		try { 
			request = new ActiveXObject("Msxmml2.XMLHTTP");
		} catch (otherMS) {
			try {
				request = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (failed) {
				request = null;
			}
		}
	}
	return request;
}

function getDetails(itemName) {
	console.log("getDetails is a going");
	request = createRequest(); // lets use our utility function to give us a
	                           // nifty request object
	if (request == null) {
		alert("Unable to create request");
		return;
	}
	//var url= "getDetails.php?ImageID=" + escape(itemName);
	var url= "http://www.headfirstlabs.com/books/hfajax/ch01/getDetails.php?ImageID=" + escape(itemName);
	// open.... 3 argument true means Asynchronous
	// -----------------------
	//                        |
	//                        V
	request.open("GET", url, true);
	request.onreadystatechange = displayDetails;
	request.send(null);	
}

function displayDetails() {
	console.log("displayDetails just got called");
	if (request.readyState == 4) {
		if (request.status == 200) {
			detailDiv = document.getElementById("description");
			detailDiv.innerHTML = request.responseText;
		}	
	}
}







window.onload=function(){
	initListeners(); 
}

var spanRes;

var calculBaseUrl = "http://127.0.0.1:5000/devise-api/v1/calculs/"

function initListeners(){
	spanRes = document.getElementById("spanRes");
	
	let btnCarre = document.getElementById("btnCarre");
	let btnRacine = document.getElementById("btnRacine");
	
	btnCarre.addEventListener("click" , ()=>{
		let xValue= (document.getElementById("inputX")).value;
		let wsUrl = calculBaseUrl + "carre/" + xValue;
		console.log("wsUrl="+wsUrl);
		makeAjaxGetRequest(wsUrl,(responseJson)=>{
			console.log("responseJson="+responseJson);
			let resObj = JSON.parse(responseJson);
			spanRes.innerHTML="" + resObj.carre
		});
	});
	
	btnRacine.addEventListener("click" , ()=>{
		let xValue= (document.getElementById("inputX")).value;
		let wsUrl = calculBaseUrl + "racine_carree/" + xValue;
		console.log("wsUrl="+wsUrl);
		makeAjaxGetRequest(wsUrl,(responseJson)=>{
			console.log("responseJson="+responseJson);
			let resObj = JSON.parse(responseJson);
			spanRes.innerHTML="" + resObj.racine
		});
	});
	
	spanRes.innerHTML="0"; //by default
}

function onLoad(response){

}



function onSubmit(event){

  event.preventDefault();


  myDiv=document.getElementById("todoitems")
  var item = document.createElement('div');
  var text = $('form').find('input[name="newitem"]').val();
  var textitem=document.createTextNode(text);

  item.appendChild(textitem);

  var button = document.createElement('BUTTON');
  button.setAttribute("class", "btn btn-danger ");
  var buttontext = document.createTextNode("Delete");
  button.appendChild(buttontext);


  item.setAttribute("class", "pr-10");
  item.appendChild(button);
  myDiv.appendChild(item);


  var data=$(event.target).serialize();
  console.log(data);

  var url=event.target['action'];
  console.log(url);

  $.post({  url:url,
    data:data,
    success:onLoad });

  // document.getElementById("todoitems").innerHTML = data['newitem'];

}



function main() {
    $('form').submit(onSubmit);



}


		// 	function Geeks() {
		// 		var myDiv = document.getElementById("GFG");
    //
		// 		// creating button element
		// 		var button = document.createElement('BUTTON');
    //
		// 		// creating text to be
		// 		//displayed on button
		// 		var text = document.createTextNode("Button");
    //
		// 		// appending text to button
		// 		button.appendChild(text);
    //
		// 		// appending button to div
		// 		myDiv.appendChild(button); ;








$(main);

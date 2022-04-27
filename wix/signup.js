// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
import wixUsers from 'wix-users';

$w.onReady(function () {
	// Write your JavaScript here

	// To select an element by ID use: $w('#elementID')

	// Click 'Preview' to run your code
	$w('#button5').onClick ( () => {

		setTimeout(function() {
			let user = wixUsers.currentUser;
			console.log(user.id);

			const username_input = $w('#input2').value
			const password_input = $w('#input1').value
			let url = "https://immense-sea-41058.herokuapp.com/api/v0/register";
			fetch(url, {
				"method": "post",
				headers: {'Content-Type': 'application/json'},
				"body": JSON.stringify({"username": username_input, "password": password_input, "api_key": user.id})
				})
			.then(response => response.json())
			.then(json => console.log(JSON.stringify(json)));	
		}, 6000);

	// const username_input = $w('#input2').value
	// const password_input = $w('#input1').value
    // let url = "https://immense-sea-41058.herokuapp.com/api/v0/register";
    // fetch(url, {
	// 	"method": "post",
	// 	headers: {'Content-Type': 'application/json'},
	// 	"body": JSON.stringify({"username": username_input, "password": password_input})
	//   })

	// .then(response => response.json())
	// .then(json => console.log(JSON.stringify(json)));
	} );

});
// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
import wixUsers from 'wix-users';


$w.onReady(function () {
	$w('#submit').onClick ( () => {

	// let user = wixUsers.currentUser;

  	// console.log(user.id);
 	// const username_input = user.id
	// const password_input = user.id
    // let url = "https://immense-sea-41058.herokuapp.com/api/v0/register";
    // fetch(url, {
	// 	"method": "post",
	// 	headers: {'Content-Type': 'application/json'},
	// 	"body": JSON.stringify({"username": username_input, "password": password_input})
	//   })

		const username_input = $w('#email').value
		const password_input = $w('#password').value
		let url = "https://immense-sea-41058.herokuapp.com/api/v0/login";
		fetch(url, {
			"method": "post",
			headers: {'Content-Type': 'application/json'},
			"body": JSON.stringify({"username": username_input, "password": password_input})
		})

		.then(response => response.json())
		.then(json => console.log(JSON.stringify(json)));
		// setTimeout(function() {
		// 	let user = wixUsers.currentUser;
		// 	console.log(user.id);
		// 	}, 3000);
	} );
	
});
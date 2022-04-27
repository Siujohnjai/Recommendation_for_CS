// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world

import {local} from 'wix-storage';

$w.onReady(function () {
	// Write your JavaScript here
	

	$w('#button2').onClick(()=>{
		let fircho = $w('#dropdown1').value;
		let seccho = $w('#dropdown2').value;
		let thicho = $w('#dropdown3').value;
		//console.log(fircho)
		local.setItem("fircho", fircho);
		local.setItem("seccho", seccho);
		local.setItem("thicho", thicho);

	})
	
	// To select an element by ID use: $w('#elementID')

	// Click 'Preview' to run your code
});


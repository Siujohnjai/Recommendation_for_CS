// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
import wixData from 'wix-data'

function get_search_list(search_input) {
   let url = "https://immense-sea-41058.herokuapp.com/api/v0/documents/search";
   return fetch(url, {"method": "post",
		                  headers: {'Content-Type': 'application/json'},
		                  "body": JSON.stringify({"search_keyword": String(search_input)})
	  })

	.then(response => response.json())
	.then(json => {return json.search_result_id});
}

$w.onReady(function () {
	
	
	$w("#repeaterhyt").onItemReady(($item1, itemData, index) => {
    $item1("#texthyt").text = itemData.title;
    $item1("#texthyt1").text = itemData.abstract;
    $item1("#buttonhytr").link = itemData.url;
  });

  $w("#repeaterhyt").data = [];

	$w('#buttonhyt').onClick ( () => {
	const search_input = $w('#inputhyt').value
	// var ra;
  get_search_list(search_input)
  .then((result) => {
      var ra = result;
    
        
      wixData.query('Article')
      .limit(50)
      .hasSome('id',ra)
      .find()
      .then((results) => {

        // console.log(results.items);
         if (results.totalCount > 0) {
          $w('#repeaterhyt').data = results.items;
         } 
      });
      })
	} );

 
	// .then(abc => console.log(ra.toString()));

	// let rav = ['abstract data type (adt)64', 'abstract method122']



	

	
});

import wixUsers from 'wix-users';

/*export function iconButton1_click(event) {
  console.log('hii')
  let $item = $w.at(event.context);
  const item = $item("#dataset1").getCurrentItem(); 
  //const item = $w('#dataset1').getCurrentItem();
  let user = wixUsers.currentUser;
  let userid = user.id;
  let itemid = item.id
  let itemurl = item.url
  let itemab = item.text
  let itemtitle = item.title
  wixData.insert('UserFavorites', { item,userid,itemid,itemurl,itemab,itemtitle});
}*/

/**
*	Adds an event handler that runs when the element is double-clicked.
	[Read more](https://www.wix.com/corvid/reference/$w.ClickableMixin.html#onDblClick)
*	 @param {$w.MouseEvent} event
*/
export function iconButton1_dblClick(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
  console.log('hii')
  let $item = $w.at(event.context);
  const item = $item("#dataset1").getCurrentItem(); 
  //const item = $w('#dataset1').getCurrentItem();
  let user = wixUsers.currentUser;
  let userid = user.id;
  let itemid = item.id
  let itemurl = item.url
  let itemab = item.text
  let itemtitle = item.title
  wixData.insert('UserFavorites', { item,userid,itemid,itemurl,itemab,itemtitle});
}
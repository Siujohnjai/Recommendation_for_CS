// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
import wixData from 'wix-data';
import wixUsers from 'wix-users';



$w.onReady(function () {
	// Write your JavaScript here

	// To select an element by ID use: $w('#elementID')
   $w("#repeater4").onItemReady(($item, itemData, index) => {
    $item("#text19").text = itemData.itemtitle;
    $item("#text18").text = itemData.itemab;
    $item("#button4").link = itemData.itemurl;
  });
	// Click 'Preview' to run your code
   let user = wixUsers.currentUser;
	console.log(user.id)

	$w("#dataset1").setFilter( wixData.filter()
	.eq('userid',user.id)
	);

   /*wixData.query('UserFavorites')
   .eq('userid', user.id)
   //.distinct('itemid')
   .find()
   .then((results) => {
     
       $w('#repeater4').data = results.items;
	   console.log("2")
     
  });*/
$w('#button6').onClick((event)=>{
    let $item = $w.at(event.context);
    let clickedItemData = $item("#dataset1").getCurrentItem();
     console.log(clickedItemData)

     wixData.remove('UserFavorites', clickedItemData._id)
 
      .then( (results) => {
         let item = results; 
         $w('#dataset1').refresh();//see item below
         console.log('nothing')
          } )
      .catch( (err) => {
         let errorMsg = err;
        } );
    
      
})

});
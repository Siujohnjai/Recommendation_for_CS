import wixData from 'wix-data'
import wixUsers from 'wix-users';
import {local} from 'wix-storage';


function get_recommendation_list() {
   let url = "https://immense-sea-41058.herokuapp.com/api/v0/documents/recommended";

   return  fetch(url, {method: 'get', headers: {"Authorization": "Token 1234"}})
    .then(response => response.json())
    .then(json => {return  json.recommendation.split(';')});

}

function get_interest_id(interest, count) {
  return wixData.query('Article')
  .limit(count)
  .contains('id', interest)
  .find()
  .then((results) => {
      return results.items;
    
  });
}

function shuffle(array) {
  let currentIndex = array.length,  randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex != 0) {

    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }

  return array;
}

$w.onReady(function () {


  $w("#repeater4").onItemReady(($item, itemData, index) => {
    $item("#text19").text = itemData.Title;
    $item("#text18").text = itemData.Abstract;
    $item("#button4").link = itemData.URL;
  });


  // get_recommendation_list()
  // .then((result) => {
      // var ra = result;
  // const ra = ['user agent20','user agent21','user agent23']
    
  let fir = local.getItem("fircho"); // "value"
  let sec = local.getItem("seccho");
  let thi = local.getItem("thicho");
  console.log(fir)
  console.log(sec)
  console.log(thi)

  // let final_items = .concat(get_interest_id(sec),get_interest_id(thir));

  get_interest_id(fir, 30)
  .then((result) => {
    let fir_list = result

    get_interest_id(sec, 20).then((result) => {
      let sec_list = result
      get_interest_id(thi, 10)
      .then((result) => {
      let thi_list = result
      let final_items = fir_list.concat(sec_list, thi_list)
      console.log(shuffle(final_items))
      $w('#repeater4').data = shuffle(final_items);

      

    })

    

    })


  })


  // })
  
});

  // wixData.query('Article')
  // .limit(20)
  // .startsWith('id', fir)
  // .or(wixData.query('Article')
  //     .limit(20)
  //     .startsWith('id', sec)
  //     .or(wixData.query('Article')
  //         .limit(20)
  //         .startsWith('id', thi)
  //     )
  // )
  // .find()
  // .then((results) => {
  //   if (results.totalCount > 0) {
  //     let items = results.items
  //     console.log(items)

  //     for(let i=0; i<60; i++)
  //     {
  //      if (Math.random()<0.5)
  //       items.splice(i, 1); 
  //     }
  //     console.log(items)
  //     console.log(shuffle(items))
  //     $w('#repeater4').data = shuffle(items);
  //   } 
  //   });


  // let url = "https://immense-sea-41058.herokuapp.com/api/v0/documents/recommended";

  // let ra = [];
  // fetch(url, {method: 'get', headers: {
  // "Authorization": "Token 1234"}})
  //   .then(response => response.json())
  //   .then(json => ra = json.recommendation.split(';'));
  //     // .then(json => console.log(JSON.stringify(json));

  // let read_id = "'''soft computing'''11";
  // let url_read = `https://immense-sea-41058.herokuapp.com/api/v0/documents/${read_id}/read`;

  // fetch(url_read, {method: 'post', headers: {"Authorization": "Token 1234"}})
  //   .then(response => response.json())
  //   .then(json => ra = json.sim_top20.split(';'));



/**
*	Adds an event handler that runs when the element is clicked.
	[Read more](https://www.wix.com/corvid/reference/$w.ClickableMixin.html#onClick)
*	 @param {$w.MouseEvent} event
*/

export function iconButton2_dblClick(event) {
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

  let url_read = `https://immense-sea-41058.herokuapp.com/api/v0/documents/${itemid}/read`;

  fetch(url_read, {method: 'post', headers: {"Authorization": `Token ${userid}`}})
    .then(response => response.json())
    .then(json => 
    {
      let ra = json.sim_top20.split(';')
      wixData.query('Article')
      .limit(20)
      .hasSome('id',ra)
      .find()
      .then((results) => {
        if (results.totalCount > 0) {
          // console.log(shuffle($w('#repeater4').data.concat(results.items)))
          $w('#repeater4').data = shuffle($w('#repeater4').data.concat(results.items));
        } 
      });
    
    }
    
  );
}
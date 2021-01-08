//5fdee52187e11161f87ce649


fetch(`https://api.jsonbin.io/b/5ff755d609f7c73f1b6edc6f`, {
  method: 'GET',
  headers: {
    "secret-key": "$2b$10$p1MJn9niCcUaS11hWerZVOpyJz8o0vmC6Sc9sitXQmjvz4lt2iriG"
  },
})
  .then((response) => response.json())
  .then((data) => {
    console.log(data);

    //For Loop iterating through DATA
    for (i = 0; i < data.length; i++) {
      //Creates new list item element
      var new_li = document.createElement("li");

      //Creating <a> element and takes 'url' from data as href
      var anchor = document.createElement("a");
      anchor.href = data[i]["url"];
      anchor.target = "_blank";

      //Creates a card <div> used for each individual product card also gives it class of "product-card"
      var card = document.createElement("div");
      card.className = "product-card";

      anchor.appendChild(card);
      new_li.appendChild(anchor);

      //Extracting 'name', 'img_src', and 'price' from data
      var img = data[i]["img_src"];
      var name = document.createTextNode(data[i]["name"]);
      var price = document.createTextNode(data[i]["price"]);

      console.log(img);

      //Create individual <div> for Name and Price
      var img_elem = document.createElement("img");
      img_elem.src = img;
      var divname = document.createElement("div");
      divname.className = "product-name";
      var divprice = document.createElement("div");
      divprice.className = "product-price";
      divname.appendChild(name);
      divprice.appendChild(price);
      card.appendChild(img_elem);
      card.appendChild(divname);
      card.appendChild(divprice);

      //Append all of the above into the list item element
      document.querySelector("#scraped-data").appendChild(new_li);

      //Hierarchy diagram: LI->ANCHOR->DivCard->DivName & DivPrice
    }
  });

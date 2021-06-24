function SearchPlayer(player){
	console.log(player)
	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      var data = JSON.parse(this.responseText);
      console.log(data['is_naydeno'][0])
      let obj = data['is_naydeno'][0];
      if (data['is_naydeno']){
          document.querySelector('.name').innerHTML = obj['name'];
          document.querySelector('.age').innerHTML = obj['age'];
          document.querySelector('.height').innerHTML = obj['height'];
          document.querySelector('.salary').innerHTML = obj['salary'];
          document.querySelector('#pImage').src = '/media/'+obj['image'];
      }
    }else{
      console.log('not yet')

      }
    }

    var url = "/test/"
    xhttp.open("GET", url+"?player="+player, true);
    xhttp.send();
}


// url = {% url 'player:searchPlayer' %}


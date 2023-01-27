
    // Download layers which are selected
    // Retrieve all layers
    var layers = document.getElementsByClassName('form-check-input');
    var places = document.getElementsByClassName('leaflet-marker-draggable');
    // Start file download.
    document.getElementById("dwn-btn").addEventListener("click", function(){
      // Retrieve the index of all layers to be download
      var listId = new Array();
      for (let i=0, c=layers.length; i<c; i++){
        if (layers[i].checked){
          listId.push(i);
        }
      };

      // Retrieve the JSON files of the corresponding layers
      i=0;
      files.map(file => file.then(data => {
        if (listId.includes(i)){
          console.log(data);
          text = JSON.stringify(data);
          var filename = dataurls[i]+ ".geojson";
          download(filename, text);
        };
        i++
      }));
    }, false);

    function searchItem(){
      var items = document.getElementsByClassName('list-group-item');
      var listStyle = new Array();
      for (let i=0, c=items.length; i<c; i++){
        listStyle.push(items[i].style.diplay);
        search=document.getElementById("search").value;
        l = search.length;
        console.log(items[i].innerText);
        if (l==0){
          items[i].setAttribute('style', 'display: '+ listStyle[i]+' !important');
        }
        else if(items[i].innerText.slice(0,l)!=search){
          items[i].setAttribute('style', 'display: none !important');
        }
        else{
          items[i].setAttribute('style', 'display: flex !important');
          // console.log(items[i].innerText.slice(0,l));
        }
      };

    };

    function download(filename, text) {
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    };

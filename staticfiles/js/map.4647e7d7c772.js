    // Gestion des Etiquettes
    document.getElementById('labelOn').addEventListener("click", function(){
      labels = document.getElementsByTagName('textPath');
      for (let i=0, c=labels.length; i<c; i++){
        labels[i].setAttribute('style', 'display: block');
      }
    }, false)
    document.getElementById('labelOff').addEventListener("click", function(){
      labels = document.getElementsByTagName('textPath');
      for (let i=0, c=labels.length; i<c; i++){
        labels[i].setAttribute('style', 'display: none');
      }
    }, false)


    // Menu contextuel
    var menubtn = document.getElementById("main")
    menubtn.addEventListener("click", function(){
      if (menubtn.className == "menu openbtn"){
        document.getElementById("accordion").style.width = "300px";
        menubtn.style.marginRight = "300px";
        menubtn.style.transform = "rotate(90deg)";
        menubtn.className = "menu closebtn";
        menubtn.innerHTML = "X";
      }
      else if(menubtn.className == "menu closebtn"){
        document.getElementById("accordion").style.width = "0px";
        menubtn.style.marginRight = "0px";
        menubtn.style.transform = "rotate(180deg)";
        menubtn.className = "menu openbtn";
        menubtn.innerHTML = "|||";
      }
    }, false);

    // Téléchargement des couches sélectionnées
    // Récupération de toutes les couches
    var layers = document.getElementsByClassName('form-check-input');
    // Démarrage du téléchargement
    document.getElementById("dwn-btn").addEventListener("click", function(){
      // Récupération des index des couches sélectionnées
      var listId = new Array();
      for (let i=0, c=layers.length; i<c; i++){
        if (layers[i].checked){
          listId.push(i);
        }
      };

      // Récupération des JSON pour chaque couche et écriture dans un fichier
      i=0;
      files.map(file => file.then(data => {
        if (listId.includes(i)){
          // console.log(data);
          text = JSON.stringify(data);
          var filename = dataurls[i]+ ".geojson";
          download(filename, text);
        };
        i++
      }));
    }, false);


    // Dessin du Pie Chart pour le pourcentage d'AOT valide
    // Récupération du nombre d'AOT en fonction de la validité
    val1 = document.getElementById("red").innerText;
    val2 = document.getElementById("orange").innerText;
    val3 = document.getElementById("green").innerText;

    // Construction du Pie Chart
    var data = [{
      values: [val1, val2, val3],
      labels: ['Expirés', 'En attente', 'A jour'],
      domain: {column: 1},
      name: 'Validité des AOT',
      marker:{
        colors:['rgb(255,57,29)', 'rgb(255,220,50)', 'rgb(76,184,33)']
      },
      hoverinfo: 'label+percent',
      hole: .4,
      type: 'pie'
    }];

    var layout = {
      title: 'Validité des AOT',
      annotations: [
        {
          font: {
            size: 20
          },
          showarrow: false,
          text: 'AOT',
          x: 0.5,
          y: 0.5
        },
      ],
      height: 200,
      width: 180,
      margin: {"t": 30, "b": 0, "l": 0, "r": 0},
      showlegend: false,
      grid: {rows: 1, columns: 1}
    };

    Plotly.newPlot('stat_aot', data, layout);


    //  Récupération des classes de cautions
    var lows = document.getElementsByClassName('low');
    var mids = document.getElementsByClassName('mid');
    var highs = document.getElementsByClassName('high');
    var low = mid = high = 0

    // Calculs des effectifs de chaque classe
    for (let i=0, c=lows.length; i<c; i++){
      low += parseInt(lows[i].innerHTML)
    };
    // console.log(low);

    for (let i=0, c=mids.length; i<c; i++){
      mid += parseInt(mids[i].innerHTML)
    };
    // console.log(mid);

    for (let i=0, c=mids.length; i<c; i++){
      high += parseInt(highs[i].innerHTML)
    };
    // console.log(high);


    var trace1 = {
      x: ['Petite', 'Moyenne', 'Elevée'],
      y: [low, mid, high],
      marker:{
        color: ['rgb(0,191,200)', 'rgb(0,191,200)', 'rgb(0,191,200)']
      },
      type: 'bar',
      width: [0.4, 0.4, 0.4]
    };

    var data = [trace1];

    var layout = {
      title: "Nombre d'AOT par <br> classes de loyer",
      height: 300,
      width: 180,
      margin: {"t": 50, "b": 50, "l": 15, "r": 25},
    };

    Plotly.newPlot('stat_cauti', data, layout);



    // Fonction de recherche pour la liste des AOT
    function searchItem(){
      var items = document.getElementsByClassName('list-group-item');
      var listStyle = new Array();
      for (let i=0, c=items.length; i<c; i++){
        listStyle.push(items[i].style.diplay);
        search=document.getElementById("search").value;
        l = search.length;
        aot = items[i].firstElementChild.firstElementChild.innerText
        // console.log(aot);
        if (l==0){
          items[i].setAttribute('style', 'display: '+ listStyle[i]+' !important');
        }
        else if(aot.toLowerCase().includes(search.toLowerCase())){
          items[i].setAttribute('style', 'display: flex !important');
        }
        else{
          items[i].setAttribute('style', 'display: none !important');
          // console.log(items[i].innerText.slice(0,l));
        }
      };
    };

    // Fonction de téléchargement des couches
    function download(filename, text) {
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    };

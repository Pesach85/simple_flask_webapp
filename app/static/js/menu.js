    var com = new Array();
    var sub = new Array();
    var men = document.getElementById("menu");
    var myVar = setInterval(myTime, 1000);

    com[0] = document.getElementById("funzioni");
    com[1] = document.getElementById("gestione");
    sub[0] = document.getElementById("sub-funzioni");
    sub[1] = document.getElementById("sub-gestione");


    function myTime() {
    var d = new Date();
    document.getElementById("hour").innerHTML = d.toLocaleTimeString();
    }

    com[0].onmouseover = function() {
//        console.log("Block");
        sub[0].style.display = "block";
    }

    sub[0].onmouseover = function() {
//        console.log("Block");
        sub[0].style.display = "block";
    }

    com[1].onmouseover = function() {
//        console.log("Block");
        sub[1].style.display = "block";
    }

    sub[1].onmouseover = function() {
//        console.log("Block");
        sub[1].style.display = "block";
    }

    men.onmouseout = function() {
//        console.log("None");
        sub[0].style.display = "none";
        sub[1].style.display = "none";
    }
    sub[0].onmouseout = function() {
//        console.log("None");
        sub[0].style.display = "none";
        sub[1].style.display = "none";
    }
    sub[1].onmouseout = function() {
//        console.log("None");
        sub[0].style.display = "none";
        sub[1].style.display = "none";
    }
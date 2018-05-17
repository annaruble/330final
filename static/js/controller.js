let titleIn = document.getElementById("titleInput")
let yearIn = document.getElementById("yearInput")

/* titleIn.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        document.getElementById("enter").click();
    }
}) */

function search() {
    let config = {};

    let title = document.getElementById("titleInput").innerHTML;
    //let title = title
    console.log(title)
    console.log('hello')
    let pTitle = title.replace(/ /g, "+")
    let year = document.getElementById("yearInput").innerHTML;
    //let year = year

    fetch(`https://www.omdbapi.com/?i=tt3896198&apikey=72961f58&t=${pTitle}&type=movie&y=${year}&plot=full`)
    .then(function(response) {
        console.log(response)
        return response.json()
    })
    .then(function(movieInfo) {
        console.log(x = movieInfo)
        if (movieInfo["Response"] == "False") {
            alert("Your title was not found. Please try rephrasing or searching a new title.")
        }
        else {
            checkTitle(movieInfo)
            let trailQ = movieInfo["Title"] + " " + movieInfo["Year"] + " Trailer"
            console.log(trailQ)
            getPromo(trailQ)
        }
    })

}


function checkTitle(movieInfo) {
    document.getElementById("titleYr").innerHTML = movieInfo["Title"] + " (" + movieInfo["Year"] + ")"
    document.getElementById("rating").innerHTML = movieInfo["Rated"]
    document.getElementById("runtime").innerHTML = movieInfo["Runtime"]
    document.getElementById("genre").innerHTML = movieInfo["Genre"]
    document.getElementById("actorsDir").innerHTML = movieInfo["Actors"] + " | Director: " + movieInfo["Director"]
    document.getElementById("plot").innerHTML = movieInfo["Plot"]

    try {
        document.getElementById("Tscore").innerHTML = movieInfo["Ratings"][1]["Value"]
    }
    catch(err) {
        document.getElementById("Tscore").innerHTML = "N/A"
    }

    try {
        document.getElementById("Mscore").innerHTML = movieInfo["Ratings"][2]["Value"]
    }
    catch(err) {
        document.getElementById("Mscore").innerHTML = "N/A"
    }

}
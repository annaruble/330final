var trailerId


function getPromo(name){
    // prepare the request
    console.log(name)
    var request = gapi.client.youtube.search.list({
        part: "snippet",
        type: "video",
        q: name.replace(/%20/g, "+"),
        maxResults: 1,
        order: "relevance",
        topicId: "/m/02vxn"

    }); 
    // execute the request
    request.execute(function(response) {
        var results = response.result;
        $.each(results.items, function(index, item){
            trailerId = item.id.videoId
            console.log("trailerId")
            console.log(trailerId)
            let youTubeLink = "//www.youtube.com/embed/" + trailerId
            console.log(youTubeLink)
            $("#trailI").attr("src",youTubeLink);
        })
        
    });
}

function init() {
    gapi.client.setApiKey("AIzaSyC-PnbR92bn-j9lGSFA_ZG5biYt5CHtPT4");
    gapi.client.load("youtube", "v3", function() {
        // yt api is ready
    })
}

function populate_video(video_meta, autoplay) {
    // adding selected styling for current video and removing for old
    var video_btn = $(".video_list").children(".video_item")[Videos.current_list_index]
    
    if($(".selected_video")[0] != undefined) {
        var current_selected_video = $(".selected_video")[0];

        $(current_selected_video).removeClass("selected_video");
    }
    $(video_btn).addClass("selected_video");

   
    // generating HTML for player
    var video_player = Videos.generate_player_html(video_meta, autoplay);
    $("#player_container").html(video_player);


    // adding title    
    var title = video_meta["title"];
    $("#title").html(unescape(title));

    $("#upper_video_meta").fadeIn(200);
    $("#post_btn").attr("href", video_meta["original_post"]);

    var tweetShareUrl = "https://twitter.com/intent/tweet?text=" + "Jamming to http://limeade.co/v/" + video_meta["_id"]["$oid"];
    $("#twitter_btn").attr("href", tweetShareUrl);


    var fbShareUrl = "http://www.facebook.com/sharer.php?u=http://limeade.co/v/" + video_meta["_id"]["$oid"];
    $("#fb_btn").attr("href", fbShareUrl);


    // onfinish event
    if(video_meta["type"] == "vimeo") {
        $('#vimeoplayer').load(function(){
            var player = $f(this);
            player.addEvent('ready', function(){
                player.addEvent('pause', function() {
                    console.log("paused");
                });
                player.addEvent('finish', function() {
                    populate_video(Videos.next_video(), true);
                });
            });
        });

    }

}

function set_video_item_listener() {
    // temp solution. live() was deprecated
    $(".video_item").on("click", function() {
        $(".selected_video").removeClass("selected_video");
        $(this).addClass("selected_video");
        Videos.current_video_id = $(this).attr("data-video-id");
        Videos.current_list_index = $(this).index();
        var video_meta = Videos.get_video_by_id(Videos.current_video_id);
        populate_video(video_meta);
    });

}


$(document).ready(function() {

    // initialization
    Videos.init();
    
    // setting current new filter
    Videos.current_list = Videos.new_videos;
    var new_videos_html = Videos.generate_video_list_html();    
    $("#new").addClass("selected_btn");
    

    // inserting new videos into list container
    $("#results").append(new_videos_html);


    // video_item listener
    set_video_item_listener();

    // filter btn listener
    $("#filters .btn").click(function() {
        $("#search-bar-input").val("");
        
        if($(this).is("#new")) {
           Videos.set_current_list("new"); 
        }
        else if($(this).is("#trending")) {
            Videos.set_current_list("trending");
        }
        $(".selected_btn").removeClass("selected_btn");
        $(this).addClass("selected_btn");
        var new_html = Videos.generate_video_list_html();
        $("#results").html(new_html);
        set_video_item_listener();
    });
  
    // back btn and text input event listeners for search bar 
    $("#back-btn").hide();
    $('input#search-bar-input').keyup(function(e) {
        if($(this).val() != "") {
            $("#back-btn").fadeIn(100);
        }
        else {
            $("#back-btn").fadeOut(100);
        }
        
        // check if enter key was pressed
        var code = (e.keyCode ? e.keyCode : e.which);
        if(code == 13) {

            // make search query
            Videos.current_list = Videos.search($(this).val());
            
            // convert to html
            var search_results_html = Videos.generate_video_list_html();
            $("#results").html(search_results_html);
            set_video_item_listener();
        }
    
    
    });
 
    // setting current new filter
    Videos.current_list = Videos.new_videos;
    var new_videos_html = Videos.generate_video_list_html();    
    $("#new").addClass("selected_btn");
    

    // inserting new videos into list container
    $("#results").append(new_videos_html);



    $("#back-btn").click(function() {
        $("#search-bar-input").val("");
        $(this).fadeOut(100);
    });

    // fade in if selected_id exists
    if(Videos.current_video_id !== undefined) {
        $("#upper_video_meta").fadeIn(200);
    }

    // color fading fb and twitter buttons
    $("#fb_btn").hover(function() {
        $(this).animate({
            backgroundColor: "#3b5998"
        }, 300); 
    }, function() {
        $(this).animate({
            backgroundColor : "#444"
        }, 300);
    });
    $("#twitter_btn").hover(function() {
        $(this).animate({
            backgroundColor: "#4099ff"
        }, 300); 
    }, function() {
        $(this).animate({
            backgroundColor : "#444"
        }, 300);
    });
    $("#post_btn").hover(function() {
        $(this).animate({
            backgroundColor: "#444"
        }, 300); 
    }, function() {
        $(this).animate({
            backgroundColor : "transparent"
        }, 300);
    });


    // info btn
    $("#info_btn").click(function() {
        $("#player_container").fadeOut(200);
        $("#about_container").delay(200).fadeIn(200);
    });

    // cancel btn
    $("#cancel_btn").click(function() {
        $("#about_container").fadeOut(200);
        $("#player_container").delay(200).fadeIn(200);
    });


    // populating video
    if(Videos.current_video_id === undefined) {
        populate_video(Videos.new_videos[0], false);
    }
    $('#vimeoplayer iframe').load(function(){
        var player = $f($(this)[0]);
        player.addEvent('ready', function(){
            player.addEvent('pause', function() {
                console.log("paused");
            });
        });
    });
});

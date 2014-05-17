var Limeade = {
    populate_video : function(video_meta, autoplay) {
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
                var that = this;
                player.addEvent('ready', function(){
                    player.addEvent('pause', function() {
                        console.log("paused");
                    });
                    player.addEvent('finish', function() {
                        that.populate_video(Videos.next_video(), true);
                    });
                });
            });

        }
    },
    set_video_item_listener : function() {
        // temp solution. live() was deprecated
        var that = this;
        $(".video_item").on("click", function() {
            $(".selected_video").removeClass("selected_video");
            $(this).addClass("selected_video");
            Videos.current_video_id = $(this).attr("data-video-id");
            Videos.current_list_index = $(this).index();
            var video_meta = Videos.get_video_by_id(Videos.current_video_id);
            that.populate_video(video_meta);
        });
    }
}


$(document).ready(function() {

    // initialization
    Videos.init();
    
    // setting current new filter
    Videos.current_list = Videos.new_videos;
    var new_videos_html = Videos.generate_video_list_html();    
    $("#new").addClass("selected_btn");
    

    // inserting new videos into list container
    $("#results_inner").append(new_videos_html);

    // video_item listener
    Limeade.set_video_item_listener();

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
        
        // generating video list
        var new_html = Videos.generate_video_list_html();
        
        // adding new html to results
        $("#results").html(new_html);

        Limeade.set_video_item_listener();
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
            $("#results_inner").html(search_results_html);
            set_video_item_listener();
        }
    
    
    });


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

    $("#blog-list-btn").click(function() {
        $("#player_container").fadeOut(200);
        $("#blog-list-container").delay(200).fadeIn(200);
    });

    // cancel btn
    $(".cancel_btn").click(function() {
        $(this).parent().parent().fadeOut(200);
        $("#player_container").delay(200).fadeIn(200);
    });

    $(".info-container").click(function() {
          $(this).fadeOut(200);
          $("#player_container").delay(200).fadeIn(200);
    });


    // populating video
    if(Videos.current_video_id === undefined) {
        Limeade.populate_video(Videos.new_videos[0], false);
    }
    $('#vimeoplayer iframe').load(function(){
        var player = $f($(this)[0]);
        player.addEvent('ready', function(){
            player.addEvent('pause', function() {
                console.log("paused");
            });
        });
    });

    
    // add click listener to load_more_btn
    $("#load_more_btn").hide();
    $("#load_more_btn").click(function() {
        var more_videos;
        if(Videos.current_collection === "new") {
            Videos.current_page = Videos.current_page + 1;

            more_videos = Videos.get_new_videos(Videos.current_page);
            var more_videos_html = Videos.generate_video_list_html(more_videos);
            console.log(more_videos);
            console.log(more_videos_html);
        }
        var more_videos_html = Videos.generate_video_list_html(more_videos);
        $("#results_inner").append(more_videos_html);
    });

    
    // detect when use hits end of video results
    // display "more video load" button
    $("#results").scroll(function() {
        if(($(this).scrollTop() + $(this).height()) >= ($("#results_inner").height() - 200)) {
            $("#load_more_btn").fadeIn();
        }
        else {
            $("#load_more_btn").fadeOut();
        }
    });
});

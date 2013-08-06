var Videos = {};


Videos.current_list = [];
Videos.featured_videos = [];
Videos.new_videos = [];
Videos.trending_videos = [];
Videos.current_list_index = 0;

Videos.get_video_by_id = function(video_id) {
    for (var video in this.current_list) {
        if (this.current_list[video]["video_id"] == video_id) {
            return this.current_list[video];
        }
    }
    return false;
};

Videos.get_featured_videos = function() {
    return [];
};
Videos.get_new_videos = function() {
    $.ajax({
        url : "/videos/?filter=new",
        type : "GET",
        async: false,
        context : this,
        success : function(response) {
            this.new_videos = JSON.parse(response);
        }

    });
    return this.new_videos;
};
Videos.get_trending_videos = function() {
    
    $.ajax({
        url : "/videos/?filter=trending",
        type : "GET",
        async : false,
        context : this,
        success : function(response) {
            this.trending_videos = JSON.parse(response);
        }
    }); 
    return this.trending_videos;
}

Videos.generate_player_html = function(source, autoplay) {
    var raw_html;
    console.log(autoplay);
    if (autoplay === undefined) {
        source["autoplay"] = "1";
    }
    else if (autoplay === false) {
        source["autoplay"] = "0";
    }
    else {
        source["autoplay"] = "1";
    }
    if(source["type"] == "youtube") {
        raw_html = $("#youtube-player-template").html();
    }
    else {
        raw_html = "<iframe id='vimeoplayer' src='http://player.vimeo.com/video/{{ video_id}}?title=0&api=1&player_id=vimeoplayer&autoplay=" + autoplay + "' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>"
    }
    
    var template = Handlebars.compile(raw_html);
    var html = template(source);
    return html;
}

Videos.generate_video_item_html = function(source) {
    var raw_html;
   

    // different html for sources
    if(source["type"] == "youtube") {
        raw_html = $("#youtube-item-template").html();
    }
    else {
        raw_html = $("#vimeo-item-template").html();
    }
    
    var template = Handlebars.compile(raw_html);
    var html = template(source);

    return html;
}

Videos.generate_video_list_html = function(videos_json) {
    if(!videos_json) {
        videos_json = this.current_list;
    }
    
    var listContainer = $('<div>').addClass('video_list');
    for (var video in videos_json) {
        var video_html = this.generate_video_item_html(videos_json[video]);
        listContainer.append(video_html);
    }

    var wrapper = $('<div>').append(listContainer);
    return wrapper.html();
}

Videos.set_current_list = function(filter) {
    if (filter === "new") {
        this.current_list = this.new_videos;
    }
    else if (filter === "featured") {
        this.current_list = this.featured_videos;
    }
    else {
        this.current_list = this.trending_videos;
    }
}



// returns the next video objext to be played
Videos.next_video = function() {
    this.current_list_index++;
    var next_video = this.current_list[this.current_list_index];
    return next_video;
}

Videos.init = function() {
    
    this.featured_videos = this.get_featured_videos();
    this.trending_videos = this.get_trending_videos();
    this.new_videos = this.get_new_videos();
};

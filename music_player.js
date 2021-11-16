var play = document.getElementById("play-button");
var back = document.getElementById("back-button");
var forward = document.getElementById("forward-button");
var albumImage = document.getElementById("player-container");
var albumName = document.getElementById("artist-name");
var index = 0;
var translateX = 0;

var albumCovers = ["url(https://pbs.twimg.com/profile_images/519563191357931520/JQw9Pj1G_400x400.jpeg)", "url(https://upload.wikimedia.org/wikipedia/commons/b/b5/Bill_de_Blasio_by_Gage_Skidmore.jpg)", "url(https://www.newhavenindependent.org/images/made/archives/upload/2017/11/EagleNovember/BookandCard_720_405_88_sha-100.jpg)", "url(https://www.emmys.com/sites/default/files/styles/bio_pics_detail/public/bios/chevy-chase-450x600.jpg?itok=xaKc9Zj2)", "url(https://i2.wp.com/courtneytheexplorer.com/wp-content/uploads/2018/09/img_9113.jpg?fit=1056%2C667&ssl=1), url(https://dg.imgix.net/where-is-heaven-right-now-xglxdwjv-en/landscape/where-is-heaven-right-now-xglxdwjv-0708f1f6346665d02088f86220ffc536.jpg?ts=1513804707&ixlib=rails-4.2.0&fit=crop&w=2000&h=1050)"]

var albumTitles = ["Kanye West - My Beautiful Dark Twisted Fantasy", "Pink Floyd - The Dark Side Of The Moon", "The Beatles - Abbey Road", "The Notorious BIG - Ready To Die", "Kendrick Lamar - To Pimp A Butterfly", "Hobbies Galore - escape(through the heavens)"];

play.addEventListener('click', function() {

    if (play.className == "fa fa-play") {
        play.className = "fa fa-pause"
      } else if (play.className == "fa fa-pause") {
        play.className = "fa fa-play"
      }
});

forward.addEventListener('click', function() {
    if (index < albumCovers.length-1) {
        index++;
    }
    else if (index = albumCovers.length) {
        index = 0;
    }
    albumImage.style.setProperty("--album-cover", albumCovers[index]);
    albumName.innerHTML = albumTitles[index];
});

back.addEventListener('click', function() {
    if (index <= 0) {
        index = albumCovers.length-1;
    }
    else if (index > 0) {
        index--;
    }
    albumImage.style.setProperty("--album-cover", albumCovers[index]);
    albumName.innerHTML = albumTitles[index];
});

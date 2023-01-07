var myNav = document.getElementById("nav");
var amsb = document.getElementById("amsb");
var nav_link = document.getElementById(".nav_link");

window.onscroll = function () {
  "use strict";
  if (
    document.body.scrollTop >= 100 ||
    document.documentElement.scrollTop >= 100
  ) {
    myNav.classList.add("nav-colored");
    amsb.style.color = "black";

    myNav.classList.remove("nav-transparent");
  } else {
    myNav.classList.add("nav-transparent");
    myNav.classList.remove("nav-colored");
    amsb.style.color = "#ffc107";
  }
};

const more = document.querySelector(".more");
const moreCont = document.querySelector(".moreContent");

more.addEventListener("click", () => {
  if (moreCont.style.display === "none") {
    moreCont.style.display = "block";
  } else {
    moreCont.style.display = "none";
  }
});

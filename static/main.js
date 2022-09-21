window.onscroll = function () { myFunction() };

function myFunction() {
  var navId = document.getElementById("navId");
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      navId.className = "navStyle2";
      console.log(navId)
    } else {
      navId.className = "navStyle";
    }
}

 
 //Navbar changing the dropdown menu

 const changeoption = document.getElementById("myselect");
        changeoption.addEventListener('click', changepage);


        function changepage(e) {
            e.preventDefault();
            switch (e.target.value) {

                case 'logout':
                    console.log("Mania")
                   window.open("users/logout","_self")
                    break;

                case 'login':
                  window.open("users/login", "_self")
                    break;

                case 'register':
                   window.open("uses/register", "_self")
                    break;
                case 'account':
                    window.open("users/profile", "_self")
                    break;
            }
        }

        //Display and hide menu bar when changing teh device width
        var hidden_menu = document.getElementById("hidden-menu");
        var button = document.getElementById("display-menu-button");
        var show = document.getElementById("list-menu")
        button.addEventListener('click', function () {
            if (show.style.display === "none") {
                console.log("Tulia")
                show.style.display = "flex"
            }
            else {
                if (hidden_menu.style.display === "none") {
                    show.style.display = "flex";
                }
                else {
                    show.style.display = "none"
                }
            }


        })

        //About us
        // Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}


// Toggle between showing and hiding the sidebar when clicking the menu icon
var mySidebar = document.getElementById("mySidebar");

function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
  } else {
    mySidebar.style.display = 'block';
  }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
}

$(document).ready(function() {
  var scroll_start = 0;
  var startchange = $('#startchange');
  var offset = startchange.offset();
  if (startchange.length) {
    $(document).scroll(function() {
      scroll_start = $(this).scrollTop();
      if (scroll_start > offset.top) {
        $(".navbar-default").css('background-color', '#c1292e');
      } else {
        $('.navbar-default').css('background-color', 'transparent');
      }
    });
  }
});
  

/*SErvice Page*/
 
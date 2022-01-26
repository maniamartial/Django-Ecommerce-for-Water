let househelp = document.getElementById("househelp-btn");
let cleaning = document.getElementById("cleaning-btn");
let plumbing = document.getElementById("plumbing-btn");
let construction = document.getElementById("construction-btn");

let h_help = document.getElementById("househelp-form");
let h_clean = document.getElementById("cleaning-form");
let h_plumb = document.getElementById("plumbing-form");
let h_construct = document.getElementById("construction-form");
function hide() {
  h_help.style.display = "none";
  h_clean.style.display = "none";
  h_plumb.style.display = "none";
  h_construct.style.display = "none";
}
cleaning.addEventListener("click", function () {
  hide();
  h_clean.style.display = "block";
});

plumbing.addEventListener("click", function () {
  hide();
  h_plumb.style.display = "block";
});

construction.addEventListener("click", function () {
  hide();
  h_construct.style.display = "block";
});
househelp.addEventListener("click", function () {
  hide();
  h_help.style.display = "block";
});
//End of service page

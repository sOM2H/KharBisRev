function disp(form) {
    if (form.style.display == "none") {
        form.style.display = "inline-block";
    } else {
        form.style.display = "none";
    }
}
function like() {
$('.fa-heart-o').click(function () {
    $(".fa-like").removeClass('.fa-heart-o');
    $(".fa-like").addClass('.fa-heart');
})}

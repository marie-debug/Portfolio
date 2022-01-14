function onNavClick() {
    var element = document.getElementById("container-id");
    var button = document.getElementById("nav-button");
    var buttonClasses = button.classList;

    if (buttonClasses.contains("collapsed") == false) {
        element.classList.add("container-padding");
    } else {
        element.classList.remove("container-padding");
    }
}

window.onload = function() {
    document.getElementById("nav-button").addEventListener('click', onNavClick);
}
const openPopup = document.getElementById('openpopup');
const popup = document.getElementById('popup');
popup.style.display = "none";

openPopup.addEventListener('click', openOnClick)
function openOnClick() {
    if (popup.style.display == "none") {
        popup.style.display = "block";
    }
    else {
        popup.style.display = "none"
    }
};
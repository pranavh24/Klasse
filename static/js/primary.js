function updateProgressBar() {

    var progress = document.getElementById("progress");
    var progressText = document.getElementById("progress-text");
    
    if(getPixelValue(window.getComputedStyle(progress).width) <= 400) {
        progressText.style.paddingLeft = getPixelValue(window.getComputedStyle(progress).width) + 20 + "px";
        progressText.style.color = "rgb(102, 102, 102)";
    } else {
        progressText.style.paddingLeft = "30px";
        progressText.style.color = "white";
    }

}

function getPixelValue(property) {
    return parseInt(property.substring(0, property.indexOf("px")));
}
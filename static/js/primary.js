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

function expandFAQ(faq) {
    var answer = faq.getElementsByTagName("P")[0];
    var arrow = faq.getElementsByClassName("faq-arrow")[0];
    
    if(answer.style.display === "block") {
        
        arrow.style.transform = "rotate(-45deg)";
        answer.style.display = "none";
        faq.style.height = "auto";
        
    } else {
        setTimeout(function(){
            arrow.style.transform = "rotate(45deg)";
            answer.style.display = "block";
            faq.style.height = "auto";
        }, 100);
    }
}
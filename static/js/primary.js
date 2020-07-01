var hoverOnDropdown = false;
var hoverOnProfile = false;

function updateProgressBar() {

    var progress = document.getElementById("progress");
    var progressText = document.getElementById("progress-text");
    
    var xp = parseInt(progressText.textContent.substring(progressText.textContent.indexOf(':') + 2, progressText.textContent.indexOf('/')));
    progress.style.width = (xp * 0.01 * (1375 - 15 * 2)) + "px";

    console.log("width = " + progress.style.width);
    

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

function dropdownHover(src, cond) {
    var dropdown = document.getElementsByClassName('dropdown-menu')[0];
    var profile = document.getElementsByClassName('profile')[0];

    if(src === dropdown) {
        hoverOnDropdown = cond;
        
        
    } else {
        hoverOnProfile = cond;
        
    }

    if(dropdown.style.visibility == 'visible' && !hoverOnDropdown && !hoverOnProfile) {
        dropdown.style.visibility = 'hidden';
        profile.style.filter = "brightness(100%)"

    } else if(hoverOnDropdown || hoverOnProfile) {
        dropdown.style.visibility = 'visible';
        profile.style.filter = "brightness(92.5%)"
    }
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
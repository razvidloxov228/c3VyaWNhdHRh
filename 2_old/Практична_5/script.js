function displayHTMLDefinition() {
    document.getElementById("result").innerText = "HTML — це мова розмітки, яка використовується для створення структури веб-сторінок.";
}

function displayCSSDefinition() {
    document.getElementById("result").innerText = "CSS — це стильова мова, яка визначає вигляд і оформлення веб-сторінок.";
}

document.getElementById("htmlButton").addEventListener("click", displayHTMLDefinition);
document.getElementById("cssButton").addEventListener("click", displayCSSDefinition);
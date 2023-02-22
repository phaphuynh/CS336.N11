imgInp.onchange = evt => {
    //var y = document.getElementById('display_image1');
    //y.parentNode.removeChild(y);
    const [file] = imgInp.files
    if (file) {
        display_image.src = URL.createObjectURL(file)
    }
}

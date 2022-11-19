function preview() {
    frame.src=URL.createObjectURL(event.target.files[0]);
}
const form = document.querySelector("form");
form.addEventListener("submit", function() {
    const Info = {
        fileName: form[0].value.split("\\").pop().slice(0,1)
    }
    localStorage.setItem("fileName", Info.fileName);
})
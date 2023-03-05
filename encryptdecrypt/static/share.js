var op = document.querySelector('#op');

document.querySelector('#share').addEventListener('click', function(){
    navigator.share(op.textContent.trim());
});

document.querySelector('#copy').addEventListener('click', function(){
    navigator.clipboard.writeText(op.textContent.trim());
    alert(text)
});
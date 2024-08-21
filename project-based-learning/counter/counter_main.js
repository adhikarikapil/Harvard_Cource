display = document.getElementById('display');

let count = 0;
document.getElementById('increase').addEventListener('click', (event) => {
    count ++;
    display.value = count;
})


document.getElementById('decrease').addEventListener('click', (event) => {
    count --;
    display.value = count;
})

document.getElementById('reset').addEventListener('click', (event) => {
    count = 0;
    display.value = count;
})

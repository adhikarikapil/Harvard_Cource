const context = document.getElementById('gameCanvas');
const ctx = context.getContext('2d');

let snake = [  {x: 150, y: 150},  {x: 140, y: 150},  {x: 130, y: 150},  {x: 120, y: 150},  {x: 110, y: 150},];

function drawSnakePart(snakePart) {  
    ctx.fillStyle = 'lightgreen';  
    ctx.fillRect(snakePart.x, snakePart.y, 10, 10);  

    ctx.strokestyle = 'darkgreen';  
    ctx.strokeRect(snakePart.x, snakePart.y, 10, 10);
}

function drawSnake() {  
    snake.forEach(drawSnakePart);
}
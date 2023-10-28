const game = document.getElementById('game');
const snake = document.createElement('div');
snake.classList.add('snake');
game.appendChild(snake);

let snakeX = 0;
let snakeY = 0;
let dx = 20;
let dy = 0;

function moveSnake() {
    snakeX += dx;
    snakeY += dy;
    snake.style.left = snakeX + 'px';
    snake.style.top = snakeY + 'px';
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        dx = 20;
        dy = 0;
    } else if (e.key === 'ArrowLeft') {
        dx = -20;
        dy = 0;
    } else if (e.key === 'ArrowUp') {
        dx = 0;
        dy = -20;
    } else if (e.key === 'ArrowDown') {
        dx = 0;
        dy = 20;
    }
});

setInterval(moveSnake, 200);

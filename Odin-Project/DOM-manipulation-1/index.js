const container = document.querySelector('#container');

const pharagraph = document.createElement('p');
pharagraph.textContent = "Hey I'm red!"
pharagraph.style.cssText = 'color: red;'

container.appendChild(pharagraph);

const h3Text = document.createElement('h3');
h3Text.textContent = "I'm a blue h3!"
h3Text.style.cssText = 'color: blue;'
container.appendChild(h3Text);

const newDiv = document.createElement('div');
newDiv.classList.add('newDiv')
newDiv.style.cssText = 'background-color: pink; border-color: black;'
container.appendChild(newDiv);

const div = document.querySelector('.newDiv');
const titleDiv = document.createElement('h1');
titleDiv.textContent = "I'm in a div"
div.appendChild(titleDiv)

const pharagraphDiv = document.createElement('p');
pharagraphDiv.textContent = "ME TOO!";
div.appendChild(pharagraphDiv)

btn.addEventListener('click', function (e) {
    console.log(e.target);
});

btn.addEventListener('click', function (e) {
    e.target.style.background = 'blue';
});
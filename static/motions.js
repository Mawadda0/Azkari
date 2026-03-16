
function setupCounters() {
    const buttons = document.querySelectorAll(".counter-btn");

    buttons.forEach(btn => {
        const counter = btn.previousElementSibling;
        const max = parseInt(counter.dataset.max);
        counter.dataset.current = 0;
        counter.textContent = `0 / ${max}`;

        btn.addEventListener("click", () => {
            let current = parseInt(counter.dataset.current);
            current++;
            if(current > max)
                {
                current = 0;
            }
            counter.dataset.current = current;
            counter.textContent = `${current} / ${max}`;
        });
    });
}

window.addEventListener('DOMContentLoaded', setupCounters);




function setupSimpleCounters() {

    const containers = document.querySelectorAll(".counter-container");

    containers.forEach(container => {

        const counter = container.querySelector(".counter-reset");
        const plusBtn = container.querySelector(".counter-btn-reset");
        const resetBtn = container.querySelector(".reset-btn");

        counter.dataset.current = 0;
        counter.textContent = 0;

        plusBtn.addEventListener("click", () => {

            let current = parseInt(counter.dataset.current);
            current++;

            counter.dataset.current = current;
            counter.textContent = current;

        });

        resetBtn.addEventListener("click", () => {

            counter.dataset.current = 0;
            counter.textContent = 0;

        });

    });
}

window.addEventListener("DOMContentLoaded", setupSimpleCounters);
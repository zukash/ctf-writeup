function toggleFlagInstructions() {
  var instructions = document.querySelector(".flagInstructions");
  instructions.style.display =
    instructions.style.display == "flex" ? "none" : "flex";
}

document.querySelector(".readInstructions").addEventListener("click", (ev) => {
  ev.preventDefault();
  toggleFlagInstructions();
});

document
  .querySelector(".flagInstructions .backdrop")
  .addEventListener("click", (ev) => {
    ev.preventDefault();
    toggleFlagInstructions();
  });

[...document.querySelectorAll(".btn")].forEach((e) =>
  e.addEventListener("click", (ev) => {
    var page = ev.target.innerText.toLowerCase();
    var selectedElement = document.querySelector("h1.selected");

    if (selectedElement != ev.target) {
      selectedElement.classList.remove("selected");
      ev.target.classList.add("selected");
    }

    var selectedPage = document.querySelector(".page." + page);
    if (!selectedPage.classList.contains("active")) {
      document.querySelector(".page.active").classList.remove("active");
      selectedPage.classList.add("active");
    }
  })
);

document.querySelector("input").addEventListener("input", (ev) => {
  const term = ev.target.value;

  const tasks = [...document.querySelectorAll(".challenges .task")];

  tasks.forEach((el) => {
    el.style.display =
      el.innerText.toLowerCase().indexOf(term.toLowerCase()) > -1 &&
      !el.classList.contains("none")
        ? "block"
        : "none";
  });
});

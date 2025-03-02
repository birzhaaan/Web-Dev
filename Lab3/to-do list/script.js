const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");
const historyContainer = document.getElementById("history-container")
function addTask() {
  if (inputBox.value === "") {
    alert("Your must write something!");
  } else {
    let li = document.createElement("li");
    li.innerHTML = inputBox.value;
    listContainer.appendChild(li);
    let span = document.createElement("span");
    span.innerHTML = "\u00d7";
    li.appendChild(span);
    updateHistory("Added", inputBox.value);
  }
  inputBox.value = "";
  saveData();
}
listContainer.addEventListener(
  "click",
  function (e) {
    if (e.target.tagName === "LI") {
      e.target.classList.toggle("checked");
      let action = e.target.classList.contains("checked") ? "Completed" : "Uncompleted";
      updateHistory(action, e.target.innerText.replace("×", "").trim());
      saveData();
    } else if (e.target.tagName === "SPAN") {
      e.target.parentElement.remove();
      updateHistory("Deleted", e.target.parentElement.innerText.replace("×", "").trim());
      saveData();
    }
  },
  false
);
function updateHistory(action, task) {
  let li = document.createElement("li");
  li.innerHTML = `${action}: ${task}`;
  historyContainer.appendChild(li);
  saveData();
}
function saveData() {
  localStorage.setItem("data", listContainer.innerHTML);
}
function showTask() {
  listContainer.innerHTML = localStorage.getItem("data");
}
showTask();
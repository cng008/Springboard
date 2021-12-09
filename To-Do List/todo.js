/*Part 1
For this assignment you will be combining your knowledge of DOM access and events to build a todo app!
As a user, you should be able to:

Add a new todo (by submitting a form)
Mark a todo as completed (cross out the text of the todo)
Remove a todo

Part 2
Now that you have a functioning todo app, save your todos in localStorage! 
Make sure that when the page refreshes, the todos on the page remain there.*/

const toggleSwitch = document.querySelector('input[type="checkbox"]');
//CHECK TO SEE IF ITEM CROSSED ENABLED IS IN LOCAL STORAGE
if (localStorage.getItem("isDone")) {
  document.body.className = "crossed"; //if there, add to class 'checked' ^
  toggleSwitch.checked = true; //keeps item checked
}

//WHEN WE CHECK OFF, UPDATE LOCAL STORAGE & CHANGE THE className on li
toggleSwitch.addEventListener("click", function (e) {
  const { checked } = toggleSwitch;
  if (checked) {
    // set localStorage based on checked
    localStorage.setItem("isDone", true);
  } else {
    localStorage.removeItem("isDone"); //removed object rather than saying 'false'
  }
  document.body.className = checked ? "crossed" : ""; //if checked = crossed; not = do nothing
});

// const form = document.querySelector("#toDo");
const toDoList = document.querySelector("#toDoList");
// const li = document.querySelectorAll("li");
const edit = document.querySelector("#edit");
// const add = document.querySelector("#add");
const addUnder = document.querySelector("#addUnder #add");
// const input = document.querySelector('input[type="text"]');

//BUTTON EVENTS
toDoList.addEventListener("click", function (e) {
  if (e.target === edit) {
    e.preventDefault();
    e.target.parentElement.remove(); //delete item
  } else if (e.target === addUnder) {
    e.preventDefault();
    return addNew(); //run function and add new li
  }
});

//add item under clicked + button
function addNew() {
  const newToDo = document.createElement("li");
  const newAddBtn = document.createElement("button");
  const newEditBtn = document.createElement("button");
  const newCheck = document.createElement("input");
  const newInput = document.createElement("input");
  // const newLine = newToDo + newBtns + newInput;

  for (let li of newToDo) {
    newToDo.append(newAddBtn);
    newAddBtn.id = "add";
    newAddBtn.innerHTML = "&#10303;"; //https://www.htmlsymbols.xyz/unicode/U+283F

    newToDo.append(newEditBtn);
    newEditBtn.id = "edit";
    newEditBtn.innerHTML = "&#43;"; //https://www.htmlsymbols.xyz/unicode/U+002B

    newToDo.append(newCheck);
    newCheck.type = "checkbox";

    newToDo.append(newInput);
    newInput.type = "text";
    newInput.placeholder = "Add something to do!";
  }
  toDoList.append(newToDo);

  //   localStorage.setItem("newLine", JSON.stringify(newLine));
  //   JSON.parse(localStorage.getItem(newLine));
}

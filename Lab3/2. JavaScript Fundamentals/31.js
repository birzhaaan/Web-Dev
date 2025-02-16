<<<<<<< HEAD
function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

ask(
  "Вы согласны?",
  () => alert("Вы согласились."),
  () => alert("Вы отменили выполнение.")
=======
function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

ask(
  "Вы согласны?",
  () => alert("Вы согласились."),
  () => alert("Вы отменили выполнение.")
>>>>>>> fe60499 (Lab4)
);
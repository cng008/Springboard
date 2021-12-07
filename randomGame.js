/*
Write a function called randomGame that selects a random number between 0 and 1 every 1000 milliseconds
and each time that a random number is picked, add 1 to a counter.
If the number is greater than .75, stop the timer and
console.log the number of tries it took before we found a number greater than .75.
*/

function randomGame() {
  let tries = 0;
  let game = setInterval(function () {
    if (Math.random() <= 0.75) {
      tries++; //adds to count when random number is under .75
    } else {
      clearInterval(game);
      console.log("It took " + tries + " tries.");
    }
  }, 1000); //returns every 1 second
}

//GIVEN SOLUTION
// function randomGame() {
//   let num;
//   let times = 0;
//   let timer = setInterval(function () {
//     num = Math.random();
//     times++;
//     if (num > 0.75) {
//       clearInterval(timer);
//       console.log("It took " + times + " try/tries.");
//     }
//   }, 1000);
// }

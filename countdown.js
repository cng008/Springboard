/*
Write a function called countdown that accepts a number as a parameter
and every 1000 milliseconds decrements the value and console.logs it.
Once the value is 0 it should log “DONE!” and stop.
countDown(4);
// 3
// 2
// 1
// "DONE!"
*/

function countDown(num) {
  let timer = setInterval(function () {
    num--; //subtracts 1 from num
    if (num > 0) {
      console.log(num); //prints every number over 0
    } else {
      clearInterval(timer);
      console.log("DONE!");
    }
  }, 1000); //returns every 1 second
}

//GIVEN SOLUTION
// function countDown(time){
//   let timer = setInterval(function(){
//     time--;
//     if(time <= 0){
//       clearInterval(timer);
//       console.log('DONE!');
//     }
//     else {
//       console.log(time);
//     }
//   },1000)
// }

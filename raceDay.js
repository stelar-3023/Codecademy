let raceNumber = Math.floor(Math.random() * 1000);

const early = false;

const age = 44;

if (age > 18 && early == true) {
  raceNumber += 1000;
}
if (age > 18 && early == true) {
  console.log(
    `Your race will start at 9:30 am, and your race number is: ${raceNumber}`
  );
} else if (age > 18 && early == false) {
  console.log(
    `Your race will start at 11:00 am, and your race number is: ${raceNumber}`
  );
} else if (age < 18) {
  console.log(
    `Your race will start at 12:30 pm, and your race number is: ${raceNumber}`
  );
} else {
  console.log("Please go to the registration desk. Thank you.");
}

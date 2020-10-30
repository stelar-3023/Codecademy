// set variable equal to my age
const myAge = 44;
// set variable qual to 2 (earlyYears)
let earlyYears = 2;

earlyYears *= 10.5;

// set variable laterYears to myAge - 2
let laterYears = myAge - 2;

//Multiply the laterYears variable by 4 to calculate the number of dog years
laterYears *= 4;

console.log(earlyYears);
console.log(laterYears);

// Add earlyYears and laterYears together, and store that in a variable named myAgeInDogYears
myAgeInDogYears = earlyYears + laterYears;

// Write your name as a string, call its built-in method .toLowerCase(), and store the result in a variable called myName
myName = "STEVE".toLowerCase();

// Use string interpolation to write a statement that displays name and age in dog years.
console.log(
  `My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`
);

/* const reverseArray = (arr) => {
  let reversed = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reversed.push(arr[i]);
  }
  return reversed;
};

const sentence = ['sense.','make', 'all', 'will', 'This'];
console.log(reverseArray(sentence))  */

/* const greetAliens = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    console.log(
      "Oh powerful " + arr[i] + ", we humans offer our unconditional surrender!"
    );
  }
};
const aliens = ["Blorgous", "Glamyx", "Wegord", "SpaceKing"];
greetAliens(aliens); */

/* const convertToBaby = (arr) => {
  const babyArray = [];
  for (let i = 0; i < arr.length; i++) {
    babyArray.push("baby " + arr[i]);
  }
  return babyArray;
};

const animals = ["panda", "turtle", "giraffe", "hippo", "sloth", "human"];

console.log(convertToBaby(animals)); */

/* const numbers = [5, 3, 9, 30];

const smallestPowerOfTwo = (arr) => {
  let results = [];
  // The 'outer' for loop:
  for (let i = 0; i < arr.length; i++) {
    number = arr[i];

    // The 'inner' while loop:
    // We needed to create a new variable!
    let j = 1;
    while (j < number) {
      j = j * 2;
    }
    results.push(j);
  }
  return results;
};

console.log(smallestPowerOfTwo(numbers)); */

/* const veggies = ["broccoli", "spinach", "cauliflower", "broccoflower"];

const politelyDecline = (veg) => {
  console.log("No " + veg + " please. I will have pizza with extra cheese.");
};

// Checkpoint 1 solutions:
const declineEverything = (arr) => {
  arr.forEach(politelyDecline);
};
// Using an anonymous function and string interpolation:
const acceptEverything = (arr) => {
  arr.forEach((e) => {
    console.log(`Ok, I guess I will eat some ${e}.`);
  });
};
declineEverything(veggies)
acceptEverything(veggies) */

/* const numbers = [2, 7, 9, 171, 52, 33, 14];

const toSquare = (num) => num * num;

const squareNums = arr => arr.map(toSquare)
console.log(squareNums(numbers)) */

/* const shoutGreetings = (arr) => arr.map((word) => word.toUpperCase() + "!");
const greetings = ["hello", "hi", "heya", "oi", "hey", "yo"];

console.log(shoutGreetings(greetings)); */

/* const sortYears = arr => arr.sort((x, y) => y - x);

const years = [1970, 1999, 1951, 1982, 1963, 2011, 2018, 1922]
console.log(sortYears(years)) */

/* const justCoolStuff = (firstArray, secondArray) =>
  firstArray.filter((item) => secondArray.includes(item));

const coolStuff = [
  "gameboys",
  "skateboards",
  "backwards hats",
  "fruit-by-the-foot",
  "pogs",
  "my room",
  "temporary tattoos",
];

const myStuff = [
  "rules",
  "fruit-by-the-foot",
  "wedgies",
  "sweaters",
  "skateboards",
  "family-night",
  "my room",
  "braces",
  "the information superhighway",
];

console.log(justCoolStuff(myStuff, coolStuff)); */

/* const isTheDinnerVegan = (arr) => arr.every((food) => food.source === "plant");
const dinner = [
  //{ name: "hamburger", source: "meat" },
  //{ name: "cheese", source: "dairy" },
  { name: "ketchup", source: "plant" },
  { name: "bun", source: "plant" },
  //{ name: "dessert twinkies", source: "unknown" },
];

console.log(isTheDinnerVegan(dinner)); */

/* const speciesArray = [
  { speciesName: "shark", numTeeth: 50 },
  { speciesName: "dog", numTeeth: 42 },
  { speciesName: "alligator", numTeeth: 80 },
  { speciesName: "human", numTeeth: 32 },
];
const sortSpeciesByTeeth = arr => arr.sort((speciesObj1, speciesObj2) => speciesObj1.numTeeth > speciesObj2.numTeeth)

console.log(sortSpeciesByTeeth(speciesArray)); */

/* const findMyKeys = arr => arr.findIndex(item => item === 'keys')

const randomStuff = ['credit card', 'screwdriver', 'receipt', 'gum', 'keys', 'used gum', 'plastic spoon'];

console.log(findMyKeys(randomStuff)) */

/* const dogFactory = (name, breed, weight) => {
  return {
      // add getters and setters
    _name: name,
    _breed: breed,
    _weight: weight,
    get name() {
      return this._name;
    },
    set name(newName) {
      this._name = newName;
    },
    get breed() {
      return this._breed;
    },
    set breed(newBreed) {
      this._breed = newBreed;
    },
    get weight() {
      return this._weight;
    },
    set weight(newWeight) {
      this._weight = newWeight;
    },
    // add methods
    bark() {
      return "ruff! ruff!";
    },
    eatTooManyTreats() {
      this._weight++;
    },
  };
}; */

/* function factorial(num) {
    if (num === 0 || num === 1)
    return 1;
    for (var i = num - 1; i >= 1; i--) {
        num *= i
    }
    return num
}
console.log(factorial(5)) */

const subLength = (string, charact) => {
    const splitWord = string.split('');
    const appears = splitWord.filter(letter => letter === charact);
    if (appears.length < 2 || appears.length > 2){
        return 0;
    } else if (appears.length === 2){
        const first = string.indexOf(charact);
        const second = string.lastIndexOf(charact);
        return second - first + 1;
    }
};
console.log(subLength('Saturday', 'a'))
console.log(subLength('digitize', 'i'))
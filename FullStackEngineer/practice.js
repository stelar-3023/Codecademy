// function colorMessage(favoriteColor, shirtColor) {
//   if (favoriteColor == shirtColor) {
//     return 'The shirt is your favorite color!';
//   } else {
//     return 'That is a nice color.';
//   }
// }

// function isEven(num) {
//   if (num % 2 === 0) {
//     return true;
//   } else {
//     return false;
//   }
// }

// function numberDigits(x) {
//   if (x >= 0 && x <= 9) {
//     return 'One digit: ' + x;
//   } else if (x >= 10 && x <= 99) {
//     return 'Two digits: ' + x;
//   } else {
//     return 'The number is: ' + x;
//   }
// }

// // reverseArray
// function reverseArray(arr) {
//   let newArr = [];
//   for (let i = arr.length - 1; i >= 0; i--) {
//     newArr.push(arr[i]);
//   }
//   return newArr;
// }

// const sentence = ['sense.', 'make', 'all', 'will', 'This'];

// console.log(reverseArray(sentence));

// function greetAliens(arr) {
//   for (i = 0; i < arr.length; i++) {
//     console.log(
//       `Oh powerful ${arr[i]}, we humans offer our unconditional surrender!`
//     );
//   }
// }
// const aliens = ['Blorgous', 'Glamyx', 'Wegord', 'SpaceKing'];

// greetAliens(aliens);

// function convertToBaby(arr) {
//   let newArr = [];
//   for (let i = 0; i < arr.length; i++) {
//     newArr.push('baby ' + arr[i]);
//   }
//   return newArr;
// }

// const animals = ['panda', 'turtle', 'giraffe', 'hippo', 'sloth', 'human'];

// console.log(convertToBaby(animals));

// function smallestPowerOfTwo(arr) {
//   let results = [];
//   for (let i = 0; i < arr.length; i++) {
//     let num = arr[i];
//     let j = 1;
//     while (j < num) {
//       j = j * 2;
//       console.log(j);
//     }
//     results.push(j);
//   }
//   return results;
// }
// const numbers = [5, 3, 9, 30];
// console.log(smallestPowerOfTwo(numbers));

// const veggies = ['broccoli', 'spinach', 'cauliflower', 'broccoflower'];

// const politelyDecline = (veg) => {
//   console.log('No ' + veg + ' please. I will have pizza with extra cheese.');
// };

// function declineEverything(arr) {
//   arr.forEach(politelyDecline);
// }

// declineEverything(veggies);

// function acceptEverything(arr) {
//   arr.forEach((item) => {
//     console.log(`Ok, I guess I will eat some ${item}.`);
//   });
// }

// acceptEverything(veggies);

// const numbers = [2, 7, 9, 171, 52, 33, 14]

// const toSquare = num => num * num

// function squareNums(arr) {
//   return arr.map(toSquare)
// }

// console.log(squareNums(numbers))

// const shoutGreetings = arr => arr.map(word => word.toUpperCase() + '!')

// const greetings = ['hello', 'hi', 'heya', 'oi', 'hey', 'yo'];

// console.log(shoutGreetings(greetings))

// function sortYears(arr) {
//   return arr.sort((a, b) => b - a);
// }
// const years = [1970, 1999, 1951, 1982, 1963, 2011, 2018, 1922]

// console.log(sortYears(years))

// function justCoolStuff(arr1, arr2) {
//   return arr1.filter(item => arr2.includes(item))
// }

// const coolStuff = ['gameboys', 'skateboards', 'backwards hats', 'fruit-by-the-foot', 'pogs', 'my room', 'temporary tattoos'];

// const myStuff = [ 'rules', 'fruit-by-the-foot', 'wedgies', 'sweaters', 'skateboards', 'family-night', 'my room', 'braces', 'the information superhighway'];

// console.log(justCoolStuff(myStuff, coolStuff))

// function isTheDinnerVegan(arr) {
//   return arr.every(food => food.source === 'plant')
// }

// const dinner = [{name: 'hamburger', source: 'meat'}, {name: 'cheese', source: 'dairy'}, {name: 'ketchup', source:'plant'}, {name: 'bun', source: 'plant'}, {name: 'dessert twinkies', source:'unknown'}];

// const meal = [{name: 'arugula', source: 'plant'}, {name: 'tomatoes', source: 'plant'}, {name: 'lemon', source:'plant'}, {name: 'olive oil', source: 'plant'}];

// console.log(isTheDinnerVegan(dinner))
// console.log(isTheDinnerVegan(meal))

// function sortSpeciesByTeeth(arr) {
//   return arr.sort((a, b) => a.numTeeth - b.numTeeth)
// }

// const speciesArray = [ {speciesName:'shark', numTeeth:50}, {speciesName:'dog', numTeeth:42}, {speciesName:'alligator', numTeeth:80}, {speciesName:'human', numTeeth:32}];

// console.log(sortSpeciesByTeeth(speciesArray))

// function findMyKeys(arr) {
//   return arr.findIndex(item => item === 'keys')
// }
// const randomStuff = ['credit card', 'screwdriver', 'receipt', 'gum', 'keys', 'used gum', 'plastic spoon'];

// console.log(findMyKeys(randomStuff))

// function dogFactory(name, breed, weight) {
//   return {
//     _name: name,
//     _breed: breed,
//     _weight: weight,
//     get name() {
//       return this._name;
//     },
//     set name(newName) {
//       this._name = newName;
//     },
//     get breed() {
//       return this._breed;
//     },
//     set breed(newBreed) {
//       this._breed = newBreed;
//     },
//     get weight() {
//       return this._weight;
//     },
//     set weight(newWeight) {
//       this._weight = newWeight;
//     },
//     bark() {
//       return 'ruff! ruff!';
//     },
//     eatTooManyTreats() {
//       this._weight++;
//     },
//   };
// }

// const factorial = (n) => {
//   if (n < 0) {
//     return -1;
//   } else if (n == 0) {
//     return 1;
//   } else {
//     return n * factorial(n - 1);
//   }
// };
// console.log(factorial(5));

// const subLength = (str, char) => {
//   let charCount = 0;  // set charCount to 0
//   let len = -1;  // set len to -1 to account for 0 index of string 
//   for (let i = 0; i < str.length; i++) { // loop through string
//     if (str[i] === char) { // if character matches
//       charCount++; // increment charCount
//       if (charCount > 2) { // if charCount is greater than 2
//         return 0; // return 0
//       }
//       if (len === -1) { // if len is -1
//         len = i; // set len to i
//       } else {
//         len = i - len + 1; // set len to i - len + 1
//       }
//     }
//   } if (charCount < 2) { // if charCount is less than 2
//     return 0; // return 0
//   }
//   return len; // return len
// };
// console.log(subLength('Funny', 'n'));

const generateNumberSets = () => {
  const numberSets = [];

  for (let i = 0; i < 10; i++) {
    const numberSet = new Set();

    while (numberSet.size < 5) {
      const randomNumber = Math.floor(Math.random() * 70) + 1;
      numberSet.add(randomNumber);
    }

    const additionalNumber = Math.floor(Math.random() * 25) + 1;
    numberSet.add(additionalNumber);

    numberSets.push([...numberSet]);
  }

  return numberSets;
};

const sets = generateNumberSets();

for (let i = 0; i < sets.length; i++) {
  console.log(`Set ${i + 1}: ${sets[i].join(', ')}`);
}

// const groceries = (arr) => {
//   let str = ''; // empty string to add to
//   for (let i = 0; i < arr.length; i++) { // loop through array
//     str += arr[i].item; // add item to string
//     if (i < arr.length - 2) { // if not last item
//       str += ', '  // add comma
//     } else if (i === arr.length - 2) { // if second to last item
//       str += ' and ' // add and
//     }
//   }
//   return str;
// };
// groceries([
//   { item: 'Carrots' },
//   { item: 'Hummus' },
//   { item: 'Pesto' },
//   { item: 'Rigatoni' },
// ]);
// // returns 'Carrots, Hummus, Pesto and Rigatoni'

// console.log(groceries([{ item: 'Lettuce' }, { item: 'Onions' }, { item: 'Tomatoes' }]));
// // returns 'Bread and Butter'

// console.log(groceries([{ item: 'Cheese Balls' }]));
// // returns 'Cheese Balls'

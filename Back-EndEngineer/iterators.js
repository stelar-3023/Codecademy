// for each
const fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi', 'pear'];
fruits.forEach((fruit) => {
  console.log(`I want to eat a ${fruit}.`);
});

// map
const animals = [
  'Hen',
  'elephant',
  'llama',
  'leopard',
  'ostrich',
  'Whale',
  'octopus',
  'rabbit',
  'lion',
  'dog',
];
const secretMessage = animals.map((animal) => {
  return animal[0];
});
console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];
const smallNumbers = bigNumbers.map((number) => {
  return number / 100;
});
console.log(smallNumbers);

// filter
const randomNumbers = [375, 200, 3.14, 7, 13, 852];
const smallNumbers2 = randomNumbers.filter((number) => {
  return number < 250;
});
console.log(smallNumbers2);

const favoriteWords = [
  'nostalgia',
  'hyperbole',
  'fervent',
  'esoteric',
  'serene',
];
const longFavoriteWords = favoriteWords.filter((word) => {
  return word.length > 7;
});
console.log(longFavoriteWords);

// findIndex
const animals2 = [
  'hippo',
  'tiger',
  'lion',
  'seal',
  'cheetah',
  'monkey',
  'salamander',
  'elephant',
];
const foundAnimal = animals2.findIndex((animal) => {
  return animal === 'elephant';
});
const startsWithS = animals2.findIndex((animal) => {
  return animal[0] === 's';
});
console.log(foundAnimal);
console.log(startsWithS);


// reduce
const newNumbers = [1, 3, 5, 7];

const newSum = newNumbers.reduce((accumulator, currentValue) => {
  console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator + currentValue
}, 10)
console.log(newSum);

const cities = ['Orlando', 'Dubai', 'Edinburgh', 'Chennai', 'Accra', 'Denver', 'Eskisehir', 'Medellin', 'Yokohama'];

const nums = [1, 50, 75, 200, 350, 525, 1000];

//  Choose a method that will return undefined
cities.forEach(city => console.log('Have you visited ' + city + '?'));

// Choose a method that will return a new array
const longCities = cities.filter(city => city.length > 7);

// Choose a method that will return a single value
const word = cities.reduce((acc, currVal) => {
  return acc + currVal[0]
}, "C");

console.log(word)

// Choose a method that will return a new array
const smallerNums = nums.map(num => num - 5);

// Choose a method that will return a boolean value
nums.every(num => num < 0);
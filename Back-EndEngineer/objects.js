// let fasterShip = {
//   'Fuel Type': 'Turbo Fuel',
//   color: 'silver',
// };

// let spaceship = {
//   homePlanet: 'Earth',
//   color: 'silver',
//   'Fuel Type': 'Turbo Fuel',
//   numCrew: 5,
//   flightPath: ['Venus', 'Mars', 'Saturn']
// };

// let crewCount = spaceship.numCrew;
// console.log(crewCount);

// let planetArray = spaceship.flightPath;
// console.log(planetArray);

// let spaceship = {
//   'Fuel Type' : 'Turbo Fuel',
//   'Active Mission' : true,
//   homePlanet : 'Earth',
//   numCrew: 5
//  };

// let propName =  'Active Mission';

// let isActive = spaceship['Active Mission'];
// console.log(spaceship[propName]);

// let spaceship = {
//   'Fuel Type' : 'Turbo Fuel',
//   homePlanet : 'Earth',
//   color: 'silver',
//   'Secret Mission' : 'Discover life outside of Earth.'
// };

// // Write your code below
// spaceship.color = 'glorious gold'

// spaceship.numEngines = 10;

// delete spaceship['Secret Mission']

// let retreatMessage =
//   'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

// // Write your code below
// const alienShip = {
//   retreat() {
//     console.log(retreatMessage);
//   },
//   takeOff() {
//     console.log('Spim... Borp... Glix... Blastoff!');
//   },
// };
// alienShip.retreat();
// alienShip.takeOff();

// Nested Objects
// let spaceship = {
//   passengers: [
//     { name: 'Space Dog', age: 2 },
//     { name: 'Space Cat', age: 5 },
//   ],
//   telescope: {
//     yearBuilt: 2018,
//     model: '91031-XLT',
//     focalLength: 2032,
//   },
//   crew: {
//     captain: {
//       name: 'Sandra',
//       degree: 'Computer Engineering',
//       encourageTeam() {
//         console.log('We got this!');
//       },
//       'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'],
//     },
//   },
//   engine: {
//     model: 'Nimbus2000',
//   },
//   nanoelectronics: {
//     computer: {
//       terabytes: 100,
//       monitors: 'HD',
//     },
//     'back-up': {
//       battery: 'Lithium',
//       terabytes: 50,
//     },
//   },
// };
// let capFave = spaceship.crew.captain['favorite foods'][0];

// let firstPassenger = spaceship.passengers[0];

// Pass By Reference
// let spaceship = {
//   'Fuel Type' : 'Turbo Fuel',
//   homePlanet : 'Earth'
// };

// // Write your code below
// let greenEnergy = spaceship => {
//   spaceship['Fuel Type'] = 'avocado oil'
// }
// greenEnergy(spaceship);
// console.log(spaceship['Fuel Type'])

// let remotelyDisable = spaceship => {
//   spaceship.disabled = true
// }

// console.log(remotelyDisable(spaceship));
// console.log(spaceship.disabled);
// console.log(spaceship);

// Looping Through Objects
let spaceship = {
  crew: {
    captain: {
      name: 'Lily',
      degree: 'Computer Engineering',
      cheerTeam() {
        console.log('You got this!');
      },
    },
    'chief officer': {
      name: 'Dan',
      degree: 'Aerospace Engineering',
      agree() {
        console.log('I agree, captain!');
      },
    },
    medic: {
      name: 'Clementine',
      degree: 'Physics',
      announce() {
        console.log(`Jets on!`);
      },
    },
    translator: {
      name: 'Shauna',
      degree: 'Conservation Science',
      powerFuel() {
        console.log('The tank is full!');
      },
    },
  },
};

// // Write your code below
for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
}
for (let crewMember in spaceship.crew) {
  console.log(
    `${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`
  );
}
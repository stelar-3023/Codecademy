// const canIVote = (age) => {
//     if (age >= 18) {
//         return true
//     } else {
//         return false
//     }
// };
// console.log(canIVote(18));

// const agreeOrDisagree = (string1, string2) => {
//     if (string1 === string2) {
//         return "You agree!";
//     } else {
//         return "You disagree!";
//     }
// }
// console.log(agreeOrDisagree("yep", "yep"));

// const lifePhase = (age) => {
//     if (age < 0 || age > 140) {
//         return 'This is not a valid age'
//     }
//     if (age >= 0 && age <= 3) {
//         return 'baby';
//     } 
//     else if (age >= 4 && age <= 12) {
//         return 'child';
//     }
//     else if (age >= 13 && age <= 19) {
//         return 'teen';
//     }
//     else if (age >= 20 && age <= 64) {
//         return 'adult';
//     }
//     else {
//         return 'senior citizen';
//     }
// };
// console.log(lifePhase(141));

// const finalGrade = (midterm, final, homework) => {
//     if ((midterm < 0 || midterm > 100) || (final < 0 || final > 100) || (homework < 0 || homework > 100)) {
//         return 'You have entered an invalid grade.'
//     }
//     let average = (midterm + final + homework) / 3
//     if (average < 60) {
//         return 'F'
//     }
//     else if (average < 70) {
//         return 'D'
//     }
//     else if (average < 80) {
//         return 'C'
//     }
//     else if (average < 90) {
//         return 'B'
//     } else {
//         return 'A'
//     }
// }
// console.log(finalGrade(80,30,100));

// const reportingForDuty = (rank, lastName) => {
//     return `${rank} ${lastName} reporting for duty!`
// }
// console.log(reportingForDuty('Captain', 'Larsen'));

// const rollTheDice = () => {
//       // Math.random() gives us a random number from 0 up to, but not including, 1
//   // We multiplied that by 6 to get a number between 0 and up to, but not including, 6
//   // But since we actually wanted numbers from 1 to 6, inclusive, we added 1
//     let die1 = Math.floor(Math.random() * 6 + 1);
//     let die2 = Math.floor(Math.random() * 6 + 1);
//     return die1 + die2
// }
// console.log(rollTheDice());

// const calculateWeight = (earthWeight, planet) => {
//     if (planet === 'Mercury') {
//         return earthWeight * 0.378
//     }
//     else if (planet === 'Venus') {
//         return earthWeight * 0.907
//     }
//     else if (planet === 'Mars') {
//         return earthWeight * 0.377
//     }
//     else if (planet === 'Jupiter') {
//         return earthWeight * 2.36
//     }
//     else if (planet === 'Saturn') {
//         return earthWeight * 0.916
//     }
//     return 'Invalid Planet Entry. Try: Mercury, Venus, Mars, Jupiter, or Saturn.'
// }
// console.log(calculateWeight(100, "Jupiter"));

// const truthyOrFalsy = (value) => {
//     if (value) {
//         return true
//     }
//     return false
// }
// console.log(truthyOrFalsy(2));

// const numImaginaryFriends = (num1) => {
//     return Math.round(num1 * .33)
// }
// console.log(numImaginaryFriends(18));

// const sillySentence = (param1, param2, param3) => {
//     return `I am so ${param1} because I ${param2} coding! Time to write some more awesome ${param3}!`
// }
// console.log(sillySentence('excited', 'love', 'functions')) 

// const howOld =(age, year) => {
//     // The following 2 lines make it so the function always knows the current year
//     let dateToday = new Date();
//     let thisyear = dateToday.getFullYear();

//     const yearDifference = year - thisyear
//     const newAge = age + yearDifference

//     if(newAge < 0) {
//         return `The year ${year} was ${-newAge} years before you were born.`
//     }
//     else if (newAge > age) {
//         return `You will be ${newAge} in the year ${year}.`
//     }
//     else {
//         return `You were ${newAge} in the year ${year}.`
//     }
// }
// console.log(howOld(44, 1975));

// const whatRelation = percentSharedDNA => {
//     if (percentSharedDNA === 100) {
//         return 'You are likely identical twins.'
//     }
//     if (percentSharedDNA > 34) {
//         return 'You are likely parent and child or full siblings.'
//     }
//     if (percentSharedDNA > 13) {
//         return 'You are likely grandparent and grandchild, aunt/uncle and niece/nephew, or half siblings.'
//     }
//     if (percentSharedDNA > 5) {
//         return 'You are likely 1st cousins.'
//     }
//     if (percentSharedDNA > 2) {
//         return 'You are likely 2nd cousins.'
//     }
//     if (percentSharedDNA > 0) {
//         return 'You are likely 3rd cousins'
//     }
//     return 'You are likely not related.'
// }

// console.log(whatRelation(34))

// console.log(whatRelation(3))

// const tipCalculator = (quality, total) => {
//     if (quality === 'bad') {
//         return total * .05
//     }   
//     else if (quality === 'ok') {
//         return total * .15
//     }
//     else if (quality === 'good') {
//         return total * .20
//     }
//     else if (quality === 'excellent') {
//         return total * .30
//     }
//     else {
//         return total * .18
//     }
// }
// console.log(tipCalculator('good', 175));

// const toEmoticon = (word) => {
//     switch (word) {
//         case 'shrug':
//             return  '|_{"}_|';
//             break;
//         case 'smileyFace':
//             return ':)';
//             break;
//         case 'frownyFace':
//             return ':(';
//             break;
//         case 'winkyFace':
//             return ';)';
//             break;
//         case 'heart':
//             return '<3';
//             break;
//         default:
//             return '|_(* ~ *)_|';
//     }
// }
// console.log(toEmoticon('winkyFace'));
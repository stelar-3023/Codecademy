// const annoyingLongVariableName = () => {
//   for (let i = 0; i < 100; i++) {
//     console.log('why is this so hard to read?');
//   }
// }

// const shorter = annoyingLongVariableName;
// console.log(shorter.name); // annoyingLongVariableName
// shorter(); // why is this so hard to read? x100


const addTwo = (num) => num + 2;

const checkConsistentOutput = (func, val) => {
  const checkA = val + 2;
  const checkB = func(val);
  if (checkA === checkB) {
    return func(val);
  } else {
    return 'This function returned inconsistent results';
  }
};

console.log(checkConsistentOutput(addTwo, 2));

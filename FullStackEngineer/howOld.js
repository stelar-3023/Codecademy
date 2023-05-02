function howOld(age, year) {
  const currentYear = 2023;
  const yearDifference = year - currentYear;
  const newAge = age + yearDifference;
  if (newAge < 0) {
    return `The year ${year} was ${-newAge} years before you were born`;
  } else if (newAge > age) {
    return `You will be ${newAge} in the year ${year}`;
  } else {
    return `You were ${newAge} in the year ${year}`;
  }
}

console.log(howOld(48, 1974));
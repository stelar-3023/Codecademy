const getSleepHours = (day) => {
  if (day === "Sunday" || day === "Saturday") {
    return 8;
  }
  if (day === "Monday" || day === "Tuesday") {
    return 8;
  }
  if (day === "Wednesday" || day === "Thursday") {
    return 7;
  }
  if (day === "Friday") {
    return 6;
  }
};

const getActualSleepHours = () =>
  getSleepHours("Monday") +
  getSleepHours("Tuesday") +
  getSleepHours("Wednesday") +
  getSleepHours("Thursday") +
  getSleepHours("Friday") +
  getSleepHours("Saturday") +
  getSleepHours("Sunday");

const getIdealSleepHours = () => {
  const idealHours = 8;
  return idealHours * 7;
};

calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();

  if (actualSleepHours === idealSleepHours) {
    console.log("You got the perfect amount of sleep.");
  } else if (actualSleepHours > idealSleepHours) {
    console.log("You got more sleep than needed.");
  } else if (actualSleepHours < idealSleepHours) {
    console.log(
      "You got " +
        (idealSleepHours - actualSleepHours) +
        " hours(s) less sleep than you needed this week. You should get some more rest."
    );
  }
};

console.log(calculateSleepDebt());

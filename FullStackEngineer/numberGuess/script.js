let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => {
  return Math.floor(Math.random() * 10);
};

const compareGuesses = (humanGuess, computerGuess, target) => {
  if (Math.abs(humanGuess - target) < Math.abs(compputerGuess - target)) {
    return true;
  } else if (Math.abs(computerGuess - target) < Math.abs(humanGuess - target)) {
    return false;
  } else {
    return true;
  }
};

const updateScore = (winner) => {
  if (winner === "human") {
    return humanScore++;
  } else {
    return computerScore++;
  }
};

const advanceRound = () => {
  currentRoundNumber++;
};

const team = {
  _players: [
    {
      firstName: 'Michael',
      lastName: 'Jordan',
      age: 21,
    },
    {
      firstName: 'Kobe',
      lastName: 'Bryant',
      age: 22,
    },
    {
      firstName: 'Lebron',
      lastName: 'James',
      age: 23,
    },
  ],
  _games: [
    {
      opponent: 'Lakers',
      teamPoints: 100,
      opponentPoints: 98,
    },
    {
      opponent: 'Celtics',
      teamPoints: 110,
      opponentPoints: 105,
    },
    {
      opponent: 'Warriors',
      teamPoints: 120,
      opponentPoints: 115,
    },
  ],
  get players() {
    return this._players;
  },
  get games() {
    return this._games;
  },
  addPlayer(newFirstName, newLastName, newAge) {
    const player = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge,
    };
    this._players.push(player);
  },
  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    const game = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints,
    };
  },
};
team.addPlayer('Steph', 'Curry', 28);
team.addGame('Rockets', 115, 110);
console.log(team.players);
console.log(team.games);

// Create an empty class named Surgeon
class Surgeon {
  // Inside the Surgeon class, create a constructor() method that accepts two parameters: name and department
  constructor(name, department) {
    this._name = name;
    this._department = department;
    this._remainingVacationDays = 20;
  }
  // create a getter called name that returns the value saved to _name
  get name() {
    return this._name;
  }
  // create a getter called department that returns the value saved to _department
  get department() {
    return this._department;
  }
  // create a getter called remainingVacationDays that returns the value saved to _remainingVacationDays
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  // Inside the Surgeon class, create a method called takeVacationDays that accepts one argument named daysOff
  takeVacationDays(daysOff) {
    // Inside the method, subtract daysOff from the number saved to _remainingVacationDays
    this._remainingVacationDays -= daysOff;
  }
} // class declaration

//  Create an instance of the Surgeon class — set the name to 'Francisco Romero' and department to 'Cardiovascular'.

// Save the instance to a constant variable called surgeonRomero
const surgeonRomero = new Surgeon('Francisco Romero', 'Cardiovascular');

// Create an instance of the Surgeon class — set the name to 'Ruth Jackson' and department to 'Orthopedics'.

// Save the instance to a constant variable called surgeonJackson.
const surgeonJackson = new Surgeon('Ruth Jackson', 'Orthopedics');

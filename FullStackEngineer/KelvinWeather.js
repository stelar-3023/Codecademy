// set variable kelvin = 293
const kelvin = 293;
// set variable celsius
const celsius = kelvin - 273;
// set variable fahrenheit
let fahrenheit = celsius * (9 / 5) + 32;
// round down fahrenheit temperature
fahrenheit = Math.floor(fahrenheit);
// string interpolation
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);
// Convert to Newton
let newton = celsius * (33 / 100);
// Round down
newton = Math.floor(newton);
console.log(`The temperature is ${newton} degrees Newton.`);

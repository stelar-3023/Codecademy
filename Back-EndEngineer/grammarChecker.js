let story =
  'Last weekend, I took literally the most beautifull bike ride of my life. The route is called "The 9W to Nyack" and it stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it literally took me an entire day. I stopped at Riverbank State Park to take some artsy photos. It was a short stop, though, because I had a freaking long way to go. After a quick photo op at the very popular Little Red Lighthouse I began my trek across the George Washington Bridge into New Jersey. The GW is a breathtaking 4,760 feet long! I was already very tired by the time I got to the other side. An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautifull park along the coast of the Hudson. Something that was very surprising to me was that near the end of the route you literally cross back into New York! At this point, you are very close to the end.';

// story into an array
let storyWords = story.split(' ');
// console.log(storyWords)

let unnecessaryWord = 'literally';
let misspelledWord = 'beautifull';
let badWord = 'freaking';

let count = 0;

//  filter out unnecessary words
storyWords = storyWords.filter((word) => {
  return word !== unnecessaryWord;
});

storyWords.forEach((word) => {
  count++;
});
console.log(`There are ${count} words in the story`);

//  spell check using map
let spellCheckedWords = storyWords.map((word) => {
  if (word === misspelledWord) {
    return 'beautiful';
  } else {
    return word;
  }
});
// console.log(spellCheckedWords);

//  check for bad words
let badWordIndex = spellCheckedWords.findIndex((word) => {
  return word === badWord;
});
console.log(badWordIndex);

spellCheckedWords[78] = 'really'; //  replace bad word with
console.log(spellCheckedWords);

let lengthCheck = spellCheckedWords.every((word) => {
  return word.length <= 10;
});
console.log(lengthCheck);

spellCheckedWords.forEach((word) => {
  if(word.length > 10) {
    console.log(word);
    // index
    console.log(spellCheckedWords.indexOf(word));
  }})

spellCheckedWords[111] = 'stunning';


//  change spellCheckedWords back into a string
let finalStory = spellCheckedWords.join(' ');
console.log(finalStory);

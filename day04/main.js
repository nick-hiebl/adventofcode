const { toInt } = require("../utils");

const print = (...arguments) => {
  console.log(...arguments);
};

const lines = ``.split('\n').filter(t => !!t);

let total = 0;

const matches = [];
let cards = [];

// BODY
for (const line of lines) {
  const data = line.split(': ')[1];

  const [winners, have] = data.split(' | ').filter(t => !!t).map(t => t.split(' ').filter(t => !!t).map(toInt));
  print(winners, have);

  let score = 0;
  let ms = 0;
  for (const num of have) {
    if (winners.includes(num)) {
      ms += 1;
      if (score === 0) { score = 1; }
      else { score *= 2; }
    }
  }
  matches.push(ms);

  // total += score;
  print(score);
  cards.push(1);
}

for (let i = 0; i< matches.length; i++) {
  const ms = matches[i];
  const copies = cards[i];
  for (let j = 0; j < ms; j++) {
    cards[i + j + 1] += copies || 1;
  }

  if (copies && ms) {
    // total += 
  }
}

for (let i = 0; i < cards.length; i++) {
  if (matches[i]) {
    total += Math.pow(2, matches[i] - 1) * cards[i];
  }
}

console.log(cards);
console.log(matches);

// POST-BODY

console.log('pt 2 answer', cards.reduce((a,b)=>a+b,0))

// print(symbols);
print(total);

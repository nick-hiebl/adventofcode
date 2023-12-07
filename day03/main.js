const { toInt } = require("../utils");

const print = (...arguments) => {
  console.log(...arguments);
};

const lines = ``.split('\n').filter(t => !!t);

let total = 0;

const symbols = [];

// BODY
for (let r = 0; r < lines.length; r++) {
  const symbolRow = [];
  for (let c = 0; c < lines[r].length; c++) {
    if (!'0123456789.'.includes(lines[r][c])) {
      symbolRow.push({ c: c, char: lines[r][c], nums: [] });
    }
  }
  symbols.push(symbolRow);
}

for (let r = 0; r < lines.length; r++) {
  for (let c = 0; c < lines[r].length; c++) {
    if ('0123456789'.includes(lines[r][c])) {
      const [digits] = /\d+/.exec(lines[r].slice(c));
      const number = toInt(digits);

      print(digits, r, c);
      let rows = [symbols[r - 1], symbols[r], symbols[r + 1]].filter(t => !!t).flat();
      const left = c - 1, right = c + digits.length;

      for (const symbol of rows) {
        if (symbol.char !== '*') {
          continue;
        }
        if (left <= symbol.c && symbol.c <= right) {
          symbol.nums.push(number);
        }
      }

      // if (rows.some(row => row.some(sym => left <= sym.c && sym <= right))) {
      //   total += number;
      //   print('Found symbol:', number);
      // } else {
      //   print('Bad symbol:', number);
      // }
      c += digits.length;
    }
  }
}
// POST-BODY

total = 0;

for (const symbol of symbols.flat()) {
  if (symbol.char === '*') {
    print(symbol);
    if (symbol.nums.length === 2) {
      total += symbol.nums.reduce((a, b) => a * b, 1);
    }
  }
}

// print(symbols);
print(total);

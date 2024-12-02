const { toInt } = require("../utils");

const lines = `<INPUT>`.split('\n').filter(t => !!t);

let invalidGames = 0;

const MAX_RED = 12;
const MAX_GREEN = 13;
const MAX_BLUE = 14;

for (const line of lines) {
  const [id, games] = line.split(': ');
  const [_, gameId] = id.split(' ');
  const gId = toInt(gameId);
  // console.log(gId, '---', line);

  const gameSegs = games.split('; ');

  let possible = true;

  let lowRed = 0;
  let lowGreen = 0;
  let lowBlue = 0;

  for (const seg of gameSegs) {
    const balls = seg.split(', ');
    let g = 0, r = 0, b = 0;
    for (const ballC of balls) {
      const [c, col] = ballC.split(' ');
      if (col === 'red') {
        r += toInt(c);
      } else if (col === 'green') {
        g += toInt(c);
      } else if (col === 'blue') {
        b += toInt(c);
      }
    }
    // if (g > MAX_GREEN || r > MAX_RED || b > MAX_BLUE) {
    //   possible = false;
    //   console.log('Invalid because:', seg);
    //   break;
    // }
    lowRed = Math.max(lowRed, r);
    lowGreen = Math.max(lowGreen, g);
    lowBlue = Math.max(lowBlue, b);
  }

  // if (possible) {
  //   console.log('>>', gId, line);
  //   invalidGames += gId;
  // }
  invalidGames += lowRed * lowGreen * lowBlue;

}

console.log(invalidGames);
// console.log(inp.reduce((a,b) => a+b, 0));

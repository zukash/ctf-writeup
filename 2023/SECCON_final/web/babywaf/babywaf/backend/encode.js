function toUnicodeEscape(str) {
  return Array.from(str)
    .map((char) => {
      const charCode = char.charCodeAt(0);
      const highSurrogate = charCode >= 0xd800 && charCode <= 0xdbff;
      if (highSurrogate) {
        const high = charCode.toString(16);
        const low = char.codePointAt(1).toString(16);
        return `\\u00${high}\\u00${low}`;
      } else {
        return `\\u00${charCode.toString(16)}`;
      }
    })
    .join("");
}

const emoji = "()";
// const emoji = "givemeflag";
// const emoji = '"';
const unicodeEscape = toUnicodeEscape(emoji);

console.log(emoji);
console.log(unicodeEscape); // 出力: \ud83d\udc4d

const CryptoJS = require("crypto-js");

// async function getFlag() {
//   const flag = [
//     0x45, 0x00, 0x50, 0x39, 0x08, 0x6f, 0x4d, 0x5b, 0x58, 0x06, 0x66, 0x40,
//     0x58, 0x4c, 0x6d, 0x5d, 0x16, 0x6e, 0x4f, 0x00, 0x43, 0x6b, 0x47, 0x0a,
//     0x44, 0x5a, 0x5b, 0x5f, 0x51, 0x66, 0x50, 0x57,
//   ];
//   const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
//   const resp = await fetch(
//     "https://timeapi.io/api/time/current/zone?timeZone=" + tz
//   );
//   const date = await resp.json();
//   const base = date.timeZone + "-" + date.date + "-" + date.time;
//   var hash = CryptoJS.MD5(base).toString();

//   const result = flag
//     .map((x, i) => String.fromCharCode(x ^ hash.charCodeAt(i)))
//     .join("");
//   document.querySelector("span").innerText = result;

//   document.getElementsByClassName("ready")[0].style.display = "block";
//   document.getElementsByClassName("loading")[0].style.display = "none";
// }

// {"year":2025,"month":4,"day":12,"hour":0,"minute":55,"seconds":31,"milliSeconds":390,"dateTime":"2025-04-12T00:55:31.3906051","date":"04/12/2025","time":"00:55","timeZone":"UTC","dayOfWeek":"Saturday","dstActive":false}

function getFlag() {
  const flag = [
    0x45, 0x00, 0x50, 0x39, 0x08, 0x6f, 0x4d, 0x5b, 0x58, 0x06, 0x66, 0x40,
    0x58, 0x4c, 0x6d, 0x5d, 0x16, 0x6e, 0x4f, 0x00, 0x43, 0x6b, 0x47, 0x0a,
    0x44, 0x5a, 0x5b, 0x5f, 0x51, 0x66, 0x50, 0x57,
  ];
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
  const date = {
    year: 2025,
    month: 4,
    day: 12,
    hour: 0,
    minute: 55,
    seconds: 31,
    milliSeconds: 390,
    dateTime: "2025-04-12T00:55:31.3906051",
    date: "04/12/2025",
    time: "00:55",
    timeZone: "UTC",
    dayOfWeek: "Saturday",
    dstActive: false,
  };
  const base = date.timeZone + "-" + date.date + "-" + date.time;
  console.log(base);
  var hash = CryptoJS.MD5(base).toString();

  const result = flag
    .map((x, i) => String.fromCharCode(x ^ hash.charCodeAt(i)))
    .join("");
  console.log(result);
  return result;
}

function decrypto(timeZone, date, time) {
  const flag = [
    0x45, 0x00, 0x50, 0x39, 0x08, 0x6f, 0x4d, 0x5b, 0x58, 0x06, 0x66, 0x40,
    0x58, 0x4c, 0x6d, 0x5d, 0x16, 0x6e, 0x4f, 0x00, 0x43, 0x6b, 0x47, 0x0a,
    0x44, 0x5a, 0x5b, 0x5f, 0x51, 0x66, 0x50, 0x57,
  ];
  const base = timeZone + "-" + date + "-" + time;
  var hash = CryptoJS.MD5(base).toString();

  const result = flag
    .map((x, i) => String.fromCharCode(x ^ hash.charCodeAt(i)))
    .join("");

  console.log(result);
}

const timeZones = Intl.supportedValuesOf("timeZone");

// for (let tz of timeZones) {
//   if (tz === "Europe/Warsaw") console.log(tz);
// }

// const timeZones = [];
// timeZones.push("UTC");
// timeZones.push("Europe/Warsaw");
for (let tz of timeZones) {
  for (let month = 1; month < 4; month++) {
    for (let day = 1; day < 32; day++) {
      for (let hh = 0; hh < 24; hh++) {
        for (let mm = 0; mm < 60; mm++) {
          const date = `${String(month).padStart(2, "0")}/${String(
            day
          ).padStart(2, "0")}/2025`;

          const time = `${String(hh).padStart(2, "0")}:${String(mm).padStart(
            2,
            "0"
          )}`;
          // console.log(tz, date, time);
          decrypto(tz, date, time);
        }
      }
    }
  }
}

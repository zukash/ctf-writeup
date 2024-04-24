const url = "http://localhost:3000/flag";

async function fetchData() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
}

try {
  const result = fetchData();
  result;
  console.log("同期的なfetchの結果:", result);
} catch (error) {
  console.error("エラーが発生しました:", error);
}

// // HTTPリクエストを構築
// fetch(url, { method: "GET", headers: { "X-Flag": "any" } })
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }
//     return response.json();
//   })
//   .then((data) => {
//     // レスポンスデータを処理
//     console.log(data);
//   })
//   .catch((error) => {
//     // エラーハンドリング
//     console.error("There was a problem with the fetch operation:", error);
//   });

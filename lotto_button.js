var lotto = [];
const URL =
  "https://skp7t6j64m.execute-api.ap-northeast-2.amazonaws.com/2021-11-24/lotto";
function get() {
  fetch(URL, {
    headers: {
      Accept: "application/json",
    },
  })
    .then((res) => res.json())
    .then((res) => {
      lotto[0] = res.n1;
      lotto[1] = res.n2;
      lotto[2] = res.n3;
      lotto[3] = res.n4;
      lotto[4] = res.n5;
      lotto[5] = res.n6;
    });
}

get();

function lottoGen() {
  get();
  console.log("lotto : " + lotto);
  var html = "<tr>";
  html += "<td>";
  html += lotto + "<br/>";
  html += "</td>";
  html += "</tr>";
  $("#lotto_table").find("tbody").prepend(html);
}

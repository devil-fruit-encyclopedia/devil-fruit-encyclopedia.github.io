let result = "";
fetch("./frontEndData1.json")
  .then(function (response) {
    return response.json();
  })
  .then(function (data1) {
    appendData(data1);
  })
  .catch(function (err) {
    console.log("error: " + err);
  });
function appendData(data1) {
  data1.forEach(({ Name, Japanese_Name, Type, image, Description, wiki } = rows) => {
    result += `
        <div class="card">
        <h2 class="card-name">${Name}</h2>
        <h2 class="card-name">${Japanese_Name}</h2>
        <img class="card-image" src="${image}" alt="Image of the ${Name}"/>
        <p class="card-link"><div class="dropdown"><span>▼</span><div class="dropdown-content"><p>${Description}<br><br>
        <a class="card-link" href="${wiki}"><button class="btn">Read More</button></a></p></div></div></p>
        </div>
        `;
  });
  document.querySelector(".container").innerHTML = result;
}
if ("serviceworker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceworker
        .register("js/serviceworker.js")
        .then((res) => console.log("service worker registered"))
        .catch((err) => console.log("service worker not registered", err));
    });
  }
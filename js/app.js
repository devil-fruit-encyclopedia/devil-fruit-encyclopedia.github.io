let result = "";
fetch("./frontEndData.json")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    appendData(data);
  })
  .catch(function (err) {
    console.log("error: " + err);
  });
function appendData(data) {
  data.forEach(({ extID, Name, Japanese_Name, Type, image, User, Description, wiki, Use } = rows) => {
    result += `
        <div class="card">
        <h3 class="card-about">${extID}. ${Type}</h3>
        <img class="card-image" src="${image}" alt="Image of the ${Name}"/> 
        <h2 class="card-name">${Name}</h2>
        <h2 class="card-name">${Japanese_Name}</h2>
        <p class="card-link"><div class="dropdown"><span>▼</span><div class="dropdown-content"><p>${Description}<br><br>User: ${Use}<br><br><img class="card-image" src="${User}" alt="Image depicting ${Use}"/><br><br> 
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
function getWeather() {
    const city = document.getElementById("city").value;
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("weather-data").innerHTML = `
                <h2>${data.city}</h2>
                <p>Temperature: ${data.temp}°C</p>
                <p>Weather: ${data.weather}</p>
            `;
        })
        .catch(error => console.log(error));
}
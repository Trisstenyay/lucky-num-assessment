/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault();
    // Get the form values
    const name = document.querySelector("#name").value;
    const year = document.querySelector("#year").value;
    const email = document.querySelector("#email").value;
    const color = document.querySelector("#color").value;
  
    // Create a JSON object
    const data = { name, year, email, color };

    try {
        // Send a POST request to the server
        const response = await fetch("/api/get-lucky-num", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });



        // Parse the JSON response
        const result = await response.json();
    
        // Handle the response (e.g., display lucky number or errors)
        console.log(result);
    
        // Optionally, display results on the page
        const resultsDiv = document.querySelector("#lucky-results");
        resultsDiv.innerHTML = `Your lucky number is ${result.num.num}. <br>${result.num.message}. <br> Your birth year ${result.year.year} fact is ${result.year.message}.`

      } catch (err) {
        console.error("Error:", err);
        const errorTag = document.getElementById("name-err");
        errorTag.textContent = err;
      }
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
}


$("#lucky-form").on("submit", processForm);
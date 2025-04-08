document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const priceFilter = document.getElementById('price-filter');
    const loginLink = document.getElementById('login-link');
    const placesList = document.getElementById('places-list');


    if (placesList) {
        placesList.style.display = 'none'; // Ensure it's hidden when the page loads
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            await loginUser(email, password);
        });
    }


    // Check user authentication on page load
    checkAuthentication(loginLink, placesList);


    // Set up the price filter dropdown
    if (priceFilter) {
        priceFilter.innerHTML = `
            <option value="10">10</option>
            <option value="50">50</option>
            <option value="100">100</option>
            <option value="All">All</option>
        `;
        
        priceFilter.addEventListener('change', (event) => {
            const selectedPrice = event.target.value;
            filterPlacesByPrice(selectedPrice);
        });
    }
});


// Helper function to get a cookie value by name
function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
}


// Function to check if the user is authenticated
function checkAuthentication(loginLink, placesList) {
    const token = getCookie('token');


    if (!token) {
        loginLink.style.display = 'block'; // Show the login link if no token
        if (placesList) {
            placesList.style.display = 'none'; // Ensure places list is hidden before login
        }
    } else {
        loginLink.style.display = 'none'; // Hide the login link if the token exists
        if (placesList) {
            placesList.style.display = 'flex'; // Show places list after authentication
        }
        fetchPlaces(token); // Fetch places if the user is authenticated
    }
}


// Function to log in the user
async function loginUser(email, password) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });


        if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html'; // Reload the page after login
        } else {
            const errorData = await response.json();
            alert('Login failed: ' + errorData.error);
        }
    } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred. Please try again.');
    }
}


// Function to fetch places data from the API
async function fetchPlaces(token) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`, // Include JWT token for authorization
                'Content-Type': 'application/json'
            }
        });


        if (response.ok) {
            const places = await response.json();
            displayPlaces(places); // Display places if fetch is successful
        } else {
            console.error('Failed to fetch places data');
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}


// Function to display places in the DOM
function displayPlaces(places) {
    const placesList = document.querySelector('#places-list');


    // Clear the list before displaying new places
    placesList.innerHTML = ''; // Clear out any previous content


    if (places.length === 0) {
        placesList.innerHTML = '<p>No places available</p>';
        return;
    }


    // Create the ul element to hold the list of places
    const list = document.createElement('ul');
    list.classList.add('place-list');


    places.forEach(place => {
        const li = document.createElement('li');
        li.classList.add('place-card');


        li.innerHTML = `
            <h2>${place.title || 'No title available'}</h2>
            <p>Price per night: $${place.price || 'N/A'}</p>
            <button class="details-button">View Details</button>
        `;
        list.appendChild(li); // Append each li to the ul
    });


    // Append the ul to the places-list section
    placesList.appendChild(list);
}


// Function to filter places by price
function filterPlacesByPrice(selectedPrice) {
    const placesList = document.querySelector('#places-list');
    const placeCards = Array.from(placesList.getElementsByClassName('place-card'));


    placeCards.forEach(place => {
        const priceText = place.querySelector('p').textContent;
        const price = parseInt(priceText.replace('Price per night: $', '').trim());

        if (selectedPrice === 'All' || price <= selectedPrice) {
            place.style.display = 'flex'; // Show the place if it meets the filter criteria
        } else {
            place.style.display = 'none'; // Hide the place if it doesn't meet the filter criteria
        }
    });
}

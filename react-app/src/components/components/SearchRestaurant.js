import React, { useState } from "react";
import './SearchRestaurant.css'; // New CSS file

const SearchRestaurant = () => {
  const [location, setLocation] = useState("");
  const [restaurants, setRestaurants] = useState([]);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    setError("");
    setRestaurants([]);

    if (!location.trim()) {
      alert("Please enter a valid location.");
      return;
    }

    try {
      const response = await fetch(
        `https://api.yelp.com/v3/businesses/search?location=${location}&sort_by=best_match&limit=40`,
        {
          method: "GET",
          headers: {
            accept: "application/json",
            Authorization: "Bearer M2Jfn4iG0Nq_AFKYEfJFVny4q4Hed6qFjKwUWAQwWp_h7bya8bfGSQ-YoT3lrorG2vchpvmyAti88NgLIl4qvjoW4ujh7lm8FIDuIELG-WSpLhTAXlLEmRLNeOVEZ3Yx",
          },
        }
      );

      if (!response.ok) {
        setError("Failed to fetch restaurants. Please try again.");
        return;
      }

      const data = await response.json();
      const fetchedRestaurants = data.businesses;

      if (fetchedRestaurants.length === 0) {
        setError("No restaurants found in this location.");
        return;
      }

      setRestaurants(fetchedRestaurants);
    } catch (error) {
      console.error("Error fetching restaurants:", error);
      setError("Error fetching restaurants. Please try again.");
    }
  };

  return (
    <div className="search-container">
      <div className="search-header">Search Restaurants by Location</div>
      <div className="input-container">
        <input
          type="text"
          placeholder="Enter location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div className="restaurant-list">
        {restaurants.map((restaurant) => (
          <div key={restaurant.id} className="restaurant-card">
            <img
              src={restaurant.image_url || "https://via.placeholder.com/250"}
              alt={restaurant.name}
              onError={(e) =>
                (e.currentTarget.src = "https://via.placeholder.com/250")
              }
            />
            <div className="restaurant-card-body">
              <a
                href={restaurant.url}
                target="_blank"
                rel="noopener noreferrer"
                className="restaurant-name"
              >
                {restaurant.name}
              </a>
              <div className="restaurant-details">
                {restaurant.categories
                  .map((category) => category.title)
                  .join(", ") || "Cuisine not specified"}
              </div>
              <div className="restaurant-details">
                {restaurant.location.display_address.join(", ")}
              </div>
              <div className="restaurant-rating">
                Rating: {restaurant.rating} ★ | {restaurant.review_count} reviews
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SearchRestaurant;
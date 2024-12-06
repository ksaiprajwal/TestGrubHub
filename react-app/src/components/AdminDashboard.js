import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllBusinessesThunk } from '../store/business';
import './Businesses/BusinessCard/BusinessCard.css'; // Reuse BusinessCard styles

const AdminDashboard = () => {
  const dispatch = useDispatch();
  const businesses = useSelector(state => state.businesses.allBusinesses);
  const [searchQuery, setSearchQuery] = useState('');
  const [filteredBusinesses, setFilteredBusinesses] = useState([]);
  const [showDuplicates, setShowDuplicates] = useState(false);

  useEffect(() => {
    dispatch(getAllBusinessesThunk());
  }, [dispatch]);

  useEffect(() => {
    if (searchQuery) {
      const filtered = Object.values(businesses).filter((business) =>
        business.business_name.toLowerCase().includes(searchQuery.toLowerCase())
      );
      setFilteredBusinesses(filtered);
    } else {
      setFilteredBusinesses(Object.values(businesses));
    }
  }, [searchQuery, businesses]);

  const handleDelete = async (businessId) => {
    try {
      const response = await fetch(`/api/businesses/${businessId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await response.json();

      if (response.ok) {
        alert('Business deleted successfully');
        dispatch(getAllBusinessesThunk()); // Refresh the list
      } else {
        alert(`Error: ${data.message}`);
      }
    } catch (error) {
      console.error('Failed to delete the business:', error);
      alert('An unexpected error occurred.');
    }
  };

  const findDuplicates = () => {
    const duplicateMap = {};
    const duplicates = [];

    Object.values(businesses).forEach((business) => {
      const key = `${business.business_name}-${business.address}`;
      if (duplicateMap[key]) {
        duplicateMap[key].push(business);
      } else {
        duplicateMap[key] = [business];
      }
    });

    Object.values(duplicateMap).forEach((group) => {
      if (group.length > 1) {
        duplicates.push(...group);
      }
    });

    setFilteredBusinesses(duplicates);
    setShowDuplicates(true);
  };

  const imageOnErrorHandler = (event) => {
    event.currentTarget.src = 'https://via.placeholder.com/250'; // Placeholder for missing images
  };

  if (!businesses) {
    return <p>Loading businesses...</p>;
  }

  return (
    <div id="center-div-container">
      <h1 style={{ textAlign: 'center', margin: '20px 0' }}>Admin Dashboard</h1>
      
      {/* Search Bar and Duplicates Button */}
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Search businesses by name"
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            setShowDuplicates(false); // Reset duplicates view when searching
          }}
          style={{
            padding: '10px',
            width: '70%',
            borderRadius: '5px',
            border: '1px solid lightgray',
            fontSize: '16px',
          }}
        />
        <button
          onClick={findDuplicates}
          style={{
            marginLeft: '10px',
            padding: '10px 20px',
            borderRadius: '5px',
            border: 'none',
            backgroundColor: '#007BFF',
            color: 'white',
            cursor: 'pointer',
          }}
        >
          Duplicates
        </button>
      </div>

      <div id="middle-div-list-container">
        {filteredBusinesses.map((business) => (
          <div id="business-card-container" key={business.id}>
            <div id="business-card-img-div">
              <img
                id="business-card-image"
                alt={business.business_name}
                src={business.images?.url || 'https://via.placeholder.com/250'}
                onError={imageOnErrorHandler}
              />
            </div>
            <div id="business-card-text-container">
              <div id="business-card-business-name">{business.business_name}</div>
              <div>{business.city}</div>
              <div>{business.state}</div>
              <div>{business.address}</div>
              <div>{business.about}</div>
              <div>
                <span>
                  {business.price_range ? `$${'$'.repeat(business.price_range)}` : 'N/A'}
                </span>
              </div>
              <button
                style={{
                  marginTop: '10px',
                  padding: '8px 12px',
                  backgroundColor: '#FF5733',
                  color: 'white',
                  border: 'none',
                  borderRadius: '5px',
                  cursor: 'pointer',
                }}
                onClick={() => handleDelete(business.id)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
        {filteredBusinesses.length === 0 && (
          <p style={{ textAlign: 'center', marginTop: '20px' }}>
            {showDuplicates ? 'No duplicate businesses found' : 'No businesses found'}
          </p>
        )}
      </div>
    </div>
  );
};

export default AdminDashboard;
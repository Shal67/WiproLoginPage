import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import { deleteDB } from 'idb';


const Header = () => {
  const { user, logoutUser } = useContext(AuthContext);

  const handleLogout = async () => {
    await logoutUser();
    await deleteIndexedDB();
  };

  const deleteIndexedDB = async () => {
    await deleteDB('Alpine'); // Replace 'Alpine' with your actual database name
    console.log('IndexedDB deleted');
  };

  return (
    <div>
      <Link to="/">Home</Link>
      <span> | </span>
      {user ? (
        <button onClick={handleLogout} >
          Logout
        </button>
      ) : (
        <Link to="/login">Login</Link>
      )}

      {user && <p>Hello {user.username}</p>}
    </div>
  );
};

export default Header;
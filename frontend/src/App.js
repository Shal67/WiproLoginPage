
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import PrivateRoute from './utils/PrivateRoute'
import { AuthProvider } from './context/AuthContext';
import SignUp from './pages/SignUp';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
        <Header>
          </Header>
          <Routes>
            {/* Use PrivateRoute for the protected route */}
           <Route element={<PrivateRoute/>}>

                    <Route element={<HomePage/>} path='/'exact/>

                    </Route>
                               <Route path="/signup" element={<SignUp/>} />
            {/* Use Route for the public route */}
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
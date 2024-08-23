import jwt_decode from "jwt-decode"
import { useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

function Navbar() {
  // Extract user and logoutUser from AuthContext.
  const {user, logoutUser} = useContext(AuthContext)

  // Retrieve the authentication token from local storage.
  const token = localStorage.getItem("authTokens")

  // Decode the token if it exists to get the user ID.
  if (token){
    const decoded = jwt_decode(token) 
    var user_id = decoded.user_id // Consider using let or const for variable declaration.
  }

  return (
    <div>
        <nav className="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            <img style={{width:"90px", padding:"6px"}} src="https://img.freepik.com/free-vector/bird-colorful-logo-gradient-vector_343694-1365.jpg?t=st=1724267866~exp=1724271466~hmac=ad3408b6aa62a3ca3657233ae81099962bc409817e8330be6eefcf40d8ba7b9b&w=740" alt="" />

          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#"> <i className='fas fa-home'></i> Home</a>
              </li>
              {token === null && 
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/login"><i className='fas fa-sign-in-alt'></i> Login</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/register"><i className='fas fa-user-plus'></i> Register</Link>
                </li>
              </>
              }

            {token !== null && 
              <>
                <li className="nav-item">
                  <Link className="nav-link" to="/todo"> <i className='fas fa-pen'></i> Todo</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/inbox"> <i className='fas fa-envelope'></i> Inbox</Link>
                </li>
                <li className="nav-item">
                  <a className="nav-link" onClick={logoutUser} style={{cursor:"pointer"}}> <i className='fas fa-sign-out-alt'></i>Logout</a>
                </li>
              </>
              }   
              
            </ul>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar
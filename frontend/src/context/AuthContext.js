import jwt_decode from "jwt-decode";
import { createContext, useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
const swal = require('sweetalert2')

// Create a context for authentication
const AuthContext = createContext();

export default AuthContext;

// AuthProvider component to provide authentication context to the app
export const AuthProvider = ({ children }) => {
    // State to store authentication tokens
    const [authTokens, setAuthTokens] = useState(() =>
        localStorage.getItem("authTokens")
            ? JSON.parse(localStorage.getItem("authTokens"))
            : null
    );
    
    // State to store the decoded user info from tokens
    const [user, setUser] = useState(() => 
        localStorage.getItem("authTokens")
            ? jwt_decode(localStorage.getItem("authTokens"))
            : null
    );

    // State to manage loading status
    const [loading, setLoading] = useState(true);

    // Hook to programmatically navigate
    const history = useHistory();

    // Function to log in a user
    const loginUser = async (email, password) => {
        // Send login request to the API
        const response = await fetch("http://127.0.0.1:8000/api/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, password })
        });

        // Parse response data
        const data = await response.json();
        console.log(data);

        if (response.status === 200) {
            // Successfully logged in
            console.log("Logged In");
            setAuthTokens(data);
            setUser(jwt_decode(data.access));
            localStorage.setItem("authTokens", JSON.stringify(data));
            history.push("/");
            swal.fire({
                title: "Login Successful",
                icon: "success",
                toast: true,
                timer: 6000,
                position: 'top-right',
                timerProgressBar: true,
                showConfirmButton: false,
                showCancelButton: true,
            });
        } else {
            // Login failed
            console.log(response.status);
            console.log("there was a server issue");
            swal.fire({
                title: "Username or password does not exist",
                icon: "error",
                toast: true,
                timer: 6000,
                position: 'top-right',
                timerProgressBar: true,
                showConfirmButton: false,
                showCancelButton: true,
            });
        }
    };

    // Function to register a new user
    const registerUser = async (email, username, password, password2) => {
        // Send registration request to the API
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, username, password, password2 })
        });

        if (response.status === 201) {
            // Registration successful
            history.push("/login");
            swal.fire({
                title: "Registration Successful, Login Now",
                icon: "success",
                toast: true,
                timer: 6000,
                position: 'top-right',
                timerProgressBar: true,
                showConfirmButton: false,
                showCancelButton: true,
            });
        } else {
            // Registration failed
            console.log(response.status);
            console.log("there was a server issue");
            swal.fire({
                title: "An Error Occurred " + response.status,
                icon: "error",
                toast: true,
                timer: 6000,
                position: 'top-right',
                timerProgressBar: true,
                showConfirmButton: false,
                showCancelButton: true,
            });
        }
    };

    // Function to log out the user
    const logoutUser = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem("authTokens");
        history.push("/login");
        swal.fire({
            title: "You have been logged out...",
            icon: "success",
            toast: true,
            timer: 6000,
            position: 'top-right',
            timerProgressBar: true,
            showConfirmButton: false,
            showCancelButton: true,
        });
    };

    // Context data to be provided to components
    const contextData = {
        user,
        setUser,
        authTokens,
        setAuthTokens,
        registerUser,
        loginUser,
        logoutUser,
    };

    // Effect to set user state based on authTokens when the component mounts
    useEffect(() => {
        if (authTokens) {
            setUser(jwt_decode(authTokens.access));
        }
        setLoading(false);
    }, [authTokens, loading]);

    // Provide context to children components
    return (
        <AuthContext.Provider value={contextData}>
            {loading ? null : children}
        </AuthContext.Provider>
    );
};

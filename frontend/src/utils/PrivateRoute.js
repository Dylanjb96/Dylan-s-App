import { useContext } from "react";
import { Redirect, Route } from "react-router-dom";
import AuthContext from "../context/AuthContext";

// PrivateRoute component to protect routes that require authentication
const PrivateRoute = ({ children, ...rest }) => {
    // Access authentication context
    let { user } = useContext(AuthContext);

    return (
        // Render a Route with provided props
        <Route
            {...rest}
            render={({ location }) =>
                // Check if user is authenticated
                !user ? (
                    // Redirect to login page if user is not authenticated
                    <Redirect
                        to={{
                            pathname: "/login",
                            state: { from: location }, // Pass the current location to redirect back after login
                        }}
                    />
                ) : (
                    // Render children if user is authenticated
                    children
                )
            }
        />
    );
};

export default PrivateRoute;

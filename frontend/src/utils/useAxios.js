import axios from "axios";
import dayjs from "dayjs";
import jwt_decode from "jwt-decode";
import { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const baseURL = "http://127.0.0.1:8000/api";

const useAxios = () => {
  // Access authentication tokens and update functions from AuthContext
  const { authTokens, setUser, setAuthTokens } = useContext(AuthContext);
  const history = useHistory();

  // Create an Axios instance with a base URL and authorization header
  const axiosInstance = axios.create({
    baseURL,
    headers: { Authorization: `Bearer ${authTokens?.access}` },
  });

  // Add a request interceptor to handle token expiration and refresh
  axiosInstance.interceptors.request.use(
    async (req) => {
      try {
        // Decode the access token to check its expiration
        const user = jwt_decode(authTokens.access);
        const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

        if (!isExpired) return req; // If token is not expired, proceed with the request

        // If token is expired, attempt to refresh it
        const response = await axios.post(`${baseURL}/token/refresh/`, {
          refresh: authTokens.refresh,
        });

        // Update auth tokens in local storage and context
        localStorage.setItem("authTokens", JSON.stringify(response.data));
        setAuthTokens(response.data);
        setUser(jwt_decode(response.data.access));

        // Update the Authorization header with the new access token
        req.headers.Authorization = `Bearer ${response.data.access}`;
        return req;
      } catch (error) {
        console.error("Token refresh error:", error);

        // Handle token refresh failure
        if (error.response && error.response.status === 401) {
          // Clear auth tokens from context and local storage, then redirect to login
          setAuthTokens(null);
          setUser(null);
          localStorage.removeItem("authTokens");
          history.push("/login");
        }

        return Promise.reject(error); // Propagate the error
      }
    },
    (error) => {
      return Promise.reject(error); // Propagate the error
    }
  );

  return axiosInstance; // Return the configured Axios instance
};

export default useAxios;

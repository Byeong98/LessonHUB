import axios from "axios";

const baseURL = process.env.REACT_APP_BASE_URL;

const ApiClient = axios.create({
  baseURL: baseURL,
});

export default ApiClient;
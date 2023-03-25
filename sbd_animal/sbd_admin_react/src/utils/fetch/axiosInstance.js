import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;

const myAxios = axios.create({
	baseURL: import.meta.env.VITE_axios_baseURL,
});

export default myAxios;

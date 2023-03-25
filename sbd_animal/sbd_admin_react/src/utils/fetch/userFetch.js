import myAxios from './axiosInstance';

export async function isAuthenticated() {
	const URL = 'is_authenticatied/';
	const res = await myAxios.get(URL);
	return res;
}

export async function whoAmI() {
	const URL = 'whoami/';
	const res = await myAxios.get(URL);
	return res;
}

export async function setCSRF() {
	const URL = 'set_csrf/';
	const res = await myAxios.get(URL);
	return res;
}

export async function AdminLogin(data) {
	const URL = 'login/';
	const res = await myAxios.post(URL, data);
	return res;
}

export async function AdminLogout() {
	const URL = 'logout/';
	const res = await myAxios.post(URL);
	return res;
}

export async function getAllUsers() {
	const URL = 'api/users/';
	const res = await myAxios.get(URL);
	return res;
}

export async function getUser(id) {
	const URL = `api/user/${id}/`;
	const res = await myAxios.get(URL);
	return res;
}

export async function deactivateUser(id, cur_activation) {
	const URL = `api/user/${id}/`;
	const res = await myAxios.put(URL, { is_active: !cur_activation });
	return res;
}

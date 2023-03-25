import myAxios from './axiosInstance';

export async function getInqueries() {
	const URL = 'api/inqueries/';
	const res = myAxios.get(URL);
	return res;
}
export async function getInquery(id) {
	const URL = `api/inquery/${id}/`;
	const res = myAxios.get(URL);
	return res;
}

export async function postReply(data) {
	const URL = 'api/inquery/reply/';
	const res = myAxios.post(URL, data);
	return res;
}
export async function updateReply(data) {
	const URL = 'api/inquery/reply/';
	const res = myAxios.put(URL, data);
	return res;
}
export async function deleteReply(id) {
	const URL = `api/inquery/reply/`;
	const delete_data = { reply_id: id };
	const res = myAxios.delete(URL, { data: delete_data });
	return res;
}

import myAxios from './axiosInstance';

export async function getWorkouts() {
	const URL = 'api/workouts/';
	const res = await myAxios.get(URL);
	return res;
}

/**
 * WorktoutType = {id:int,name:str,workout_distance:str(Decimal),category:str}
 * 을 업데이트 한다.
 * @param {WorkoutType Object} data
 * @returns
 */
export async function updateWorkoutType(data) {
	const URL = `api/workout/${data.id}/`;
	const res = await myAxios.put(URL, data);
	return res;
}

export async function createWorkoutType(data) {
	const URL = 'api/workouts/';
	const res = await myAxios.post(URL, data);
	return res;
}

export async function deleteWorkoutType(id) {
	const URL = `api/workout/${id}/`;
	const res = await myAxios.delete(URL);
	return res;
}

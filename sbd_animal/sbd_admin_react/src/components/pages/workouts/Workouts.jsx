import { useEffect, useState, useCallback } from 'react';
import {
	getWorkouts,
	updateWorkoutType,
} from '../../../utils/fetch/workoutsFetch';

import useWorkoutStores from '../../../stores/useWorkoutStores';
import WorkoutSortingBar from '../../UI/molecules/workouts/WorkoutSortingBar';
import WorkoutList from '../../UI/molecules/workouts/WorkoutList';
import WorkoutDetail from '../../UI/molecules/workouts/WorkoutDetail';

const Workouts = () => {
	const { getWorkoutList, setWorkoutList } = useWorkoutStores();
	const [workouts, setWorkouts] = useState([]);
	const [focusedWorkout, setFocusedWorkout] = useState({
		id: -1,
		name: '',
		workout_distance: '',
		category: '',
	});
	const [mode, setMode] = useState({
		name: 'display',
	});
	useEffect(() => {
		const MygetWorkouts = async () => {
			const res = await getWorkouts();
			return res;
		};
		if (getWorkoutList()[0] === undefined) {
			MygetWorkouts().then((res) => {
				setWorkoutList(res.data);
				setWorkouts([...res.data]);
			});
		} else {
			setWorkouts(getWorkoutList());
		}
	}, []);
	return (
		<div className="p-3 pl-6 text-white">
			<div className="text-2xl flex items-center bg-slate-500 text-black p-2 rounded-md mb-2">
				운동목록
			</div>
			<div className="flex">
				<div className="w-[70%]">
					<WorkoutSortingBar setWorkouts={setWorkouts} />
					{workouts.length > 0 ? (
						<WorkoutList
							workouts={workouts}
							focusedWorkout={focusedWorkout}
							setFocusedWorkout={setFocusedWorkout}
							setWorkouts={setWorkouts}
							setMode={setMode}
						/>
					) : null}
				</div>
				<div className="w-[30%]">
					<WorkoutDetail
						focusedWorkout={focusedWorkout}
						setWorkouts={setWorkouts}
						mode={mode}
						setMode={setMode}
					/>
				</div>
			</div>
		</div>
	);
};

export default Workouts;

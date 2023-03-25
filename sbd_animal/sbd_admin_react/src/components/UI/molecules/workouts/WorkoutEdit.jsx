import { useState } from 'react';

import useWorkoutStores from '../../../../stores/useWorkoutStores';
import {
	updateWorkoutType,
	createWorkoutType,
} from '../../../../utils/fetch/workoutsFetch';

const WorkoutEdit = ({ data, mode, setMode, setWorkouts }) => {
	const [workoutInput, setWorkoutInput] = useState({
		id: mode === 'edit' ? data.id : -1,
		name: mode === 'edit' ? data.name : '',
		workout_distance: mode === 'edit' ? data.workout_distance : '',
		category: mode === 'edit' ? data.category : '',
	});
	const { updateWorkoutList, setWorkoutList } = useWorkoutStores();
	const onInputChangeHandler = (e) => {
		setWorkoutInput((prev) => ({
			...prev,
			[e.target.name]: e.target.value,
		}));
	};

	/**
	 * workout_distance 는 0.**의 꼴이어야한다.
	 * @param {string} val
	 * @returns
	 */
	const workoutDistanceValidator = (val) => {
		const myReg = /^0\.\d{2}$/;
		return myReg.test(val);
	};

	const onSubmitEdit = async () => {
		if (workoutDistanceValidator(workoutInput.workout_distance)) {
			if (mode === 'edit') {
				await updateWorkoutType(workoutInput).then((res) => {
					setWorkouts((prev) =>
						[...prev].map((el) => {
							if (el.id === res.data.id) {
								return { ...res.data };
							} else {
								return el;
							}
						})
					);
					updateWorkoutList(res.data);
				});
			} else if (mode === 'create') {
				const data = { ...workoutInput };
				delete data.id;
				await createWorkoutType(data).then((res) => {
					setWorkoutList([res.data]);
					setWorkouts((prev) => [...prev, ...[res.data]]);
				});
			}
			setMode((prev) => ({ ...prev, name: 'display' }));
		} else {
			alert('wrong input');
		}
	};
	return (
		<div className="flex flex-col gap-y-2">
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2 gap-y-2">
				<label className="text-sm" htmlFor="workout-name">
					운동이름
				</label>
				<input
					type="text"
					value={workoutInput.name}
					name="name"
					id="workout-name"
					className="text-lg bg-slate-800/70"
					onChange={onInputChangeHandler}
				/>
			</div>
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2 gap-y-2">
				<label className="text-sm" htmlFor="workout-distance">
					운동거리/키
				</label>
				<input
					type="text"
					value={workoutInput.workout_distance}
					name="workout_distance"
					id="workout-distance"
					className="text-lg bg-slate-800/70"
					onChange={onInputChangeHandler}
				/>
			</div>
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2 gap-y-2">
				<label className="text-sm" htmlFor="workout-category">
					운동그룹
				</label>
				<select
					id="workout-category"
					defaultValue={data.category}
					className="bg-stone-800 focus:outline-none p-1 rounded-md"
					name="category"
					onChange={onInputChangeHandler}
				>
					<option value="s">스쿼트</option>
					<option value="b">벤치프레스</option>
					<option value="d">데드리프트</option>
				</select>
			</div>
			<div className="flex">
				<button
					className="bg-sky-700/50 rounded-md p-2 text-lg hover:bg-sky-600 hover:cursor-pointer flex-1"
					onClick={() => onSubmitEdit()}
				>
					{mode === 'edit' ? '수정제출' : '운동생성'}
				</button>
				<button
					className="bg-slate-500/50 rounded-md p-2 text-lg hover:bg-slate-500 hover:cursor-pointer flex-1"
					onClick={() => setMode((prev) => ({ ...prev, name: 'display' }))}
				>
					취소
				</button>
			</div>
		</div>
	);
};

export default WorkoutEdit;

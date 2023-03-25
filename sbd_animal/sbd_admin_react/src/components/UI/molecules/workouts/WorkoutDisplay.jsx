import useWorkoutStores from '../../../../stores/useWorkoutStores';
import { deleteWorkoutType } from '../../../../utils/fetch/workoutsFetch';

const WorkoutDisplay = ({ data, setMode, setWorkouts }) => {
	const { deleteWorkoutList } = useWorkoutStores();
	const showWorkoutName = (val) => {
		if (val === 's') {
			return '스쿼트';
		} else if (val === 'b') {
			return '벤치프레스';
		} else {
			return '데드리프트';
		}
	};
	return (
		<div className="flex flex-col gap-y-2">
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2">
				<label className="text-sm" htmlFor="workout-name">
					운동이름
				</label>
				<p id="workout-name" className="text-lg">
					{data.name}
				</p>
			</div>
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2">
				<label className="text-sm" htmlFor="workout-distance">
					운동거리/키
				</label>
				<p id="workout-distance" className="text-lg">
					{data.workout_distance}
				</p>
			</div>
			<div className="flex flex-col rounded-md bg-slate-600/50 p-2">
				<label className="text-sm" htmlFor="workout-category">
					운동그룹
				</label>
				<p id="workout-category" className="text-lg">
					{showWorkoutName(data.category)}
				</p>
			</div>
			<div className="flex">
				<button
					className="bg-sky-700/50 rounded-md p-2 text-lg hover:bg-sky-600 hover:cursor-pointer flex-1"
					onClick={() => setMode((prev) => ({ ...prev, name: 'edit' }))}
				>
					편집
				</button>
				<button
					className="bg-red-700/50 rounded-md p-2 text-lg hover:bg-red-600 hover:cursor-pointer flex-1"
					onClick={async () =>
						await deleteWorkoutType(data.id).then((res) => {
							deleteWorkoutList(data.id);
							setWorkouts((prev) =>
								[...prev].filter((el) => el.id !== data.id)
							);
						})
					}
				>
					삭제
				</button>
			</div>
		</div>
	);
};

export default WorkoutDisplay;

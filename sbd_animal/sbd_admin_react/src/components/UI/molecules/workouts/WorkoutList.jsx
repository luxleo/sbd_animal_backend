import WorkoutElement from './WorkoutElement';

const WorkoutList = ({
	workouts,
	focusedWorkout,
	setFocusedWorkout,
	setMode,
}) => {
	/**
	 * 운동리스트 중 선택된 하나의 운동을 보이기 위하여
	 * Workouts.focusedWorkout을 바꾼다.
	 * @param {Object} data
	 */
	const onClickElementHandler = (data) => {
		setFocusedWorkout({ ...data });
	};
	return (
		<div>
			{workouts?.map((el) => (
				<div
					key={`workout-${el.id}`}
					className={`hover:bg-slate-400/50 p-1 ${
						el.id === focusedWorkout.id ? 'bg-slate-300/50' : null
					}`}
					onClick={() => onClickElementHandler(el)}
				>
					<WorkoutElement data={el} />
				</div>
			))}
			<div className="flex p-1">
				<button
					className="w-full rounded-md bg-slate-300/70 hover:bg-lime-500/50"
					onClick={() => setMode((prev) => ({ ...prev, name: 'create' }))}
				>
					운동추가
				</button>
			</div>
		</div>
	);
};

export default WorkoutList;

const WorkoutElement = ({ data }) => {
	return (
		<div className="flex">
			<div className="flex justify-center border-slate-700 flex-1">
				{data.id}
			</div>
			<div className="flex justify-center border-slate-700 flex-1">
				{data.name}
			</div>
			<div className="flex justify-center border-slate-700 flex-1">
				{data.workout_distance}
			</div>
			<div className="flex justify-center border-slate-700 flex-1">
				{data.category}
			</div>
		</div>
	);
};

export default WorkoutElement;

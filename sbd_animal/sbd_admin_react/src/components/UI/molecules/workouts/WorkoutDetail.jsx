import { useState } from 'react';

import WorkoutDisplay from './WorkoutDisplay';
import WorkoutEdit from './WorkoutEdit';

const WorkoutDetail = ({ mode, setMode, focusedWorkout, setWorkouts }) => {
	return (
		<div className="w-full bg-slate-500/30 rounded-md">
			<div className="p-2">
				{mode.name === 'display' ? (
					<WorkoutDisplay
						data={focusedWorkout}
						setMode={setMode}
						setWorkouts={setWorkouts}
					/>
				) : (
					<WorkoutEdit
						data={focusedWorkout}
						mode={mode.name}
						setMode={setMode}
						setWorkouts={setWorkouts}
					/>
				)}
			</div>
		</div>
	);
};

export default WorkoutDetail;

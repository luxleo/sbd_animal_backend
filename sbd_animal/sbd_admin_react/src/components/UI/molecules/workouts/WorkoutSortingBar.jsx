import { AiFillCaretDown } from 'react-icons/ai';

const WorkoutSortingBar = ({ setWorkouts }) => {
	const handleSort = (e) => {
		if (e.target.id === 'sort_id') {
			setWorkouts((prev) => [...prev].sort((a, b) => a.id - b.id));
		} else {
			setWorkouts((prev) =>
				[...prev].sort((a, b) => {
					if (a.category > b.category) {
						return 1;
					} else if (a.category < b.category) {
						return -1;
					}
					return 0;
				})
			);
		}
	};
	return (
		<div className="w-full">
			<div></div>
			<div className="flex w-full bg-slate-600">
				<div
					id="sort_id"
					className="flex justify-center items-center border-r-2 border-slate-700 flex-1 hover:bg-slate-500/60 hover:cursor-pointer hover:text-gray-200 gap-x-1"
					onClick={handleSort}
				>
					ID
					<AiFillCaretDown />
				</div>
				<div className="flex justify-center border-r-2 border-slate-700 flex-1">
					운동이름
				</div>
				<div className="flex justify-center border-r-2 border-slate-700 flex-1">
					운동거리/키
				</div>
				<div
					id="sort_group"
					className="flex justify-center items-center border-r-2 border-slate-700 flex-1 hover:bg-slate-500/60 hover:cursor-pointer hover:text-gray-200 gap-x-1"
					onClick={(e) => handleSort(e)}
				>
					운동그룹
					<AiFillCaretDown />
				</div>
			</div>
		</div>
	);
};

export default WorkoutSortingBar;

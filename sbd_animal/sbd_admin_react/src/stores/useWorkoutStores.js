import { create } from 'zustand';

const useWorkoutStores = create((set, get) => ({
	workoutList: [],
	getWorkoutList: () => get().workoutList,
	setWorkoutList: (List) => {
		set((state) => ({ workoutList: [...state.workoutList, ...List] }));
	},
	updateWorkoutList: (target) => {
		set((state) => ({
			workoutList: [...state.workoutList].map((el) => {
				if (el.id === target.id) {
					return { ...target };
				} else {
					return el;
				}
			}),
		}));
	},
	deleteWorkoutList: (id) => {
		set((state) => ({
			workoutList: [...state.workoutList].filter((el) => el.id !== id),
		}));
	},
}));

export default useWorkoutStores;

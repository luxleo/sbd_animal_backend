import { create } from 'zustand';

const useInqueryStores = create((set, get) => ({
	isInqueryList: false,
	getIsInqueryList: () => get().isInqueryList,
	setIsInqueryList: () => {
		set((state) => ({ isInqueryList: true }));
	},
	inqueryList: [],
	getInqueryList: () => get().inqueryList,
	setInqueryList: (data) => {
		set((state) => ({
			inqueryList: [...data],
		}));
	},
}));

export default useInqueryStores;

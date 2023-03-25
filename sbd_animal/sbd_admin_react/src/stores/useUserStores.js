import { create } from 'zustand';

const useUserStores = create((set, get) => ({
	isUser: false,
	user: { username: '', email: '', id: 0 },
	getUser: () => get().user,
	setUser: (val) => {
		set((state) => ({ user: val }));
	},
	getIsUser: () => get().isUser,
	setIsUser: (val) => {
		set((state) => ({ isUser: val }));
	},
	user_list: [],
	appendUser: (val) => {
		set((state) => ({ user_list: [...state.user_list, val] }));
	},
	getUserList: () => get().user_list,
	updateUserList: (id, new_activate) => {
		set((state) => ({
			user_list: [...state.user_list].map((el) => {
				if (el.id === id) {
					return { ...el, is_active: new_activate };
				} else {
					return el;
				}
			}),
		}));
	},
}));

export default useUserStores;

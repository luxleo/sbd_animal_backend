import { HiUserGroup, HiDocumentText } from 'react-icons/hi';
import { GiWeightLiftingUp } from 'react-icons/gi';
const Menus = [
	{
		title: '유저',
		TitleIcon: HiUserGroup,
		menuList: [
			{ name: '유저목록', path: 'users/user_list' },
			{ name: 'DM', path: 'users/user_dm' },
		],
	},
	{
		title: 'FAQ',
		TitleIcon: HiDocumentText,
		menuList: [
			{ name: '공지사항', path: 'FAQ/notices' },
			{ name: '문의사항', path: 'FAQ/inqueries' },
		],
	},
	{
		title: 'Workout',
		TitleIcon: GiWeightLiftingUp,
		menuList: [{ name: '운동목록', path: 'workouts' }],
	},
];
export { Menus };

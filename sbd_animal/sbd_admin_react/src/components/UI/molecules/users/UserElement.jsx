import { parseISO, format } from 'date-fns';
const UserElement = ({ user }) => {
	const showUserGroup = (val) => {
		if (val) {
			return 'Staff';
		} else {
			return 'normal';
		}
	};
	const showUserName = (val) => {
		if (val.length > 15) {
			return val.slice(0, 9) + '...';
		} else {
			return val;
		}
	};
	return (
		<div className="flex w-full py-1 hover:bg-slate-400/50 hover:cursor-pointer">
			<div className="flex justify-center w-[6%]">{user.id}</div>
			<div className="flex pl-1 w-[15%]">{showUserName(user.username)}</div>
			<div className="flex pl-1 w-[25%]">
				{user.email.length > 20 ? user.email.slice(0, 20) + '...' : user.email}
			</div>
			<div className="flex justify-center w-[10%]">
				{showUserGroup(user.is_staff)}
			</div>
			<div className="flex justify-center w-[15%]">
				{format(parseISO(user.date_joined), 'd MMM yyyy')}
			</div>
			<div className="flex justify-center w-[15%]">
				{format(parseISO(user.last_login), 'd MMM yyyy')}
			</div>
			<div className="flex justify-center w-[15%]">
				{user.is_active ? (
					<span className="text-lime-600">ON</span>
				) : (
					<span className="text-red-600">Off</span>
				)}
			</div>
		</div>
	);
};

export default UserElement;

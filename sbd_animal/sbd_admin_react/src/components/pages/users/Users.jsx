import { useEffect, useState, useCallback } from 'react';

import { getAllUsers } from '../../../utils/fetch/userFetch';
import useUserStores from '../../../stores/useUserStores';

import UserSortingBar from '../../UI/molecules/users/UserSortingBar';
import UserList from '../../UI/molecules/users/UserList';
import UserFilterDashboard from '../../UI/molecules/users/UserFilterDashboard';

const Users = () => {
	const { getUserList, appendUser } = useUserStores();
	const [userList, setUserList] = useState([]);

	useEffect(() => {
		const initialUsersLoader = async () => {
			const res = await getAllUsers();
			return res;
		};
		if (getUserList()[0] === undefined) {
			initialUsersLoader()
				.then((res) => {
					res.data.forEach((el) => appendUser(el));
					return res.data;
				})
				.then((res) => setUserList([...res]));
		} else {
			setUserList(getUserList());
		}
	}, []);

	return (
		<div className="p-3 pl-6 text-white">
			<div className="text-2xl flex items-center bg-slate-500 text-black p-2 rounded-md mb-2">
				유저목록
			</div>
			<div className="flex">
				<div className="w-[70%]">
					<UserSortingBar />
					{userList.length > 0 ? <UserList users={userList} /> : null}
				</div>
				<div className="flex-1 pl-3">
					<UserFilterDashboard setUserList={setUserList} />
				</div>
			</div>
		</div>
	);
};

export default Users;

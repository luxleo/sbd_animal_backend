import { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';

import useUserStores from '../../stores/useUserStores';
import { isAuthenticated, whoAmI } from '../../utils/fetch/userFetch';
import Sidebar from '../layouts/Sidebar';
import Login from './Login';

export default function Root() {
	const { getIsUser, setIsUser, setUser } = useUserStores();

	useEffect(() => {
		const check_authentication = async () => {
			const res = await isAuthenticated();
			return res;
		};
		check_authentication().then(async (res) => {
			if (res.data.message === 'authenticated') {
				const user = await whoAmI().then((res) => res.data.user);
				setUser(user);
				setIsUser(true);
			} else {
				setIsUser(false);
			}
		});
	}, []);
	return (
		<>
			<div className="flex">
				{getIsUser() ? (
					<>
						<Sidebar />
						<div className="flex-1 bg-zinc-800">
							<Outlet />
						</div>
					</>
				) : (
					<Login />
				)}
			</div>
		</>
	);
}

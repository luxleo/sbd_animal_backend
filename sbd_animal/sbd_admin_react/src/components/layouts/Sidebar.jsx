import { useState, useCallback } from 'react';

import { IconContext } from 'react-icons';
import { BsArrowLeftCircle, BsArrowRightCircle } from 'react-icons/bs';
import useUserStores from '../../stores/useUserStores';
import { AdminLogout } from '../../utils/fetch/userFetch';

import SidebarMenu from '../UI/molecules/SidebarMenu';
import { Menus } from '../../utils/data/sidebarMenu';

const Sidebar = () => {
	const [isSideOpen, setIsSideOpen] = useState(true);
	const { getUser, setIsUser } = useUserStores();
	const user = getUser();
	const childIsOpenController = useCallback((val) => {
		setIsSideOpen(val);
	}, []);
	const showNameShortly = (val) => {
		if (val.length > 10) {
			return val.slice(0, 5);
		} else {
			return val;
		}
	};
	return (
		<>
			<div
				className={`${
					isSideOpen ? 'w-60' : 'w-20'
				} duration-300 bg-slate-700 h-screen relative text-white`}
			>
				<div
					className="inline absolute -right-3 top-9 z-10"
					onClick={() => setIsSideOpen((prev) => !prev)}
				>
					<IconContext.Provider value={{ color: 'white', size: '1.5em' }}>
						{isSideOpen ? <BsArrowLeftCircle /> : <BsArrowRightCircle />}
					</IconContext.Provider>
				</div>
				<div className="relative top-9 pl-3">
					<div className="flex gap-x-4 mb-3">
						<h2>{`${showNameShortly(user.username)}`}</h2>
						<button
							className={`duration-300 origin-left ${
								!isSideOpen && 'scale-0'
							} p-1 rounded-md bg-red-600/50 hover:bg-red-600`}
							onClick={async () => {
								const res = await AdminLogout();
								setIsUser(false);
							}}
						>
							Log out
						</button>
					</div>
					<div className="flex flex-col gap-y-3 pr-3 mt-6">
						{Menus.map((el) => (
							<SidebarMenu
								key={`menu-ul-${el.title}`}
								title={el.title}
								TitleIcon={el.TitleIcon}
								menuList={el.menuList}
								isOpen={isSideOpen}
								setIsOpen={childIsOpenController}
							/>
						))}
					</div>
				</div>
			</div>
		</>
	);
};

export default Sidebar;

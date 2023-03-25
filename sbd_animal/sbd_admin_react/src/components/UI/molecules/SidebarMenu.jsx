import { NavLink } from 'react-router-dom';
const SidebarMenu = ({ title, TitleIcon, menuList, isOpen, setIsOpen }) => {
	return (
		<div>
			<ul>
				<div
					className={`flex gap-x-2 rounded-md ${
						isOpen ? 'border-b-2' : 'inline-flex p-2 hover:bg-slate-300/60'
					}`}
					onClick={() => setIsOpen(true)}
				>
					{<TitleIcon />}
					{isOpen ? <h2>{title}</h2> : null}
				</div>
				<div
					className={`pt-2 pl-4 ${
						!isOpen && 'h-0 scale-0'
					} transition duration-300 origin-top`}
				>
					{menuList.map((el) => (
						<li key={`menu-list-${el.name}`}>
							<NavLink
								to={el.path}
								className={({ isActive }) =>
									isActive ? 'bg-slate-200/60 p-1 rounded-md' : undefined
								}
								onClick={() => setIsOpen(false)}
							>
								{el.name}
							</NavLink>
						</li>
					))}
				</div>
			</ul>
		</div>
	);
};

export default SidebarMenu;

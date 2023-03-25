import { useState, forwardRef } from 'react';

import { differenceInCalendarDays, parseISO } from 'date-fns';
import DatePicker from 'react-datepicker';
import { BsFillCalendarDayFill } from 'react-icons/bs';

import 'react-datepicker/dist/react-datepicker.css';

import useUserStores from '../../../../stores/useUserStores';

const CustomInput = forwardRef(({ value, onClick }, ref) => (
	<div className="flex ">
		<button
			className="flex items-center rounded-md bg-slate-500 p-1 gap-x-2"
			onClick={onClick}
			ref={ref}
		>
			<BsFillCalendarDayFill />
			{value}
		</button>
	</div>
));

const UserFilterDashboard = ({ setUserList }) => {
	const [filterState, setFilterState] = useState({
		search: '',
		targetGroup: '',
		startDate: new Date(),
		endDate: new Date(),
		isDate: false,
	});
	const { getUserList } = useUserStores();
	const onSearchChange = (e) => {
		setFilterState((prev) => ({
			...prev,
			[e.target.name]: e.target.value,
		}));
	};
	const onSelectValue = (e) => {
		setFilterState((prev) => ({
			...prev,
			[e.target.name]: e.target.value,
		}));
	};
	const onDateChange = (dates) => {
		const [start, end] = dates;
		setFilterState((prev) => ({
			...prev,
			startDate: start,
			endDate: end,
			isDate: true,
		}));
	};
	const isDateIn = (userDate) => {
		const targetDate = parseISO(userDate);
		const diff_start = differenceInCalendarDays(
			targetDate,
			filterState.startDate
		);
		const diff_end = differenceInCalendarDays(filterState.endDate, targetDate);
		if (diff_start >= 0 && diff_end >= 0) {
			return true;
		} else {
			return false;
		}
	};
	const onFilterSubmit = () => {
		if (filterState.targetGroup === 'staff') {
			if (filterState.isDate) {
				setUserList((prev) =>
					[...getUserList()].filter(
						(el) =>
							el.username.includes(filterState.search) &&
							el.is_staff &&
							isDateIn(el.date_joined)
					)
				);
			} else {
				setUserList((prev) =>
					[...getUserList()].filter(
						(el) => el.username.includes(filterState.search) && el.is_staff
					)
				);
			}
		} else if (filterState.targetGroup === 'normal') {
			if (filterState.isDate) {
				setUserList((prev) =>
					[...getUserList()].filter(
						(el) =>
							el.username.includes(filterState.search) &&
							!el.is_staff &&
							isDateIn(el.date_joined)
					)
				);
			} else {
				setUserList((prev) =>
					[...getUserList()].filter(
						(el) => el.username.includes(filterState.search) && !el.is_staff
					)
				);
			}
		} else {
			if (filterState.isDate) {
				setUserList((prev) =>
					[...getUserList()].filter(
						(el) =>
							el.username.includes(filterState.search) &&
							isDateIn(el.date_joined)
					)
				);
			} else {
				setUserList((prev) =>
					[...getUserList()].filter((el) =>
						el.username.includes(filterState.search)
					)
				);
			}
		}
	};

	return (
		<div className="w-full bg-slate-500/30 rounded-lg">
			<div className="p-2 flex flex-col gap-y-2">
				<div className="flex gap-x-2">
					<label htmlFor="search" className="text-sm flex items-center">
						유저
					</label>
					<input
						type="text"
						name="search"
						id="search"
						value={filterState.search}
						placeholder="이름, 이메일로 검색"
						className="bg-gray-800/70 p-1 rounded-md focus:outline-none foucs:border-amber-500 focus:ring-1 focus:ring-amber-500"
						onChange={onSearchChange}
					/>
				</div>
				<div className="flex gap-x-2">
					<label htmlFor="UserGroup" className="text-sm flex items-center">
						유저그룹
					</label>
					<select
						id="UserGroup"
						defaultValue="all"
						name="targetGroup"
						className="bg-stone-800 focus:outline-none p-1 rounded-md"
						onChange={onSelectValue}
					>
						<option value="all">모두</option>
						<option value="staff">직원</option>
						<option value="normal">일반유저</option>
					</select>
				</div>
				<div className="flex gap-x-2">
					<label htmlFor="UserGroup" className="text-sm flex items-center">
						활성상태
					</label>
					<select
						id="UserGroup"
						defaultValue="all"
						name="targetGroup"
						className="bg-stone-800 focus:outline-none p-1 rounded-md"
						onChange={(e) => {
							if (e.target.value === 'on') {
								setUserList((prev) => prev.filter((el) => el.is_active));
							} else {
								setUserList((prev) => prev.filter((el) => !el.is_active));
							}
						}}
					>
						<option value="on">On</option>
						<option value="off">Off</option>
					</select>
				</div>
				<div className="text-black w-full flex gap-x-2">
					<label htmlFor="calendar" className="text-white text-sm">
						가입일자
					</label>
					<div id="calendar" className="flex-1">
						<DatePicker
							dateFormat={'d MMM yy'}
							selected={filterState.startDate}
							startDate={filterState.startDate}
							endDate={filterState.endDate}
							onChange={onDateChange}
							selectsRange
							isClearable={true}
							customInput={<CustomInput />}
						/>
					</div>
				</div>
				<div className="flex gap-x-1">
					<button
						className="flex justify-center items-center rounded-md bg-slate-500/50 hover:bg-lime-500/70 w-1/2"
						onClick={onFilterSubmit}
					>
						필터
					</button>
					<button
						className="flex justify-center items-center rounded-md bg-slate-500/50 hover:bg-sky-500/70 w-1/2"
						onClick={() => setUserList((prev) => [...getUserList()])}
					>
						초기화
					</button>
				</div>
			</div>
		</div>
	);
};

export default UserFilterDashboard;

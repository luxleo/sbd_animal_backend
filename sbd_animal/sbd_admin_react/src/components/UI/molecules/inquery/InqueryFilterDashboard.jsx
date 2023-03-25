import { useState, forwardRef } from 'react';

import { differenceInCalendarDays, isDate, parseISO } from 'date-fns';
import DatePicker from 'react-datepicker';
import { BsFillCalendarDayFill } from 'react-icons/bs';

import 'react-datepicker/dist/react-datepicker.css';

import useInqueryStores from '../../../../stores/useInqueryStores';
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

const InqueryFilterDashboard = ({ setInqueries }) => {
	const [filterState, setFilterState] = useState({
		search: '',
		targetGroup: '미응답',
		startDate: new Date(),
		endDate: new Date(),
		isDate: false,
	});
	const { getInqueryList } = useInqueryStores();
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
	/**
	 * 필터 날짜 범위에 해당하는지 check한다.
	 */
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
		if (filterState.isDate) {
			setInqueries((prev) =>
				[...getInqueryList()].filter(
					(el) =>
						(el.author.username.includes(filterState.search) ||
							el.title.includes(filterState.search)) &&
						el.state_label === filterState.targetGroup &&
						isDateIn(el.created_at)
				)
			);
		} else {
			setInqueries((prev) =>
				[...getInqueryList()].filter(
					(el) =>
						(el.author.username.includes(filterState.search) ||
							el.title.includes(filterState.search)) &&
						el.state_label === filterState.targetGroup
				)
			);
		}
	};
	return (
		<div className="w-full bg-slate-500/30 rounded-lg">
			<div className="p-2 flex flex-col gap-y-2">
				<div className="flex gap-x-2">
					<label htmlFor="search" className="text-sm flex items-center">
						검색
					</label>
					<input
						type="text"
						name="search"
						id="search"
						value={filterState.search}
						placeholder="작성자이름, 문의 제목으로 검색"
						className="bg-gray-800/70 p-1 rounded-md focus:outline-none foucs:border-amber-500 focus:ring-1 focus:ring-amber-500"
						onChange={onSearchChange}
					/>
				</div>
				<div className="flex gap-x-2">
					<label htmlFor="UserGroup" className="text-sm flex items-center">
						응답상태
					</label>
					<select
						id="UserGroup"
						defaultValue="미응답"
						name="targetGroup"
						className="bg-stone-800 focus:outline-none p-1 rounded-md"
						onChange={onSelectValue}
					>
						<option value="미응답">미응답</option>
						<option value="응답">응답</option>
						<option value="추가의문">추가의문</option>
						<option value="처리완료">처리완료</option>
					</select>
				</div>
				<div className="text-black w-full flex gap-x-2">
					<label htmlFor="calendar" className="text-white text-sm">
						생성일자
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
						onClick={() => {
							setInqueries((prev) => [...getInqueryList()]);
							setFilterState((prev) => ({
								search: '',
								targetGroup: '미응답',
								startDate: new Date(),
								endDate: new Date(),
								isDate: false,
							}));
						}}
					>
						초기화
					</button>
				</div>
			</div>
		</div>
	);
};

export default InqueryFilterDashboard;

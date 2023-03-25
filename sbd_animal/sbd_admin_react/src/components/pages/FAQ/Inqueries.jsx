import { useState, useEffect } from 'react';

import useInqueryStores from '../../../stores/useInqueryStores';
import { getInqueries } from '../../../utils/fetch/inqueryFetch';

import InquerySortingBar from '../../UI/molecules/inquery/InquerySortingBar';
import InqueryList from '../../UI/molecules/inquery/InqueryList';
import InqueryFilterDashboard from '../../UI/molecules/inquery/InqueryFilterDashboard';

const Inqueries = () => {
	const { getIsInqueryList, setIsInqueryList, getInqueryList, setInqueryList } =
		useInqueryStores();
	const [inqueries, setInqueries] = useState([]);
	useEffect(() => {
		const initialInqueriesLoad = async () => {
			await getInqueries().then((res) => {
				setIsInqueryList();
				setInqueryList(res.data);
				setInqueries((prev) => [...res.data]);
			});
		};
		if (!getIsInqueryList()) {
			initialInqueriesLoad();
		} else {
			setInqueries((prev) => [...getInqueryList()]);
		}
	}, []);
	return (
		<div className="p-3 pl-6 text-white">
			<div className="text-2xl flex items-center bg-slate-500 text-black p-2 rounded-md mb-2">
				문의사항
			</div>
			<div className="flex">
				<div className="w-[70%]">
					<InquerySortingBar />
					{inqueries.length > 0 ? <InqueryList inqueries={inqueries} /> : null}
				</div>
				<div className="w-[30%]">
					<InqueryFilterDashboard setInqueries={setInqueries} />
				</div>
			</div>
		</div>
	);
};

export default Inqueries;

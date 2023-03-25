import React from 'react';
import { Link } from 'react-router-dom';

import InqueryElement from './InqueryElement';
const InqueryList = ({ inqueries }) => {
	return (
		<div>
			{inqueries?.map((el) => (
				<Link key={`inquery-${el.id}`} to={`../${el.id}`}>
					<InqueryElement inquery={el} />
				</Link>
			))}
		</div>
	);
};

export default InqueryList;

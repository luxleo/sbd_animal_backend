import React from 'react';

const InquerySortingBar = () => {
	return (
		<div className="flex w-full bg-slate-600">
			<div className="flex justify-center border-r-2 border-slate-700 flex-1">
				ID
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 flex-1">
				글쓴이
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 flex-1">
				제목
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 flex-1">
				상태
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 flex-1">
				생성일
			</div>
		</div>
	);
};

export default InquerySortingBar;

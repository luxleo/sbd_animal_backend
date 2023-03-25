import { parseISO, format } from 'date-fns';

const InqueryElement = ({ inquery }) => {
	const displayIn10 = (val) => {
		if (val.length > 10) {
			return val.slice(0, 10) + '..';
		} else {
			return val;
		}
	};
	const coloringStateLabel = (val) => {
		if (val === '미응답') {
			return 'text-red-600';
		} else if (val === '응답') {
			return 'text-lime-600';
		} else if (val === '추가의문') {
			return 'text-pink-600';
		} else {
			return 'text-sky-600';
		}
	};
	return (
		<div className="flex w-full py-1 hover:bg-slate-400/50 hover:cursor-pointer">
			<div className="flex justify-center flex-1">{inquery.id}</div>
			<div className="flex justify-center flex-1">
				{displayIn10(inquery.author.username)}
			</div>
			<div className="flex justify-center flex-1">
				{displayIn10(inquery.title)}
			</div>
			<div
				className={`flex justify-center flex-1 ${coloringStateLabel(
					inquery.state_label
				)}`}
			>
				{inquery.state_label}
			</div>
			<div className="flex justify-center flex-1">
				{format(parseISO(inquery.created_at), 'd MMM yyyy')}
			</div>
		</div>
	);
};

export default InqueryElement;

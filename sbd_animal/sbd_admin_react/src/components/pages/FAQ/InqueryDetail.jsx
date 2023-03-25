import { useState } from 'react';
import { IoIosArrowBack } from 'react-icons/io';
import { Link, useLoaderData } from 'react-router-dom';

import { postReply } from '../../../utils/fetch/inqueryFetch';
import { getInquery } from '../../../utils/fetch/inqueryFetch';
import useInqueryStores from '../../../stores/useInqueryStores';
import Reply from '../../UI/molecules/reply/Reply';

export async function loader({ params }) {
	const data = await getInquery(params.inquery_id).then((res) => res.data);
	return { data };
}

const InqueryDetail = () => {
	const { data } = useLoaderData();
	const { getInqueryList, setInqueryList } = useInqueryStores();
	const [replyMessage, setReplyMessage] = useState('');
	const [replyList, setReplyList] = useState(data.reply_list);
	const onChangeReplyMessage = (e) => {
		setReplyMessage((prev) => e.target.value);
	};
	const onReplySubmit = async () => {
		if (replyMessage.length > 5 && replyMessage.length < 500) {
			await postReply({
				inquery_pk: data.inquery.id,
				content: replyMessage,
			}).then((res) => {
				setReplyList((prev) => [...prev, res.data]);
				setInqueryList(
					[...getInqueryList()].map((el) => {
						if (el.id === data.inquery.id) {
							return { ...el, state_label: '응답' };
						} else {
							return el;
						}
					})
				);
				setReplyMessage('');
			});
		} else {
			alert('댓글은 5글자 이상 500글자 미만으로 작성해주세요');
		}
	};
	return (
		<div className="p-3 pl-6 text-white max-h-screen overflow-y-auto">
			<div className="text-2xl flex items-center bg-slate-500 text-black p-2 rounded-md mb-2">
				<div className="hover:bg-slate-400/50 rounded-md p-2 hover:mr-2 hover:text-white">
					<Link to={'../inqueries'}>
						<IoIosArrowBack />
					</Link>
				</div>
				{`문의-${data.inquery.id}`}
				<span className="ml-2 text-sm">{`${data.inquery.created_at}`}</span>
			</div>
			<div className="flex flex-col p-2 w-full bg-slate-500/30 rounded-md">
				<div className="text-sm w-full bg-slate-500/40 mb-3">
					제목: {data.inquery.title}
				</div>
				<div className="mb-3">
					<span className="text-sm">본문</span>
					<br />
					{data.inquery.content}
				</div>
				<div className="flex flex-col gap-y-2">
					<div className="flex flex-col gap-y-1">
						<label className="text-sm" htmlFor="reply-textarea">
							댓글작성
						</label>
						<textarea
							id="reply-textarea"
							value={replyMessage}
							onChange={onChangeReplyMessage}
							placeholder="작성할 댓글 내용을 입력해주세요"
							className="flex-1 bg-stone-700 min-h-[15vh] max-h-[30vh] overflow-y-auto"
						/>
						{replyMessage.length > 0 ? (
							<div className="flex w-full mt-1">
								<button
									className="w-full rounded-md bg-lime-600/50 hover:bg-lime-600"
									onClick={onReplySubmit}
								>
									댓글 작성
								</button>
							</div>
						) : null}
					</div>
					<span className="text-sm">댓글</span>
					{replyList?.map((el) => (
						<Reply
							key={`reply-${el.id}`}
							data={el}
							setReplyList={setReplyList}
						/>
					))}
				</div>
			</div>
		</div>
	);
};

export default InqueryDetail;

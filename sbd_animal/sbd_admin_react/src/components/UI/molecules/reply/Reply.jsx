import { useState } from 'react';
import { format, parseISO } from 'date-fns';

import useUserStores from '../../../../stores/useUserStores';
import { updateReply, deleteReply } from '../../../../utils/fetch/inqueryFetch';

const Reply = ({ data, setReplyList }) => {
	const { getUser } = useUserStores();
	const [mode, setMode] = useState('display');
	const [replyMessage, setReplyMessage] = useState(data.content);
	const [replyEditContent, setReplyEditContent] = useState(data.content);
	const onContentChange = (e) => {
		setReplyEditContent(e.target.value);
	};
	const onSubmitEdit = async () => {
		if (replyEditContent.length > 5 && replyEditContent.length < 500) {
			const sendData = { reply_id: data.id, content: replyEditContent };
			await updateReply(sendData).then((res) => {
				setReplyMessage(res.data.content);
				setReplyEditContent(res.data.content);
			});
			setMode('display');
		}
	};
	return (
		<article className="p-3 text-base rounded-lg bg-gray-900/60 hover:bg-gray-900/90 max-h-screen overflow-y-auto">
			<footer className="flex justify-between items-center mb-2">
				<div className="flex items-center">
					<p className="inline-flex items-center mr-3 text-sm text-white ml-2">
						{data.author.username}
					</p>
					<p className="text-gray-500">
						{format(parseISO(data.created_at), 'do MMM yy')}
					</p>
					{getUser().username === data.author.username ? (
						<div className="pl-1 flex gap-x-1">
							<button
								className="text-xs p-1 rounded-md bg-sky-800/50 hover:bg-sky-800"
								onClick={() => setMode('edit')}
							>
								수정
							</button>
							<button
								className="text-xs p-1 rounded-md bg-red-700/50 hover:bg-red-700"
								onClick={async () => {
									await deleteReply(data.id).then((res) => {
										setReplyList((prev) =>
											[...prev].filter((el) => el.id !== data.id)
										);
									});
								}}
							>
								삭제
							</button>
						</div>
					) : null}
				</div>
			</footer>
			{mode === 'display' ? (
				<p className="text-gray-400">{replyMessage}</p>
			) : (
				<div>
					<textarea
						value={replyEditContent}
						onChange={onContentChange}
						className="bg-gray-600/60 w-[50%] max-h-[20vh] overflow-y-auto"
					/>
					<div className="pl-1 flex gap-x-1">
						<button
							className="text-xs p-1 rounded-md bg-sky-800/50 hover:bg-sky-800"
							onClick={onSubmitEdit}
						>
							수정
						</button>
						<button
							className="text-xs p-1 rounded-md bg-slate-700/50 hover:bg-slate-700"
							onClick={() => {
								setReplyEditContent(replyMessage);
								setMode('display');
							}}
						>
							취소
						</button>
					</div>
				</div>
			)}
		</article>
	);
};

export default Reply;

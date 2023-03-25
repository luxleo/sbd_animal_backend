import { useLoaderData, Link, useNavigate } from 'react-router-dom';
import { format, parseISO } from 'date-fns';

import useUserStores from '../../../stores/useUserStores';
import { getUser, deactivateUser } from '../../../utils/fetch/userFetch';

import { IoIosArrowBack } from 'react-icons/io';

export async function loader({ params }) {
	const userInfo = await getUser(params.user_id).then((res) => res.data);
	return { userInfo };
}

const UserDetail = () => {
	const { userInfo } = useLoaderData();
	const { updateUserList } = useUserStores();
	const showUserGroup = (val) => {
		if (val) {
			return 'Staff';
		} else {
			return 'normal';
		}
	};
	const navigate = useNavigate();
	/**
	 * 유저 활성 상태를 토글로 변환 시킨후 유저리스트 업데이트후
	 * 유저리스트 페이지로 리다이렉트
	 */
	const onToggleActivationState = async () => {
		await deactivateUser(userInfo.id, userInfo.is_active).then((res) => {
			updateUserList(userInfo.id, res.data.is_active);
			navigate('../user_list');
		});
	};
	return (
		<div className="p-3 pl-6 text-white">
			<div className="text-2xl flex items-center bg-slate-500 text-black p-2 rounded-md mb-2">
				<div className="hover:bg-slate-400/50 rounded-md p-2 hover:mr-2 hover:text-white">
					<Link to={'../user_list'}>
						<IoIosArrowBack />
					</Link>
				</div>
				{`${userInfo.username}`}
			</div>
			<div className="w-full bg-slate-500/30 rounded-md">
				<div className="flex flex-col w-[40%] p-2 gap-y-2">
					<div className="flex gap-x-2 w-full">
						<div className="flex flex-col w-1/3 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2">
							<span className="pl-1 text-sm">닉네임</span>
							<p className="text-xl font-sans">{userInfo.username}</p>
						</div>
						<div className="flex flex-col w-2/3 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2">
							<span className="pl-1 text-sm">이메일</span>
							<p className="text-xl font-sans">{userInfo.email}</p>
						</div>
					</div>
					<div className="flex gap-x-2 w-full">
						<div className="flex flex-col w-1/2 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2">
							<span className="pl-1 text-sm">최근 로그인</span>
							<p className="text-xl font-sans">
								{format(parseISO(userInfo.last_login), 'd MMM yyyy')}
							</p>
						</div>
						<div className="flex flex-col w-1/2 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2">
							<span className="pl-1 text-sm">가입일</span>
							<p className="text-xl font-sans">
								{format(parseISO(userInfo.date_joined), 'd MMM yyyy')}
							</p>
						</div>
					</div>
					<div className="flex gap-x-2 w-full">
						<div className="flex flex-col w-1/2 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2">
							<span className="pl-1 text-sm">유저그룹</span>
							<p className="text-xl font-sans">
								{showUserGroup(userInfo.is_staff)}
							</p>
						</div>
						<div
							className="flex flex-col w-1/2 shadow-inner hover:shadow-md shadow-slate-500/50 hover:shadow-slate-300/50 p-2"
							onClick={onToggleActivationState}
						>
							<span className="pl-1 text-sm">활성상태</span>
							<p className="text-xl font-sans">
								{userInfo.is_active ? (
									<span className="text-lime-600">On</span>
								) : (
									<span className="text-red-600">Off</span>
								)}
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default UserDetail;

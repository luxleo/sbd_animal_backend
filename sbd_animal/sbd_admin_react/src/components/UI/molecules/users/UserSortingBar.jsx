const UserSortingBar = () => {
	return (
		<div className="flex w-full bg-slate-600">
			<div className="flex justify-center border-r-2 border-slate-700 w-[6%]">
				ID
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[15%]">
				닉네임
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[25%]">
				이메일
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[10%]">
				유저그룹
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[15%]">
				가입일자
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[15%]">
				최근활동
			</div>
			<div className="flex justify-center border-r-2 border-slate-700 w-[15%]">
				활성상태
			</div>
		</div>
	);
};

export default UserSortingBar;

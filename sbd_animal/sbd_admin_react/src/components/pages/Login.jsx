import { useState, useEffect } from 'react';

import useUserStores from '../../stores/useUserStores';
import { AdminLogin, setCSRF } from '../../utils/fetch/userFetch';

const Login = () => {
	const { setIsUser, setUser } = useUserStores();
	const [loginInput, setLoginInput] = useState({
		email: '',
		password: '',
	});
	const onChangeHandler = (e) => {
		setLoginInput((prev) => ({
			...prev,
			[e.target.name]: e.target.value,
		}));
	};
	const onSubmit = async () => {
		const sendData = { email: loginInput.email, password: loginInput.password };
		const isSet = await setCSRF().then(() => {
			return true;
		});
		if (isSet) {
			await AdminLogin(sendData).then((res) => {
				setUser(res.data.user);
				setIsUser(true);
			});
		}
	};
	return (
		<div className="flex h-screen w-full bg-zinc-800 justify-center items-center">
			<div className="flex flex-col w-[30%] p-3 bg-black bg-opacity-30">
				<div className="flex flex-col mb-1">
					<label htmlFor="login-email" className="text-white">
						email
					</label>
					<input
						id="login-email"
						name="email"
						type={'email'}
						value={loginInput.email}
						onChange={onChangeHandler}
					/>
				</div>
				<div className="flex flex-col mb-2">
					<label htmlFor="login-password" className="text-white">
						password
					</label>
					<input
						id="login-password"
						name="password"
						type={'pasword'}
						value={loginInput.password}
						onChange={onChangeHandler}
					/>
				</div>
				<div className="w-full">
					<button
						className="rounded-md bg-amber-600 w-full hover:z-10"
						onClick={onSubmit}
					>
						Login
					</button>
				</div>
			</div>
		</div>
	);
};

export default Login;

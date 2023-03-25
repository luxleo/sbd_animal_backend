import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import './index.css';
import Root from './components/pages/Root';
import Users from './components/pages/users/Users';
import UserDetail, {
	loader as userInfoLoader,
} from './components/pages/users/UserDetail';
import Workouts from './components/pages/workouts/Workouts';
import UserDM from './components/pages/users/UserDM';
import Inqueries from './components/pages/FAQ/Inqueries';
import InqueryDetail, {
	loader as inqueryLoader,
} from './components/pages/FAQ/InqueryDetail';

const router = createBrowserRouter(
	[
		{
			path: '/',
			element: <Root />,
			children: [
				{
					path: 'users',
					children: [
						{
							path: 'user_list',
							element: <Users />,
						},
						{
							path: ':user_id',
							element: <UserDetail />,
							loader: userInfoLoader,
						},
						{
							path: 'user_dm',
							element: <UserDM />,
						},
					],
				},
				{
					path: 'workouts',
					element: <Workouts />,
				},
				{
					path: 'FAQ',
					children: [
						{
							path: 'notices',
						},
						{
							path: 'inqueries',
							element: <Inqueries />,
						},
						{
							path: ':inquery_id',
							element: <InqueryDetail />,
							loader: inqueryLoader,
						},
					],
				},
			],
		},
	],
	{ basename: '/beastTamers' }
);

ReactDOM.createRoot(document.getElementById('root')).render(
	<RouterProvider router={router} />
);

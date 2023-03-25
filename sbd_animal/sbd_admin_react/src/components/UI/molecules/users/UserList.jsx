import { Link } from 'react-router-dom';

import UserElement from './UserElement';
/**
 * Users컴포넌트 에서 getUsers && 으로 users prop 넘길수 있을때만 렌더링한다.
 */
const UserList = ({ users }) => {
	return (
		<div>
			{users?.map((el) => (
				<Link key={`users-${el.id}`} to={`../${el.id}`}>
					<UserElement user={el} />
				</Link>
			))}
		</div>
	);
};

export default UserList;

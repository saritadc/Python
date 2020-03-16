from user import User

users = [User(1, "ram", "ram123")]
"""for u in users:
		print(u)
	is similar to 
	u for u in users
"""

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
# users = [{'id': 1, 
# 			'username': 'ram', 
# 			'password': 'ram123'}]

# username_mapping  = {'ram': {'id' :1,   #indexing
# 					'username': 'ram',
# 					'password': 'ram123'}}

# userid_mapping = {1:{'id': 1, 
# 					'username': 'ram',
# 					'password': 'ram123'}}

def authenticate(username, password): #for security
	user = username_mapping.get(username, None)
	if user and user.password == password:
		return user

def identity(payload): #for security
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)
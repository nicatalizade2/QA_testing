# with open('users.txt.txt') as file:
#     for line in file:
#         print(line.strip())

# def read_users(filename):
#     users.txt = []
#     with open(filename) as file:
#         for line in file:
#             users.txt.append(line.strip())
#     return users.txt
# users_list = read_users("users.txt.txt")
# for user in users_list:
#     print(user)

# count = 0
# with open('users.txt.txt', 'r') as file:
#     for line in file:
#         count += 1
#     print('Total users.txt:', count)

# with open('users.txt.txt', 'r') as file:
#     for line in file:
#         user = line.strip()
#         if 'qa' in user:
#             print(user)

# users.txt = []
# with open('users.txt.txt', 'r') as file:
#     for line in file:
#         users.txt.append(line.strip())
#     print(users.txt)

#
# def load_user(filename):
#     with open(filename, 'r') as file:
#         return [line.strip() for line in file]
#
# users.txt = load_user('users.txt')
# for user in users.txt:
#     print(user)

#
# with open('users.txt', 'r') as infile, open('results.txt', 'w') as outfile:
#     for line in infile:
#         user = line.strip()
#         outfile.write(f'Test executed for user:{user}\n')
#
#
# def login_test(essek):
#     if essek == 'admin':
#         return 'PASS'
#     else:
#         return 'FAIL'
#
#
# with open('users.txt', 'r') as file:
#     for line in file:
#         user = line.strip()
#         result = login_test(user)
#         print(f'Login test for {user}: {result}')


# user_dic = {}
# with open('users.txt.txt', 'r') as file:
#     for id, line in enumerate(file, start=1):
#         user_dic[id] = line.strip()
#     print(user_dic)

def run_test(user):
    return 'PASS' if user == 'admin' else "FAIL"


results = []

with open("users.txt", 'r') as file:
    for line in file:
        user = line.strip()
        if not user:
            continue
        results.append(f'{user}:{run_test(user)}')
# print(results)

with open('report.txt', 'w') as report:
    for line in results:
        report.write(line + "\n")

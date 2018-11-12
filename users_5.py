#!/usr/bin/env python
# coding=utf-8
users = {
    'first_name':'chen',
    'last_name':'ping',
    'age':'40',
    'city':'taizhou',
}
users_0 = {
    'first_name':'wang',
    'last_name':'fang',
    'age':'35',
    'city':'changsha',
}
people  = [users,users_0]
for user in people:
    print(user)

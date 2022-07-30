# princess_app
https://devsheet.com/code-snippet/join-models-or-tables-query-sqlalchemy/
from sqlalchemy import or_, and_

#USING AND CONDITION
session.query(
    EmployeeModel.name,
    EmployeeDepartment.dept_name
).join(
    EmployeeDepartment,
    and_(
        EmployeeDepartment.employee_id == EmployeeModel.id, 
        EmployeeDepartment.dept_code == 'P01'
    )
).all()


#USING OR CONDITION
session.query(
    EmployeeModel.name,
    EmployeeDepartment.dept_name
).join(
    EmployeeDepartment,
    or_(
        EmployeeDepartment.employee_id == EmployeeModel.id, 
        EmployeeDepartment.dept_code == 'P01'
    )
).all()





#JOINING TABLE (User and Address)
self.session.query(
    User.id,
    User.first_name,
    User.last_name,
    Address.city,
    Address.State
).join(
    Address, User.id == Address.user_id
).filter(
    Address.city.like('new%'))
).all()


userList = users.query.join(friendships, users.id==friendships.user_id).add_columns(users.id, users.userName, users.userEmail, friendships.id, friendships.user_id, friendships.friend_id).filter(friendships.friend_id == userID).paginate(page, 1, False)
     return render_template('friends.html', userList=userList)


     userList = users.query\
    .join(friendships, users.id==friendships.user_id)\
    .add_columns(users.userId, users.name, users.email, friends.userId, friendId)\
    .filter(users.id == friendships.friend_id)\
    .filter(friendships.user_id == userID)\
    .paginate(page, 1, False)




    user_counts = session.query(
                UserModel.role, 
                func.count(UserModel.role).label("total_counts")
            ).group_by(
                UserModel.role
            ).all()

#THE ABOVE QUERY CAN OUTPUT DATA:
#  +-------------+----------------+
#  | role        | total_counts   |
#  +-------------+----------------+
#  | Admin       | 100            |
#  | Super Admin | 50             |
#  | user        | 1700           |
#  +-------------+----------------+
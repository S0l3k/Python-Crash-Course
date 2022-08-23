from User import User, Admin, Privileges

profile_user = Privileges('a', 's', 'd', '12', 'f', 'g', 'h')
profile_user.privileges()

administrator = Admin('a', 's', 'd', '13', 'q', 'w', 'e')
administrator.show_privileges()
class User():
    """"All information"""

    def __init__(self, f_name, l_name, patronymic, b_day, address, work,
                 study):
        """"Initializes attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.patronymic = patronymic
        self.b_day = b_day
        self.address = address
        self.work = work
        self.study = study
        self.login_attempts = 0

    def describe_user(self):
        """"Describe all user"""
        print(f"\nFirst name: {self.f_name}")
        print(f"Last name: {self.l_name}")
        print(f"Patronymic: {self.patronymic}")
        print(f"Birthday: {self.b_day}")
        print(f"Address: {self.address}")
        print(f"Work in: {self.work}")
        print(f"Study in: {self.study}")

    def greet_user(self):
        """"Greetings"""
        print(f"\nHello dear guest, {self.l_name} {self.f_name}!")

    def increment_login_attempts(self):
        """Increment number of attempt +1"""
        self.login_attempts += 1
        print(f"Increment {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset number of attempt -1"""
        if self.login_attempts >= 0:
            self.login_attempts = 0
            print(f"Profile clear {self.login_attempts}")
        else:
            print(f"Nothing to enter in profile user")

class Admin(User):
    """Preparents User"""

    def __init__(self, f_name, l_name, patronymic, b_day, address, work,
                 study):
        """Copy information about Admin"""

        super().__init__(f_name, l_name, patronymic, b_day, address, work,
                 study)

    def show_privileges(self):
        """Show privileges Admin"""

        privileges = ('can add message', 'can delete user', 'can banned user')
        print(f"Admin can do {privileges}")

administrator = Admin('Vadim', 'N', 'D', '19.06.2001', 'None','free',
                      'university')

administrator.show_privileges()
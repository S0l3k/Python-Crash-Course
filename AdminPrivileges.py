from UserOnly import User

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

class Privileges(Admin):
    """Получаем из класса Admin ф-цию show_privileges"""

    def privileges(self):
        """Из класс Admin получаем информацию об методе show_privileges"""

        super().show_privileges()
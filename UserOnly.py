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
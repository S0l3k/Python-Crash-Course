class User():
    """"All information"""

    def __init__(self, f_name, l_name, patronymic, b_day, address, work, study):
        """"Initializes attributes"""
        self.f_name = f_name
        self.l_name = l_name
        self.patronymic = patronymic
        self.b_day = b_day
        self.address = address
        self.work = work
        self.study = study

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

vadim = User('Vadim', 'Novikov', 'Denisovich', '19.06.2001',
             'c.Moscow st.Fsfad h.1 kv.123', 'Uniqlo', 'University')

vadim.describe_user()
vadim.greet_user()
class User:

    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_passowrd):
        self.password = new_passowrd

    def change_job_title(self, new_title_job):
        self.current_job_title = new_title_job

    def get_user_info(self):
        print(
            f"User {self.name} currently works as a {self.current_job_title}. You can contact for email {self.email} ")




# user = User("teste@teste.com", "Ana", "123", "DevOps")
# user.get_user_info()
#
# user2 = User("seila@teste.com", "Clara", "123345", "Suport")
# user2.get_user_info()




from User import *
from post import Post

app1 = User("teste@teste.com", "Ana", "123", "DevOps")
app1.get_user_info()

app2 = User("seila@teste.com", "Clara", "123345", "Suport")
app2.get_user_info()

new_post =  Post("on a secret mission today", app1.name)
new_post.get_post_info()
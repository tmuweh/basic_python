import random
import  urllib.request

def download_web_img(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_img("https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/30708196_1644215269007569_388408615725170688_n.jpg?_nc_cat=0&oh=9a2b2cb172e1c262d4bafe2df91b7f39&oe=5B5069EE")
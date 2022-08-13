from instapy import InstaPy

#login credentials
insta_username = 'mahdi1vep'
insta_password = '12345678m'

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()
session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=600)
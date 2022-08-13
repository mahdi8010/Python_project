from instapy import InstaPy

#login credentials
insta_username = 'sma.group.ir'
#insta_username = 'sma_sarina'
insta_password = '1012345610'

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

session.follow_by_tags(['زعفران'], amount=10)

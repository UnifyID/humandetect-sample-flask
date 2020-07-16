import requests
import os

test_url = os.environ['UnifyIDHerokuURL']
img = open('test.png', 'rb')
files = {'file': img}

r = requests.post(test_url, files=files, data={'token': 'AVQb1Xm4jugWOUZ3iafp8taNEbIV1BZ+V7MbOzV4jqkd2ohxkqnSUducX5bEpVBPRGU7J7isC61atEUjiYo5852Ps96gAu+TDhOKK48qrBxESX31YDIkB+bkfQ/tHOp8VtZwzA6BQh8Sj/vj6YgaBaHhhbDo2n9XZgRNQ6Eo0SQfi88ahAujMf7ERmsdlhUk+pqYOpy/kQ9j9y7/wseX0UCmFrReyk5Kpeau+Ly879zZy/YBRDFd2b2eQtqZXA5g0VrNqqGsuutxboN+BsbB97IiaTLTph2owR5Z7pmJ9saRmA=='})
print(r.text)

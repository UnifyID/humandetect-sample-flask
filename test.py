# Copyright (c) 2020 UnifyID, Inc. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import requests
import os

test_url = os.environ['UnifyIDHerokuURL']
img = open('test.png', 'rb')
files = {'file': img}

r = requests.post(test_url, files=files, data={'token': 'AVQb1Xm4jugWOUZ3iafp8taNEbIV1BZ+V7MbOzV4jqkd2ohxkqnSUducX5bEpVBPRGU7J7isC61atEUjiYo5852Ps96gAu+TDhOKK48qrBxESX31YDIkB+bkfQ/tHOp8VtZwzA6BQh8Sj/vj6YgaBaHhhbDo2n9XZgRNQ6Eo0SQfi88ahAujMf7ERmsdlhUk+pqYOpy/kQ9j9y7/wseX0UCmFrReyk5Kpeau+Ly879zZy/YBRDFd2b2eQtqZXA5g0VrNqqGsuutxboN+BsbB97IiaTLTph2owR5Z7pmJ9saRmA=='})
print(r.text)

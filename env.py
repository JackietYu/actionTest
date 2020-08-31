#注意：.env中变量的写法一般是 TEST_KEY = TEST_VALUE。最好去除每个字符两边的空格，否则加到环境变量里也读取不到
import os

print(os.environ['MY_HUB'])
hub1 = os.getenv('MY_HUB')
hub2 = os.environ.get('MY_HUB')
print(hub1)
print(hub2)

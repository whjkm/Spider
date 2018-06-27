# 最常规的匹配
'''
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())
'''

# 泛匹配
'''
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
'''

# 匹配目标
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
print(result)
print(result.group(1))
print(result.span())
'''

# 贪婪匹配
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
'''

# 非贪婪匹配
'''
import re
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
'''

# 匹配模式
'''
import re
content = '''# Hello 1234567 World_This
# is a Regex Demo
'''
print(len(content))
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result)
print(result.group(1))
'''

# 转义
'''
import re
content = 'price is $5.00'
result = re.match('price is \$5\.00', content)
print(result)
'''

# 总结:尽量使用泛匹配、
# 使用括号得到匹配目标、
# 尽量使用非贪婪模式，
# 有换行符就用re.S

# re.search
# re.search 扫描整个字符串并返回第一个成功的匹配
'''
import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)
'''
'''
import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
'''

# 总结： 为匹配方便， 能用search就不用match

# 匹配演练

import re
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

'''
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result:
    print(result.group(1), result.group(2))
'''

# re.findall
'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])
'''

'''
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
print(results)
for result in results:
    print(result[1])
'''

# re.sub
# 替换字符串中的每一个匹配的子串后返回替换后的字符串
'''
import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
content = re.sub('\d+', '', content)
print(content)
'''

'''
import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
content = re.sub('\d+', 'Replacement', content)
print(content)
'''
'''
import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
content = re.sub('(\d+)', r'\1 8910', content)
print(content)
'''

'''
html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
print(results)
for result in results:
    print(result.strip())
'''

# re.compile
# 将正则字符串编译成正则表达式对象
# 将一根正则表达式串编译成正则对象，以便于复用该匹配模式
'''
import re
content = '''# Hello 1234567 World_This
# is a Regex Demo
'''
pattern = re.compile('Hello.*Demo', re.S)
result = re.match(pattern, content)
# result = re.match('Hello.*Demo', content, re.S)
print(result)
'''

# 实战练习 (豆瓣读书)
import requests
import re
content = requests.get('https://book.douban.com/').text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)



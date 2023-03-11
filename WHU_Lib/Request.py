import requests
import re

Stu_id = "2020302111129"
url = "http://202.114.65.165/libseat-luojia/whu/mobile/login?username="

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

# res = requests.get(url, headers=headers).text

pattern_content = "<div class=\"contentdiv\"[\s\S]+?<\/div>[\s\S]+?<\/div>[\s\S]+?<\/div>[\s\S]+?<\/div>[\s\S]+?<\/div>"
pattern_book = "<input id =\"book\"[\s\S]+?\/>"
pattern_user = "<input id =\"user\"[\s\S]+?\/>"


# Str_content = re.search(pattern_content, res).group()
# Str_book = re.search(pattern_book, Str_content)
# Str_user = re.search(pattern_user, Str_content)
# print(Str_book.group(0))
# print(Str_user.group(0))


def getBook(stu_id=Stu_id):
    URL_TEMP = url + stu_id

    Str_temp = requests.get(URL_TEMP, headers=headers).text
    try:
        Str_content = re.search(pattern_content, Str_temp).group(0)
        Str_book = re.search(pattern_book, Str_content).group(0)
        Str_user = re.search(pattern_user, Str_content).group(0)
    except AttributeError as n:
        return "不在运行时间内"

    return Str_book + '\n' + Str_user

# print(getBook())

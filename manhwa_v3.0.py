import requests
from bs4 import BeautifulSoup
import re
import os

# 1-1030

from manhua3_ui import A

A().aa()

'''
for num1 in range(first, last):
    # 716字符问题无法生成文件夹

    import urllib.request  # url包

    def openUrl(circle):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Host': 'jandan.net'
        }
        req = urllib.request.Request(circle, headers=headers)
        response = urllib.request.urlopen(req)  # 请求
        html = response.read()  # 获取
        html = html.decode("utf-8")  # 解码
        print(html)  # 打印


    if __name__ == "__main__":
        circle = requests.get('https://www.manhwa.cc/book/' + str(num1))

    # circle = requests.get('https://www.manhwa.cc/book/'+str(num1))
    # 将获取的图片地址依次放入count中
    count = []
    # 将获取的网页内容放入BeautifulSoup
    soup = BeautifulSoup(circle.text, 'lxml')
    # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list

    for item_book in soup.select('.d_bg_t'):
        for book_name in item_book.select('a')[0]:
            book_name_clean = book_name.string
            print(num1, book_name_clean)

    for item in soup.select('.d_menu>ul>li'):
        # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
        for a in item.find_all('a'):
            # print('a', a)
            # m 是 img标签中存在的属性
            menu_path = 'https://www.manhwa.cc/' + a.get('href')
            # count.append(menu_path)
            # menu_path_num.append(re.findall(r"\d+\.?\d*", menu_path))
            menu_path_num = re.findall(r"\d+\.?\d*", menu_path)

            # 当前一部书爬取循环，从上面得到每一章地址后，遍历这么多“章”次

            # for num in menu_path_num:
            print('book_url:', menu_path)

            circle = requests.get(menu_path)
            # 将获取的图片地址依次放入count中
            count = []
            # 将获取的网页内容放入BeautifulSoup
            soup = BeautifulSoup(circle.text, 'lxml')

            for title in soup.select('div.fl.r_tab_l'):
                for title in title.find_all('span'):
                    print('title:', title.text)
                    title = title.text

            for item in soup.select('.r_img'):
                # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
                for img in item.find_all('img'):
                    print('img_url:', img)
                    # m 是 img标签中存在的属性
                    img_path = img.get('data-original')
                    count.append(img_path)

            # 用enumerate依次取出count中的图片地址 放入v中
            os.makedirs('D://manhua//整站爬取www.manhwa.cc//整站漫画爬取//' + book_name_clean + '//' + str(title) + '//')
            for i, v in enumerate(count):
                # 将获取的v值再次放入request中进行与网站相应
                image = requests.get(v)
                # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
                with open('D://manhua//整站爬取www.manhwa.cc//整站漫画爬取//' + book_name_clean + '//' + str(title) + '//' + str(
                        i) + '.jpg', 'wb') as file:
                    # with open('C://Users//50159//Desktop//manhua//test//' + str(num1) + '_' + str(i) + '.jpg', 'wb') as file:
                    # content：图片转换成二进制，进行保存。
                    file.write(image.content)
'''                #print(i)


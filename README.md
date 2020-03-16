## 爬取QQ好友列表或定位QQ好友秘密
**可用于爬取QQ好友的列表，或者对QQ好友进行对比找出发秘密的那个人**
**version 1**

[github地址](https://github.com/wvdon/QQ-FirendsOrSecret-List) 记得Star哦

#### 介绍
- 通过selenium对模拟浏览器操作，然后获取QQ好友的列表。
- 在多个好友的情况下可以进行定位发秘密的QQ好友范围。
> - 定位原理是通过不同好友之间的关系进行筛选，因为不同的人看到秘密的可能是朋友，或者朋友的朋友。
> - 对这些看到不同的人同时做差集和子集能够快速定位到好友的范围。
> - 当然参与的人数越多筛选范围就越小。 
- 此程序并非全自动，需要手动点击登录或输入验证码。
#### Secret 
假设1：QQ1,2,3,对于该秘密都显示为朋友，则红色方为初始定位范围。
假设：Q4具有不显示此秘密，或者显示为朋友的朋友，Q5显示为朋友，即初步筛选范围为红色区域
通过重复性的假设1，假设2，范围最后会逐渐缩小。如果你最后还没确信是谁，不妨删除最可疑的好友之后看看是否变化（不建议）
![](http://web.wvdon.com/list.png)
## 使用
Python3 Chrome ChromeDriver

下载 clone
```shell
git clone https://github.com/wvdon/QQ-FirendsOrSecret-List.git
```
安装环境
```shell script
pip install -r requirements.txt
```
安装webdriver,先查看Chrome的版本，安装对于版本的工具。
chrome内打开`chrome://settings/help` 查看版本

下载地址`https://sites.google.com/a/chromium.org/chromedriver/home`
选择对应的版本号和相应操作系统版本。

> 如果你不能访问google，这里为你提供80,81对应的windows版本的webdriver
>
>[80](http://web.wvdon.com/80/chromedriver.exe) 
>[81](http://web.wvdon.com/81/chromedriver.exe)

将 webdriver.exe 复制到 python的安装目录。==记得在friends里面修改你的webdriver的路径==

假设你已经完成以上步骤并没有任何问题了。
## 运行
电脑端登录qq，跳转浏览器后点击一下快速登陆。（目前没实现自动登录）
```shell
python friends.py
```
输入qq号码

### QQ好友筛选分析
```shell script
python locater.py
```
```
输入有为是好友秘密的QQ账号，多个请用空格隔开：>? 5215522
输入有为非好友秘密的QQ账号，多个请用空格隔开：>? 1536516
筛选结果如下:
222
552
``
```


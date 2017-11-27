## 日常开发项目 - 打造自己的专属追剧看片app

### 序 

> 介于[moviecatcher](https://github.com/MrLevo520/moviecatcher)因为索引网站的问题挂掉了，应该是全盘崩的状态，就看作者会不会去修复了，但里面的代码方式是可以借鉴的，套路都是一样的，介于大家对代码解读的难度和兴趣，我准备开启一个项目开发流程，从0开始，带大家最后完成一个整体项目，没有存稿，亚历山大，不过也算强迫自己进行额外学习了！项目会涉及网页解析，爬取，GUI构造，cookie登录等一些列的问题。希望共勉！



### 目的

> 目前影视资源因为xx的原因，很难被大家在网上检索到，特别是需要xx会员等等，个人而言获取影视剧最多的途径是公共号，百度网盘保存什么的，*** 涉及到一些边缘地带，所以打枪的不要，悄悄地做技术就可以了！ ***，跑题了，简单说，就是，聚合~搜索~点击播放~提供下载~一步到位~看片不愁~嗯？



### 目前资源

- (1) http://m.mei123478.com/
- 待定，如有好的公共号可以提供给我，进行资源整合



### 目前问题

1. 一般看剧路线，进入公共号-检索-点击跳转页面-百度云盘保存-登录到自己的百度云盘客户端-在线点击播放
2. 网页版本的网盘链接和密码都是被隐藏的，只能是手机登录端才会看到链接，这就导致电脑用户打开网页后根本无法保存链接，这就很尴尬了，需要手机先保存链接然后再电脑端导出再看，具体的问题大家可以自行打开1.的网页查看资源，所以说，大家悄悄的搞定就可以了~不过说实话，资源整理不易，请不要举报，要记得感谢整理公共号的人，讲真的！

![](https://ws2.sinaimg.cn/large/006tNc79ly1fli4m71cbqj31kw0k71kx.jpg)



**而机智的我~以为藏了链接我就找不到了？**



![](https://ws2.sinaimg.cn/large/006tNc79ly1fli4plw0cxj31kw0e1h3p.jpg)



### To Do

- 网页解析部分
    - [x]  TV show（韩剧，单剧非剧集连载部分） 网盘与密码解析完成 [// Done 2017.11.15](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
    - [x] 美剧，英剧等多剧集连载部分网盘与密码解析完成[// Done 2017.11.17](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
    - [x] 未知剧种类 网盘与密码解析完成[// Done 2017.11.20](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
    - [x] 重构结果文件完成[// Done 2017.11.27](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
    - [ ] what's more？

- GUI搭建部分
    - [ ] 设计Gui 逻辑
    - [ ] 搭建Gui 部件
    - [ ] what's more？

- 自动在线播放部分

  - [ ] 自动登录百度云
  - [ ] 提供在线播放
  - [ ] 提供下载
  - [ ] what's more？

- 版本发布部分

  - [ ] 打包app部分
  - [ ] 版本更迭部分
  - [ ] what's more？

- 修复各种乱七八糟的bugs

  - [x] selenium 获取不到指定标签下的文本 [// Done 2017.11.15](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
  - [x] 查询时并非跳转页面后的首选项是目标文件，需要改进查询精确匹配[// Done 2017.11.20](https://github.com/MrLevo520/SeeMoreM.T/blob/master/CodesModule/getUrlPw.py)
  - [ ] what's more？


### Update

- 第一次更新：2017.11.15
- 第二次更新：2017.11.17
- 第三次更新：2017.11.20 增加单元测试的UnitTest.ipynb文件作为调试记录
- 第四次更新：2017.11.27 重构网页结果解析文件，btw，happy birthday to me


### 最后

> 希望能早点睡觉啊！Launch Day 2017.11.15 02:15 






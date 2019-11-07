# ReptileSomething



## 项目简介
人生苦短 我用python  用一次就爱上了~
用Python弄点有趣的东西玩玩，抓抓小姐姐，写写工具脚本，
抓点有用数据，做下数据分析，以下是我的


## 项目结构

```
├── build(执行相关目录)
│   └── outputs (生成文件目录)
│       ├── documents (生成文档目录)
│       ├── logs (生成日志目录，中途过渡用)
│       ├── pictures (生成图片目录)
│       └── videos (生成非图片类资源目录)
├── code (代码存放目录)
│   ├── analysis (数据分析类)
│   │   ├── CatchWorkingReport.py (抓取2018年政府报告高频词做词云)
│   │   ├── LGDataAnalysis.py (拉取拉勾网2018年Android岗位相关做数据分析)
│   │   ├── WZLYAnalysis.py (Jupyter Notebook分析我主良缘妹子交友信息)
│   │   └── WZLY.ipynb (抓取我主良缘妹子交友数据，并做数据分析)
│   ├── meizi (图片抓取类)
│   │   ├── CatchAiTaoTuPic.py (抓取爱套图网妹子图)
│   │   ├── CatchBcyCosPic.py (抓取半次元Cos图)
│   │   ├── CatchHuaBanPic.py (抓取花瓣网妹子图)
│   │   ├── CatchJianDanMeiziPic.py (抓取煎蛋网妹子图)
│   │   ├── CatchMWeiboPic.py (抓取某个微博里的所有图)
│   │   ├── CatchTieBaPic.py (抓取某个贴吧链接里的所有图片)
│   │   ├── CatchTuChongPic.py (抓取图虫妹子图)
│   │   ├── FuliShePicCatch.py (抓取福利社妹子图)
│   │   ├── GankPicCatch.py (抓取GankIO妹子图)
│   │   └── win400MeituCatch.py (抓取win400妹子图)
│   ├── threading (多线程相关)
│   │   ├── BarrierTest.py (栅栏Barrier使用示例)
│   │   ├── ConditionTest.py (Condition条件变量使用示例，实现简单的生产者与消费者)
│   │   ├── EventTest.py (通用的条件变量Event 使用示例)
│   │   ├── lockTest.py (Lock指令锁的使用示例)
│   │   ├── queueTest.py (队列queue使用示例)
│   │   ├── SemaphoreTest.py (信号量Semaphore的使用示例)
│   │   ├── threadlocalTest.py (线程局部变量使用示例)
│   │   └── TimerTest.py (定时器Timer使用示例)
│   └── tools (工具类)
│       ├── CatchCityCode.py (抓取城市编码)
│       ├── CatchDoubanMusic250.py (抓取豆瓣音乐250写入Excel)
│       ├── CatchIdCardAreaCodeN.py (抓取身份证前6位地区码，新)
│       ├── CatchIdCardAreaCode.py (抓取身份证前6位地区码，旧)
│       ├── CatchPostCode.py (抓取邮政编码)
│       ├── CatchWeChatRes.py (抓取某篇微信文章里所有的图片，语音，视频)
│       ├── CatchXiCiProxyIPs.py (抓取西刺代理中速度较快的代理ip)
│       ├── CsdnLogin.py (CSDN模拟登录)
│       └── CsdnReaderHelper.py (刷CSDN博客访问量脚本)
│       └── WechatXYZHelper.py (基于itchat的机器人，小宇宙新闻群发，自动通过好友申请，自动回复)
├── coderpig_n.py (自己写简易工具模块，版本2)
├── coderpig.py (自己写简易工具模块，版本1)
├── config.py (配置文件，目前主要用于指定输出路径)
├── dldl.py (斗罗大陆 ting56连接抓取)    
├── locustio.py (蝗虫web&api并发测试)    
├── md5sign.py (tensentAi 签名)    
├── wx_robot.py (微信机器人自动聊天 加好友 等等功能 需要完善功能 加微信好友)    
├── spiderCase.py (给朋友写的企业抓取数据)    
├── spiderNews.py (同上)    
├── spiderProduct.py (同上)    
├── workThread.py (“多线程” code说明 实践是检验真理的唯一标识)
├── LICENSE (授权文件)
├── proxy_ip.txt (代理ip列表文件)
├── README.md
└── tools.py (自己写简易工具模块，版本3)

```
如有其它文件未更新 请见谅 也不是懒  就是不想动~

## 项目说明

不定期更新脚本，脚本失效了，或者你有想抓的网站，想做的小工具，欢迎提issues    
喜欢光脚盆友的，可以加下我微信！    
![微信二维码](https://img-blog.csdnimg.cn/20191107155108438.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2phY2tib244,size_16,color_FFFFFF,t_70)

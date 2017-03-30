
	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
##python版本问题解决方法

####参考  
	Windows 下 Python2 与 Python3 共存的环境配置
		https://www.v2ex.com/t/282819
	python virtualenv使用 解决依赖、版本等问题 
		http://www.ttlsa.com/python/python-virtualenv/
	命令行帮助virtualenv -h
### 1 python两版本安装
	目前已解决,python目录安装在D:\Posoft\Python  
	安装方法:
		首先安装python27,安装选项不安装环境变量
		再安装python35 安装环境变量,所有用户 使用打勾
		path 添加D:\Posoft\Python\Python27\Scripts
		
	使用方法
		27版本 启动: 命令行py或使用py -2  使用pip install
		35版本 启动: 命令行python或使用py-3 使用pip2 install
### 2 解决不同项目依赖不同库,python版本问题
	pip install virtualenv  把virtualenv 安装到python3的库
	
	使用帮助cmd>virtualenv
			   >virtualenv -h
	使用>virtualenv venv  创建默认的python35版的依赖和库
		>virtualenv -p D:\Posoft\Python\Python27\python.exe venv27 创建27版
		>D:\_python>virtualenv -p D:\Posoft\Python\Python27\python.exe --no-site-packages myvenv27 创建无依赖27版
		>deactivate 退出项目
	
	PS:linux可以使用方便的virtualenvwrapper来管理（新增，删除，复制）切换虚拟环境

### 3 在独立的依赖环境安装flask
	参考安装Flask 
		http://docs.jinkan.org/docs/flask/installation.html#virtualenv
	>mkdir myproject
	>cd myproject
	>virtualenv venv  文件夹中多了venv目录
	>venv\scripts\activate 激活虚拟项目
	测试是否成功
		>python
		>>>from flask import Flask 不报错
		在其他目录>python
				  >>>from flask import Flask 报错
		说明flask框架只安装在了venv虚拟项目里

4 安装flask的demo教程:flaskr注意要点

	1 首先在windows安装sqlite3
	2 复制.10版本的flaskr
		修改里面flaskr.py
			# configuration
			DATABASE = 'flaskr.db'
			DEBUG = True
			SECRET_KEY = 'development key'
			USERNAME = 'admin'
			PASSWORD = '123456'
			
		PS:如果已有数据库可以
			# init_db()
	在myproject目录
		myproject>python flaskr\flaskr.py
		在当前目录会生成flaskr.db
		http://localhost:5000/成功运行
###语法略记
	格式
		整数
	>>> 'd' % 2
	'2'
	>>> '%3d' % 2
	'  2'
		浮点数
	>>> '%f' % 3.1415
	'3.141500'
	>>> '%.2f' % 3.1415
	'3.14'
    	转码
	#由于Python的字符串类型是str，在内存中以Unicode表示，
	#一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，
	#就需要把str变为以字节为单位的bytes。
	>>> 'arpher'.encode('ascii')
	b'arpher'
	>>> '阿福'.encode('utf-8')
	b'\xe9\x98\xbf\xe7\xa6\x8f'
	#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
	#要把bytes变为str，就需要用decode()方法：
	>>> b'arpher'.decode('ascii')
	'arpher'
	>>> b'\xe9\x98\xbf\xe7\xa6\x8f'.decode('utf-8')
	'阿福'


# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 09:57
@Auth ： 一条咸鱼
@File ：__init__.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
配置元素
"""
from selenium.webdriver.common.by import By

# -------登陆链接------
url = "http://pc-toutiao-python.itheima.net/#/login"

# -----登陆元素配置信息-----

# 登陆用户名
login_username = By.XPATH, "//input[@placeholder='请输入手机号']"

# 登陆验证码
login_code = By.XPATH, "//input[@placeholder='验证码']"

# 点击登陆按钮
login_click = By.XPATH, "//button[@class='el-button el-button--primary']"

# 登陆成功 关闭
login_X = By.XPATH, "//div[@class='el-notification__closeBtn el-icon-close']"

# 登陆用户名
login_success_username = By.XPATH, "//span[@class='user-name']"

# 退出按钮
login_quit = By.XPATH, "//li[@class='el-dropdown-menu__item el-dropdown-menu__item--divided']"

# 登陆成功断言
login_success = By.XPATH, "//span[@class='company-container']"

# ----------配置发布文章信息-----------

# 内容管理
content_management = By.XPATH, "//div[2]//li[1]//div[1]//span[1]"

# 发布文章
content_article = By.XPATH, "//*[contains(text(),'发布文章')]"

# 文章标题
content_title = By.XPATH, "//input[@placeholder='文章名称']"

# 文章内容 frame

content_frame = By.CSS_SELECTOR, "#publishTinymce_ifr"

# 文章内容ID

content_text = By.CSS_SELECTOR, "#tinymce"

# 选择图片

content_img = By.XPATH, "//div[@class='single_pic']//img"

# 图片
content_select_img = By.XPATH, "//div[@id='pane-first']//div[1]//img[1]"

# 确定按钮

content_OK_btu = By.XPATH, "//button[@class='el-button el-button--primary']//span"

# 请选择按钮

content_select_btu = By.XPATH, "//button[@class='el-button el-button--primary']//span"

# 请选择按钮
choose = By.XPATH, "//input[@placeholder='请选择']"

# -----------跳转到Git页------------
# git地址
git_Git = By.XPATH, "//li[contains(text(),'git')]"
# 黑马头条标签页
git_heima_title = "黑马头条"
# git 地址标浅页
git_Git_title = "PanJiaChen/vue-element-admin: A magical vue admin                                                                https://panjiachen.github.io/vue-element-admin"
# 新页面

git_new_code = By.XPATH, "//span[contains(text(),'Code')]"

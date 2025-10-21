# 基本配置
import numpy as np
import subprocess as sp
import pyperclip as ppc
from time import sleep as 等_秒
from time import time as 当前秒
import pyautogui as pag
from jieba import cut
import os, requests, json
import re
import logging
logging.getLogger('jieba').setLevel(logging.CRITICAL)

等待_秒 = 等_秒
显示_ = print
是 = True
否 = False

# 执行
def 执行_(命令):
	# 第一步，提取引号内容，被“【引号】”标记位置
	引号内容 = []
	while "“" in 命令 and "”" in 命令:
		引号内容.append(命令[命令.find("“")+1: 命令.find("”")].replace('‘','“').replace('’','”')) # 不含引号本身，并把单引号变成双引号
		命令 = 命令[:命令.find("“")] + '【引号】' + 命令[命令.find("”")+1:] # 不剩下引号
	# 第二步，提取坐标或者去括号
	while '（' in 命令 and '）' in 命令:
		try:
			if np.array(命令[命令.find('（')+1: 命令.find('）')].split('，')).astype(float).dtype == np.dtype('float64'): # 括号内的内容是数字
				命令 = 命令[:命令.find('（')]+'('+命令[命令.find('（')+1: 命令.find('）')].replace('，',',')+')'+命令[命令.find('）')+1:] # 括号外的内容
		except:
			命令 = 命令.replace(命令[命令.find('（'): 命令.find('）')+1], '') # 作为注释被去除
	# 第三步，正常处理
	命令 = 命令.replace('！', "\n").replace("!", "\n").replace("；", '\n').replace(";", '\n').replace("。", '\n').replace('：', '冒号')
	# 第四步换行并逐行读取
	命令 = 命令.replace('，', "\n")
	命令 = 命令.split('\n')
	正在处理第_个引号 = 0
	for 结构 in 命令: # 注：后期结构化数据与格式化数据可以并行计算
		# 结构化，引号优先级最高，在最开始已经处理
		坐标内容 = []
		数值内容 = []
		while '(' in 结构 and ')' in 结构:
			坐标内容.append(结构[结构.find('(')+1: 结构.find(')')]) # 填进来的时候不包括括号
			结构 = 结构.replace(结构[结构.find('('): 结构.find(')')+1], '【坐标】') # 这种括号目前只有坐标会有
		数据分析 = list(cut(结构))
		for i in range(len(数据分析)):
			if 48<=ord(数据分析[i][0])<=57:
				数值内容.append(数据分析[i])
				数据分析[i]='【数值】' # 直接的数值
		结构 = ''.join(数据分析)
		# 格式化数据
		本行数据 = []
		while '【' in 结构:
			if 结构[结构.find('【'):结构.find('】')+1]=='【引号】':
				本行数据.append('"'+引号内容.pop(0)+'"')
				结构 = 结构[:结构.find('【')] + '_' + 结构[结构.find('】')+1:]
			elif 结构[结构.find('【'):结构.find('】')+1]=='【坐标】':
				本行数据.append(坐标内容.pop(0))
				结构 = 结构[:结构.find('【')] + '_' + 结构[结构.find('】')+1:]
			elif 结构[结构.find('【'):结构.find('】')+1]=='【数值】':
				本行数据.append(数值内容.pop(0))
				结构 = 结构[:结构.find('【')] + '_' + 结构[结构.find('】')+1:]
		# 执行
		exec(结构+'('+', '.join(本行数据)+')') if 结构!='' else 0



# 机关区
def 机关区():
	while 是:
		输入 = input('【我】')
		try:
			执行_(输入)
		except:
			try:
				显示_(f"【火小兔】：“{对话冒号_(输入)}”")
			except:
				显示_('【ToT】：“我怎么被关起来了? ”')

# 把_重复_次
def 把_重复_次(命令, 次数):
	for i in range(次数):
		执行_(命令)

# 指定的秒内一直重复
def 指定_秒内一直重复_(秒数, 命令):
	起点 = 当前秒()
	终点 = 起点
	while 终点-起点<秒数:
		执行_(命令)
		终点 = 当前秒()

# 系统操作
def 休眠():
	sp.run(['PowerShell', '-Command', 'shutdown -h'])
def 关机():
	sp.run(['PowerShell', '-Command', 'shutdown -s -f -t 00'])
def 重启():
	sp.run(['PowerShell', '-Command', 'shutdown -r -f -t 00'])

def 打开程序_(地址):
	sp.run(['PowerShell', '-Command', f'start {地址}'])

def 打开_(程序):
	pag.press('win')
	打出_(程序)
	回车()

def 卸载():
	sp.run(['PowerShell', '-Command', 'start ms-settings:appsfeatures'])

## 启动一个程序，也可以用于快速切换到该活动界面
def 记录步骤():
	sp.run(['cmd', '/c', 'psr'])
教别人如何操作 = 记录步骤
教他人如何操作 = 教别人如何操作

def 记事本():
	打开程序_('notepad')

def QQ邮箱():
	sp.run(['PowerShell', '-Command', 'start "https://mail.qq.com/"'])

def 文件传输助手():
     打开程序_('https://szfilehelper.weixin.qq.com')

## 接入AI
### 360智脑
def 对话冒号_(内容):
  url = "https://api.360.cn/v1/chat/completions"
  payload = json.dumps({
    "model": "360gpt-pro",
    "messages": [
      {
        "role": "user",
        "content": 内容
      }
    ],
    "stream": False,
    "temperature": 0.9,
    "max_tokens": 2048,
    "top_p": 0.5,
    "top_k": 0,
    "repetition_penalty": 1.05,
    "num_beams": 1,
    "user": "andy"
  })
  headers = {
    'Authorization': 'fk1357707141.BSCoDrkjDWq4N2aiATwpNRVnUL7WKimz726d4e68', # Replace it with your api key like this
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return eval(response.text.replace('null', 'None'))['choices'][0]['message']['content']

# 文件操作

def 复制():
	pag.hotkey('ctrl', 'c')

def 粘贴():
	pag.hotkey('ctrl', 'v')

def 新建():
	pag.hotkey('ctrl', 'n')

def 保存():
	pag.hotkey('ctrl', 's')

def 全选():
	pag.hotkey('ctrl', 'a')

def 打出_(文字=''):
    text = ppc.paste()
    ppc.copy(文字)
    粘贴()
    ppc.copy(text)

def 按下_(键盘):
	pag.press(键盘)

def 外化_(文本):
    ppc.copy(文本)
输出_ = 外化_

def 内化信息():
   return ppc.paste()
吸收信息 = 内化信息

##Excel转置内加工
def 竖变横内加工():
	复制()
	数据 = ppc.paste().replace('\r\n','\t')
	ppc.copy(数据)
def 横变竖内加工():
	复制()
	数据 = ppc.paste().replace('\t','\n')
	ppc.copy(数据)

# 界面操作

def 切换界面():
   pag.hotkey('alt', 'tab')

def 切换桌面():
   pag.hotkey('win', 'tab')

def 查找_(目标):
	pag.hotkey('ctrl', 'f')
	打出_(目标)

## 点击指定位置
def 鼠标移到_(长, 宽):
	pag.moveTo(长, 宽)
def 点击_(长, 宽):
	pag.moveTo(长, 宽)
	pag.click()
单击_ = 点击_

def 右击_(长, 宽):
	pag.moveTo(长, 宽)
	pag.rightClick()

## 鼠标从位置1拉到位置2
def 选中_到_(位置1长,位置1宽, 位置2长,位置2宽):
	pag.moveTo(位置1长,位置1宽)
	pag.mouseDown()
	pag.moveTo(位置2长,位置2宽)
	pag.mouseUp()

## 双击
def 左键双击_(长, 宽):
    pag.moveTo(长, 宽)
    pag.doubleClick()

def 右键双击_(长, 宽):
    pag.moveTo(长, 宽)
    pag.doubleClick(button='right')

## 关闭
def 关闭页面():
	pag.hotkey('ctrl','w')

def 关闭程序():
	pag.hotkey('alt','f4')

## 缩放
def 放大():
	pag.hotkey('ctrl', '+')

def 缩小():
	pag.hotkey('ctrl', '-')

def 全屏():
	pag.press('f11')

def 回车():
	pag.press('enter')

def 最大化():
	pag.hotkey('win', 'up')
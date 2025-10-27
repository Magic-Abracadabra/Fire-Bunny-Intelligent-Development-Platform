from fbidp import *
import sys
执行_('显示“【火小兔】：‘你好呀！我是火小兔！’”')
if len(sys.argv)==1:
	机关区()
else:
	with open(sys.argv[1], encoding='utf-8') as 秘籍:
		咒语 = 秘籍.read()
	try:
		执行_(咒语)
	except:
		pag.alert('【ToT】', '机关区')

	秘籍.close()

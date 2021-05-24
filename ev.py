import os
import time

# exit=0

# 妈的 windows setx 自动truncate把我搞了个半死
# 使用pathed来实现path的添加，具体见 http://p-nand-q.com/download/gtools/pathed.html

# cur_dir=os.getcwd()

while 1:
	ev_name=input("EV name:")
	ev_value=input("EV value:")
	temp_or_not=input("Temp?[Not Default]:")	
	topath_or_not=input("Add2Path?[Yes Default]")

	if temp_or_not!="y" and temp_or_not!= "temp":
		comm=f"setx {ev_name} {ev_value}"
		os.system(comm)
		if topath_or_not!='n':
			# txt_path=f"{cur_dir}{os.sep}cc.txt"

			# 这里不能用ev_name，因为windows比较操蛋的一点在于
			# 他在程序没运行完之前不会自动把ev_name跟你的ev_value进行绑定

			addpath_comm=f"pathed /APPEND {ev_value} /USER"

			print("addpath:",addpath_comm)
			time.sleep(5)
			os.system(addpath_comm)
			# with open(txt_path,"r",encoding="utf-8") as f:
			# 	str1=f.read()
			# str2=str1+f"%{ev_name}%;"
			# comm2=f"setx PATH \"%PATH%;{str2}\""
			# os.system(comm2)

	else:
		comm=f"set {ev_name} {ev_value}"
		os.system(comm)

	exit_or_not=input("quit?[y for yes]")
	if exit_or_not=='y':
		break
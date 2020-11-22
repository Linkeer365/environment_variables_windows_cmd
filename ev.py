import os

# exit=0

while 1:
	ev_name=input("EV name:")
	ev_value=input("EV value:")
	temp_or_not=input("Temp?[Not Default]:")

	if temp_or_not!="y" and temp_or_not!= "temp":
		comm=f"setx {ev_name} {ev_value}"
	else:
		comm=f"set {ev_name} {ev_value}"

	os.system(comm)

	exit_or_not=input("quit?[y for yes]")
	if exit_or_not=='y':
		break
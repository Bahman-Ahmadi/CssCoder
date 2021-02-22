'''projectName: CssCoder
projectStartDate: 2020/02/20
projectAuthor: Bahman-Ahmadi
projectProgrammingLanguage: python3
projectInfo: a program for help programmer in writing css codes!
projectVersion: 1.0.0Alpha'''

def add(mode, name, listProperty, listValue):
	if mode == "class": head = f"\n.{name} "+"{\n"
	elif mode == "id": head = f"\n#{name} "+"{\n"
	elif mode == "tag": head = f"\n{name} "+"{\n"
	else: return "SelectorError: selector type is not correct !"
	body = ""
	for Property, Value in zip(listProperty,listValue):
		body += f"   {Property}: {Value};\n"	
	return head + body + "}"

if __name__ == "__main__":
	import langlib1
	print(langlib1.style("","white"),end="")
	addLoop = input(">>> do u want add new style?(y/n): ").lower() == "y"
	result = ""
	while addLoop:
		selectedMode = input(">>> select mode: (tag/class/id): ")
		selectedName = input(f">>> enter {selectedMode}: ")
		addPropertyLoop = input(">>> do u want add a new property?(y/n): ") == "y"	
		properties, values = [], []
		while addPropertyLoop:
			properties.append(input(">>>> enter property name: "))
			values.append(input(">>>> enter property value: "))
			addPropertyLoop = input(">>> do u want add a new property?(y/n): ") == "y"	

		result += add(selectedMode, selectedName, properties, values)
		addLoop = input(">>> do u want add new style?(y/n): ").lower() == "y"
	
	import os
	os.system("clear")
	langlib1.style(result,"lyellow")
	try:
		open("cssCodes.css","x")
		open("cssCodes.css","w").write(result)
	
	except:
		open("cssCodes.css","w").write(result)
	
	finally:
		input()
		print(langlib1.style("css codes saved at cssCodes.css","lgreen"))

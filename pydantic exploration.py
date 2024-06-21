'''selector {
	rules }


if <bool> then <function>

if True:
	name = must be string

*{
	name:{
		type: str
	}
}	


class PydanticModelBase():
	name: str | 




door {
	width: {
		min: 720mm;
	}
}

door[isAccessible=True] {
	width: {
		min: 820mm;
	}
}'''


from pydantic import BaseModel, Field
from pydantic import create_model
from typing import Tuple, List, Literal



rules = {
	"True":{
		"test": {"type":str, "defaultValue":"default value"},
		"helloworld": {"type":str, "defaultValue":"Hello World"}
	}
}


class dynamicChecker(BaseModel):
	#dimensions : Tuple[int, int]
	fruits: Literal["apple", "orange"]
	#install_component_version: str = Field(pattern=r"^[0-9]+.[0-9]+.[0-9]$")

#print(dynamicChecker.schema_json())
#print(dir(dynamicChecker))

checkObject = dynamicChecker(fruits="789123")

for selector, properties in rules.items():
	#print(selector, properties)
	## check selector
	if selector:
		create_model_args = {"__model_name":"newDynamicChecker"} #"test":(str, 'default value')

		for variableName, variableProperties in properties.items():
			
			create_model_args[variableName] = (variableProperties["type"],variableProperties["defaultValue"])

		newDynamicChecker = create_model(**create_model_args)
		a = newDynamicChecker()
		print(a.test)
		print(a.helloworld)

		#newDynamicChecker = create_model("newDynamicChecker", test=(str, 'default value'))
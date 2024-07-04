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


from pydantic import BaseModel, Field, ValidationError
from pydantic import create_model
from typing import Tuple, List, Literal



rules = {
    "True":{
        "test": {"type": str, "defaultValue": "default value", "pattern": r"^[0-9]+.[0-9]+.[0-9]$"},
        "helloworld": {"type": str, "defaultValue": "Hello World", "pattern": r"^[0-9]+.[0-9]+.[0-9]$"}
    }
}

class dynamicChecker(BaseModel):
    #dimensions: Tuple[int, int]
    fruits: Literal["apple", "orange"]
    #install_component_version: str = Field(pattern=r"^[0-9]+.[0-9]+.[0-9]$")

#print(dynamicChecker.schema_json())
#print(dir(dynamicChecker))

checkObject = dynamicChecker(fruits="apple")

for selector, properties in rules.items():
    #print(selector, properties)
    if selector:
        model_name = "newDynamicChecker"
        create_model_args = {}

        for variableName, variableProperties in properties.items():
            field_args = {}
            if "pattern" in variableProperties:
                field_args["pattern"] = variableProperties["pattern"]
            create_model_args[variableName] = (variableProperties["type"], Field(default=variableProperties["defaultValue"], **field_args))

        newDynamicChecker = create_model(model_name, **create_model_args)
        
        try:    
            a = newDynamicChecker()
            print(a)
        except ValidationError as e:
            print(f"Validation error: {e}")

try:
    # Valid case: Matches the pattern
    valid_instance = newDynamicChecker(test="1.2.3", helloworld="0.5.6")
    print(valid_instance)

    # Invalid case: Does not match the pattern
    invalid_instance = newDynamicChecker(test="123", helloworld="abc")
except ValidationError as e:
    print(f"Validation error: {e}")
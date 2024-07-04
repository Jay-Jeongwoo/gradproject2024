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
        "test": {"type": str, "default": "default value", "pattern": r"^[0-9]+.[0-9]+.[0-9]$"},
        "helloworld": {"type": str, "default": "Hello World", "pattern": r"^[0-9]+.[0-9]+.[0-9]$"},
        "evenNumber": {"type": int, "default": 0, "multiple_of":2},
        "choiceTest": {"_choices": ["apple","banana"]}
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
            #field_args = {}
            #if "pattern" in variableProperties:
                #field_args["pattern"] = variableProperties["pattern"]
            # field_args = {"default": "Hello World", pattern":"blahwhatever"}
            # default=variableProperties["defaultValue"]

            fieldType = variableProperties.pop("type")
            if "_choices" not in variableProperties:
                create_model_args[variableName] = (fieldType, Field(**variableProperties))
            if "_choices" in variableProperties:
                create_model_args[variableName] = (fieldType, variableProperties["_choices"])
                #print(create_model.__doc__)
        newDynamicChecker = create_model(model_name, **create_model_args)
        
        try:    
            a = newDynamicChecker()
            print(a)
        except ValidationError as e:
            print(f"Validation error: {e}")

try:
    # Valid case: Matches the pattern
    valid_instance = newDynamicChecker(test="1.2.3", helloworld="0.5.6", choiceTest="orange")
    print(valid_instance)

    # valid_instance = newDynamicChecker(test="1.2.3", helloworld="0.5.6", evenNumber=3)
    # Invalid case: Does not match the pattern
    # invalid_instance = newDynamicChecker(test="123", helloworld="abc")
except ValidationError as e:
    print(f"Validation error: {e}")
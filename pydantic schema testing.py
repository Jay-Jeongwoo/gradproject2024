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
	dimensions : Tuple[int, int]
	fruits: Literal["apple", "orange",55]
	# install_component_version: Field(pattern=r"^[0-9]+.[0-9]+.[0-9]$")

test = dynamicChecker(dimensions=["hello","world"],fruits=55)
json_schema = dynamicChecker.schema_json(indent=2)

print(json_schema)

from datamodel_code_generator import DataModelType, PythonVersion
from datamodel_code_generator.model import get_data_model_types
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser

data_model_types = get_data_model_types(
    DataModelType.PydanticV2BaseModel,
    target_python_version=PythonVersion.PY_311
)
parser = JsonSchemaParser(
   json_schema,
   data_model_type=data_model_types.data_model,
   data_model_root_type=data_model_types.root_model,
   data_model_field_type=data_model_types.field_model,
   data_type_manager_type=data_model_types.data_type_manager,
   dump_resolve_reference_action=data_model_types.dump_resolve_reference_action,
                       )
result = parser.parse()

print(result)

exec(result)

print(DynamicChecker)
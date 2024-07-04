import json
from datamodel_code_generator import DataModelType, PythonVersion
from datamodel_code_generator.model import get_data_model_types
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
data_model_types = get_data_model_types(
			DataModelType.PydanticV2BaseModel,
			target_python_version=PythonVersion.PY_311
		)
'''jsonSchema ={
	"properties": {
		"fruits": {
			"enum": [
				"apple",
				"orange",
				55
			],
			"title": "Fruits"
		}
	},
	"required": [
		"fruits"
	],
	"title": "dynamicChecker",
	"type": "object"
}'''

rules = {
		"True":{
				"choiceTest": {"enum": ["apple","banana",55]},
				"arrayTest": {"maxItems": 2,"minItems": 2,"prefixItems": [{"type": "integer"}, {"type": "integer"} ], "type": "array"},
				# "patternTest": {"pattern":"^[0-9]+.[0-9]+.[0-9]$","type": "string"}
		}
}



for selector, properties in rules.items():
	#print(selector, properties)
	if selector:
		baseSchema = {"title": "dynamicChecker", "type": "object", "properties":{}, "required":[]}
		for variableName, variableProperties in properties.items():
			fieldDictionary = {"title":variableName}
			#if "choices" in variableProperties:
				#fieldDictionary["enum"] = variableProperties["choices"]
			
			fieldDictionary.update(variableProperties)
			baseSchema["properties"][variableName] = fieldDictionary
			#could have if required
			baseSchema["required"].append(variableName)
			#print(variableName,variableProperties)
		print(baseSchema)
		jsonSchema = json.dumps(baseSchema)
		parser = JsonSchemaParser(
		   jsonSchema,
		   data_model_type=data_model_types.data_model,
		   data_model_root_type=data_model_types.root_model,
		   data_model_field_type=data_model_types.field_model,
		   data_type_manager_type=data_model_types.data_type_manager,
		   dump_resolve_reference_action=data_model_types.dump_resolve_reference_action,)
		result = parser.parse()

		print(result)

		exec(result)

		print(DynamicChecker)

test = DynamicChecker(choiceTest=55, arrayTest=["hello","world"])
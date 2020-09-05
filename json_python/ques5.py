import json
def is_complex_num(objct):
	if '_complex_'in objct:
		return complex(objct["real"],objct['img'])

	return objct
complex_object=json.loads('{"_complex_":true,"real":4, "img":5}',object_hook=is_complex_num)
simple_object=json.loads('{"real":4,"img":3}',object_hook=is_complex_num)
print("complex_object",complex_object)

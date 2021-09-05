
def exponen(base,exponent):
	CONST = 1000000009
	if base == 1:
		return 1
	result =1
	while exponent >0:
		if exponent &1:
			result=result *base % CONST
		exponent =exponent >>1
		base =base **2 %CONST
	return result

print exponen(133,13333)
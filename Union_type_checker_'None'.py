from typing import Union, optional

union: Union[int, None] = None   # 10
optional: Optional[int] = None

# From python 3.10, works
var: int | None = 20

# Do not Do this
wrong: int or None = None

# Wrong answer - don't use it

print(int or None)
print(type(int or None))

<class 'int'>
<class 'type'>

# Correct answer - use this

# print(int | None)
# print(type(int | None))

# int | None
# <class 'types.UnionType'>

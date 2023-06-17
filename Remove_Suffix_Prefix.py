# Left white space and right white space remove by strip()
# removeprefix = 'abc' Prefix remove from here
# removesuffix = 'ghk' Suffix remove from here 

string_sup_pre = "    abcPythonghk    "

string_sup_pre = string_sup_pre.strip()

string_sup_pre = string_sup_pre.removeprefix("abc")

string_sup_pre = string_sup_pre.removesuffix("ghk")

print(string_sup_pre)

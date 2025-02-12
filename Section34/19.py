
# Multiple Arguments Call
# Insert the proper value/-s inside foo() in line 5 so that the script outputs [2, 6, 10] .

# Do not change the foo function definition. Just write the proper values in the function call.

def foo(*args):
    double_list = [x*2 for x in args]
    return double_list
    
print(foo(1,3,5))
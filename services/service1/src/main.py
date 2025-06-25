from common.src.utils import add, sub

def super_calc(a:int, b:int):
    print(f"calc -> add: {add(a,b)}, subs: {sub(a,b)}")
    return add(a,b) - sub(a,b)

def super_dumb_calc(a:int, b:int):
    print(f"dumb_calc -> add: {add(a,b)}, subs: {sub(a,b)}")
    return sub(a,b) - add(a,b)



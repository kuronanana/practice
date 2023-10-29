# 無條件進位浮點數並回傳整數

def ceil_float(num):
	integer_part = int(num)
	if num >0 and num != float(integer_part):
		return integer_part +1
	
	return integer_part

number = float(input("輸入一個浮點數: "))
print(f"無條件進位後的整數為:{ceil_float(number)}")


#判斷三角形類型

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "非三角形"
    
    is_right_angle = (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a)
    
    if a == b == c:
        return "正三角形"
    elif a == b or a == c or b == c:
        if is_right_angle:
            return "等腰直角三角形"
        else:
            return "等腰三角形"
    elif is_right_angle:
        return "直角三角形"
    else:
        return "其他"

a, b, c = map(int, input("請輸入三個整數: ").split())
print(f"該三角形為: {triangle_type(a, b, c)}")

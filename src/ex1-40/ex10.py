# escape scequence 转义字符

# \t 意味着 8 个字符的缩进
taddy_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"

# 字符串内显示 \ 的方式是 \\ 
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a listt:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(taddy_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

temp = "I'm a {} man \"why not\""
print(temp.format("handsome"))

#字符串实战练习 - split和strip
print("===字符串分割与清理实战===")

#场景1：split分割字符串
print("\n1.split()方法：字符串分割")
sentence="苹果,香蕉,橙子,西瓜"
fruits_list=sentence.split(",")#以逗号为分隔符进行分割
print(f"原始字符串:{sentence}")
print(f"分割后的列表:{fruits_list}")
print(f"现在我可以单独访问第二个水果:{fruits_list[1]}")

#场景2:strip清理字符串
print("\n2.strip()方法：清理空白字符")
user_input="  你好,世界! "
cleaned_input=user_input.strip()
print(f"清理前:{user_input}")
print(f"清理后:'{cleaned_input}'")
print(f"长度对比：清理前{len(user_input)}字符，清理后{len(cleaned_input)}字符")

#场景3:综合应用 - 处理用户输入
print("\n3.综合应用:处理用户输入的标签")
tags_input="  python,编程,学习,算法  "#用户输入可能带有空格
print(f"原始输入:'{tags_input}'")

#先清理，再分割
cleaned_tags=tags_input.strip()   #先去掉首尾空格
tags_list=cleaned_tags.split(",")  #按逗号分割
print(f"清理后:'{cleaned_tags}'")
print(f"分割结果:{tags_list}")

#进阶：进一步清理每个标签的空格
final_tags=[tag.strip() for tag in tags_list]
print(f"最终标签列表:{final_tags}")

print ("\n🎯 实战总结：")
print("split() - 像用剪刀把字符串剪成多段")
print("strip() - 像用橡皮擦擦掉字符串两端的空白")

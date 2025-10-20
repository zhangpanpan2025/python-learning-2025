#学习重启计划——2025年10月15日
from datetime import datetime
print("🌟学习之旅在2025年10月15日重新起航!")

#1.精确时间计算
start_date=datetime(2025,10,15)
end_date=datetime(2026,1,19)
days_remaining=(end_date - start_date).days
print(f"今天是{start_date.strftime('%Y年%m月%d日')}")
print(f"⏳距离寒假({end_date.strftime('%Y年%m月%d日')})还有{days_remaining}天")

#可行性分析
hours_per_day=1.5
total_hours=days_remaining*hours_per_day
print(f"💪每天学习{hours_per_day}小时,累计还可学习{total_hours}小时")

#3.核心目标
print("\n🎯未来两周核心目标(10.15-10.31):")
phase1_goals=[
    "完成小甲鱼前20集视频学习",
    "建立每日编码习惯(VSCode+GitHub)",
    "完成三个实战小程序"
]

for i,goal in enumerate(phase1_goals,1):
    print(f"{i}.{goal}")

print("\n✅ 全新的开始,全新的进度!")
print("   从今天开始,每天都是进步的")

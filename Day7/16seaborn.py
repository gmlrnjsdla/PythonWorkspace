import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
# 사람의 특징별 종업원에게 주는 팁 데이터

# print(tips)
# print(tips.describe())
tips_day = tips.groupby('day').tip.sum()    # 요일별 팁의 합계
# print(tips_day)

xlabel = ['Thur', 'Fri', 'Sat', 'Sun']
sns.barplot(x = xlabel, y=tips_day)

plt.show()

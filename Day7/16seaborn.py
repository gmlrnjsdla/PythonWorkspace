import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
# 사람의 특징별 종업원에게 주는 팁 데이터

# print(tips)
# print(tips.describe())
tips_day = tips.groupby('day').tip.sum()    # 요일별 팁의 합계
print(tips_day)

male_tip = tips[tips['sex']=='Male'].groupby('day').tip.sum()
# 요일별 남자 팁의 합계
female_tip = tips[tips['sex']=='Female'].groupby('day').tip.sum()
# 요일별 여자 팁의 합계


xlabel = ['Thur', 'Fri', 'Sat', 'Sun']
index = [0, 1, 2, 3]

p1 = plt.bar(index, male_tip)
p2 = plt.bar(index, female_tip)

plt.legend((p1[0], p2[0]), ('Male', 'Female'))

# sns.barplot(x=xlabel, y=tips_day)


plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")



# 연령대 별 구매자 수
#막대그래프 시각화
bins = [10, 19, 29, 39, 49, 59, 69, 100]  # 나이 구간 설정
labels = ["10s", "20s", "30s", "40s", "50s", "60s", "over 70s"]  # 범주 이름
df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)
age_group_counts = df["Age Group"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette="viridis")
plt.xlabel("age", fontsize=12)
plt.ylabel("number of buyer", fontsize=12)
plt.title("buyers by age group ", fontsize=14)

# 파이 차트 시각화
plt.figure(figsize=(7, 7))
colors = sns.color_palette("GnBu", len(age_group_counts))  # 색상 설정
plt.pie(
    age_group_counts,
    labels=age_group_counts.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
    wedgeprops={'edgecolor': 'black'}
)
plt.title("buyers by age group", fontsize=14)
plt.show()

#상품 카테고리별 구매자수
plt.figure(figsize=(8, 4))
sns.countplot(x="Product Category", data=df, hue ="Gender")
plt.title("correlation between gender and product category")
plt.xlabel("Category")
plt.ylabel("Gender")
plt.show()


#상품 리뷰 평점과 반품률 사이의 상관관계
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Review Rating", y="Return Rate", data=df, hue="Gender", palette="Set2")
plt.title("correlation between product review ratings and return rates")
plt.xlabel("review rating")
plt.ylabel("return rate")
plt.show()

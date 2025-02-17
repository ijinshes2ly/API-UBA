```python

import matplotlib.pyplot as plt

# CSV 파일 로드
csv_filename = "google_analytics_data.csv"
google_analytics_data = pd.read_csv(csv_filename)

# 주요 지표 계산
total_sessions = google_analytics_data["Sessions"].sum()
total_users = google_analytics_data["Users"].sum()
total_new_users = google_analytics_data["New_Users"].sum()
total_pageviews = google_analytics_data["Pageviews"].sum()
avg_pages_per_session = round(google_analytics_data["Pages_per_Session"].mean(), 2)

# 신규 사용자 비율 계산
new_user_ratio = round((total_new_users / total_users) * 100, 2)

# 데이터 시각화: 세션 수 및 페이지뷰 수
plt.figure(figsize=(10, 5))
plt.plot(google_analytics_data["Date"], google_analytics_data["Sessions"], label="Sessions", marker='o', linestyle='-')
plt.plot(google_analytics_data["Date"], google_analytics_data["Pageviews"], label="Pageviews", marker='s', linestyle='--')
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Daily Sessions and Pageviews")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 데이터 시각화: 신규 사용자 비율
plt.figure(figsize=(8, 5))
plt.bar(["New Users", "Returning Users"], [total_new_users, total_users - total_new_users], color=['blue', 'gray'])
plt.xlabel("User Type")
plt.ylabel("Count")
plt.title(f"New Users vs Returning Users (New User Ratio: {new_user_ratio}%)")
plt.grid(axis='y')
plt.show()

# 데이터 시각화: 세션당 페이지뷰 평균
plt.figure(figsize=(8, 5))
plt.bar(["Average Pages per Session"], [avg_pages_per_session], color='green')
plt.ylabel("Pages per Session")
plt.title("Average Pages per Session Over Time")
plt.ylim(0, max(google_analytics_data["Pages_per_Session"]) + 1)
plt.grid(axis='y')
plt.show()

# 주요 지표 출력
summary_metrics = {
    "Total Sessions": total_sessions,
    "Total Users": total_users,
    "Total New Users": total_new_users,
    "New User Ratio (%)": new_user_ratio,
    "Total Pageviews": total_pageviews,
    "Average Pages per Session": avg_pages_per_session,
}

# 데이터프레임 생성 및 출력
summary_df = pd.DataFrame(summary_metrics, index=[0])
print(summary_df)
```

import requests
import openpyxl
from bs4 import BeautifulSoup


url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".rank01 span a")
artists = soup.select(".rank02 span a")

for i, title in enumerate(titles, 1):
    print(f"{i}. {title.text.strip()} - {artists[i-1].text.strip()}")

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "멜론차트"

# 헤더
ws.append(["순위", "곡명", "가수"])

# 데이터 입력
for i, (title, artist) in enumerate(zip(titles, artists), 1):
    ws.append([i, title.text.strip(), artist.text.strip()])

# 저장
wb.save("melon_chart.xlsx")
print("저장 완료!")
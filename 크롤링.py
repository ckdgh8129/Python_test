import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = "Java 백엔드"
url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword={keyword}"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "취업공고"
ws.append(["회사명", "공고제목", "경력", "학력", "지역", "링크"])

for job in soup.select(".item_recruit"):
    title = job.select_one(".job_tit a")
    company = job.select_one(".corp_name a")
    conditions = job.select(".job_condition span")

    if not title or not company:
        continue

    experience = conditions[0].text.strip() if len(conditions) > 0 else ""
    education = conditions[1].text.strip() if len(conditions) > 1 else ""
    location = conditions[2].text.strip() if len(conditions) > 2 else ""
    link = "https://www.saramin.co.kr" + title["href"]

    print(f"{company.text.strip()} | {title.text.strip()} | {experience} | {education} | {location}")
    ws.append([company.text.strip(), title.text.strip(), experience, education, location, link])

wb.save("saramin_jobs.xlsx")
print("저장 완료")
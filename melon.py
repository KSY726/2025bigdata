from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

# 셀레니움 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.melon.com/chart/index.htm"
driver.get(url)
time.sleep(3)

titles = driver.find_elements(By.CSS_SELECTOR, 'div.ellipsis.rank01 > span > a')
artists = driver.find_elements(By.CSS_SELECTOR, 'div.ellipsis.rank02 > span > a')

melon_chart = []
for i in range(len(titles)):
    melon_chart.append({
        "rank": i + 1,
        "title": titles[i].text,
        "artist": artists[i].text
    })


def print_songs(count):
    print(f"\n=== 멜론 TOP {count} ===")
    for song in melon_chart[:count]:
        print(f"{song['rank']}위: {song['title']} - {song['artist']}")


def print_artists(count):
    print(f"\n=== TOP {count} 가수 목록 ===")
    for song in melon_chart[:count]:
        print(f"{song['artist']}")


def ai_recommend_song():
    song = random.choice(melon_chart)
    print("\n=== AI 추천곡 ===")
    print(f"{song['rank']}위: {song['title']} - {song['artist']}")


# 메뉴
while True:
    print("\n===== 멜론 실시간 차트 메뉴 =====")
    print("1. 멜론 TOP 100 출력")
    print("2. 멜론 TOP 50 출력")
    print("3. 멜론 TOP 10 출력")
    print("4. AI 추천곡 출력")
    print("5. TOP 10 가수 목록 출력")
    print("0. 종료")

    menu = input("메뉴 번호를 선택하세요: ")

    if menu == '1':
        print_songs(100)
    elif menu == '2':
        print_songs(50)
    elif menu == '3':
        print_songs(10)
    elif menu == '4':
        ai_recommend_song()
    elif menu == '5':
        print_artists(10)
    elif menu == '0':
        print("프로그램을 종료합니다.")
        driver.quit()
        break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")

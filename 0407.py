import random

# 예시 데이터 : [순위, 노래제목, 가수이름]
melon_chart = [[i+1, f"노래제목{i+1}", f"가수{i%10 + 1}"] for i in range(100)]

def print_songs(count):
    print(f"\n=== 멜론 TOP {count} ===")
    for song in melon_chart[:count]:
        print(f"{song[0]}위 : {song[1]} - {song[2]}")

def ai_recommend_song():
    song = random.choice(melon_chart)
    print(f"\nAI 추천곡 → {song[1]} - {song[2]}")

def search_artist():
    name = input("\n검색할 가수 이름 입력 : ")
    result = [song for song in melon_chart if name in song[2]]
    if result:
        print(f"\n'{name}' 가수의 노래 목록")
        for song in result:
            print(f"{song[0]}위 : {song[1]} - {song[2]}")
    else:
        print(f"\n'{name}' 가수의 노래가 없습니다.")

while True:
    print("\n=== 멜론 차트 메뉴 ===")
    print("1. 멜론 TOP 100 출력")
    print("2. 멜론 TOP 50 출력")
    print("3. 멜론 TOP 10 출력")
    print("4. AI 추천곡 출력")
    print("5. 가수 이름 검색")
    print("0. 프로그램 종료")

    menu = input("메뉴 번호 입력 : ")

    if menu == "1":
        print_songs(100)
    elif menu == "2":
        print_songs(50)
    elif menu == "3":
        print_songs(10)
    elif menu == "4":
        ai_recommend_song()
    elif menu == "5":
        search_artist()
    elif menu == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택하세요.")

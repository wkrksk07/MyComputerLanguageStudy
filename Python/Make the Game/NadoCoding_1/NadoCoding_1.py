# https://youtu.be/kWiCuklohdY 기본편

#str == string / print + 대신 , 가능  / ** 제곱 // 몫  % 나머지 / not or ! 가능 / &&아닌 & 이나 and 쓰기 / || 말고 | 이나 or 쓰기

'''주석처리 하는 법'''

# from random import *

# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# sentence = '나는 소년이다'
# print(sentence)
# sentence2 = "파이썬은 쉽다"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 파이썬은 쉽다 """
# print(sentence3)

# jumin = "990120-1234567"
# print("성별 : " +jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2 직전까지 = 0~1
# print("월 : " +jumin[2:4])
# print("일 :" + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[-7:]) # 뒤에서 부터 -7직전까지

# print("나는 %d살입니다" % 20) # 정수
# print("나는 %s을 좋아한다" % "파이썬") # 문자열
# print("Apple 은 %c로 시작한다" % "A") # 문자
# print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨간"))

# print("나는 {} 살입니다".format(20))
# print("나는 {1}{0}{age} 살입니다".format(20,22, age = 1212))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아한다.")

# print("가나다라마바사 \n 아자차카타파하")
# print('나는 "사람" 입니다')
# print("나는 \"사람\" 입니다")

# #\\ = 문장 내에서 하나의 \ 
# print("C:\\----\\-\\Documents\\---\\-------------LanguageStudy\\Python>")

# #\r = 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# #\b : 백스페이스
# print("Redd\bApple")

# #\t : 탭 역할
# print("Red\tApple")

# url = "https://naver.com"
# my_str = url.replace("https://", "") #https를 찾아 공백으로
# my_str = my_str[:my_str.index(".")] #처음부터 처음나오는 .의 위치직전까지
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{}의 비번은 {}이다.".format(url, password))


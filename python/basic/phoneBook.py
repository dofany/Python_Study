import sys

data = [
    ["지디", "010-111-1111", "서울시 송파구"],
    ["태양", "010-222-2222", "서울시 강동구"],
    ["탑", "010-333-3333", "서울시 광진구"],
    ["대성", "010-444-4444", "서울시 강남구"],
]


a = list(data)
name = sys.argv[1]

for i in range(0,4):
        if name == data[i][0]:
            print("이름 : {}".format(data[i][0]))
            print("전화번호 : {}".format(data[i][1]))
            print("주소 : {}".format(data[i][2]))



n = int(input())
moves = list(map(int, input().split()))

balloons = [(i+1, moves[i]) for i in range(n)]

result = []
idx = 0

while balloons:
    num, move = balloons.pop(idx)
    result.append(num)

    if not balloons:
        break

    if move > 0:
        idx = (idx + (move - 1)) % len(balloons)
    else:
        idx = (idx + move) % len(balloons)

print(*result)

"""
5
3 2 1 -3 -1  >> 1 4 5 3 2 
x d d  d  d
  d d  d  x
  d d  x
  x
    d               
1번째 터트리고 3 나왔으니 -1 
좋은 질문이다 

👍 이 부분에서 많이 헷갈림.

결론부터 말하면
👉 다음은 5번이 아니라 4번이 맞다

🔥 왜 헷갈리냐?

네 생각:

3이니까
2 → 1 → -3 거쳐서
다음은 -1 (5번) 아닌가


👉 여기서 “거친다”의 기준이 틀렸어

🧠 핵심 기준 (중요)

👉 "현재 위치에서 몇 칸 이동해서 도착한 곳"이 다음 풍선

중간에 “거치는 것”은 의미 없음

🎯 실제로 따라가보자

초기 상태:

[ (1,3), (2,2), (3,1), (4,-3), (5,-1) ]
✅ 1번 터짐 (move = 3)

남은 리스트:

[ (2,2), (3,1), (4,-3), (5,-1) ]

현재 위치 = 2번 위치 (index 0)

👉 이동 규칙
move = 3 (양수)
이미 하나 빠졌으니까 → 2칸 이동
👉 이동 과정
현재: 2번 (시작)

1칸 → 3번
2칸 → 4번 ← 도착!

👉 그래서 4번이 다음

❗ 핵심 오류 포인트

너는 이렇게 생각한 거야:

2 → 3 → 4 → 5

👉 이건 3칸 이동을 다 세버린 것

하지만 실제는:

👉 이미 1번에서 출발했기 때문에 1칸 줄여야 함

🔥 직관적으로 기억하는 법

👉 풍선을 터뜨리면

이미 한 칸 이동한 상태라고 생각해라

"""

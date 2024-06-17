import random

for _ in range(5):
    # 1부터 100 사이의 숫자 10개로 랜덤 리스트 생성
    unsorted_data = random.sample(range(1, 1000), random.randint(5, 15))
    sorted_data = sorted(unsorted_data)

    print("Unsorted data:", unsorted_data)
    print("Sorted data:  ", sorted_data)
    print("---" * 10)
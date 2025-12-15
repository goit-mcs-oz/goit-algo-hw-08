import heapq


'''
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
'''


def min_cost(lengths):
    if len(lengths) <= 1:
        return 0

    heapq.heapify(lengths)

    total_cost = 0
    while len(lengths) > 1:
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)
        cost = a + b
        total_cost += cost
        heapq.heappush(lengths, cost)

    return total_cost


lengths = [1, 2, 3]
print(
    f"Мінімальна з можливих сум загальних витрат: {min_cost(lengths)}")


'''
Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.
'''


def merge_k_lists(lists):
    lists = lists.copy()
    merged = []
    min_heap = []

    while (lists):
        list = lists.pop()
        while (list):
            item = list.pop()
            heapq.heappush(min_heap, item)

    while min_heap:
        merged.append(heapq.heappop(min_heap))

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

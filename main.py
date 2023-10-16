# 1
def list_reorder(ref_list):
    names = ref_list[0]
    surnames = ref_list[1]
    result = []

    for name, surname in zip(names, surnames):
        result.append([name, surname])

    return result


# Пример использования
ref_list = [['Имя 1', 'Имя 2'], ['Фамилия 1', 'Фамилия 2']]
reordered_list = list_reorder(ref_list)
print(reordered_list)


# 2
def del_rep(num):
    unique_sorted_list = sorted(list(set(num))
    return unique_sorted_list


# Пример использования
num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
result = del_rep(num)
print(result)


# 3
def lim_max(nums, limit):
    max_value = -1

    for num in nums:
        if num < limit and num > max_value:
            max_value = num

    return max_value


# Пример использования
nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)
limit = 50
result = lim_max(nums, limit)
print(result)


# 4
def temp_cat(temp):
    if temp < -20:
        return 0  # Холодно
    elif -20 <= temp < 0:
        return 1  # Прохладно
    elif 0 <= temp < 15:
        return 2  # Зябко
    elif 15 <= temp < 25:
        return 3  # Тепло
    else:
        return 4  # Жарко


# Пример использования
temp = -30
result = temp_cat(temp)
print(result)



# 5
def check_phn(phones):
    def is_valid_phone(phone):
        if len(phone) != 11 or (phone[0] != '7' and phone[0] != '8'):
            return False

        phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        if not phone.isdigit():
            return False

        return True

    result = []
    for phone in phones:
        if is_valid_phone(phone):
            if phone[0] == '8':
                phone = '+7' + phone[1:]
            result.append(phone)
        else:
            result.append(-1)

    return result


# Пример использования
phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
result = check_phn(phones)
print(result)
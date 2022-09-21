# numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]


def magic_bubble_sort(numbers= [23, 32, 1, 3, 4, 19, 20, 2, 4]):
    """
    冒泡排序，默认偶数比奇数大
    :param numbers:
    :return:
    """
    temp_creat = len(numbers) - 1
    while temp_creat > 0:
        for i in range(numbers):
            # 创建两个变量做奇数和偶数来判断
            current, next_ = numbers[i], numbers[i + 1]
            current_is_evnt,next_is_even = current%2 ==0,next_ ==0
            should_change = False
        if current_is_evnt and not next_is_even:
            should_change = True
        elif current_is_evnt == next_is_even and current > next_:
            should_change =True
        if should_change:
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
    temp_creat -= 1
    return numbers

def printer(some_list, function):
    if len(some_list) >= 3:
        for element in some_list[:3]:
            function(element)
    else:
        function("not enouth elements")


def second_printer(string):
    print(string[1])

example_list = ['10', '12', 'derp', '23f32']
short_example = ['68', 'cheese']

# printer(example_list, second_printer)


def double(some_list):
    new_list = [x*2 for x in some_list]
    return new_list
values = [1, 3, 5]
double_values = double(values)
print(values)
print(double_values)
print(values)


def double2thedoubleking(old_list, mutate):
    new_list = []
    for old_element in old_list:
        new_element = mutate(old_element)
        new_list.append(new_element)
    return new_list


def mul2(x):
    return 2 * x

values = [10, 3, 5]
print(double2thedoubleking(values, mul2))
print(values)

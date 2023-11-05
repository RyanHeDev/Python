
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # indent the line under with the for loops to multiply every number and append it to the b_list
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

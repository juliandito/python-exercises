def is_chain(list_of_string):
    
    status = []

    tmp_item = list_of_string[0]
    tmp_first_char0 = tmp_item[0]
    tmp_last_char0 = tmp_item[len(tmp_item)-1]
    if len(list_of_string) == 2:
        for i in range(1, len(list_of_string)):
            tmp_item = list_of_string[i]
            tmp_first_char = tmp_item[0]
            tmp_last_char = tmp_item[len(tmp_item)-1]

            if tmp_first_char != tmp_last_char0:
                status.append(False)
            else:
                status.append(True)
    else:
        for i in range(1, len(list_of_string)-1):
            tmp_item = list_of_string[i]
            tmp_first_char = tmp_item[0]
            tmp_last_char = tmp_item[len(tmp_item)-1]

            tmp_item2 = list_of_string[i+1]
            tmp_first_char_next = tmp_item2[0]
            tmp_last_char_next = tmp_item2[len(tmp_item2)-1]

            if i == 1:
                if tmp_first_char != tmp_last_char0:
                    status.append(False)
                else:
                    status.append(True)
            else:
                if tmp_first_char_next != tmp_last_char:
                    status.append(False)
                else:
                    status.append(True)

        if tmp_first_char_next != tmp_last_char:
            status.append(False)
        else:
            status.append(True)
    
    flag_false = 0
    for i in range(0, len(status)):
        if status[i] == False:
            flag_false += 1
            print(i)
    
    if flag_false != 0:
        final_status = False
    else:
        final_status = True

    return final_status


#test
list_test = ["camel", "leopard", "dog", "giraffe", "elephant"]
print("kata: ",is_chain(list_test))
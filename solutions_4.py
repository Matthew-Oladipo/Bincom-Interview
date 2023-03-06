# Question 1 solution
def pu_result(polling_unit_uniqueid, announced_pu_results):
    '''
    Returns the result of any polling_unit_uniqueid polling unit in announced_pu_results.
    '''
    for i in announced_pu_results:
        for j in i:
            if j == str(polling_unit_uniqueid):
                print(i[2], i[3])
            else:
                print("Can't find polling_unit_uniqueid")


# Question 2 solution
def lga_result(lga_name, announced_lga_results):
    '''
    Returns the summed total result of all the polling units under any particular local government.
    '''
    for i in announced_lga_results:
        for j in i:
            if j == str(lga_name):
                print(i[2], i[3])
            else:
                print("Can't find lga_name")

# Question 3 solution
def result_all_parties(polling_unit_uniqueid, pu_results):
    '''
    Stores results of all parties for a new polling unit.
    '''
    file = open('newfile.txt', 'a')   #'a' is used to append instead of 'w' which replaces what's in the file every time.
    data = file.write(str(polling_unit_uniqueid) +", "+ str(pu_results))
    return data

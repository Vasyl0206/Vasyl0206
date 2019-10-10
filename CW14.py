def count_positives_sum_negatives(*arr):
    #your code here
    kilk_pos = []
    sum_neg =0
    for i in list(arr):
        if i > 0:
            kilk_pos.append(i) 
        elif i<0:
            sum_neg = sum_neg + i
    return arr,[len (kilk_pos),sum_neg]
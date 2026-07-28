def return_sum(L):
    even_sum = 0
    odd_sum = 0
    div3_sum = 0
    result_sum=0
    
    for i in L:
        if i % 2 == 0:
            even_sum = even_sum + i
        if  i%2 != 0:
            odd_sum = odd_sum + i
            
    return (even_sum,odd)
        
L=[11,14,21,23,56,78,45,29,28]

result = result_sum(L)
print(result)


    
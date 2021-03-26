def productSum(arr,mul=1):
    sum=0
    for element in arr:
        if type(element) is list:
            sum+=productSum(element,mul+1)
        else:
            sum+=element
    return sum * mul

arr=[5,2,[7-1],3,[6,[-13,8],4]]

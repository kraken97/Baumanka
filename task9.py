def trib(n):
    if  n in [0,1]: return 0;
    elif n in [2,3] :return 1;
    else:
         return trib(n-1)+trib(n-2)+trib(n-3);



print([trib(a) for a in range(3,6)])

#данная функция   это аналог рекурсивной фукнции чисел фибоначи , 
# но с тем условием  , что  Fn=F(n-1)+F(n-2)+F(n-3)
# даже не запуская программу легко увидеть 
#что значение 4 елемента "трибоначи" будет сумма первого  , второго , и третьего чисел т.е 0+1+1


#результатом выражения будет массив из 3 чисел [1,2,4]

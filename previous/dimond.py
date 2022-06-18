import math
x=int(input())
for y in range(1,math.ceil(x/2)):
    print(' '*(x-y)+'* '*y)
for y in range(math.ceil(x/2),0,-1):
    print(' '*(x-y)+'* '*y)

'''
                  * 
                 * *
                * * *
               * * * *
              * * * * *
             * * * * * *
            * * * * * * *
           * * * * * * * *
          * * * * * * * * *
         * * * * * * * * * *
          * * * * * * * * *
           * * * * * * * *
            * * * * * * *
             * * * * * *
              * * * * *
               * * * *
                * * *
                 * *
                  *
'''
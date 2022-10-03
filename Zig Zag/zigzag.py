class Solution(object):
    def convert(s, numRows):
        length = len(s)
        columns = 0
        switch = numRows
        final = ""
        while(length > 0):
            if(switch == numRows):
                length = length - switch
                if(numRows >= 3):
                    switch = switch - 2
                columns = columns + 1
            else:
                length = length - switch
                switch = switch + 2
                columns = columns + 1
        indicator = 0
        indicator2 = -1
        for count in range(numRows):
            indicator = indicator + 1
            if(indicator > 3):
                indicator = indicator + 1
        numbersequence = ""
        length = len(s)
        
        for x in range(numRows):
            limit = x+1
            if(x == 0 or x == numRows-1):
                y = columns
                while(y > 0):
                    y = y-2
                    limit = limit + indicator
                    if(y>0 and limit <= len(s)):
                        if(x==0):
                            numbersequence = numbersequence + str(indicator)
                        if(x==numRows-1):
                            numbersequence = numbersequence + str(indicator2)
                indicator = indicator-2
                indicator2 = indicator2 + 2
            else:
                limit = x
                for i in range(columns-1):
                    if((i+1)%2 == 1):
                        limit = limit + indicator + 1
                        if(limit < len(s)):
                            numbersequence = numbersequence + str(indicator)
                    else:
                        limit = limit + indicator2 + 1
                        if(limit < len(s)):
                            numbersequence = numbersequence + str(indicator2)
                
                indicator = indicator-2
                indicator2 = indicator2+2
            numbersequence = numbersequence + "0"
        position = 0      
        numbersequence = numbersequence + "0"
        
        f = 0
        t = 0 
        final = ""
        jump = numbersequence[f]
        for position in range(numRows):
            t = position
            while(int(jump) != 0):
                if(len(final) == len(s)):
                    break
                final = final + s[t]
                jump = numbersequence[f]
                t = t + int(jump) + 1
                f = f + 1
            jump = numbersequence[f]
        return final
    print(convert("YourMessageYouWantToPutInZigZag",6))

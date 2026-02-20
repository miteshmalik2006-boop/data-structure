def plasone(self,digits):
    s=0
    for i in digits:
        s*=10
        s+=1
        while s>0:
            var=s%10
            self.l1.append(var)
            s//=10
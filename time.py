class Time:
    def __init__(self,sec,min,hour):
        self.sec=sec
        self.min=min
        self.hour=hour

    def to_time(self):
        
        self.hour=self.sec//3600
        self.min=self.sec//60
        self.sec=self.sec%60
        if(self.sec>59):
            self.min+=self.sec//60
            self.sec=self.sec%60
        if(self.min>59):
            self.hour+=self.min//60 
            self.min=self.min%60
        
        return self.sec,self.min,self.hour
            

    def to_second(self):
        self.sec=self.hour*3600+self.min*60+self.sec
        #return self.hour
        return self.sec

    def sum(self,t):
        result=Time(0,0,0)
        result.sec=self.sec+t.sec
        result.min=self.min+t.min
        result.hour=self.hour+t.hour
        if(result.sec>59):
            result.min+=result.sec//60
            result.sec=result.sec%60
        if(result.min>59):
            result.hour+=result.min//60 
            result.min=result.min%60
        return result

    def sub(self,t):
        result=Time(0,0,0)
        result.sec=abs(self.sec-t.sec)
        result.min=abs(self.min-t.min)
        result.hour=abs(self.hour-t.hour)
        return result

    def show(self):
        print(self.hour ,":",self.min,":",self.sec)


t1=Time(34,45,10)
t1.show()

t2=Time(32,59,12)
t2.show()

t=t1.sum(t2)
t.show()

t=t1.sub(t2)
t.show()

s=Time(12030,0,0)
sec,min,hour=s.to_time()
print("sec=",sec,"min=",min,"hour=",hour)

tt=Time(30,20,6)
second=tt.to_second()
print("Second=",second)


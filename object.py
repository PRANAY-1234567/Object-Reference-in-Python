class Time:
    def __init__(self, hrs=0, min=0, sec=0):
        self.hrs = hrs
        self.min = min
        self.sec = sec

    def display(self):
        print(f"{self.hrs:02d} : {self.min:02d} : {self.sec:02d}")

t1 = Time(10, 25, 45)
t1.display()

t2 = t1
t2.display()

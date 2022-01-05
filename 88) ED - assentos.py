class SeatMap:
    def __init__(self,width,height,seatlist):
        self.width = width 
        self.height = height
        self.seatlist = seatlist
    
    def seatListOrdenation(self):
        for item in self.seatlist:
            if item[0] > self.width or item[1]>self.height:
                return f"O assento {item} não existe."
            for i in range(len(self.seatlist)-1):
                if self.seatlist[i][1] > self.seatlist[i+1][1]:
                    self.seatlist[i], self.seatlist[i+1] = self.seatlist[i+1], self.seatlist[i]
            
            for i in range(len(self.seatlist)-1):
                if self.seatlist[i][0] > self.seatlist[i+1][0]:
                    self.seatlist[i], self.seatlist[i+1] = self.seatlist[i+1], self.seatlist[i]

            return(self.seatlist)

if __name__ == "__main__":
    seatmap = SeatMap(3,3,[(3,2),(2,0),(0,2),(3,3),(2,2)])
    print(seatmap.seatListOrdenation())

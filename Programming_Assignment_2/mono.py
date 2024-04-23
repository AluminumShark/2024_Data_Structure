import argparse
import numpy as np
import time

class mono_routing():
    def __init__(self, args):
        pass
    def parser(self): #You can modify it by yourself.
        with open("%s" % args.input, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("BoundaryIndex"):
                    value_list = lines.split(' ')
                    self.Bx1 = int(value_list[1])
                    self.By1 = int(value_list[2])
                    self.Bx2 = int(value_list[3])
                    self.By2 = int(value_list[4])
                if lines.startswith("DefaultCost"):
                    value_list = lines.split(' ')
                    self.default_cost = int(value_list[-1])
                if lines.startswith("NumNonDefaultCost"):
                    value_list = lines.split(' ')
                    self.size = int(value_list[-1])
                    break
            
            source_list = list(f[-2].split(' '))
            target_list = list(f[-1].split(' '))
            self.sx = source_list[1]
            self.sy = source_list[2]
            self.tx = target_list[1]
            self.ty = target_list[2]
            """Saving cost"""
            self.NDcost = {}
            for x in range(self.Bx2+1):
                for y in range(self.By2+1):
                    #self.NDcost['%d%d%d%d' %(x,y,x,y+1)] = self.default_cost --> this is wrong
                    self.NDcost[(x,y,x,y+1)] = self.default_cost
            for y in range(self.By2+1):
                for x in range(self.Bx2+1):
                    #self.NDcost['%d%d%d%d' %(x,y,x+1,y)] = self.default_cost --> this is wrong
                    self.NDcost[(x,y,x+1,y)] = self.default_cost
            num_cost = f[3:3+int(self.size)]
            for NDcost in num_cost:
                NDcost_list = NDcost.split(' ')
                if(NDcost_list[4] == 'x'):
                    self.NDcost[(int(NDcost_list[0]), int(NDcost_list[1]), int(NDcost_list[2]), int(NDcost_list[3]))] = 'x'
                else:
                    self.NDcost[(int(NDcost_list[0]), int(NDcost_list[1]), int(NDcost_list[2]), int(NDcost_list[3]))] += int(NDcost_list[4])
    
        """Print parameters"""
        print('BoundaryIndex:',self.Bx1,self.By1,self.Bx2,self.By2)
        print('DefaultCost:',self.default_cost)
        print('NumNonDefaultCost:',self.size)
        for i in range(len(num_cost)):
            print(num_cost[i])
        print('Source:',self.sx, self.sy)
        print('Target:',self.tx, self.ty)
    def routing(self):
        self.routing_path = []
        self.grid_cost = np.full((self.By2+1,self.Bx2+1), float('inf'), dtype='object')
        self.grid_cost[0][0] = 0
        self.prev = np.full((self.By2+1,self.Bx2+1), None, dtype='object')
        # ---TODO:
        # Write down your routing algorithm by using dynamic programming.
        # ---
        for y in range(self.By2+1):
            for x in range(self.Bx2+1):
                if x == 0 and y == 0:
                    continue
                if x > 0:
                    if self.NDcost[(x-1, y, x, y)] != 'x':
                        self.grid_cost[y][x] = min(self.grid_cost[y][x], self.grid_cost[y][x-1] + self.NDcost[(x-1, y, x, y)])
                        self.prev[x][y] = [x-1, y]
                if y > 0:
                    if self.NDcost[(x, y-1, x, y)] != 'x':
                        self.grid_cost[y][x] = min(self.grid_cost[y][x], self.grid_cost[y-1][x] + self.NDcost[(x, y-1, x, y)])
                        if self.grid_cost[y][x] == self.grid_cost[y-1][x] + self.NDcost[(x, y-1, x, y)]:
                            self.prev[x][y] = [x, y-1]
        current = [self.Bx2, self.By2]
        while current:
            self.routing_path.insert(0, current)
            current = self.prev[current[0]][current[1]]


    def output(self): # You can modify it by yourself, but the output format should be correct.
        with open("%s" % args.output, 'w', newline='') as file_out:
            file_out.writelines('RoutingCost %d'% self.grid_cost[self.By2][self.Bx2])
            file_out.writelines('\nRoutingPath %d'% len(self.routing_path))
            for i in range(len(self.routing_path)):
                file_out.writelines('\n%d %d'% (self.routing_path[i][0], self.routing_path[i][1]))
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './5x5.in',help="Input file root.")
    parser.add_argument("--output", type=str, default = './5x5.out',help="Output file root.")
    args = parser.parse_args()

    print('#################################################')
    print('#              Monotonic Routing                #')
    print('################################################# \n')

    routing = mono_routing(args)
    """Parser"""
    routing.parser()
    print('################ Parser Down ####################')
    """monotonic route"""
    start = time.time()
    routing.routing()
    print('run time:', round(time.time()-start,3))
    """output"""
    routing.output()

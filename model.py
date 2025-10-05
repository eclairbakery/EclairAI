import random
import re
import math

DebugMode = False

def Normalize(data):
    t = sum(data)
    if t == 0:
        return 0
    return [x / t for x in data]

class Model:
    Connections = {}

    def Learn(self, data):
        d = data.split()
        for a, b in zip(d, d[1:]):
            if a not in self.Connections:
                self.Connections[a] = {}
            
            if b in self.Connections[a]:
                self.Connections[a][b] += 0.1
            else:
                self.Connections[a][b] = 1.0

        if d:
            l = d[-1]
            if l not in self.Connections:
                self.Connections[l] = {}

        if DebugMode:
            print(self.Connections)


    def Format(self, data):
        return re.sub(r"[!@#$%^&*()\-=+_\[\]{}\\|;':\",.<>/?]", "", data).lower()
    
    def GenerateResponse(self, data):
        r = []
        w = random.choice(list(self.Connections.keys()))
        for i in range(10):
            r.append(w)
            s = self.Connections.get(w, {})
            if not s:
                break
            k = list(s.keys())
            p = Normalize(list(s.values()))
            w = random.choices(k, weights=p, k=1)[0]
        self.LastResponse = " ".join(r)
        return " ".join(r)

test = Model()
while True:
    uin = input("\x1b[92mTy: \x1b[0m")
    test.Learn(test.Format(uin))
    print("\x1b[96mEclairAI: \x1b[0m" + test.GenerateResponse(test.Format(uin)))

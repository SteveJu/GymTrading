import math


def cnd(x):
    a1 = 0.31938153
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429
    one_div_sqrt2pi = 0.39894228040143270286
    L = abs(x)
    K = 1.0 / (1.0 + (0.2316419 * L))
    a12345k = (a1 * K) + (a2 * (K ** 2)) + (a3 * (K ** 3)) + \
              (a4 * (K ** 4)) + (a5 * (K ** 5))
    result = 1.0 - one_div_sqrt2pi * math.exp(-math.pow(L, 2) / 2.0) * a12345k
    if x < 0:
        result = 1 - result
    return result


class models:
    def __init__(self, fCall: int, S: float, X: float, T: float,
                 r: float, v: float, lamb: float, gamma_val: float):
        self.fCall = fCall
        self.S = S
        self.X = X
        self.T = T
        self.r = r
        self.v = v
        self.lamb = lamb
        self.gamma_val = gamma_val
        self.fact_lookup = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    def JumpDiffusion(self):
        result = 0.0
        elT = math.exp(-self.lamb * self.T)
        p2v = math.pow(self.v, 2)
        p2delta = math.pow(math.sqrt(self.gamma_val * p2v / self.lamb), 2)
        p2Z = math.pow(math.sqrt(p2v - self.lamb * p2delta), 2)

        for i in range(11):
            vi = math.sqrt(p2Z + p2delta * (i / self.T))
            vst = vi * math.sqrt(self.T)
            d1 = (math.log(self.S / self.X) + (self.r + math.pow(vi, 2) / 2) * self.T) / vst
            if self.fCall:
                bs = self.gbs_call(self.r, vst, d1)
            else:
                bs = self.gbs_put(self.r, vst, d1)

            result += elT * math.pow(self.lamb * self.T, i) / self.fact_lookup[i] * bs
        return result

    def gbs_call(self, b, vst, d1):
        return self.S * math.exp((b - self.r) * self.T) * cnd(d1) - \
               self.X * math.exp(-self.r * self.T) * cnd(d1 - vst)

    def gbs_put(self, b, vst, d1):
        return self.X * math.exp(-self.r * self.T) * cnd(-(d1 - vst)) - \
               self.S * math.exp((b - self.r) * self.T) * cnd(-d1)


S = 100.0
X = 80.0
T = 0.25
r = 0.08
v = 0.25
lamb = 1.0
Gamma = 0.25
m = models(1, S, X, T, r, v, lamb, Gamma)
print(m.JumpDiffusion())

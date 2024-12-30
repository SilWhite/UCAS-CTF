# write by ChatGPT

from sympy import mod_inverse


# 椭圆曲线上的点运算
class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = p  # 有限域大小
        self.a = a  # 曲线参数 a
        self.b = b  # 曲线参数 b

    def is_on_curve(self, x, y):
        """检查点是否在曲线上"""
        return (y * y) % self.p == (x**3 + self.a * x + self.b) % self.p

    def add_points(self, P, Q):
        """椭圆曲线上的点加法"""
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 == -y2 % self.p:
            return None  # 相加为无穷远点

        if P != Q:
            lam = ((y2 - y1) * mod_inverse(x2 - x1, self.p)) % self.p
        else:
            lam = ((3 * x1**2 + self.a) * mod_inverse(2 * y1, self.p)) % self.p

        x3 = (lam**2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k, P):
        """标量乘法 k * P"""
        R = None  # 无穷远点
        T = P
        while k:
            if k & 1:
                R = self.add_points(R, T)
            T = self.add_points(T, T)
            k >>= 1
        return R


# 已知参数
p = 10829670737591616881
a = 5654694684284925384
b = 8813703413191082292
G_coords = (1641649954652386070, 6138061874724201376)
pk_coords = (5002204260689444003, 4864358965035087900)
C1_coords = (51088427393127044, 4878776382292322395)
C2_coords = (10781379197071597919, 6012831518044176787)

# 初始化椭圆曲线和点
curve = EllipticCurve(p, a, b)
G = G_coords
pk = pk_coords
C1 = C1_coords
C2 = C2_coords


# 暴力破解 k (离散对数)
def solve_discrete_log(G, C1, curve):
    """暴力求解 k，满足 C1 = k * G"""
    for k in range(1, curve.p):
        if curve.scalar_mult(k, G) == C1:
            return k
    raise ValueError("离散对数求解失败")


k = solve_discrete_log(G, C1, curve)

# 恢复明文点 pt
neg_k_pk = curve.scalar_mult(k, pk)
neg_k_pk = (neg_k_pk[0], -neg_k_pk[1] % p)  # 求负值
pt = curve.add_points(C2, neg_k_pk)

# 输出 FLAG
flag = f"NeSE{{{pt[0]}{pt[1]}}}"
print(flag)

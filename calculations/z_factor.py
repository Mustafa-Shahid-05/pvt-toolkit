import numpy as np
from scipy.optimize import newton, brentq

def papayJ(ppr, tpr): 
    a = 3.53
    b = 0.9813
    c = 0.274
    d = 0.8157
    z = 1 - (a * ppr / (10**(b * tpr))) + ((c * ppr**2) / (10**(d * tpr)))
    return z

def hallYarbough(ppr, tpr):
    t = 1 / tpr
    X1 = -0.06125 * t * ppr * np.exp(-1.2 * (1 - t**2))
    X2 = 14.76 * t - 9.76 * t**2 + 4.58 * t**3
    X3 = 90.7 * t - 242.2 * t**2 + 42.4 * t**3
    X4 = 2.18 + 2.82 * t

    def F(Y):
        if Y <= 0 or Y >= 1:
            return 1e6
        return X1 + (Y + Y**2 + Y**3 - Y**4) / (1 - Y)**3 - X2 * Y**2 + X3 * Y**X4

    def Fprime(Y):
        if Y <= 0 or Y >= 1:
            return 1e6
        term1 = (1 + 4*Y + 4*Y**2 - 4*Y**3 + Y**4) / (1 - Y)**4
        term2 = -2 * X2 * Y
        term3 = X3 * X4 * Y**(X4 - 1)
        return term1 + term2 + term3

    Y0 = 0.0125 * ppr * t * np.exp(-1.2 * (1 - t**2))
    try:
        Y = brentq(F, 1e-4, 0.99)
    except ValueError:
        Y = newton(F, x0=max(1e-4, min(Y0, 0.99)), fprime=Fprime, maxiter=100)
    
    z = -X1 / Y
    return z

def dranchukAbouKassem(ppr, tpr):
    A = [
        0.3262, -1.0700, -0.5339, 0.01569, -0.05165,
        0.5475, -0.7361, 0.1884, 0.1056, 0.6134, 0.7210
    ]
    
    def f(rho):
        term1 = A[0] + A[1]/tpr + A[2]/(tpr**2) + A[3]/(tpr**4) + A[4]/(tpr**5)
        term2 = A[5] + A[6]/tpr + A[7]/(tpr**2)
        term3 = A[8] * (A[6]/tpr + A[7]/(tpr**2))
        term4 = A[9] * (1 + A[10]*(rho**2)) * (((rho**2) * np.exp(-A[10] * (rho**2))) / (tpr**3))
        return term1*rho + term2*(rho**2) - term3*(rho**5) + term4 + 1 - (0.27*ppr)/(rho*tpr) 

    rho_r = brentq(f, 1e-4, 3.0)
    z = (0.27 * ppr) / (rho_r * tpr)
    return z

def DranchukPurvisRobinson(ppr, tpr):
    A = [  
        0.31506237,
        -1.0467099,
        -0.57832729,
        0.53530771,
        -0.61232032,
        -0.10488813,
        0.68157001,
        0.68446549
    ]
    
    def rho_R(Z): 
        return (0.27 * ppr) / (Z * tpr)
    
    def f(Z): 
        rho = rho_R(Z)
        term1 = (A[0] + A[1]/tpr + A[2]/(tpr**3)) * rho
        term2 = (A[3] + A[4]/tpr) * (rho)**2
        term3 = (A[4]*A[5]/tpr) * (rho)**5
        term4 = (A[6]/tpr**3) * rho**2
        term5 = (1 + A[7]*(rho)**2)
        term6 = np.exp(-A[7]*(rho)**2)
        return 1 + term1 + term2 + term3 + term4*term5*term6 - Z
        
    # Try brentq with safe fallback bounds, otherwise use Newton's method
    try:
        Z = brentq(f, 0.01, 5.0)
    except ValueError:
        Z = newton(f, x0=1.0)
        
    return Z

def HankinsonThomasPhilips(ppr, tpr): 
    if ppr <= 5:
        A = [0.001290236, 0.38193005, 0.022199287,
             0.12215481, -0.015674794, 0.027271364,
             0.023834219, 0.43617780]
    else: 
        A = [0.0014507882, 0.37922269, 0.024181399,
             0.11812287, 0.037905663, 0.19845016,
             0.048911693, 0.0631425417]
        
    def f(Z): 
        if Z <= 0:
            return 1e6
        term1 = (A[3]*tpr - A[1] - (A[5]/tpr**2)) * (ppr / (Z**2 * tpr**2))
        term2 = (A[2]*tpr - A[0]) * (ppr**2 / (Z**3 * tpr**3))
        term3 = (A[0]*A[4]*A[6]) * (ppr**5 / (Z**6 * tpr**6))
        term4 = 1 + (A[7]*ppr**2 / (Z**2 * tpr**2))
        expo = np.exp(-term4)
        return 1/Z - 1 + term1 + term2 + term3*term4*expo
        
    # Robust solver wrapper: try bounded brentq first, then fall back to Newton with multiple guesses
    try:
        Z = brentq(f, 0.01, 3.0)
    except ValueError:
        try:
            Z = newton(f, x0=0.5, maxiter=200)
        except RuntimeError:
            Z = newton(f, x0=1.0, maxiter=200)
            
    return Z

def BrillandBeggs(ppr, tpr): 
    tr = 1 / tpr
    A = 0.06125 * tr * np.exp(-1.2 * (1 - tr)**2)
    B = tr * (14.76 - 9.76 * tr + 4.58 * tr**2)
    C = tr * (90.7 - 242.2 * tr + 42.4 * tr**2)
    D = 2.18 + 2.82 * tr
    
    def f(Y): 
        if Y <= 0 or Y >= 1:
            return 1e6
        term = (Y + Y**2 + Y**3 - Y**4) / (1 - Y)**3
        return term - A*ppr - B*Y**2 + C*Y**D
        
    def fprime(Y): 
        if Y <= 0 or Y >= 1:
            return 1e6
        term = (1 + 4*Y + 4*Y**2 - 4*Y**3 + Y**4) / ((1 - Y)**4)
        return term - 2*B*Y + C*D*Y**(D - 1)
        
    try:
        Y = brentq(f, 1e-4, 0.99)
    except ValueError:
        Y = newton(f, fprime=fprime, x0=0.5)
        
    Z = A * ppr / Y
    return Z

def Brill(ppr, tpr):
    E = 9 * (tpr - 1)
    F = 0.3106 - 0.49 * tpr + 0.1824 * tpr**2
    
    # Use real representation for fractional powers to avoid complex numbers
    A = 1.39 * np.real((tpr - 0.92)**0.5) - 0.36 * tpr - 0.1
    
    B = (
        (0.62 - 0.23 * tpr) * ppr
        + (0.066 / (tpr - 0.86) - 0.037) * ppr**2
        + 0.32 * ppr**6 / 10**E
    )

    C = 0.132 - 0.32 * np.log(tpr)
    D = 10**F
    
import numpy as np

def Brill(ppr, tpr):
    E = 9 * (tpr - 1)
    F = 0.3106 - 0.49 * tpr + 0.1824 * tpr**2
    
    A = 1.39 * np.real(np.emath.power(tpr - 0.92, 0.5)) - 0.36 * tpr - 0.1
    B = (
        (0.62 - 0.23 * tpr) * ppr
        + (0.066 / (tpr - 0.86) - 0.037) * ppr**2
        + 0.32 * ppr**6 / 10**E
    )

    C = 0.132 - 0.32 * np.log(tpr)
    D = 10**F
    
    # Safely evaluate power and cast back to float to prevent complex JSON serialization issues
    Z_val = A + (1 - A) / np.exp(B) + C * np.real(np.emath.power(ppr, D))
    return float(Z_val)

def cg(ppr, tpr, ppc, Zfunc, h=1e-5):
    Z = Zfunc(ppr=ppr, tpr=tpr)
    Z1 = Zfunc(ppr=ppr + h, tpr=tpr)
    Z0 = Zfunc(ppr=ppr - h, tpr=tpr)
    dZ = (Z1 - Z0) / (2 * h)
    cpr = (1 / ppr) - (1 / Z) * dZ
    cg_val = (1 / ppc) * cpr
    return cg_val
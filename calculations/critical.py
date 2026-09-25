

def Standing(gamma_g):
    
    if gamma_g <= 0.7:
        # Use original Standing for light gases
        Ppc = 709.604 - 58.718 * gamma_g
        Tpc = 170.491 + 307.344 * gamma_g
        
    else:
        # Use modified Standing for heavier gases
        Ppc = 756.8 - 131.07 * gamma_g - 3.6 * gamma_g**2
        Tpc = 169.2 + 349.5 * gamma_g - 74 * gamma_g**2
     
    return Ppc, Tpc


def Katz(gamma_g):
    if gamma_g < 0.75 :
        Tpc = 168 + 325 * gamma_g - 12.5 * (gamma_g**2)
        Ppc = 677 + 15 *  gamma_g - 37.5 * (gamma_g**2)
    else: 
        Tpc = 187 + 330  * gamma_g - 71.5 * (gamma_g**2)
        Ppc = 706 - 51.7 * gamma_g - 11.1 * (gamma_g**2)
    return Ppc , Tpc


def Sutton (gamma_g,yH2S=0, yCO2=0, yN2=0):
    M_air = 28.97
    M_H2S = 34.08
    M_CO2 = 44.01
    M_N2  = 28.01

    yHC = 1 - yH2S - yCO2 - yN2
    denHC = (gamma_g * M_air -
             (yH2S * M_H2S +
              yCO2 * M_CO2 +
              yN2  * M_N2)) / (yHC * M_air)
    
    PcHC = 744   - 125.4 * denHC +  5.9 * (denHC**2)
    TcHC = 164.3 + 375.7 * denHC - 67.7 * (denHC**2)
    return PcHC , TcHC

def WichertAziz(Pc, Tc, yH2S=0, yCO2=0, yN2=0):
    YA = yCO2 + yN2
    YH = yH2S
    eps = 120*(YA**0.9 - YA**1.6) + 15*(YH**0.5 - YH**4)
    Tpc = Tc - eps
    Ppc = Pc * Tpc / (Tc + eps*YH*(1 - YH))
    return Ppc, Tpc

def CarrKobayashiBurrows (Pc, Tc, yH2S=0, yCO2=0, yN2=0): 
    Tpc = Tc -  80 * yCO2 + 130 * yH2S - 250 * yN2
    Ppc = Pc - 440 * yCO2 + 600 * yH2S - 170 * yN2
    return Ppc , Tpc




def Elsharkawy(yLW , TcLW , PcLW , yC7=0 , TcC7=0 , PcC7=0 , yN2=0 , TcN2=0 ,PcN2=0 ,yCO2=0 ,
               TcCO2=0 , PcCO2=0 , yH2S=0 , TcH2S=0 , PcH2S=0 ):
    a = [-0.04027993 , 0.881709332 , 0.800591625 , 1.037850321 , 1.059063178]
    b = [-0.77642332 , 1.030721752 , 0.734009058 , 0.909963446 , 0.888959152]

    # Light components sum
    lighSum_J  = sum(yi*(Tci/Pci) for (yi, Tci, Pci) in zip(yLW, TcLW, PcLW) if Pci != 0)
    Heavyterm  = a[0] + a[1] * (yC7 * (TcC7/PcC7) if PcC7 != 0 else 0)
    N2term     = a[2] * yN2 * (TcN2/PcN2 if PcN2 != 0 else 0)
    CO2term    = a[3] * yCO2 * (TcCO2/PcCO2 if PcCO2 != 0 else 0)
    H2Sterm    = a[4] * yH2S * (TcH2S/PcH2S if PcH2S != 0 else 0)
    J = lighSum_J + Heavyterm + N2term + CO2term + H2Sterm

    # Light components sum for K
    lighSum_K = sum(yi*(Tci/(Pci**0.5)) for (yi, Tci, Pci) in zip(yLW, TcLW, PcLW) if Pci != 0)
    Heavyterm_k  = b[0] + b[1] * (yC7 * (TcC7/(PcC7**0.5)) if PcC7 != 0 else 0)
    N2term_k     = b[2] * yN2 * (TcN2/(PcN2**0.5) if PcN2 != 0 else 0)
    CO2term_k    = b[3] * yCO2 * (TcCO2/(PcCO2**0.5) if PcCO2 != 0 else 0)
    H2Sterm_k    = b[4] * yH2S * (TcH2S/(PcH2S**0.5) if PcH2S != 0 else 0)
    K = lighSum_K + Heavyterm_k + N2term_k + CO2term_k + H2Sterm_k

    if J == 0:
        return None, None
    Tpc = (K**2)/J
    Ppc = Tpc/J
    return Ppc, Tpc











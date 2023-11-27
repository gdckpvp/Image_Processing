import cv2
import numpy as np


L = 256

def Spectrum(imgin):
    M, N = imgin.shape
    P = cv2.getOptimalDFTSize(M)
    Q = cv2.getOptimalDFTSize(N)
    f = np.zeros((P,Q), np.float)
    f[0:M,0:N] = imgin.astype(np.float)/(L-1)
    F = cv2.dft(f, flags = cv2.DFT_COMPLEX_OUTPUT)
    F = np.fft.fftshift(F)
    S = cv2.magnitude(F[:,:,0],F[:,:,1])
    S = np.clip(S, 0, L-1).astype(np.uint8)
    return S

def FrequencyFilter(imgin):
    # Buoc 1 va 2
    # Mo rong anh co kich thuoc PxQ
    # Them 0 vao phan mo rong
    M, N = imgin.shape
    P = cv2.getOptimalDFTSize(M)
    Q = cv2.getOptimalDFTSize(N)
    f = np.zeros((P,Q), np.float)
    f[0:M,0:N] = imgin

    # Buoc 2: Tinh DFT
    F = cv2.dft(f, flags = cv2.DFT_COMPLEX_OUTPUT)
    # Buoc 3: Shift vao the center of the image
    F = np.fft.fftshift(F)

    # Buoc 4: Tao bo loc H
    H = np.zeros((P,Q,2), np.float)
    n = 2
    D0 = 60
    for u in range(0, P):
        for v in range(0, Q):
            Duv = np.sqrt((u-P//2)**2 + (v-Q//2)**2)
            if Duv > 0:
                H[u,v,0] = 1/(1 + np.power(D0/Duv,2*n))
    # Buoc 5: G = FH
    G = cv2.mulSpectrums(F, H, flags = cv2.DFT_ROWS)
    # Buoc 6: Shift nguoc tro lai
    G = np.fft.ifftshift(G)
    # Buoc 7: IDFT
    g = cv2.idft(G, flags = cv2.DFT_SCALE)
    # Buoc 8: Get real image with kich thuoc ban dau
    g = g[0:M,0:N,0]
 
    g = np.clip(g, 0, L-1).astype(np.uint8)
    return g

def CreateNotchRejectFilter():
    P = 250
    Q = 180
    u1, v1 = 44, 58
    u2, v2 = 40, 119
    u3, v3 = 86, 59
    u4, v4 = 82, 119

    D0 = 10
    n = 2
    H = np.ones((P,Q), np.float32)
    for u in range(0, P):
        for v in range(0, Q):
            h = 1.0
            # Bộ lọc u1, v1
            Duv = np.sqrt((u-u1)**2 + (v-v1)**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0
            Duv = np.sqrt((u-(P-u1))**2 + (v-(Q-v1))**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0

            # Bộ lọc u2, v2
            Duv = np.sqrt((u-u2)**2 + (v-v2)**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0
            Duv = np.sqrt((u-(P-u2))**2 + (v-(Q-v2))**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0

            # Bộ lọc u3, v3
            Duv = np.sqrt((u-u3)**2 + (v-v3)**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0
            Duv = np.sqrt((u-(P-u3))**2 + (v-(Q-v3))**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0

            # Bộ lọc u4, v4
            Duv = np.sqrt((u-u4)**2 + (v-v4)**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0
            Duv = np.sqrt((u-(P-u4))**2 + (v-(Q-v4))**2)
            if Duv > 0:
                h = h*1.0/(1.0 + np.power(D0/Duv,2*n))
            else:
                h = h*0.0
            H[u,v] = h
    return H

def DrawNotchRejectFilter():
    H = CreateNotchRejectFilter()
    H = H*(L-1)
    H = H.astype(np.uint8)
    return H

#def RemoveMoire(imgin):
    # Buoc 1 va 2
    # Mo rong anh co kich thuoc PxQ
    # Them 0 vao phan mo rong
    M, N = imgin.shape
    P = cv2.getOptimalDFTSize(M)
    Q = cv2.getOptimalDFTSize(N)
    f = np.zeros((P,Q), np.float)
    f[0:M,0:N] = imgin

    # Buoc 2: Tinh DFT
    F = cv2.dft(f, flags = cv2.DFT_COMPLEX_OUTPUT)
    # Buoc 3: Shift vao the center of the image
    F = np.fft.fftshift(F)

    # Buoc 4: Tao bo loc H
    H = CreateNotchRejectFilter()

    # Buoc 5: G = FH
    G = cv2.mulSpectrums(F, H, flags = cv2.DFT_ROWS)
    # Buoc 6: Shift nguoc tro lai
    G = np.fft.ifftshift(G)
    # Buoc 7: IDFT
    g = cv2.idft(G, flags = cv2.DFT_SCALE)
    # Buoc 8: Get real image with kich thuoc ban dau
    g = g[0:M,0:N,0]
 
    g = np.clip(g, 0, L-1).astype(np.uint8)
    return g
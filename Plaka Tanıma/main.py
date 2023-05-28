import pytesseract as pyt  # metin okuma için
import cv2, imutils  

foto = cv2.imread("licence_plate.jpg") # gorseli okuyuoruz
griTonlu = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY) # foto gritonlu oluyr
filtre = cv2.bilateralFilter(griTonlu, 20,80,80) # puslandırma efekti ekliyoruz
koseliCizgi = cv2.Canny(filtre, 100, 150)
noiseEfekt = cv2.findContours(koseliCizgi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
# fotodaki küçük karıncalanma efektlerini temizle
renkYakala = imutils.grab_contours(noiseEfekt)

renkYakala = sorted(renkYakala, key=cv2.contourArea, reverse=True)[:10]
# print(renkYakala)

# cv2.imshow("gorsel", noiseEfekt)

pencere = None   # plaka olan gorsel başta gorunmesin

for renk in renkYakala:  
    epsilon = 0.018*cv2.arcLength(renk, True) 
    approx = cv2.approxPolyDP(renk, epsilon, True) 
    
    if (len(approx) == 4):  # bu bir dortgendir ve donguyu bitirsin
        pencere = approx
        break

import numpy as np
# gri tonlu gorselden sıfırlardan oluşan 8 bitlik numpy serisi oluştur
maske = np.zeros(griTonlu.shape, np.uint8)

maskeliPlaka = cv2.drawContours(maske, [pencere], 0, (255,255,255), -1)
maskeliPlaka = cv2.bitwise_and(foto, foto, mask=maske)


# ---- Gorselin ust, alt sağ ve solunda oluşan siyah alanları temizle -----
# beyaz olan yerdeki bilgileri (x,y) koordinatında sakla
(x,y) = np.where(maske == 0)
# en üst ve en alt değerleri bul
(topX, topY) = (np.min(x), np.min(y))
(bottomX, bottomY) = (np.max(x), np.max(y))

kirpilanResim = griTonlu[topX:bottomX +1, topY:bottomY +1]

plakaDegeri = pyt.image_to_string(maskeliPlaka)


cv2.imshow("kırpılan resim", maskeliPlaka)
print("Plaka.:", plakaDegeri)
cv2.waitKey(0)


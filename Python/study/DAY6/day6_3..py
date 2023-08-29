import math
def solution(numer1, denom1, numer2, denom2):
    top = (numer1*denom2) + (numer2*denom1)
    bottom = denom1*denom2
    
    gcd=math.gcd(top,bottom)
    top = top/gcd
    bottom = bottom/gcd
    
    return [top,bottom]

#최대공약수를 구하는 라이브러리 및 함수가 있었다. 라이브러리 math 내의 gcd 함수. 알아두장.
#그렇지만 이런 라이브러리를 사용하지 않고도 만들 줄 알아야겠당...
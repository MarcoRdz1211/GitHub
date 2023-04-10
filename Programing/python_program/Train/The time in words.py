h = int(input())
m = int(input())

A = ["zero","one","two","three","four","five","six","seven","eight","nine",
     "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
     "seventeen","eighteen","nineteen","twenty","twenty one","twenty two",
     "twenty three","twenty four","twenty five","twenty six","twenty seven",
     "twenty eight","twenty nine"]

if m==0:
    a = A[h]+" o' clock"

elif m==1:
    a = A[1]+" minute past "+A[h]

elif m==15:
    a = "quarter past "+A[h]

elif m<30:
    a = A[m]+" minutes past "+A[h]

elif m==30:
    a = "half past "+A[h+1]

elif m>30:
    a = A[60-m]+" minutes to "+A[h+1]

elif m==45:
    a = "quarter to "+A[h+1]


print(a)

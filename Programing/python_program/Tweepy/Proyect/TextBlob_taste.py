from textblob import TextBlob
A='1234567890qwertyuiopasdfghjklñzxcvbnm,.-{+´}¿|<°!#$%&/()=?¡]*¨[PÑOLIKUJYHTGRFEDWSQAZX>CVBNM;:_]'
X = []

for t in A:
    X.append(str(t))

def translate(r):
    A = ascii(r)
    B = TextBlob(A)
    C = B.translate(from_lang="es", to="en")
    D = C.sentiment
    print(D)

for t in X:
    print(5*t)
    try:
        print(translate(5*t))

    except:
        None

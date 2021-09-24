n=int(input('Dati numarul de elemente din vector n='))
z=[]

print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('elementul z[' +str(i)+']='))
    z.append(x)
print('vectorul obtinut',z)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii: \n', z[0:10:5])

b=z[0:]
b.reverse()
print('b)  afişează pe ecran vectorul în ordinea inversă \n:',b)

c=z[0:]
c.sort(reverse=True)
print('c)  sortează componentele tabloului în ordine descrescătoare: \n', c)

d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        d.append(z[i])
print('d)  afişează pe ecran doar componentele pare: \n',d)

media = sum(d)/len(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare: ',media)

f=[]
for i in range(0,len(z)):
    if z[i]%2==1:
        f.append(z[i])
print('f)  afişează pe ecran doar componentele impare: ',f) 

        
x=2
y=4
g=[]
for i in range(0,len(z)):
    if z[i]>x and z[i]%y>0:
        g.append(z[i])
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x=',x,' şi nu sunt divizibile cu y=',y,' :',g)
        

x=2
y=4
h=[]
for i in range(0,len(z)):
    if z[i]>x and z[i]<y:
        h.append(z[i])
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x=',x,' şi mai mici decât y=',y,' : ',h)


print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i in range(0,len(z)):
    if z[i]%2==1 and z[i]<0:
            print(i)

print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
for i in range(0,len(z)):
    if z[i]>9 and z[i]<100:
            print(i)

print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k = z[0:]
k[0]=min(k)
print(k)

print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=z[0:]
l[l.index(min(l))]=l[0]
print(l)

print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        m.append(z[i])
print(m)

print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
r=[]
for i in range(0,len(z)):
    if z[i]%3==0:
        r.append(z[i])
print(r)

print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')


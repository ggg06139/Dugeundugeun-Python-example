import turtle as t
t.shape('turtle')

a = t.textinput('황승현','몇각형을 원하시나요?')

a = int(a)

for _ in range(a):
    t.fd(100)
    t.lt(360/a)

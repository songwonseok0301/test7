import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

a = st.number_input('a의 값을 입력하시오',value=2.0,step=1.0)
b = st.number_input('b의 값을 입력하시오',value=-1.0,step=1.0)
c = st.number_input('c의 값을 입력하시오',value=15.0,step=1.0)
d= st.number_input('d의 값을 입력하시오',value=2000.0,step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','blue','orange','purple'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오',['-','--','~'])
m1 = st. sidebar.radio('마커의 스타일을 선택하시오',['o','^','s','p'])


x = []
y1 = []
y2 = []
for i in range(-29,30,3):
    x.append(i)
    y1.append(a*i*i + b*i + c)
    y2.append(d/i)
    

plt.plot(x,y1, color=c1, linestyle=s1, marker=m1 )

st.pyplot(fig)











#col = st.columns(3)
#with col [0]:
#    a = st. number_input('insert a', step = 10)
#with col [1]:
#    b = st. number_input('insert b', step = 10)
#with col [2]:
#    c = st. number_input('insert c', step = 10)
#
#    y = []
#    for i in x:
#        y.append(a*1**2 + b*1 + c)













#mx = -1e10
#mx
#for i in s:
#    if i > mx:
#        mx = 1




















































#import turtle
#import random
#t1 = turtle.Turtle()
#t2 = turtle.Turtle()

#screen=turtle.Screen()
#image1= 'rabbit.gif'
#image2= 'turtle.gif'
#screen.addshape(image1)
#screen.addshape(image2)

#t1= turtle.Turtle()
#t1.shape(image1)
#t1.pensize(5)
#t1.penup()
#t1.goto(-300,0)


#t2=turtle.Turtle()
#t2.shape(image2)
#t2.pnesize(5)
#t2.penup()
#t2.goto(-300,-200)

#t1.pendown()
#t2.pendown()
#t1.speed(1)
#t2.speed(1)

#for i in range(100):
   # d1 = random.randint(1,60)
    #t1.forward(d1)
   # d2 = random.randint(1,60)
    #t2.forward(d2)













#turtle.done()






# distance = 150
# angle = 120
# for i in range(3):
#     t.forwadr(distance)
#     t.left(angle)



# t.fillcolor('blue')
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(100)

# t.fillcolor('red')
# t.begin_fill()
# t.circle(120)
# t.end_fill()



# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)
# t.left(144)
# t.forward(100)







# a=3.141592*10*10.0
# b=(1/100)*1234
# a,b
# print(a,b)

# print('Hello')
# st.write('Hello')
# st.write('강아지'+'고양이')

# st.write('1'+'1')
# st.write(1+1)




# st.write("스플림릿")
# st.title("streamlit Image")
# st.image("im.jfif")



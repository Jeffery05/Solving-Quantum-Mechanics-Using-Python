import numpy as np
import matplotlib.pyplot as plt

h = 1  #6.62607015e-34  #Planck's constant
L = 1  #length of box
n = 500  #steps
k = 1  # wavenumber
E_theoretical = np.pi**2 * k**2 / 2  # energy level (theoretical)
total_probability = 0  #total probability
U = 0  # potential energy inside box
x_len = 1000  #length
dx = 1 / x_len
a = 0  #constant to normalize
E = 3
m = 1
de = 0.01
V = 0
x = np.arange(0, L, dx)
Elist = np.arange(E, 1000, 0.01)
#BestE = 0 #what's this?
threshold = 0.001
#p[0] = 0  #initial value for schrodinger

#for j in range(0, len(Elist)):

condition = True
N = 0

while condition and N < 10000:  # Condition
    p = np.zeros(len(x))  #psi
    q = np.zeros(len(x))  #Change of variable
    q[0] = 1  #Set the initial value of psi to 1

    for i in np.arange(len(x) - 1):  # cycle through the indexes of q and p
        q[i +
          1] = q[i] - (2 * m / h**2) * E * p[i] * dx  # 2 coupled integrals woo
        p[i + 1] = p[i] + q[i + 1] * dx
    if (abs(p[-1]) < threshold):  # if the last value is less than 0.01
        condition = False  # break out of loop
    else:  # keep incrementing E
        E += de
    N += 1  # Increment N

#Squaring psi for probability
p_squared = np.array(p)**2


#verifying probability
def probability_integral():

    # integral_dx = 0.00001 #x increment
    x = np.arange(0, 1, dx)  #start,end,increment

    integral = 0  #initialize empty value

    def func(eqn):
        return (eqn**2) * dx  ##equation to calculate area
        #of rectangle. Function = y and dx = x, multiply = area

    for i in np.arange(0, len(x)):  #len(x)
        integral += func(abs(p[i]))

    print("integral =" + str(integral))
    return integral


#end

a = 1 / (np.sqrt(probability_integral()))
#normalizing to make total probability = 1
print("a = " + str(a))
p *= a

#print total probability
for i in range(len(p)):
    total_probability += (p[i]**2) * dx

print("total probability =" + str(total_probability))

plt.plot(x, p * a)
plt.title("Psi Function normalized")
plt.xlabel("x")
plt.ylabel("Psi (x)")
plt.show()

plt.plot(x, p_squared * (a)**2)
plt.title("Probability Distribution normalized")
plt.xlabel("x")
plt.ylabel("Probabilities")
plt.show()

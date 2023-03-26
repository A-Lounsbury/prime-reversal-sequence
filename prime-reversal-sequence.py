import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# converts a decimal number to a list of binary digits
def decimalToBinary(n):
    digits = []
    while n >= 1:
        digits.append(n % 2)
        if n % 2 == 1:
            n = int((n - 1) / 2)
        elif n % 2 == 0:
            n = int(n / 2)
    return digits

# converts a list of binary digits to a decimal number
def binaryToDecimal(digits):
    result = 0
    digits.reverse()
    for i, d in enumerate(digits):
        result += d * (2 ** i)
    return result

def generate_prime_reversal_sequence(n):
    sequence = []
    i = 2
    while len(sequence) < n:
        if prime(i):
            binary = decimalToBinary(i)
            num = binaryToDecimal(binary)
            sequence.append(i - num)
        if i == 2:
            i += 1
        else:
            i += 2
    return sequence

sequence = generate_prime_reversal_sequence(20)
print(sequence)

# Basic Scatterplots
n = 10
sequence = generate_prime_reversal_sequence(n)
df = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(n):
    indices.append(i)
df['index'] = indices

sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 100
sequence = generate_prime_reversal_sequence(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 1000
sequence = generate_prime_reversal_sequence(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 10000
sequence = generate_prime_reversal_sequence(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

# Average plots
n = 10
sequence = generate_prime_reversal_sequence(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x='index', y='Average', data=df)
plt.show()

n = 100
sequence = generate_prime_reversal_sequence(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x='index', y='Average', data=df)
plt.show()

n = 1000
sequence = generate_prime_reversal_sequence(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x='index', y='Average', data=df)
plt.show()

n = 10000
sequence = generate_prime_reversal_sequence(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x='index', y='Average', data=df)
plt.show()

n = 100000
sequence = generate_prime_reversal_sequence(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x='index', y='Average', data=df)
plt.show()
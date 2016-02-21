seq = input('What is your DNA sequence?')
a = seq.count('a')
c = seq.count('c')
t = seq.count('t')
g = seq.count('g')
gc_percentage = (g + c) / (a + c + t + g) * 100
print ('Your GC percentage is:')
print (gc_percentage) 

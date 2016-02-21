seq = input("What is your sequence?")
seq_reverse = seq[::-1] #reverses DNA sequence 
seq_reverse_u = seq_reverse.replace('A', 'U')
seq_reverse_ua = seq_reverse_u.replace('T', 'A')
seq_reverse_uag = seq_reverse_ua.replace('C','G')
seq_reverse_uagc = seq_reverse_uag.replace ('G', 'C')
print ('The mRNA sequence is:')
print (seq_reverse_uagc.lower())

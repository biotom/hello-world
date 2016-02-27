##simple script for working out the reverse complement or mRNA sequence of DNA input
seq = input("What is your sequence?")
seq = seq.upper()
seq = seq [::-1]
answer = input('Do you want the mRNA sequence as well as the reverse complement?') ## No real reason you wouldn't just work directly with the coding strand, so this probably doesn't make much sense.
answer.lower()

##clumsy solution until I work out a better way

def complementary(seq):
    seq = seq.replace('A', 'X')
    seq = seq.replace('T', 'Y')
    seq = seq.replace('C', 'Z')
    seq = seq.replace('G', 'N')
    seq = seq.replace('X', 'T')
    seq = seq.replace('Y', 'A')
    seq = seq.replace('Z', 'G')
    seq = seq.replace('N', 'C')
    return seq
	
if answer == 'no':
    seq = complementary(seq)
    print(seq)


elif answer == 'yes':
    seq = complementary(seq)
    seq = seq.replace('T', 'U')
    seq = seq.lower()
    print(seq)

    
else:
    print ('Invalid answer.')




    

    
    

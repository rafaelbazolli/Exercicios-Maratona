dna = input()
if(dna[:3] == 'ATG' and dna[-3:] == 'TAG'):
    print('S' if any(seq in dna[3:-3] for seq in ['AAATG', 'AATTG', 'AAGTG']) else 'F') 
else: print('F')
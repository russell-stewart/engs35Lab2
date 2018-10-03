forward_primer = 'CCCCTGAATTCCATGGCACCAAAAGCAAAAATCGT'
reverse_primer = 'CCCCTGGATCCTTAAGCTAATGCCTTCATTCTCT'

forward_primer_Tm = 0
for character in forward_primer:
    if character is 'G' or character is 'C':
        forward_primer_Tm += 4
    if character is 'T' or character is 'A':
        forward_primer_Tm += 2
print 'The Tm of the forward primer is %d degrees celsius' % forward_primer_Tm

reverse_primer_Tm = 0
for character in reverse_primer:
    if character is 'G' or character is 'C':
        reverse_primer_Tm += 4
    if character is 'T' or character is 'A':
        reverse_primer_Tm += 2
print 'The Tm of the reverse primer is %d degrees celsius' % reverse_primer_Tm

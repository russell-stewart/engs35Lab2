#Define sequences of forward and reverse primers as given in lab manual
forward_primer = 'CCCCTGAATTCCATGGCACCAAAAGCAAAAATCGT'
reverse_primer = 'CCCCTGGATCCTTAAGCTAATGCCTTCATTCTCT'

#Start the Tm of the forward primer at zero. Iterate over each base in the
#sequence of the forward primer and add 4 for each occurance of G or C, or 2
#for each occurance of T or A. Print the result.
forward_primer_Tm = 0
for character in forward_primer:
    if character is 'G' or character is 'C':
        forward_primer_Tm += 4
    if character is 'T' or character is 'A':
        forward_primer_Tm += 2
print 'The Tm of the forward primer is %d degrees celsius' % forward_primer_Tm

#Repeat the same algorithm for the reverse primer.
reverse_primer_Tm = 0
for character in reverse_primer:
    if character is 'G' or character is 'C':
        reverse_primer_Tm += 4
    if character is 'T' or character is 'A':
        reverse_primer_Tm += 2
print 'The Tm of the reverse primer is %d degrees celsius' % reverse_primer_Tm

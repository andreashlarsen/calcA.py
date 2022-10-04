# program calculates and stores Schilling coefficients
# schilling 1990. Coll Math J.
# https://doi.org/10.1080/07468342.1990.11973306

import numpy as np

def calc_A(M,C,table):
  # calculates the Schilling coefficients
  # schilling 1990. Coll Math J. 
  # https://doi.org/10.1080/07468342.1990.11973306
  if M<=C:
    A = 2**M
  else:
    A = 0
    for j in range(C+1): 
      m = M-1-j
      if table[m,C] > 0:
        A += table[m,C]
      else:
        A += calc_A(m,C,table)
  if table[M,C] == 0: 
    table[M,C] = A      
  return A

# main program starts here
N_M,N_C=5000,500
name = 'A_table.dat'
f = open(name,'w')
table = np.zeros((N_M,N_C))
for m in range(N_M):
  for c in range(N_C):
    A = calc_A(m,c,table)
    #print('(M=%d,C=%d) => A = %d' % (m,c,A))
    f.write('%e ' % A)
    if c==N_C-1:
      f.write('\n')
print(table)
print('table of A values in %s' % name)
f.close()


import pandas as pd
import scoring
#A= input("insert the first sequence")
#B= input("insert the second sequence")
A='ATCGTGCT'
B='ATACGTGCA'
#implement that the user insert the scoring schem--> if not the scoring scheme used is ours
s=input("insert match score")

#INITIALIZING MATRIX
df=pd.DataFrame(columns=list(' '+A), index=list(' '+B)) #empty matrix leave a space at 1st column and row

#initialize first row to gap values
num=0
for c in range(len(A)+1): #since we added a space to build the matrix correctly we need to add 1 to the length of the string in order to reach the end
    df.iloc[0, c] = num
    num-=2

#initialize first column to gap values
num=0
for r in range(len(B)+1):
    df.iloc[r,0]=num
    num-=2

#MATRIX FILLING

#scoring scheme
match= 1
mismatch= -1
gap= -2

for r in range (1,len(B)+1): #iterate on each row with nt.
    for c in range(1,len(A)+1): #iterate on each column with nt.
        s_r_gap = df.iloc[r, c - 1] + gap  # right gap
        s_u_gap = df.iloc[r - 1, c] + gap  # up gap

        if df.columns[c]==df.index[r]: #match situation
            s_match = df.iloc[r-1,c-1] + match   #r-1,c-1 is the diagonal number found up left of the computed one
            df.iloc[r, c] = max(s_match, s_r_gap, s_u_gap) #select the max score among the possible one and assign it to the cell

        else: #mismatch situation
            s_mismatch =  df.iloc[r-1,c-1] + mismatch #mismatch in diagonal
            df.iloc[r, c] = max( s_mismatch, s_r_gap, s_u_gap)

#TRACEBACK











print(df)


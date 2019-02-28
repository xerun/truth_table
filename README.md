# truth_table
Truth Table in Python without using library

Automation of Truth Assignment
---
The program does the following
1.	Run the application and read the statements from the file q1_in.txt file line by line
2.	System breaks down the variables from the sentence and replaces all the operators using replace_operators()
3.	The recursive function find_truth_values() is used to do a loop and find all the truth values
4.	Finally write all the truth values line by line in a new file q1_out.txt

P1,P2,P3	T,T,T	( ( P1 AND P2 ) OR ( P3 AND TRUE ) ) OR ( ( - P1 AND - P3 ) AND P2 )

P1,P2,P3	T,F,F	( ( P1 AND P2 ) OR ( P3 AND TRUE ) ) OR ( ( - P1 AND - P3 ) AND P2 )

P1,P2	T,T	( P1 THEN P2 ) AND ( P2 THEN P1 )

P1,P2	F,T	( P1 THEN P2 ) AND ( P2 THEN P1 )

P1,P2	F,T	( P1 THEN P2 ) AND ( P2 THEN P1 ) EQ ( P1 EQ P2 )

P1,P2,P3,P4	T,F,T,F	P1 AND P2 AND P3 OR P4

P1,P2	T,T	- P1 AND ( P1 THEN P2 )

P1,P2,P3	F,F,T	( ( P1 THEN P2 ) OR ( P2 THEN P3 ) ) EQ ( P1 THEN P3 ) THEN P2

P1,P2,P3	F,T,T	( ( P1 THEN P2 ) OR ( P2 THEN P3 ) ) THEN ( ( P1 THEN P3 ) THEN P2 ) OR - P1

P1,P2	F,T	( P1 OR FALSE ) AND ( P2 OR TRUE )

Saves the output in another file q1_out.txt

Propositional Sentence Classifier
---
1.	Run the application and read the statements from the file q2_in.txt line by line
2.	System breaks down the variables from the sentence and calculate the number of possible sentences to make based on the number of variables and replaces all the operators using replace_operators()
3.	The function find_truth_values() is used to do a recursive loop and find all the truth values
4.	All the truth values are checked to see if they are Tautology, Contingency or Contradiction
5.	Finally write all the classifier line by line in a new file q2_out.txt


P1,P2,P3	( ( P1 AND P2 ) OR ( P3 AND TRUE ) ) OR ( ( - P1 AND - P3 ) AND P2 )

P1,P2,P3	( ( P1 AND P2 ) OR ( P3 AND TRUE ) ) OR ( ( - P1 AND - P3 ) AND P2 )

P1,P2	( P1 THEN P2 ) AND ( P2 THEN P1 )

P1,P2	( P1 THEN P2 ) AND ( P2 THEN P1 )

P1,P2	( ( P1 THEN P2 ) AND ( P2 THEN P1 ) ) EQ ( P1 EQ P2 )

P1,P2,P3,P4	( ( P1 AND P2 ) AND P3 ) OR P4

P1,P2	- P1 AND ( P1 THEN P2 )

P1,P2,P3	( ( P1 THEN P2 ) OR ( P2 THEN P3 ) ) EQ ( ( P1 THEN P3 ) THEN P2 )

P1,P2,P3	( ( P1 THEN P2 ) OR ( P2 THEN P3 ) ) THEN ( ( ( P1 THEN P3 ) THEN P2 ) OR - P1 )

P1,P2	( P1 OR FALSE ) AND ( P2 OR TRUE )

P1,P2	( - P1 AND ( P1 OR P2 ) ) THEN P2

P1,P2	P2 AND ( P1 THEN - P2 ) AND ( - P1 THEN - P2 )

P1,P2,P3	( P1 THEN ( P2 THEN P3 ) ) THEN ( ( P1 THEN P2 ) THEN P3 )

P1,P2,P3	( ( P1 OR P2 ) AND ( P1 THEN P3 ) AND ( P2 THEN P3 ) ) THEN P3

P1,P2,P3	- ( ( ( P1 OR P2 ) AND ( P1 THEN P3 ) AND ( P2 THEN P3 ) ) THEN P3 )

P1,P2	- ( P2 AND ( P1 THEN - P2 ) AND ( - P1 THEN - P2 ) )

P1,P2,P3	- ( ( P1 THEN ( P2 THEN P3 ) ) THEN ( ( P1 THEN P2 ) THEN P3 ) )

P1,P2	P1 OR ( P1 AND P2 ) EQ P1

P1,P2	P1 OR ( P1 AND P2 ) THEN P1

P1,P2	- P1 AND ( - P1 OR - P2 ) EQ - P1

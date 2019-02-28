# truth_table
Truth Table in Python without using library

This code reads the statements from a file q1_in.txt

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

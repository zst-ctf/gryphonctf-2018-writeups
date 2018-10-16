# Math Test
Programming - 250 points

## Challenge 
The challenge title says it all :)

nc prog.chal.gryphonctf.com 18300

Creator - Noans


## Solution

We are given math equations, but it does not follow BODMAS rules


Let's do some trial runs

----

#### 1st, Addition

	Sum: 14 + 15 * 9 * 2 / 10 / 3
	Answer:
	Sending: 23.0000000000000000000000000
	Received: Well, that was a good attempt, but the answer was 17.400000000000002

As you can see, `(14 + 15) * 9 * 2 / 10 / 3 = 17.4`

---

	Sum: 10 + 11 + 10 * 14 + 14 + 15 * 11 + 8
	Answer:
	Sending: 5101.0000000000000000000000000
	Received: Well, that was a good attempt, but the answer was 25327

Similarly `(10 + 11 + 10) * (14 + 14 + 15) * (11 + 8) = 25327`

---

#### Subtraction < Addition

	Sum: 12 - 12 + 3
	Answer: 

	Well, that was a good attempt, but the answer was -3

This will be 12 - (12 + 3)

---

	Sum: 14 / 12 + 5 - 1 + 9 + 7 - 3 + 11
	Answer: 

	Well, that was a good attempt, but the answer was -1

Which will be `14 / ((12 + 5) - ((1 + 9) + 7) - (3 + 11))
= 14 / -14 = -1`


---

#### Multiplication > Division

	Sum: 13 / 9 * 3
	Answer: 

	Well, that was a good attempt, but the answer was 0.48148148148148145

==> `13 / (9 * 3)`


----

#### Operations Order

1. Addition
2. Multiplication
3. Subtraction
4. Division

So we need to parse the equation with this custom order of operation.

So I made a function to calculate one operation at a time and then I inputted the custom order

    for operation in ['+', '*', '-', '/']:
        while operation in equ_list:
            equ_list = calculate_one(equ_list, operation)

And with this, it passes all the tests!

## Flag

	GCTF{G00D_4T_M47H}

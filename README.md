# Assignment3
As in the past, 5 questions, some flowcharts, some IPO and some Trace tables
Generic Rubric for Programming Assignments applies

Assignment # 3  -  out of 113. (I know wierd, but it's based on the work and effort of each question.)
NOTE:  The first question is not the easiest, but you can work on it immediately as completed everything on it.


1)	Recursion – The Koch curve is described in terms of “levels” or “degrees”.  The Koch curve of degree 0 is a straight line.  The first degree curve is formed by placing an accent (^).  The original line has been divided into 4( -^-), each of which is 1/3 the length of the original.  The accent or accent rises at 60 degrees, so it forms two sides of an equilateral triangle.  To get a second-degree curve, you put an accent in each of the line segments of the first-degree curve.  Successive curves are constructed by placing accents on each segment or the previous curve.  

A turtle always knows where it currently sits and what direction it is facing.  To draw a Koch curve of a given length and degree, you might (but don’t need to) use an algorithm like:

	My Koch(Turtle, length, degree):
		if degree = = 0:
			# tell the turtle to draw for length steps in here
		else:
			length1 = length/3
			degree1 = degree-1
			Koch(Turtle, length1, degree1)
			# tell the turtle to turn left 60 degrees
			Koch(Turtle, length1, degree1)
'# tell the turtle to turn left 120 degrees
			Koch(Turtle, length1, degree1)
'# tell the turtle to turn left 60 degrees
			Koch(Turtle, length1, degree1)
(Idea copied from Prof. John Zelle, Python Programming and introduction to computer science 2nd edition {Python 2}.)		
1.	 Create a flowchart for this problem
2.	Create an IPO chart for this problem
3.	Create a trace (table in any form) for this question when you have an error and hand it in.
4.	Complete the coding and hand it in.
	
Implement this algorithm with a Turtle class that contains instance variables location (a point) and Direction (a float?) and moveTo (somePoint), draw (length), and turn (degrees).

A little advanced math if you are stuck (you do not need to use this):
If you are maintaining direction as an angle in radians, the point you are going to can be computed from your current location direction x = length * cos(direction) and current location direction y = length * sin(direction)

IMPORTANT NOTE:  Contrary to all other assignments, your Koch snowflake can be very basic and it will be marked as a level 3 if you have made an honest attempt (Application and Thinking).  You must have a base case and your program must end.  Use error capture.  BE very careful in your attempt to earn a Level 4 – you must cite your sources AND must not borrow more than 25% of your code.
 
Knowledge & Understanding  -		/5
Application               	-		/8
Communication        	    	-		/5
Thinking	              		-		/7
[total marks       	/25 ] 
 
2)   Please create a flowchart, IPO chart and trace table for a particular guess.:
 
Weeks ago you were given a version 1 and then a version 2 of hangman.  You are to complete this task, use versioning and commit regularly as you add each piece, nothing hardcoded. Your words will be input from either a txt file or a csv file, your choice.  Your word list should come from the hardware components readings from Week 9.

Application         	      	  	/5        
Communication                 		/5 
Thinking & Inquiry     	       	 	/5
Knowledge		                  		/5 
[total marks		 	      	/20 ] 

3)	Please create a flowchart, IPO chart and trace table for a particular error you had while creating your work.  Please let me know which version you were on so that I may see the code and match up the trace table to that (now fixed) code.
  
a.	Your task, create a basic Yatzee game (top of score card only) using the msdie class created in class.
Application                   	   /6

Knowledge			                     /4
 
Communication             	      /4
 
Thinking & Inquiry           	    /4
 
[total marks       		/18] 


4)	Please create a flowchart, IPO chart and trace table for a particular error you had while creating your work.  Please let me know which version you were on so that I may see the code and match up the trace table to that (now fixed) code.
  
Your task, create one of two games using the Card class you and your classmates created.
a)	Easy choice (highest level possible is a Level 3).  In this option you will create a basic matching game.  Consider that Hearts and Diamonds match (red) and Spades and Clubs match (Black).  You must use at least a 5 x 5 set of cards and  the entire deck.is at your disposal.  You will need complete instructions for your user.

b)	More difficult option, (full marks possible). You will create the game of 21 or Blackjack, also using the Card class created in class. You will need complete instructions for your user.


Application                   	   /8

Knowledge		                	     /6
 
Communication               	    /3
 
Thinking & Inquiry           	    /8
 
[total marks       	/25 ] 



 5)  WOW me with your Pygame Sprite knowledge – you may begin with the sprite given in class, but do not need to.
Have fun with this one!
 
Knowledge & Understand.    /4         		Application         	      	  /8
Communication   	          /5	         	Thinking & Inquiry     	    	  /8
 						[total marks       /25]


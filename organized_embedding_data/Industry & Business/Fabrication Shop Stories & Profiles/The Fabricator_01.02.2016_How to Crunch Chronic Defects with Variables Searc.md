# How to Crunch Chronic Defects with Variables Search

[TARİH: 01.02.2016 The Fabricator]

A disciplined review of possible causal factors can lead to big quality gains

By Joseph Dunn

Figure 1

These plots are used to reveal the factor or factors that are important in trying to find the root of a production problem.

W

hy do we produce so much scrap? Why does fix-it rework keep dragging on? Why are we paying so much for secondary inspectors?

These are just some of the frustrating questions routinely asked in job shops. There is an answer to each of these questions, and simply applying the variables search (VS) steps laid out in this article can lead to a positive resolution.

VS is surprisingly easy to conduct, graphically convincing to team members, and accomplished in the fewest trials compared to other experimental methods. Fabricators that produce any amount of scrap, for instance, can use VS.

VS pioneer Dorian Shainin preached three principles:

1. There’s always a Red X.

2. The fastest route to find the Red X is a progressive search using the process of elimination.

3. Talk to the parts with statistically simple and rigorous tools.

VS as a Red X statistical power tool is so simple yet accomplishes so much. It hunts down the hostile factor in the manufacturing process or product—the source of your problems. Anyone who can read and talk will reduce and finally eliminate the problems with VS. The VS results tell you how to ease the tolerances on the unimportant factors to reduce costs.

If your plant suffers from high defect levels, come hither. (Note: VS also can be used to speed product design and lower design costs.) Let’s begin down the VS path.

Step 1: Choose the Process to Improve

Choose one of the most chronic problem processes in the shop: assembly, bending, cutting, finishing, machining, stamping, or welding. Pick a process for which the operator, technician, and engineer can identify five to 20 factors that might be causing the problem. If the process has less than five potential factors, you may skip Step 3.

Step 2: List the Possible Factors

Once you’ve chosen the process that will be the focus of a campaign for zero defects, call a session to generate a list of all the factors (also known as variables or causes) that might be causing the problems. Assemble a small group of people with knowledge of the process. The group should be big enough to provide animated verbal play, yet small enough to invite individual participation and freewheeling brainstorm-style inventing. The ideal group size is five to seven people.

Check these off for your successful meeting:

Make the meeting informal.

Pick an environment that ensures that you and others can relax. Place participants side by side facing a whiteboard, and people will respond to the problem depicted there.

Ban criticism of suggested causes.

Don’t allow the discussion to drift into a debate about any particular possibility. Just write the possibility on the board and prompt for more ideas.

Take the group on a walk-around where the process actually takes place.

This will jog memories, encourage understanding, and inspire ideas. Their thorough input is necessary to be properly prepared for the testing phase of this process.

As a group, put the list of factors in a new sequence:

List them alphabetically in order of their perceived effect on the output. The team’s ranking may be right or wrong; that’s OK. You’re just trying to expose and leverage the existing knowledge. Include all of the suspect factors. You may be surprised.

Step 3: Find the Cause

The root of the problem is called the origin or source. The purpose of this step is to identify the important factors that are ruining your shop’s control and creating inefficiencies on the shop floor.

a. Designate two levels for each factor: "good," which you think will contribute to good results, and "bad," which you think will contribute to worse results. (If you think wrong, don’t worry.) Put a

b

subscript by each factor’s bad level (i.e., A

b

, B

b

, C

b

), and use a g to represent the good factors (i.e., A

g

, B

g

, C

g

).

b. Run six experiments, three with all factors at good levels, the other three with all bad levels. Scramble the sequence. Don’t do all goods then all bads. Record the six outcome readings.

c. Establish D, the difference between the two median (middle value) results. In other words,

D = (Median of the three good level readings) — (Median of the three bad level readings)

d. Establish d

avg

(the average nonrepeatability range of the other four experiments). Here’s how: Call the numerical difference between the two nonmedian values of the good level experiments d

g

, and call the difference between the two nonmedian values of the bad level experiments d

b

.

d

avg

= (d

g

– d

b

)/2

e. If D/d

avg

> 1.25 (ignore negative signs), and all three good levels are better than all three bad levels, continue to f. If either of these conditions fail, switch bad and good for one or two factors that you’re not sure of, then return to b. Repeat until D/d

avg

> 1.25

and

all three good levels are better than all three bad levels. If success doesn’t come the second time around, you probably have failed to list an important factor. Brainstorm again and then start at b again.

f. Calculate the control limits for the good three as follows:

Median of the good level readings ± 2.776 (d

avg

/1.81)

Calculate the control limits for the bad three:

Median of the bad level readings ± 2.776 (d

avg

/1.81)

g. Run a test with A bad (A

b

) and all other factors good (R

g

). Then run a test with A

g

and R

b

. (When speaking, you can call these "A good, the rest bad" and "A bad, the rest good.") If the results of both A

b

R

g

and A

g

R

b

are inside the bad three and good three control limits, respectively, factor A is unimportant. Go on to h. If there’s a complete reversal (A

b

R

g

inside the good three control limits, A

g

R

b

inside the bad three control limits), factor A is the sole important factor. Step 3 is over. If either test shows results outside the control limits, A is part of the problem along with other factors. Go on to h.

h. If there wasn’t a complete reversal in the previous action, repeat g for the next factor B. (Run a B

b

R

g

test and B

g

R

b

test, and apply the same "if-then" logic to determine B’s importance. If B is unimportant, run the same pair of tests with C, then D, etc.) You eventually will find either a factor that shows a complete reversal or a couple of factors with results outside the control limits. Reversal means you’re done. You’ve found the important factor. However, if two factors, say A and K, display a partial reversal (readings outside the control limits), go to i.

i. Run a A

b

K

b

R

g

and a A

g

K

g

R

b

test to see if R—the rest of the factors—can be eliminated. If reversal is

still

not complete (a rare case), continue to search for a third contributing factor by running a A

b

K

b

X

b

R

g

and a A

g

K

g

X

g

R

b

test. By now (and probably long before this) you’ve identified your important factors.

Step 4: Establish the Best Tolerance

In Step 3 we assigned "good" and "bad" to each factor. But what is the unmistakably

best

level for the important factors? Suppose in Step 3 you discover that factor C shows significant contribution to the problem. What is now needed to establish tolerance on that factor?

One way is via scatter plots, a graphical method formally called realistic tolerance parallelograms. Here’s how to do that:

a. Plot the important customer characteristic (the result that you’ve been measuring, such as part width or number of flaws) and call it Y (see

Figure 1

). Designate a value range of factor C that you feel confident will fine-tune Y and encompass the customer’s desired range of Y (i.e., the spec range, the fewest flaws, etc.). Run 30 experiments in that range of C, and record and plot the corresponding Y values. If the graphics plot is a ramp with only a small vertical scatter (see Plot 1), this verifies again that C is an important factor. (If the plot is not a ramp or if it is a wide ellipse as in Plot 2, the factor is unimportant.)

b. Draw a center line through the 30 plots. Draw a parallel line on each side of the center so as to enclose all but one and a half of the 30 points (see Plot 3). (Note: The vertical width of this parallelogram is the variation in Y due to all factors

other than

the factor you are testing. If the parallelogram is wide, the factor you are testing is not the only important factor. Recall the partial reversal in g and h of Step 3.)

c. Mark the customer specification limit points on the Y axis. Draw a line parallel to the C axis from the upper spec limit to the upper boundary line of the scatter, and draw a like line from the lower spec limit to the lower boundary line of the scatter (see Plot 3). Finally, drop a line from each of the two boundary-intersection points straight down to the C axis.

d. Those two lines you just dropped will intersect with the C axis at the maximum tolerances allowed, specifying a minimum C

pk

of 2.0 (a tight tolerance for zero-defect quality). Divide the span into four equal parts and designate the middle half as the tolerance for the important factor. Your new bull’s eye value for the important factor is at the center of this range between the "dropped" lines. Are you surprised by the result?

e. Compare this realistic bull’s eye and tolerance with the bull’s eye and tolerance that have been used in the shop until now. Make the change to ensure zero defects!

More Good News

The typical cost of poor quality in a U.S. company is from 10 to 25 cents per dollar of sales. And that doesn’t even include the cost of lost sales, equipment downtime, supplier poor quality, and longer design times.

The truth is that few manufacturers use balanced testing to eliminate scrap and rework, and still fewer are aware of VS. Many organizations perceive designed experiments as complex, abstract, and expensive, and they’re usually right. The design of experiment tools many corporate practitioners promote are complicated, tangled, and costly. They also are mostly closed test designs.

But now you’ve been introduced to a powerful, simple, and accurate quality tool. Put it to good use.

Putting Variables Search to Use

This chart shows the data collection results from the investigation of possible causes of setup scrap in the automated welding cell. The box in the top right-hand corner lists the possible causes that were eliminated and those factors that influenced the creation of the scrap.

A metal fabricator was generating a lot of scrap in its automated welding cell. Weld burn-through and cold lapping, where a lack of fusion exists between the weld metal and the metal surface, were eating at the cell’s bottom line. The team members on both shifts were very experienced, so the fact that they were not able to nail down the real problems was baffling.

Everyone who knew anything about the cell were interviewed, both individually and in small groups, to capture the suspect variables. This included operators, maintenance, the machine vendor, weld lab techs, team leaders, supervisors, and weld engineers. Every theory was cataloged and crossed off the list only if sound logic or evidence eliminated it as a suspect.

The next step involved setting up a test pattern and showing management how the investigation was going to proceed. The cycle time was close to a minute, so the search required a fair amount of machine and operator time to conduct all the trials and changeovers needed to complete the test pattern.

As the data emerged point by point, the team plotted each result on the chart. The shop was excited to see the results as they were made public. No one predicted the outcome correctly, and no one could argue with the data because they participated in the test plan. At each step, they adjusted the variables to the plan. They knew what they were seeing was real.

In the end, the fabricator discovered that it needed to address torch placement, travel speed, and wire feed speed. Elimination of the setup scrap led to significant savings for the fabricator.

Joseph Dunn, a certified manager of quality/organizational excellence, designated by American Society for Quality, can be reached at

joe.dunn537@gmail.com

.
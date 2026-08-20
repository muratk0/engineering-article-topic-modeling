# Going old-school with notch layout

[TARİH: 01.12.2017 The Fabricator]

Bending Basics

Such knowledge shouldn’t be lost

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

By Steve Benson

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. The author’s latest book,

Bending Basics,

is now available at the FMA bookstore,

www.fmanet.org/store

.

Question:

I have an odd question. It is difficult to explain without a picture, so I drew a crude one (see

Figure 1

).

I have a piece of sheet metal with a 150-degree bend in it. I want to keep the top part of the bend continuous and keep the bottom part flat. I need to make a few slight bends so that the bottom part is no longer straight. If I cut out a wedge (notch) from the bottom part and bring the two edges together, what should the angle of the wedge be to maintain the 150 degrees?

Answer:

The answer to your question is not quite as straightforward as it may first seem to be. First, there is no simple formula for solving this notch. By the same token, it is not that difficult to calculate either, but it does take a little bit of that esoteric knowledge I spoke about in my Bending Basics column back in September.

Figure 1 What angle should the notch be? It’s not as straightforward as you might think.

My Soapbox

The information you provided is a little slim on details, so I cannot give an exact answer. I can, however, take you through the process so that you can apply your numbers to your products. That is probably all for the best as you will then learn to solve this and future notching problems.

The information presented here will only touch on the basics of notching. Beyond the basics it can get pretty deep in the weeds, with odd angles, uneven flange lengths, center shifting, and multiple bend axes.

We are in some ways fortunate that CAD systems now make these calculations for us. At the same time, few tradespeople today can do these calculations manually. Software is efficient, but it can come at the cost of knowledge lost.

If you are interested in this topic, you may want to check out

Bending Basics

, my new textbook published by the Fabricators & Manufacturers Association Intl. I dive quite deeply into the subject. Also, keep an eye out for old pattern drafting books from the ’40s, ’50s, and ’60s. You can sometimes pick these up at used bookstores for free, or next to free. Few people realize their value.

Nonetheless, if you spend a little time studying notching and learning how it works, you will be able to make more informed decisions as to which notch is the right one to select from the many available in your CAD menu. It’s worth the effort.

The Lesson

First, you need to know about

mold lines.

On the flat pattern or drawing, the area between two mold lines represents the area the radius will be after forming.

There are two of them, an

inside mold line

and an

outside mold line.

Which line is outside and which is inside? That depends on which end of the part you are working from. Generally, the outside mold line location determines the flange’s outside dimension. The inside mold line is one bend deduction less. That is, subtract the value of one bend deduction from the outside mold line location and you find the location of the inside mold line.

Figure 2

shows a simple part with two 0.750-inch outside flange dimensions at 90 degrees, and an overall outside dimension of 2.000 in. To make things simple, we’ll assume the bend deduction is 0.100 in. and the material is 0.060-in.-thick A36 mild cold-rolled steel.

Again, the area between the inside and outside mold lines will be the radius after forming. Knowing this, we can design a notch that allows for the elongation that occurs at each bend. Working from the zero-zero point (the bottom right in Figure 2), we find our first outside mold line dimension is 0.750 in., the same as our outside flange dimension. We then subtract one bend deduction, 0.100 in., to determine the location of the inside mold line at 0.650 in. (0.750 in. – 0.100 in. = 0.650 in.).

To find the second set of mold lines for our second flange (the one on the left in Figure 2), we start at the inside mold line at 0.650 in. and then add the overall outside dimension of 2.000 in. This gives us the location of the second outside mold line at 2.650 in. (0.650 2.000 = 2.650). From the outside mold line at 2.650 in., we subtract one bend deduction (0.100 in.) to find the location of the second inside mold line, at 2.550 in. (2.650 – 0.100 = 2.550 in.). Finally, from the second inside mold line (at 2.550 in.) we add another 0.750 in. for the outside flange dimension, giving us our complete flat-blank dimension of 3.300 in. (2.550 0.750 = 3.300).

To double-check your numbers, add the two outside flange dimensions (0.750 in.) to the overall outside dimension (2.000 in.) and subtract two bend deductions from the total: (0.750 0.750 2.000) – 0.100 – 0.100 = 3.300 in.

Once placed on the flat pattern, mold lines help reveal any features that lie on the radius and, therefore, distort during forming, assuming you achieved the predicted radius in the workpiece. For more information on predicting the inside radius and the corresponding bend deduction calculations, check out the four-part "Grand unifying theory of bending" series from 2015, archived at

thefabricator.com

.

The Next Level: Two 90-degree Bends, Two Axes

The previous example was simple, with two bends on the same axis, parallel to one another. The next stop on this journey starts with the workpiece in

Figure 3

, which has bends on two axes; one bend is perpendicular to the other. The part has two side flanges of equal length bent to 90 degrees, and a single perpendicular flange also bent to 90 degrees.

To lay out this notch requires us to use those mold lines again. After we find the outside and inside mold lines for both bends, we define the

center-line

for both by subtracting half a bend deduction. Again, the distance between the inside and outside mold lines is one bend deduction, and that centerline splits the distance—half a bend deduction to one mold line and half a bend deduction to the other mold line.

With the centerlines defined, we then locate the X-Y coordinates for each of the outside notch vertices. The point at which those centerlines intersect becomes the innermost location, or top-center, of the notch.

In this example, we’ll use an H-series aluminum, 5052 H32, with an inside radius and thickness of 0.063 in. and a bend deduction of 0.100 in. To see how it’s done, refer to the flat pattern in Figure 3. The red numbers in the figure correspond to the bold numbers in the text that follows.

Figure 2 This simple part has two 0.750-in. flanges and an overall outside dimension of 2.000 in.

Figure 3 This simple part has two 90-degree flanges that are both 0.750 in. The red numbers on the flat pattern correspond to the description in this article. (IML = inside mold line; OML = outside mold line; C/L = centerline

Find where the two bend centerlines intersect (

1

). From that vertical outside mold line you subtract the outside flange dimension. In our example, the outside flange dimension is 0.750 in. So in the X direction, we measure 0.750 in. from the vertical outside mold line (

2

). That value is the coordinate of the notch corner closest to the zero-zero point (

3

).

Return to the perpendicular inside mold line and add the 0.750-in. flange dimension to that value (

4

). Now you have the coordinates for the notch corner farthest from zero-zero (

5

). With this, you can program or lay out the part and cut the notch, taking elongation during forming into account.

If you’re notching by hand, you might find it difficult to get the notch perfect, so you may need to file the edge to get the notch to close up correctly. Don’t overdo your filing, though, or you’ll end up with significant gaps where the edges meet.

Also, notching material with large amounts of springback may require you to move the outsideedge notch coordinates apart just a little bit—a degree or two on each side for the notch angles. Opening each of those angles to 46 degrees each (1 more degree each side, 2 degrees total) would accommodate for 2 degrees of springback, giving us the needed extra clearance for the bend and the mating surfaces.

Another Level: More Than 90 Degrees

Notches cut at 45 degrees work for 90-degree bending. But how exactly do you calculate the notch dimensions for bends that are

not

90 degrees? Here is where some right-angle trigonometry comes into play.

Consider

Figure 4,

which shows a notch that allows us to bend past 90 degrees. The 0.500-in. side flanges are bent at the horizontal mold lines to 90 degrees; the bend deduction (and distance between the mold lines) is 0.100 in. Meanwhile, the perpendicular bend is 120 degrees complementary (60 degrees included), with a bend deduction of 0.250 in. That 120-degree-complementary bend changes your notch dimensions.

How do we find these dimensions? First, we need to define a right triangle at the intersection of the notch, based on what we know. As shown by the side view in Figure 4, the notch is being bent to a 60-degree-included (120-degree-complementary) angle. We draw a triangle where the notch dimension will be. The triangle splits that 60-degree-included bend angle in half, so we know that angle C has to be 30 degrees. We also know that side c is the same dimension as the side flange: 0.500 in.

So now we have enough information to solve for the missing side using right-angle trigonometry. Specifically, we need to find side b, which will give us the dimension "L" shown in Figure 4:

b = c/tan(C)

b = 0.500/tan(30)

b = 0.866 in.

This 0.866-in. dimension is the adjacent side of the triangle and the required dimension needed to lay out the notch. As before, you start by finding where the two centerlines intersect. From the vertical mold lines you measure 0.866 in. to the right and left, as shown in Figure 4. All this corresponds to Steps 1 through 5 shown on Figure 2.

Another Level: Less Than 90 Degrees

Now let’s look at a notch bent to less than 90 degrees complementary, to 60 degrees. This time we need to define the right triangle shown in red in

Figure 5.

Our bend deduction for the 90-degree bend remains 0.100 in., but our bend deduction changes to 0.050 in. for the 60-degree-complementary bend.

Figure 4 This shows a side view (top) and flat pattern for a notch bent to 120 degrees complementary (60 degrees included). Side b of the right triangle gives us the 0.866-in. distance between the vertical mold lines and the bottom of the notch, shown on the bottom.

Figure 5 This shows a notch bent to 60 degrees complementary with equal side flanges. The bend deduction for the 90-degree bend is 0.100 in., while the 60-degree bend has a bend deduction of 0.050 in. The side b dimension in the right triangle is the same as the dimension between the vertical mold line and notch corner in the flat pattern, as shown.

Again, the right triangle splits the 120-degree-included angle in two, so the angle at C is 60 degrees. And we know side c is the 0.750-in. flange dimension. From here we solve for our missing value: b.

b = c/tan(C)

b = 0.750 in./tan(60)

b = 0.433 in.

We then directly apply the 0.433-in. dimension to the appropriate mold line and in the proper direction to find the notch location points on the edge of the workpiece, just as we did earlier (again, as outlined in the steps described in Figure 3, but with dimensions shown in Figure 5).

No Longer a Manual Process

We’ve looked at only a few of the notching possibilities your CAD system is capable of making. For even more, check out "Press brake bending and the notch: a deeper dive" from March 2016, archived at

thefabricator.com

.

True, with the exception of some prototype work, you probably won’t be laying out your notches by hand. It’s just too time-consuming to manufacture products this way. Regardless, by taking a little time to learn how notching works and then applying that knowledge to your corner selection on your CAD system, you can’t help but build better parts.
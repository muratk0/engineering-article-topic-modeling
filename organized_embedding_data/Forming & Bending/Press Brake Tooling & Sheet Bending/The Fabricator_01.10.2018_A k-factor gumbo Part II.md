# A k-factor gumbo: Part II

[TARİH: 01.10.2018 The Fabricator]

Bending Basics

A deep dive into the k-factor, what it is, and why it matters

By Steve Benson

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Editor’s Note: This is the second part of a series covering the variables that affect the k-factor value in bending. You can find the first article in this series archived at

thefabricator.com

.

▸ Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. The author’s latest book,

Bending Basics

, is now available at the FMA bookstore,

www.fmanet.org/store

.

▸ This series has drawn from a range of sources, from the well-known

Machinery’s Handbook

to various research papers. For a list of sources, visit the online version of this article at

www.thefabricator.com

.

O

f all the mathematical constants in precision sheet metal fabrication, the k-factor stands out. It’s the base value needed to calculate bend allowances (BA) and ultimately the bend deduction (BD). You could say it’s the roux of the precision bending gumbo. Get the roux right, and you’re on your way to making a tasty meal.

A Quick Review

The neutral axis is a theoretical area lying at 50 percent of the material thickness (Mt) while unstressed and flat. During bending, that axis shifts toward the inside of the bend. The k-factor value signifies how far the neutral axis shifts during bending. Specifically, the k-factor value is the neutral axis’ new position after bending, marked "t" in

Figure 1

, divided by the material thickness (k-factor = t/Mt).

There’s a lot that goes into this value and various factors that affect it, many of which we covered last month. These include the minimum bend radius, both as it relates to the material thickness (as specified by material suppliers) and as the borderline between "sharp" and "minimum" bend in an air form. The latter is when the pressure to form is more significant than the pressure to pierce, ultimately creating a crease in the center of the bend.

Grain direction also affects the k-factor, as does the material thickness and hardness. This month I’ll cover additional factors that affect the k-factor, then walk through a manual calculation.

Bending Method

Added to all the k-factor variables discussed last month are a few more, the first being the forming method: air bending, bottoming, or coining. First, let’s back up and cover some basics: Bottoming, or bottom bending, is not the same as coining.

When coining, the material comes into full contact with the sides of the punch and the sides of the die (see

Figure 2

). At this point and beyond, the material is put under extreme amounts of force, so extreme that the punch tip penetrates the neutral axis, and the punch and die come together at a position that is less than the material thickness.

This severely thins the material at the bottom of the stroke. These tonnage loads are large enough to cause the metallurgical structure to realign, allowing you to create a radius as small as you need to get. A very sharp, crisp inside bend radius (Ir) is generally considered the goal of a coined bend.

Bottoming, on the other hand, requires clearance between the punch and die angle. The descending punch tip forces the material to wrap around the punch; as the punch continues to apply force, the material is forced open to conform to the die angle (see

Figure 3

).

Actual bottoming occurs from the material thickness to approximately 20 percent above the material thickness, with only the inside bend radius being compressed by force from the punch tip, further thinning the material at the point of bend.

Air forming, or air bending, dominates modern precision bending (see

Figure 4

). Air forming is a three-point bend; that is, the tools contact the bend at three points—at the punch tip and the two radii leading into the die opening. The material’s expansion and compression during forming depend on its material properties.

Unlike bottoming or coining, air forming creates a floated radius based on a percentage of the die opening, and the angle is determined by the punch’s depth of penetration into the die space. Tonnages are relatively small compared to bottoming and coining. The process also requires accurate press brakes and tooling. Many older press brakes are not well-suited for air bending.

How do each of these bending methods affect the k-factor value? Air forming is our baseline method for defining the k-factor, neutral axis, and BA. Compared with air bending, bottoming will have a higher k-factor value. At least one research study has shown that switching from air forming to bottoming, using the same material and tooling, increases the k-factor value by 15 percent. This is because of the considerable amount of deformation that occurs at the radius.

Coining eliminates stresses in the material. It accomplishes this with pressures that are so great that all the metal at the radius and in the surrounding flat areas are brought up to their yield point. The release of stress is a significant factor behind why the coining process eliminates springback. This relieving of internal stress causes the neutral axis to move back toward the inside surface of the bend, compared to the neutral axis’ position during bottoming.

Die Width

As covered last month, when you increase the material thickness, the k-factor gets smaller—if, that is, you use the correct die opening for the material thickness at hand. But if you increase your material thickness and keep the same punch and die combination, a different phenomenon occurs. A greater material thickness forming with the same punch and die combination increases friction and reduces the ability of the material to slide over the die radius. This increase causes greater material deformation at the bend, which causes the k-factor value to increase.

Similarly, if you keep the same material thickness but decrease the die width, the k-factor increases. Experiments have shown that the smaller the die opening becomes, the larger the k-factor. When the material thickness remains constant, the smaller die requires considerably more force to reach the same bend angle.

Figure 1

The k-factor is defined as the neutral-axis shiftduring bending (t) divided by the material thickness (Mt).

Figure 2

When coining, the material comes in full contact with both the punch and die. The severe thinning relieves material stress and, in turn, causes the k-factor to be less than it would be during bottoming.

Figure 3

When bottoming (which is different from coining), the material wraps around the descending punch. Continued pressure then forces the metal open against the die angle. Material deformation at the radius during bottoming causes the k-factor to be higher than it would be during an air form.

Figure 4

Air bending has a floated radius that forms as a percentage of the die opening.

Figure 5

The terminology used for this discussion is presented here.

Coefficient of Friction

A coefficient of friction is the relationship of the force of friction between any two objects as they move against each other. The coefficient of kinetic friction is the resistance to movement, the "dragging" force between two objects when one moves past the other.

The coefficient of friction depends on the objects that are causing friction—in our case, the sheet metal or plate sliding over the radii on the top corners of the die. The value can be between 0 (which means no friction is present) to 1.

What does this mean to you? As the metal gets harder and/or thicker, the k-factor decreases, as discussed last month. Why, exactly? It comes back to the coefficient of friction, and the stress and pressure induced during forming.

A Review of the Ingredients

To recap, to say the k-factor "increases" means the neutral axis ends up closer to the middle of the sheet thickness. To say the k-factor "decreases" means the neutral axis shifts farther inward toward the inside surface of the bend.

With that, let’s review the k-factor gumbo ingredients, starting with the bend radius. Say you decrease the inside bend radius relative to the material thickness. When you’re bending a small radius with the grain, you can induce cracking on the outside of the bend. When you go so far as to pierce the bend line at the inside bend radius with a far-too-sharp punch tip, the grains expand on the outside of the bend, forcing the neutral axis to move inward—decreasing the k-factor.

When you change the forming method from air forming to bottoming, the k-factor increases in reaction to deformation and significant thinning of the bend radius. When you change from bottoming to coining, the k-factor decreases as stress is relieved and the neutral axis moves more toward the inside surface of the bend.

When material gets thicker and harder, the k-factor decreases. But if you change the material thickness without changing your tooling, the bending force changes. For this reason, the k-factor tends to increase with the thickness of the material when the material is being formed over the same punch and die combination. Similarly, if you keep your material thickness constant but use a narrower die width, the k-factor increases.

Levels of Accuracy

Now that you know how the ingredients interact, let’s get cooking. Before you dive into the equations, review

Figure 5

, which shows the terms used for this discussion.

Again, for many applications, using an average kfactor value of 0.4468 gets you close enough. In fact, I’ve used this k-factor average for the BA formula given many times previously in this column:

BA = [(0.17453 × Ir) + (0.0078 × Mt)] × External bend angle

That "0.0078" is the result of Π/180 × 0.446—and that 0.446 is our k-factor average.

Shop technicians also have used other quick-and-dirty methods for calculating the k-factor, one being based on the radius-to-material thickness relationship. If the radius is less than double the material thickness, the k-factor is 0.33; if the radius is greater than double the material thickness, the k-factor is 0.5. This works fine if you’re, say, forming dump truck boxes.

But if you need a little more accuracy, choose your k-factor from a chart, like in

Figure 6.

Measuring Test Pieces

If you need even

more

accuracy, you can calculate the k-factor from scratch based on some test bends. As discussed, a change in any one variable can change our k-factor. In most cases, determining a precise k-factor will require at least three test pieces of the same material grade and thickness, ideally from the same source bent under the same conditions, including the same grain direction.

Figure 6

This generic k-factor chart, based on information from

Machinery’s Handbook

, gives you average k-factor values for a variety of applications. The term "thickness" refers to the material thickness. A k-factor average of 0.4468 is used for most bending applications.

Figure 7

This shows one way in which you can use right-angle trigonometry to "walk through the triangles" and calculate the inside leg dimension (dimension F) of a bend with an external angle of 60 degrees.

Figure 8

This shows one way to use right-angle trigonometry to calculate the internal leg dimension of your test piece.

To calculate the k-factor, you need to collect some information: specifically, the BA and the Ir. Measure each test piece, determine the average, then insert that value into the k-factor formula, which I’ll get to later.

First, measure the test pieces as accurately as you can. To find the Ir, measure the formed piece with a pin gauge or radius gauge or, if you want better accuracy, an optical comparator.

Measuring the BA gets a little more complicated. Again, the BA is the arc length of the neutral axis, which, as discussed, has shifted inward during bending. Measure the flat dimension first, before forming, then find the BA.

Measuring Bend Allowance for 90 Degrees

If your bend equals 90 degrees, you can measure the total outside dimension of the formed part, then subtract the Mt and the measured Ir from the outside flange dimension; this gives you the inside leg dimension. Add your two inside leg dimensions together, then subtract the flat dimension, and you get the BA:

Inside leg dimension for 90-degree bend =

Outside dimension – Mt – Ir

Measured inside leg dimensions – Measured flat = BA

Again, this equation works only for 90-degree bends, basically because of how the radius and leg dimensions relate at a 90-degree angle. Technically speaking, it’s because the flat leg length meets the Ir at the tangent point.

Greater or Less Than 90 Degrees

To measure the BA for bends with angles greater or less than 90 degrees, things get more complicated. Start with the measured points from the test piece, then rely on some right-angle trigonometry to find the inside leg dimensions.

Note that the trigonometry equations that follow aren’t the only options. You can refer to any trigonometry reference, online or in your library, to find various equations that let you solve for different sides and angles of a right-angle triangle.

First, let’s tackle an external angle less than 90 degrees. Consider the 60-degree external bend angle in

Figure 7

. The steps that follow refer directly to the steps referenced in the figure, and you’ll need to repeat these steps for the second inside leg.

Step 1:

Measure dimension A on the test piece.

Step 2:

Add Mt to dimension A, and you get dimension B.

Step 3:

Using a device such as a pin gauge, radius gauge, or optical comparator, measure the Ir.

Step 4:

Calculate for the outside setback (OSSB): OSSB = [tangent (external bend angle/2) × (Mt + Ir). The OSSB gives side a of the green triangle. Because the external bend angle is 60 degrees,

angle C

of the green triangle is 30 and

angle B

is 60. This allows you to solve for

side b

of the green triangle: b = a × sine B. Side b is the same as dimension C, which measures to the tangent point on the material’s outside surface. (Note: At this bend angle, dimension C happens to match, or be very close to, the Mt; however, dimension C will change depending on the bend angle, so we use the OSSB to calculate dimension C’s true position.)

Step 5:

Dimension D is the same as side c of the red right-angle triangle.

Side a

(hypotenuse) is the Mt.

Angle B

of the purple triangle is the external bend angle of 60. This means

angle C

of the purple triangle is 30 degrees (60 + 30 + 90 = 180). With the material edge being 90 degrees, angle B of the red triangle is 60 degrees (30 + 90 + 60 = 180). Now you can solve for

side c

of the red triangle: c = a × cosine B.

Step 6:

Now that you know dimensions B, C, and D, you can calculate dimension E: E = B - (C + D).

Step 7:

With dimension E, you now have side b of the purple triangle. With the purple triangle angles known, you can solve for

side a

, which gives you dimension F, the inside leg length: a= b/cosine C.

What if you have a workpiece with an external bend angle that’s greater than 90 degrees? As shown in

Figure 8

, you follow a similar process, starting with your measured dimensions on the test piece and "walking" through the right triangles until you find the inside leg dimension. And like before, you repeat this procedure for the other leg.

Step 1:

Measure dimension A on the test piece.

Step 2:

Using a device such as a pin gauge, radius gauge, or optical comparator, measure the Ir.

Step 3:

Dimension B is the same as

side c

of the red right triangle.

Side a

(hypotenuse) is the Mt. With adjacent angles of 30 and 90,

angle B

has to be 60 degrees (30 + 90 + 60 = 180). Now you can solve for side c: c = a × cosine B Step 4: Once you calculate dimension B, you can find C: C = A - B

Step 5:

You’ve measured the Ir. To find

side a

of the blue triangle, calculate for the inside setback (ISSB): ISSB = [tangent (external bend angle/2) × Ir.

Step 6:

You know

side a

of the blue triangle is the ISSB. You also know

angle C

has to be 30 degrees (60 + 90 +30 = 180). You can now solve for

side b

of the blue triangle, which will give you dimension D: b = a × sine B.

Step 7:

Now that you know dimension D, you can find E: E = C - D. This gives you

side b

of the purple triangle.

Step 8:

With that, you can solve for side a of the purple triangle, which gives you dimension F, the inside leg length: a = b/cosine C. Congratulations, you’ve found the inside leg dimensions! Now, as you did for the 90-degree bend, add the two inside leg dimensions together and subtract the flat dimension to determine the BA:

Measured inside leg dimensions – Measured flat = BA

Finally … Calculating for k

Once you have the Ir and BA for your test pieces, you can plug those values into the following equation:

k-factor = [(180 × BA) / (Π × External bend angle × Mt)] - (Ir / Mt)

You then can repeat this until you have a least three test pieces, after which you can average your k-factor result. This gives you a custom-calculated k-factor for the application.

The Y-factor

But wait, there’s more! You can achieve an even greater level of precision. If you know the k-factor, you can use it to calculate the Y-factor, which takes certain material stresses into account.

Just what is the Y-factor, and how does it relate to the k-factor? It’s a very close relationship. Both Yand k-factors affect how the bend ultimately elongates during bending, and one is directly related to the other. In fact, to calculate the Y-factor, you need to know the k-factor.

The computer-aided design software you are using may employ a Y-factor instead of a k-factor when calculating for BA and the BD, enabling you to create a more precise flat pattern for your sheet metal part. You can use a Y-factor in a chart, like the one published in the March 2018 Bending Basics. (Visit

www.thefabricator.com

and type "K-factors, Y-factors, and press brake bending precision" in the search bar.) Alternatively, if you know your k-factor, you can calculate the Y-factor with the following formula:

Y-factor = (k-factor × Π) / 2

If you do use the Y-factor, you’ll need to make some adjustments to your bend calculations. Specifically, you will need to use a different formula to calculate the BA:

BA = [(Π/2) × Ir ] + (Y-factor × Mt) × (External bend angle / 90)

A Sweet Gumbo

With all this, you have what we need to insert your customized k-factor and (if desired) the Y-factor into your bend calculations. Let’s review the steps just covered, then move through the familiar bend equations:

Bend at least three test pieces.

Measure the pieces to find the Ir and the BA.

Calculate the k-factor:

k-factor = [(180 × BA) / (Π × External bend angle × Mt)] - (Ir / Mt).

For further accuracy, find the Y-factor:

Y-factor = (k-factor × Π) / 2.

Now, when preparing parts for production, insert the calculated k-factor (and Y-factor, if desired) into the BA equations. This will dial in the BD, flat layout dimensions, and, hence, your overall bending accuracy:

BA with k-factor = {[(Π/180) × Ir] + [(Π/180 × k-factor) × Mt)]

× External bend angle BA with Y-factor = BA = [(Π/2) × Ir ] + (Y-factor × Mt) × (External bend angle / 90)

OSSB = [Tangent (Bend angle/2) × (Mt + Ir)

BD = (2 × OSSB) – BA

With a k-factor calculated for the material at hand, you have what you need for some great roux, sweet and robust enough to work well with all the other ingredients, like the die width, the method of forming, and coefficient of friction.

Does every bend need such a roux? Of course not. In fact, the commonly accepted k-factor of 0.4468 works darn well for everyday use. But for certain applications, especially where you really need to dial in your precision, a custom k-factor and Y-factor may be the missing ingredients you need.

k-factor … or K-factor?

Now that you know everything about the k-factor, you page through engineering textbooks or research online and stumble upon the K-factor. Not the k-factor, but the K-factor. Confused, or did you see the difference?

The k-factor (the "k" isn’t capitalized) is used to calculate the relocation of the neutral axis during bending. The K-factor (with a capitalized "K") is used to calculate the outside setback (OSSB). You need to know the OSSB before making any bends, because you use it to determine the bend deduction (BD) as well as the location of the tangent and radius of the bend.

Compared to the k-factor (for the neutral axis shift), the K-factor is a breeze to calculate. The K-factor is simply the tangent of half the bend angle. The K-factor for a 90-degree bend is always: K = tan (90/2) = 1. A Kfactor for a 60-degree bend is K = tan (60/2) = 0.5773. In fact, it’s part of the OSSB calculation I’ve used in this column:

OSSB = [Tangent (Bend angle/2) × (Mt + Ir) See the K-factor? It’s in the first half of the equation: Tangent (Bend angle/2). (As an aside, whether you use the external or internal bend angle in the OSSB calculation depends on the flat layout method. For more on this, visit

www.thefabricator.com

and type "The basics of applying bend functions" into the search bar.)
# How to calculate your bends with precision

[TARİH: 01.03.2018 The Fabricator]

Bending Basics

K-factors and Y-factors: There’s more than one way to skin a cat

By Steve Benson

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

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Figure 1

When you bend sheet metal, the neutral axis shifts toward the inside surface of the bend. The K-factor is the ratio of the neutral axis location (t) to the material thickness (Mt).

Figure 2

You can run test pieces to calculate a specific K-factor, or you can refer to a chart such as this one.

Question:

I had a question on K-factors for our 3-D modeling software. Our design engineers typically use a factor of 0.4 for our air-formed press brake parts. However, this doesn’t work well for our parts that go into a hand transfer stamping press.

I found your

theArtofPressBrake.com

and realized that aside from this question, maybe there is more I could learn. I want to help our design engineers create more manufacturable parts. I would say that I have a good understanding of the basics, but there are still issues that I come across in production parts that I tuck away to keep in mind for future designs. Are you able to answer my question on K-factors with a general recommendation without going into too much theory or calculations?

Answer:

The answers to your questions are simple; well, sort of simple. I’ll start with the fundamentals and give some general recommendations, then end with some calculations. Math is at the heart of sheet metal bending. Luckily, it’s not too complicated—no differential calculus, just geometry.

Your press brake and stamping press form sheet metal in different ways. On the press brake you are air forming, while on the stamping press you are stamping or coining. These are all distinct methods of forming, and each is calculated differently because of how the radius is produced in the workpiece.

Types of Bends

First, let’s step back and talk about the types of bends you can make in sheet metal. Have no fear; I will bring the K-factor into the discussion soon. Until then, bear with me.

There are four types of bends: minimum-radius, sharp, perfect, and radius. A

minimum-radius

bend has a radius that’s equal to the smallest inside radius that can be produced without creasing the material. Try forming a radius smaller than the minimum, and you crease the center of the radius, giving you a

sharp bend

.

The

perfect

bend has a radius that’s equal or close to the material thickness. Specifically, the perfect bend’s radius ranges from the minimum radius value up to 125 percent of the material thickness. If your radius is 125 percent of the material thickness or more, you have a

radius bend

.

Even if you are producing a sharp bend, the smallest radius you can use for your bend calculations is the minimum bend radius, if you want your numbers to work out in practice. Note also that air forming a sharp bend usually is very detrimental to consistency. The crease in the center of the bend tends to amplify any angular variations caused by changes in material grain direction, hardness, thickness, and tensile strength. The sharper and deeper the crease, the greater the effect.

Your punch nose radius comes into play here too. If the bend turns sharp at an inside radius of 0.078 in., then punch nose radii of 1/16 in. (0.062 in.), 1/32 in. (0.032 in.), and 1/64 in. (0.015 in.) are all too sharp. As the punch nose radius gets smaller in relation to material thickness, the more significant the total amount of angle variation you will experience.

There’s a lot more to know about sharp bends. For more on the subject, check out "Predicting the inside radius when bending on a press brake," "How to calculate an air formed radius of different bend angles," "Minimum versus recommended inside bend radius," "How an air bend turns sharp," as well as the four-part series "A grand unifying theory of bending," all archived on

thefabricator.com

. And years’ worth of articles are linked on my website under the media tab at

theArtofPressBrake.com

.

But, I digress. Now that we’ve discussed what types of bends there are and how we create them, we can move on to the K-factor. You’ll notice how the different methods of forming … wait a minute—we haven’t defined the forming methods yet: air forming, bottom bending, and coining.

The Forming Methods

And yes, there is a difference between bottom bending and coining. Coining forces the punch nose into the material, penetrating the neutral axis. Bottoming occurs at about 20 percent above the material thickness, as measured from the bottom of the die. (Note: For more on the forming methods, including illustrations, see "How the inside bend radius forms," archived at

thefabricator.com

.)

There is a fair probability that the die sets on your stamping press are actually coining the material, pushing the die to less than the material thickness. Otherwise, you’re probably bottom bending, which again occurs at about 20 percent above the material thickness. One forces tighter radii than the other, but both force the material to a certain radius. Regardless of the type of bend you have—sharp, minimum, perfect, or radius—if you’re bottoming or coining, the punch nose value determines the resulting radius and, hence, is what we use in our bend calculations.

Figure 3

Every bend has two outside setbacks (OSSB). To calculate the bend deduction, multiply the OSSB by 2, and then subtract the bend allowance (BA).

Figure 4

To perform a bend allowance calculation, always use the complementary bend angle.

Figure 5

The Y-factor can make your bend calculations even more accurate. To find the Y-factor, you can run a separate calculation or refer to a chart such as this.

This is not the case in air forming, however. In an air form, the produced radius is a percentage of the die opening. An air-formed bend floats across the width of the die, and the inside radius is established as a percentage of that width. The percentage depends on the material’s tensile strength. This is called the

20 percent rule

. It’s only a title, though, because the percentage changes with the material type and tensile strength.

For instance, 304 stainless steel forms a radius 20 to 22 percent of the die width, while a radius in 5052-H32 aluminum forms at 13 to 15 percent of the width. The general rule here is this: The softer the material, the tighter the inside radius.

By the way, 60-KSI mild cold-rolled steel is our baseline material for most calculations, including the 20 percent rule. That material forms a radius between 15 and 17 percent of the die width. We start with the median, 16 percent, then adjust as necessary. Say we need to work with 120-KSI material. That’s double the 60 KSI of our baseline material; hence, this 120-KSI sheet will air-form a radius that’s about double that of mild cold-rolled steel—or 32 percent of the die opening (16 percent × 2).

And Now, the K-factor

In sheet metal, the K-factor is the ratio of the neutral axis to the material thickness. When a piece of metal is being formed, the inner portion of the bend compresses while the outer portion expands (see

Figure 1

). The neutral axis is the area of transition between compression and expansion, where no change in the material occurs—except that it moves from its original location at 50 percent of the material thickness toward the inside surface of the bend. The neutral axis does not change its length but instead relocates; this causes elongation to occur during bending. How far the neutral axis shifts depends on a given material’s physical properties, its thickness, inside bend radius, and the method of forming.

Take the customary default K-factor value of 0.446, multiply it by the material thickness, and you know where the neutral axis will relocate. What we are doing in essence is forcing the measured length from a larger radius (that is, the length of the neutral axis at 50 percent of the material thickness) onto a smaller radius. The same total measured length spread over the smaller radius means we have excess material, or elongation.

Consider 0.060-in.-thick material. We multiply that by a K-factor of 0.446 to get 0.0268 in. The axis has shifted from 0.030 in. (at half the material thickness) to 0.0268 in., as measured from the bend’s inside surface. Put another way, the axis has moved 0.0032 in. inward. From there we can find the answers we need for our bend calculations.

Note that the material type, method of forming, and the relationship of bend radius to material thickness all give us different K-factors. These in turn affect the total amount of elongation that occurs and the bend deductions we need to use.

On to the Calculations

The K-factor is defined mathematically as

t/Mt

, where

t

is the neutral axis location and

Mt

is the material thickness. Because of the specific properties of any given metal, there is no easy way to calculate that value perfectly, hence the chart in

Figure 2

.

The K-factor is usually somewhere between 0.3 and 0.5. Should you wish to calculate the K-factor rather than use a chart, you will need some test pieces—four or five pieces should do nicely for this purpose.

To calculate the K-factor, you need to collect some information. First, you need to know the dimensions before and after forming and measure the inside radius as accurately as possible. An optical comparator is a good first choice because of its accuracy; other options include gauge pins and radius gauges.

Take the total of the formed inside dimensions, subtract the flat size, and you get the bend allowance (BA). Then measure the complementary bend angle and inside bend radius (Ir). With those data points, along with the material thickness (Mt), you can solve for the K-factor (all dimensions are in inches):

Of course, it’s easiest to use a known K-factor from a table, like in Figure 2. You can use this K-factor and the inside bend radius to calculate the neutral axis. Then use the neutral axis radius to calculate the arc length of the neutral axis—which equals your BA. You next calculate the outside setback (OSSB), a dimension shown in

Figure 3

. This, along with your complementary bend angle (see

Figure 4

), gives you all you need to calculate the bend deduction (BD), or the total amount of elongation that will occur in a given bend:

The K-factor comes into play in this calculation. You’re probably wondering what those numerical values are within the formula—0.017453 and 0.0078. What do they represent? That 0.017453 is pi divided by 180, and the 0.0078 is (π/180) × K-factor.

The material type, method of forming, and the relationship of bend radius to material thickness all give us different K-factors. These in turn affect the total amount of elongation that occurs and the bend deductions we need to use.

This formula uses a K-factor of 0.446. Still, if you have any change in the method of forming, type of material, or the ratio of inside bend radius to material thickness, you will have a different K-factor value. To incorporate this new value, you can use an expanded version of the same formula. You then determine the OSSB, then use the result along with the BA to calculate your bend deduction:

Welcome the Y-factor

By using a Y-factor, your calculations can be even more precise. It does require you to change the formula for BA, however. The Y-factor takes into account stresses within the material, while the Kfactor does not. Nevertheless, the K-factor still is involved, just massaged a little.

To find the Y-factor, you can refer to a chart (see

Figure 5

), or you can use this equation:

We then insert the Y-factor into a new formula for BA:

We’ll walk through the process for both sets of equations using 60-KSI mild cold-rolled steel that’s 0.062 in. thick with a 0.062-in. inside bend radius and a 90-degree bend angle. For this example, we’ll use a K-factor of 0.446.

Now, here are bend calculations using only the Kfactor and our original BA equation:

The difference in BA between the two calculations is just 0.0001 in., and the difference in BD is also 0.0001 in., which in this example makes these two ways of calculating the BA functionally the same. But change a bend angle or an inside bend radius, and everything changes. You will find that the latter set of formulas using the Y-factor is slightly more accurate than using the K-factor.

Dial in Your Bend Calculations

It is common practice throughout the industry to use 0.446 for a K-factor value. But by selecting the proper data values, including a K-factor based on application-specific variables (material type, method of forming, and inside radius), I think you’ll find that many of the issues you are encountering between the two different methods of production will disappear.
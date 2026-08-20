# The 4 Pillars of Press Brake Tonnage Limits

[TARİH: 01.04.2015 The Fabricator]

Bending Basics

Follow these four steps and never deal with a damaged press brake

By Steve Benson, Contributing Writer

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Q:

I have read many discussions on forming tonnages, yet it still makes no sense to me. I’ve heard about numerous variables—tool load, tonnage per foot, tonnage per inch, centerline limits, even "sink" tonnage. Which one is the right one for me to use? Should I be using more than one of these values?

A:

Like many aspects of the sheet metal trade, the terms can be confusing, how they are applied can be confusing, and the worst part, not understanding how tonnage is calculated and applied can lead to some disastrous consequences. I and many others have written articles discussing tonnage and its many aspects. But I have not found one that puts all those aspects together, which ultimately would have answered your question. So here are all those variables, in order of progression, all in one place.

Note, however, that some formulas mentioned here require knowledge specific to the materials used in the manufacturing of the press brake and the tooling—so you shouldn’t consider the calculated figures as absolute values. Instead, use them as reasonable guidelines. To be sure you are operating your equipment safely within tonnage limits, be sure to consult your press brake machine and tooling manufacturer.

1. Calculate the Forming Tonnage the Job Requires

I like to call this "What will it take to do what I’m planning to do?" Press brake forming tonnage calculations are relatively easy. The trick is knowing where, when, and how to apply them. Let’s begin with the tonnage calculation, which is based on the point where the yield is broken in the material and actual bending begins. The formula is based on AISI 1035 cold-rolled steel with 60,000-PSI tensile strength. That’s our baseline material. The basic formula is as follows:

Tonnage for air bending AISI 1035 = {[575 × (Material thickness

2

)] /Die-opening width /12} × Length of bend

The 575 value is a constant; the die-opening width, material thickness, and length of bend are in inches. Abiding by the mathematical order of operations, you first square the material thickness value, then multiply that value by 575. Then divide that value by the die width in inches and then divide again by 12 (inches). You now know the tonnage per inch required to form the part. After this, multiply by the length of bend—that is, the number of inches of interface between the tooling and material.

This is assuming that you are air bending the baseline material, AISI 1035, 60,000-PSI tensile cold-rolled steel. For other material types, you need to include a

material factor

in the formula. To determine the material factor, divide the material’s tensile value by 60,000 PSI, the tensile of the baseline material. If the 304 stainless you’re bending has a tensile strength of 84,000 PSI, then you divide that by 60,000 to get a material factor of 1.4. Some other common material factors are:

T-6 Aluminum: 1.0 - 1.2

AISI 1053: 1.0

H-series aluminum: 0.5

Hot-rolled pickled and oiled: 1.0

This is just a short list. Again, to attain the material factor, compare the tensile value of the material you want to form to the baseline material’s 60,000 tensile value. If the tensile value of the new material is 120,000, then the material factor is 2.

All this assumes you’re air bending. Note that in air bending, tonnages can be reduced or increased by narrowing or widening the die-opening width. Also remember that when air bending, the dieopening width directly affects the inside bend radius. This means you need to calculate the bend deduction based on the floated inside radius created in the die width you ultimately select.

However, if you are bending with another forming method, your required tonnage will change, and you need to include a

method factor

in the formula. If you are bottom bending, you may need five times as much tonnage, and for coining it can be 10 times or even more. (Note: Bottom bending is forming to a depth within 20 percent of the material thickness, while coining occurs when forming is performed at less than the material thickness.)

Yet another variable not often discussed is the

multiple-bend tooling factor

when using special tools that form multiple bends at one time, such as offset tools, hat tools, and hemming operations. For instance, using offset bending tools or hat tools can quintuple the amount of tonnage needed; a hem tool can quadruple the needed tonnage; and if you’re using an offset tool in thick material, tonnage requirements can increase by a factor of 10.

To summarize and review, here is the complete formula to calculate the forming tonnage a job will require, incorporating material, forming method, length of bend, and multiple-bend tooling factors. Material thickness, die-opening width, and the length of bend are all in inches.

Forming tonnage

= {[575 × (Material thickness

2

)] / Die-opening width/12} × Length of bend × Material factor × Method factor × Multiple-bend tooling factor

Material factor

= Material tensile strength in PSI/60,000

Method factor

= 5.0 for bottom bending; 10.0 for coining; 1.0 for air bending

Multiple-bend tooling factor

= 5.0 for offset bending; 10 for offset bending in thick material; 5.0 for bending with a hat tool; 4.0 for bending with a hemming tool; 1.0 for conventional tooling

Air bending 60,000-PSI AISI 1035 using conventional tooling would give you a value of 1.0 for all the factors (material factor, method factor, and multiple-bend tooling factor), so they won’t affect your tonnage requirements. But if you’re bending another material with a different tensile value, using a different bending method and perhaps even special tooling, your tonnage requirements will be dramatically different.

Figure 1

To calculate tool load limits for American plane-ground tooling, with no tool rating information from the factory, you need to know the distance from the tool nose to the tangent point between the neck and the inside radius (l), the width of the neck at that same point (T), and the length of the tool (b).

Figure 2

The land area of the tool—that is, where the punch and die contact each other—is calculated by measuring the width of the shoulder and multiplying it by 2. Then multiply that number by 12.

2. Identify Your Tooling Load Limits

If you’re lucky, you are using precision-ground press brake tooling, which comes rated from the factory. Printed on the tool or in the catalog you will find the rated tonnage for that specific tool.

If you are using American planed-style tooling, this information is not provided to you. It never has been and probably never will be. To predict the maximum tool strength or resistance to pressure, your calculations will get pretty deep into the weeds. The formulas use the tool material type, heat treatments and hardness, as well as a yield point coefficient—again, all fairly complex, so we’ll avoid that here and instead cover how you can obtain a quick estimate of a punch’s ability to withstand load.

To do these calculations, you need to know the distance from the tool nose to the tangent point between the neck and the inside radius (l), the width of the neck at that same point (T), and the length of the tool (b), as shown in

Figure 1.

Note that l, T, and b values are in millimeters. You’ll also need to incorporate a safety coefficient (δ) of 19.98. (If you’re curious, you get this coefficient by multiplying 60 kg/mm

2

by 33 percent.) Z and P

1

in the formulas below are calculation factors used to attain a tool’s load limit.

P = Punch’s resistance to pressure, in tons per square meter

l = Distance from the tool nose to the tangent point between the neck and the inside radius of the tool, in millimeters

T = Width of the tool neck at the tangent point, in millimeters

δ = 19.98

b = Tool length in millimeters

Formulas:

Tons per inch

= P/39.37

Tons per foot

= Tons per inch × 12

If is 38.1 mm, T is 15.87 mm, and b is 1,000 mm, you’d run the calculations as follows:

Tons per inch

= 209/39.37= 5.308

Tons per foot

= Tons per inch × 12

Tons per foot

= 5.308 × 12 =

63.696 tons per foot

The total safe load on the tool described in this example is 63.696 tons per foot. Note that this calculation is based on the low end, with safety being the greatest concern. Regardless, know that this is only an estimate of tonnage load.

Also note that American planed-style tools are relatively soft, between 30 and 40 Rockwell C, and the new precision-ground tools are around 70 HRC. If you exceed the tool load limit of a planed tool, it will bend, go bang, and a piece will fall on the floor; overload a precision-ground tool, and

it will throw shrapnel

.

3. Calculate the Sinking Tonnage Limit

Sinking tonnage limit

refers to what it takes to physically embed your tooling into the press brake’s bed or ram. This considers the "power flow" through the tool and the maximum tonnage per foot or inch of load. To begin, we need to know the number of square inches that are interfacing between the tooling (both the punch and die). This is the land area, as shown in

Figure 2

.

To calculate the land area, measure the shoulder width on both the punch and die. Because every tool has two shoulders, you double the shoulder measurement. Finally, to get the total area in square inches, multiply this result by 12. For the total tonnage, multiply this result by 15, a number that represents the tons per square foot that the ram material can withstand before deformation begins.

Then you multiply this result by a safety factor of 0.80, reducing your tonnage limit by 20 percent. To summarize:

Land area

= (Shoulder width × 2) × 12

Total tons

= Land area × 15

Sinking tonnage limit

= Total tons × 0.80

To illustrate, if your tools have a shoulder width of 0.350 in.:

Land area

= (0.350 × 2) × 12

Land area

= 8.4 sq. in. of interface

Total tons

= 8.4 × 15 = 126

Sinking tonnage limit

= 126 × 0.80 safety factor

Sinking tonnage limit

= 100.8 tons per ft.

Is the tonnage too high? Consider using bigger shoulders! A larger land area on your tools can withstand greater pressure.

Figure 3

Assuming you are working in the center of the press brake, you will encounter deflection, or the flexing of the bed and ram. The average design limit for deflection of the bed and ram is 0.0015 in. per ft. between the side frames.

4. Calculate the Press Brake’s Centerline Load Limit

All press brakes are designed for centerline loading—that is, working in the center of the press. This does not mean you can’t work offcenter. Some machines can work off-center and some cannot. But assuming that you are working in the center of the press brake, you will encounter deflection, or the flexing of the bed and the ram, as shown in

Figure 3

. (If you can work off-center, especially under the power flow where there is no deflection in the ram, embedding the tools can become a problem; see No. 3.)

If you review and use these four steps, you will keep your loads within due bounds, and you should never have to deal with a damaged press brake or, even worse, flying shrapnel from an exploding tool.

All press brakes deflect under a normal load, and that deflection is based on the thickness and height of the press brake ram and bed. Normal deflection is the amount that the ram and bed can be subjected to and still return to their original shape after the load is removed.

The average design limit for deflection of the bed and ram between the side frames is 0.0015 in. per ft. So a press brake with 10 ft. between the side frames has an allowable bed and ram deflection limit of 0.015 in. (10 ft. × 0.0015 in. per foot = 0.015 in.) at the center. Note that this 0.0015-in. deflection is the maximum rise at the center using the average crowning or compensation device.

Figure 4

Most press brakes are designed to have a maximum allowable deflection in the ram and bed when a full-tonnage load is applied over 60 percent of the distance between the side frames.

When the load deflects the ram and bed beyond the design limit, however, the ram and bed take on a new, set shape and will never return to their original condition. This is called

ram upset

, where the press brake ram is permanently deflected in the vertical plane, leaving the distance between the ram and the bed greater in the center of the machine than at either end.

With the exception of very small machines, press brakes are designed to have a maximum allowable bed and ram deflection when a full-tonnage load is applied over 60 percent of the distance between the side frames (see

Figure 4

). It follows then that a 100-ton press brake with 10 ft. between the side frames will deflect to the design limit when the 100 tons are applied over 6 ft., split at the centerline of the ram and bed, with no resulting damage to the press. However, if that same 100 tons were to be distributed over an area less than 6 ft. (72 in.), the machine would exceed its designed deflection limits and permanently damage its bed and ram.

Following our example of the 10-ft., 100-ton press brake, divide 100 tons by 72 in. (that is, 60 percent of the bed length), and you get the maximum tonnage per inch you can achieve without exceeding the centerline load limit. To summarize:

Centerline load limit = Machine tonnage rating / (Distance between the side frames in inches × 0.60)

Centerline load limit = 100/(120 × 0.60) = 1.3888 tons per inch, or 16.66 tons per foot

Never

exceed the centerline load limit. To be absolutely sure you don’t surpass the deflection limit, contact your press brake manufacturer and ask what the centerline load limit is for the specific make and model of your machine.

Conclusion

Follow these four steps in order, and make sure you do not exceed any of these limits. To be sure, there are other tonnage factors to consider—off-center loading, balancing of the load, and the use of urethane tooling, to name a few. But if you review and use these four steps, you will keep you loads within due bounds, and you should never have to deal with a damaged press brake or, even worse, flying shrapnel from an exploding tool.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC, 2952 Doaks Ferry Road N.W., Salem, OR 97301,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. For more information on bending, check out Benson’s new book,

The Art of Press Brake: the Digital Handbook for Precision Sheet Metal Fabrication

, © 2014, available at

www.theartofpressbrake.com

.
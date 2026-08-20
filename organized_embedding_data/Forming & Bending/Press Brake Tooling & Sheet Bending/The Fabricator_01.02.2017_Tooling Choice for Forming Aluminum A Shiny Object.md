# Tooling Choice for Forming Aluminum: A Shiny Object Deep in the Woods

[TARİH: 01.02.2017 The Fabricator]

Bending Basics

How the floated radius, sharp bends, and annealing factor into the decision

By Steve Benson

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Question:

I work at an aerospace company, and I need to bend aluminum parts (6061 T6 and 2024 T3 alloys) of different thickness in three groups. The first group is 0.016, 0.020, and 0.025 inch thick, and all need to be formed to a specific inside radius; the second group is 0.032 in. thick, which needs to be formed to another inside bend radius; and the third group, 0.040 and 0.050 in. thick, needs to be bent to another inside bend radius. To make it more complicated, the bending angle ranges from 30 to 120 degrees.

What should the punch radius be? Do I need three different punch nose radii to achieve the three radii? As for the V die, what should the opening (width) and angle for each be? Ideally, I’d like to use as few tools as possible while still maintaining repeatability and accuracy.

Answer:

Without being there to see the results or knowing your customer’s specifications, I really can’t recommend a specific tool or manufacturer. I will, however, be glad to explain the process you can use to arrive at the answers. But I’ll be asking questions that are just a little different from the ones you presented.

First, I recommend that you review "How an air bend turns sharp" from the May 2015

FABRICATOR

, as well as the first three parts of "A grand unifying theory of bending," published September through November 2015. All of these articles are archived at

www.thefabricator.com

.

As you can see in these articles, we can get pretty deep into the weeds on this subject. But for now, we’ll focus on your job at hand—that shiny object right out there in the weeds.

Choosing a Die Width

First, to form the aluminum workpieces you mentioned, you will be air forming. This means the radius generated in the bend is a ratio or percentage of the die opening, known as the

20 percent rule

. This is only a label as the percentages vary by material type. The softer the material, the smaller the percentage. And for very soft material, you need to factor in where the bend turns sharp and the punch nose radius. To get deeper into the weeds on this topic, check out "What makes an air bend sharp on the press brake?" from the November 2016 issue, archived at

www.thefabricator.com

.

That being said, you have two options: (1) Buy quite a few lower dies for every application and desired inside radius or (2) purchase a die width that produces the largest inside radius you need, testbend the different materials with the die, and record the resulting inside bend radii. The radii values are then used in your calculations or CAD system to generate the bend functions: outside setback, bend allowance, and bend deduction.

Choosing a Die Angle and Die Width

Because you are air forming, and because some of the bends have a reasonably tight bend angle, a 30-degree-included die angle would be an excellent choice, giving you the widest possible range of forming options. Unless you are bottom bending, the included angle of the die will not affect the resulting inside radius.

Again, in air forming, the inside radius forms as a percentage of the die width, or die opening. So you’ll need to have tools capable of producing the smallest and largest inside bend radius required. Depending on the specifications of the parts you are building and the required inside radius, you might need to purchase another die that’s halfway between your smallest opening (which produces your smallest inside bend radius) and largest opening (which produces your largest radius).

Bend angles that exceed 90 degrees complementary will produce an inside radius in the part smaller than the nose radius of the punch. This effect is known as

multibreakage

. This manifests itself as the inside radius of the material separating from or leading the punch nose through the forming process. It is very difficult to predict, and a test bend for your application may be the best course of action.

If you have a urethane block of midrange durometer—40 to 60 on the Shore A scale—you can use it as a "solid hydraulic" that pushes back against the bend’s leading radius, forcing the material against the radius of the tool and allowing it to take on the radius of the tool. You could also use an old piece of high-pressure water hose laid in the bottom of the die.

Without the urethane backup, the inside radius will continue to collapse until the required bend angle is reached; this is true when forming in relieved dies. Small-radius bends also collapse until reaching a zero radius upon reaching a hem. For bends being formed using standard or aircraft channel dies, the radius will follow the tool radius.

Punch Angle and Radius

Because you are air forming, the radius you achieve is a function of the die opening; the punch itself is only the "pushing unit." If you follow my recommendation on die selection using a 30-degree-acute die, you will also need an acute punch. In this case, a 28-degree-included angle would be a good choice, because it gives you 2 degrees of clearance between the punch and die faces. The clearance keeps someone from bottoming or side-loading the die and causing it to break.

To achieve consistent, high-quality parts, you need to choose a punch nose radius that’s as close as possible to the naturally floated inside radius of an air formed bend, but

without

exceeding the floated radius. If your punch nose radius exceeds the naturally floated radius, the material will tend to take on the new, larger radius. For example, if the floated inside radius of your air bend is 2.25 mm, the nearest punch nose radius that is available commercially off-the-shelf is 2.00 mm. This tool will give you the most stable part-to-part bend possible.

Once again, to get farther into the weeds about calculating the naturally floated inside radius, check out "What makes an air bend sharp on the press brake?" from November 2016 on

thefabricator.com

.

Supplier Reference Materials

As you are in the aircraft industry, you know that bends can be made too sharp. This creates a crease in the bottom of the bend that in aircraft work is unacceptable, making for another piece of scrap. On that note, I recommend that you consult with the manufacturer or other reputable source for the material properties you plan on forming.

Annealing

I see you’re forming T3 and T6 series aluminum. Because T6 (as well as T4) series aluminums are difficult to form on a good day, I have one more suggestion to make: Consider forming your material of choice in its annealed condition.

T6 aluminum can be annealed (softened) by heating it to between 770 and 780 degrees F for a couple of hours, then cooling it down over several hours in a controlled manner. Once the material is in the annealed state, it will be much easier to form, especially if you need to bend to extreme angles where cracking or breaking on the bend is common.

After bending, you need to bring your material back to the T6 temper. First, raise the temperature from 970 to 990 degrees F for 60 to 90 minutes, then rapidly cool by quenching the material in water. Next comes "aging," which involves heating the material to 375 degrees F for several hours; this allows the atoms inside to align and strengthen the material structure.

It is possible to anneal and temper if you have the appropriate equipment. However, I recommend that you use a company that specializes in these processes. Doing so ensures that the quality of the temper is spot-on. Either way, working with certain materials in the annealed state is the easiest.

However, even if you do work with aluminum in its softer, annealed state, you still will find it very easy to bend sharp and put a crease along the bend line, which creates its own set of issues. Again, to delve more into the weeds on this, check out "Bending soft, but not sharp" from the June 2015 issue, archived at

thefabricator.com

.

Lacking Specifics

I understand that you have some specific questions for which I can’t provide specific answers, because there are just too many unknowns on my part. All the same, without going too deep into the weeds, I hope I’ve given you a good start to solving your problem—a shiny object stuck in the weeds. Not all shiny objects are distractions; some will lead us to the information we need the most.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. For more information on bending, check out Benson’s book,

theArtofPressBrake: the Digital Handbook for Precision Sheet Metal Fabrication,

©2014, available at

www.theartofpressbrake.com

. Steve Benson’s latest book on press brake bending, published by FMA, will be available soon.
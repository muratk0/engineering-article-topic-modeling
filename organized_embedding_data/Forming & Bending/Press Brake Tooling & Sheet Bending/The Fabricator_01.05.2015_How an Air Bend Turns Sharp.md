# How an Air Bend Turns Sharp

[TARİH: 01.05.2015 The Fabricator]

Better Bending

You can air-bend a radius that’s 63 percent the material thickness and no smaller—and here’s why

By Steve Benson, Contributing Writer

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Q:

I have just reviewed several articles in which you state that the minimum bend radius in an air form is 63 percent of the material thickness. I’ve been told by some, however, that all I need is a 1-mm punch radius to form my parts, and that the 63 percent rule isn’t real. They tell me that my radius is developed as a percentage of the die opening, which I know to be true

.

I have several questions for you. First, why is 63 percent the minimum inside radius in an air form, and why should I use this value? Second, is this the only value, or does it change by material type and thickness? Third, what are the practical effects of breaking this rule? And fourth, do I really need a large tooling selection?

A:

I’m asked these questions quite often about the 63 percent value. The most common question is, Why should I care? I was told I needed only a single 0.032-in. (1-mm) radius punch.

First, let’s clarify a few terms. A sharp bend is not necessarily the same as a

minimum bend radius

. The minimum bend radius is the minimum producible inside radius for a particular material grade’s thickness, its hardness, and bending direction (with or against the grain). However, the minimum radius may not be the recommended radius, because it often pushes your tooling and press brake near or beyond their tonnage limits, especially with thicker materials. (Editor’s note: See "

Minimum versus recommended inside bend radius

" at

www.thefabricator.com

.)

A sharp bend is the smallest radius you can airbend a part short of stamping it, and the average for this is 63 percent of the material thickness. It’s a function of the relationship between material type, tensile, yield, and thickness. When the radius becomes too small, the punch begins to penetrate the material and forces it to crease (see

Figure 1

). That crease begins to form when the radius reaches about 63 percent of the material thickness in 60,000-PSI tensile cold-rolled steel. This crease needs to be taken out of the equation if you are calculating bend deductions. This is why your bend deduction calculations should not include any radius smaller than one that’s 63 percent of the material thickness. (Editor’s note: See "

How the inside bend radius forms" at

www.thefabricator.com

.)

Figure 1 This sharp bend on 0.250-in.-thick material was made with a 0.063-in.-radius punch. Despite the narrow punch, the bend radius is 0.1575 in., or 63 percent of the material thickness.

Many materials have a minimum bend radius that is not the same as a sharp bend. Aluminum is a good example. Consult with your material supplier to obtain data about the minimum inside radius by material alloy.

Moreover, a sharp bend may not be an acceptable bend. Many applications, especially in the aircraft industry, use alloys in which a less than a 1-to-1 ratio of material thickness to inside bend radius, or if the bend has a crease, makes the part unacceptable and the material may not be warranted.

Sharp Bends in Various Materials

This 63 percent value is based on 60,000-PSI tensile cold-rolled steel with a 45,000-PSI yield. It’s a baseline material. To adapt it to other materials, you can—as with so many other calculations in bending—use a material factor, or multiplier, as shown in

Figure 2.

Sharp bend for cold-rolled steel =

Material thickness × 0.63

Sharp bend for all other materials =

Material thickness × 0.63 × Material factor

Why 63 Percent?

So where does this 63 percent value come from? That answer is a little deep in the weeds, but it’s worth learning about. We’ll begin with the baseline material, 60,000-PSI tensile cold-rolled steel with a yield strength of 45,000 PSI. In this example, our material thickness is 0.250 in. According to our rule of thumb, this bend will turn sharp (that is, a crease will start to form at the bend line) at 63 percent of Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

How an air bend turns sharp You can air-bend a radius that’s 63 percent the material thickness and no smaller—and here’s why BETTER BENDING the material thickness. That’s an inside radius of 0.157 in. (0.250 × 0.63 = 0.157 in.).

We want to choose the die opening that’s as close to perfect as possible.

(Editor’s note: For more on this, see "6 steps for successful die selection for press brakes" on

www.thefabricator.com

.)

Let’s say we choose a die opening of 1.750 in. In air bending, the inside bend radius develops as a percentage of the die opening. When air bending mild steel, the inside bend radius is between 15 and 17 percent of the die opening, and this radius measurement needs to be used when calculating bend deductions. Even at just 15 percent, the inside bend radius with a 1.750-in. die opening is 0.2625 in.—more than 0.157 in. So it’s safe to use 0.2625 in., and you shouldn’t have a sharp bend, right?

Well, although it won’t turn sharp based on your die selection, you can still create a crease in the material if your punch is too narrow. To illustrate this, we need to calculate

punching tonnage

. This isn’t forming tonnage. Instead, punching tonnage tells us how much force it takes for the punch to penetrate the surface and start forming a crease along the bend line.

To calculate punching tonnage, we need to define the

land area

, or the area of contact between the punch tip and material surface. The smaller (tighter radius) the punch tip, the smaller the land area. Let’s consider the land areas created by three different punch nose radii: 0.032 in. (less than 63 percent of the material thickness), 0.157 in. (63 percent of the material thickness), and 0.250 in. (equal to the material thickness). The land area is width multiplied by length. In this case, it’s the punch radius multiplied by 12 in. The results are:

0.032 × 12 = 0.384 sq. in. land area

0.157 × 12 = 1.884 sq. in. land area

0.250 × 12 = 3.000 sq. in. land area

Now that we know the land areas, we can determine how much force it will take for these punches to penetrate the material and start forming a crease on the bend line:

Punching tonnage =

Land area × Material thickness × 25

0.032-in. punch radius: 0.384 × 0.250 × 25 = 2.4 tons

0.157-in. punch radius: 1.884 × 0.250 × 25 = 11.775 tons

0.250-in. punch radius: 3.000 × 0.250 × 25 = 18.750 tons

A press brake can’t bend unless the force it applies exceeds the material’s yield strength. Imagine two scenarios where a punch exerts force onto the material surface. In one scenario, the punching tonnage is less than the material yield strength; as the downward pressure exceeds the punching tonnage, the punch starts to form a crease; then, as pressure exceeds the yield strength, the material starts to bend, but with that crease already formed along the bend line. In the second scenario, the punching tonnage is more than the material yield strength. As the force reaches the material yield, bending commences; the applied pressure never reaches the punching tonnage, and the crease never forms.

So to avoid a crease, make sure that the material yield strength does not exceed the punching tonnage in the land area

.

Figure 2 To determine where a bend turns sharp in materials that aren’t cold-rolled steel, you can multiply the material thickness by 63 percent, and then multiply the result by a multiplier, or material factor.

What’s the land area’s yield strength in our example? Our baseline material—60,000-PSI tensile cold-rolled steel—has a yield strength of 45,000 PSI. To determine the material yield in the land area, we first need to convert this pounds-per-square-inch (PSI) yield strength to tons per square inch. A U.S. short ton is 2,000 pounds, so to get tons per square inch, we divide 45,000 by 2,000, which gives us 22.5 tons per square inch. We then divide 22.5 by the land area:

Material Yield by Land Area

22.5 / 0.384 = 58.59 tons per square inch

22.5 / 1.884 = 11.94 tons per square inch

22.5 / 3.000 = 7.50 tons per square inch

After computing these values, you can start to see why a radius that’s 63 percent of the material thickness is the correct value for a sharp bend. Let’s start with the 0.032-in. punch radius. In the land area, it takes only 2.4 tons to have the punch tip start to penetrate the surface of the material (punching tonnage), yet the material yield in the land area is at 58.59 tons. The punching tonnage threshold is 56.19 tons less than the material yield in the land area, and this difference drives the nose of the tool into the material a good distance.

Now let’s look at the 0.157-in. punch radius, which equals 63 percent of material thickness. Here the punching tonnage is 11.775 tons, and the material yield in the land area is 11.94 tons per square inch. The punching tonnage is only 0.165 ton less than the material yield in the land area. That doesn’t seem like much, but it’s still enough to cause a crease to start to form along the bend line.

Last, we look at a 1-to-1 relationship between the punch radius and the material thickness. The punching tonnage is 18.750 tons, yet the material yield in the land area is only 7.50 tons per square inch. Here, you never come close (11.25 tons short, to be exact) to the tonnage required to crease the material.

Up until now, we’ve covered how punching tonnage relates to the material yield, but what about the die opening and resulting forming tonnage—that is, the force required to bend a given material thickness over a given die?

Following the same logic as before, if your forming tonnage exceeds the punching tonnage, creasing will ensue.

To avoid a crease, make sure that the estimated forming tonnage does not exceed the punching tonnage in the land area

. The forming tonnage for this job—0.250-in.-thick mild steel bent over a 1.750-in die—is calculated as follows:

Tonnage per foot for air bending mild steel =

[575 × (Material thickness2)] / Die width

(575 × 0.0625) / 1.750 = 20.53 tons per foot

This 20.53-ton-per-foot measurement is the estimated forming load over the same number of square inches in our calculated land area described previously, with the punch radius as the width and 12 in. (1 foot) as the length.

Consider the 0.157-in. punch radius (63 percent of the material thickness), which gave us a land area of 1.884 sq. in. If we divide 20.53 by 1.884, we get 10.90 tons per square inch. As shown earlier, it takes 11.775 tons of force (the punching tonnage) for that 0.157-in. punch radius to penetrate and crease the material in the land area. The verdict: Bending with 20.53 tons per foot isn’t enough to exceed the material’s ability to resist tonnage on a land-area basis. In other words, it’s not enough to crease the material, so the bend will not be sharp.

We could do similar calculations for other materials by using multipliers, or material factors (using the formula in the "Sharp Bends in Various Materials" section). The forming tonnage formula described previously uses 60,000-PSI cold-rolled steel as a baseline. To calculate the material factor you need, simply divide its tensile (in PSI) by 60,000. So stainless steel with a tensile of 120,000 PSI would have a material factor of 2.

Tonnage per foot for air bending =

{[575 × (Material thickness2)] / Die opening}

× Material factor

To calculate punching tonnages, we incorporate a material factor in the formula described previously, using the multipliers (material factors) shown in Figure 2.

Punching tonnage = Land area × Material thickness

× 25 × Material factor

The Practical Effects

We now know why the bend turns sharp. That’s fine, but besides applying it to your bend deduction calculations when necessary, what is the practical value of this knowledge?

In fact, there are two values to this knowledge. First, if the punch radius is less than sharp (less than 63 percent of the material thickness) in an air form, the radius value used in the bend deduction calculations must equal that of a sharp bend, nothing less, or the final bend deduction calculation will be incorrect.

Second, once you enter the sharp realm and begin creasing the material surface, the stability of your bend comes into question—that is, your ability to stabilize the bend angle from part to part. By default, if you fail to accomplish angle stability, you won’t have dimensional stability either. This will dramatically affect the final part and its quality. This is why I recommend that, for typical sheet metal applications, you keep your punch nose radius as close as you can get to a 1-to-1 relationship to the material thickness.

When forming plate and high-strength material, it’s common practice to use a punch nose that’s at least three times the material thickness. Avoiding a sharp punch nose when forming these materials prevents errors created by forcing a ditch in the center of the bend and alleviates many cracking problems.

The sharp bend percentage is just a rule-ofthumb value that changes with material. But it does describe in general terms where you will exceed the material’s ability to resist the force on the surface of the part and allow the punch nose to penetrate. Following this rule of thumb, you can calculate bend deductions accurately, stabilize your work from part to part, and in the end build better parts.

Key Terms

Land area:

In this article’s context, this is the area of contact between the punch and material surface. The length is 12 in., while the width is the punch radius.

Material yield by land area:

The material’s yield strength in the specified land area. For bending to occur, the force the press brake exerts must exceed the material’s yield strength.

Forming tonnage:

The tonnage exerted to bend a given material type and thickness over a given die opening in an air form.

Punching tonnage:

The amount of force required for the punch tip to start penetrating and creasing the material surface.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC, 2952 Doaks Ferry Road NW, Salem, OR 97301,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. For more information on bending, check out Benson’s new book,

The Art of Press Brake: the Digital Handbook for Precision Sheet Metal Fabrication

, © 2014, available at

www.theartofpressbrake.com

.
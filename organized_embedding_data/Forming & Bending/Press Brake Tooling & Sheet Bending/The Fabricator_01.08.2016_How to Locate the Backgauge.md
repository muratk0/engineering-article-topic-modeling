# How to Locate the Backgauge

[TARİH: 01.08.2016 The Fabricator]

Bending Basics

The flange dimension, tooling, and bend deduction all play a role

By Steve Benson

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Question:

I’m the drafting manager at a growing fabricator in Kansas. We started up about a year and a half ago, and although we are rapidly growing, there has been limited funding allocated to press brake tooling, so we are stuck with punch radii of 0.031 inch

.

Recently we dialed in our K factors, which on 7-gauge and thicker materials has been lower than I had ever seen (K ≈ 0.22 in.), which I’m attributing to the aforementioned punch radius. I’ve been trying to come up with a way to tell our brake operators where to set the backstops when they need to place a previous bend against them

.

I figured that if I place the stop at the material thickness plus the actual achieved radius to the new bend, it would give them the information needed. So I multiplied the material thickness by 63 percent

.

The problem is, that didn’t give us the desired results. Now, when I’m checking the actual achieved radius on this 0.25-in.-thick carbon steel, I’m measuring the radius to be closer to 0.234375 in., or about 94 percent the material thickness. Are there any other variables I haven’t taken into account besides the material thickness and material type?

Answer:

Let me begin by reviewing the terminology required for this discussion, beginning with the K factor. The

K factor

is defined as a multiplier that determines the location of the neutral axis after the forming has been completed. The neutral axis is a theoretical area within the bend where the material does not change during forming—no expansion of the material as occurs on the outside of the bend, no compression as occurs on the inside of the bend.

For example, the neutral axis in 0.250-in. material is halfway through its thickness, at 0.125 in. If you multiply the average K factor of 0.446 by the 0.250-in. material thickness, you get 0.1115 in. That’s the amount the neutral axis shifts during forming, from 0.125 to 0.0135 in. That may not seem like much, but because the neutral axis does not change in length, and simply moves toward the inside surface of the bend, that movement causes the material at the bend to elongate. It is the reason that your flat part is always smaller than the sum total of the formed part’s outside dimensions. (For more on this, you can review the July 2016 column, archived at

www.thefabricator.com

.)

Depending on the method of forming and the material to be formed, the K factor value can range from 0.33 to 0.5; 0.446 is the average value and the most commonly used for this calculation.

We use the K factor to develop the bend allowance (BA). Specifically, we multiply the K factor by π/180. When we use 0.446 for the K factor, we get 0.0078, and then multiply this by the material thickness. We then calculate π/180 to get 0.017435 and then multiply this by the inside radius. This gives us the following:

(π/180 × Inside radius) [K factor × (π/180)] × Material thickness

This gives you the BA for 1 degree of bend. To calculate the complete allowance, you simply multiply the result by the number of degrees complementary on the outside of the bend. (Note: The bend angle in the BA calculation is always complementary, never the included angle.) Here’s the formula using the average K factor of 0.446:

BA = (0.017453 × Inside radius) (0.0078 × Material thickness) × Degrees of bend complementary

While the BA alone can be used to develop the flat blank, we are going to take it a step further and develop the bend deduction, or the total amount of elongation that is going to occur in a given bend. To do this, we calculate the outside setback (OSSB) and, ultimately, the bend deduction (BD). (For more on this, including the detailed formulas, see "The basics of applying bend functions," archived at the

fabricator.com

.)

Calculating the Actual Inside Radius

Considering the thickness of your material, I assume that you are air forming. That being true, the inside radius you achieve in your part is a function of die width or die opening.

Based on the radius you achieve in the part, my guess is you are forming in a 1.500-in. V die. This produces the inside radius based on the 20 percent rule. Remember that "20 percent" is a title only; the actual percentage values vary by material type. (See "Dissecting bend deductions and die openings" from September 2012, archived at

www.thefabricator.com

.) For carbon steel, we use a median value of 16 percent and adjust over time as needed—and 16 percent of 1.5 is 0.24, very close to the radius you measured.

Finding the Backgauge Location

Because you are bending on a press brake and into a V or channel die, the center of the bend is established by the nose of the punch, with one-half of the material elongation (the BD) going to either side of the center. Once these three calculations have been made, you can determine your backgauge location.

Calculate the total amount of elongation for the bend—that is, the BD—based on that floated inside radius of the bend. Divide that value by 2 and subtract that value from the outside dimension of the flange. That resulting value is the backgauge location from the center of the bend (bend line) to the backgauge itself. For example, if you have a 2-in. flange with a 0.100-in. BD, you would place the backgauge at 1.950 in.: 2.000 – (0.1000/2) = 1.950

If you are setting your backgauges by measuring from the front of the die, you will need to add onehalf of the die body’s width (not just the opening, but the width of the entire die body) to the calculated centerline value.

Gauging subsequent bends (bends gauging off a previous bend) is a little different. For 90-degree bends, you take the outside dimension of the flange, place that value into the controller at that appropriate step in the program, and put in an adjustment value of one-half the BD into the appropriate "bending adjustment" input. If you are using a manual backgauge, the process is the same, except that here again you will add one-half of the die body width to your calculation: the flange dimension plus half of the die body width minus half of the BD.

Some controllers do work from the bend line rather than the outside flange dimension. In this case, the process is the same except that you would need to remove half the BD for the bend that is being gauged from. This will set the backgauge in the correct position.

One other consideration for gauging a second bend is the angle of the bend being gauged from. If it’s 90 degrees, you proceed as described previously. If it’s greater than 90 degrees complementary, gauging shouldn’t be a problem, though some adjustment to the backgauge may be necessary, depending on where the dimension is called on the print. The dimension could be called to the surface of the part or to the apex of the bend.

Even under the best of conditions you will have minor variations in bend angle due to springback, which makes gauging from open angle bends (less than 90 degrees complementary) almost impossible. No doubt, you will have to find another location to gauge from, such as an edge, feature, or a different bend.

Using a Small Punch Radius

It is also fair to say that by using a 0.031-in. radius on the punch nose with 0.250-in. material, you are bending sharp. That relationship alone will cause an increase in variation from part to part.

To achieve the most stable and predictable parts, try using a nose radius that’s as close as possible to the natural floated radius of the material, without exceeding that value. If you use a punch nose radius larger than the natural floated radius, the material may take on the punch radius rather than what was expected. In your case, the resulting radius was 0.234, so a 0.218-in. punch nose radius would be optimal.

The effects of the small radius on the punch nose could be rather dramatic, depending on the circumstances and the material being formed. I would refer you to "Predicting the inside radius when bending with the press brake," archived at

thefabricator.com

.

Briefly, here’s what happens: When the force required to make the bend exceeds the material’s ability to resist that force, the nose of the tool will embed itself into the material and create a crease in the center of the bend. This is similar to calculating punching tonnage. In fact, it uses the same formula.

Creasing the bend amplifies the effects of grain direction, hardness, tensile strength, and other factors from part to part. This increases the angular variation from part to part as well, and if the angles vary, so will the linear dimensions.

A sharp punch nose radii—that is, one that’s less than the minimum radius—creates a parabola, more of a "U" than a true radius; this will affect the actual radius you achieve.

A

minimum radius

is the point where the bend turns sharp and the punch nose begins to pierce the material. In 60-KSI mild cold-rolled steel, that value is 63 percent of the material thickness. Remember that 63 percent is not the only value used here; that percentage changes by material type, yield, and tensile strength.

For more on this, including the punching tonnage formula and the different percentages used for the minimum radius, see "How an air bend turns sharp," archived at

thefabricator.com

.

Summary

To recap, first determine the radius that is actually going to appear in the finished part. Calculate the BD for that radius. Divide that value by 2 and subtract it from the outside dimension of the flange. If you’re measuring from the front of the die, you’ll need to add one-half of the width of the entire die body (again, not just the die opening). This gives you your bend line-to-backgauge dimension.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. For more information on bending, check out Benson’s book,

The Art of Press Brake: the Digital Handbook for Precision Sheet Metal Fabrication

, © 2014, available at

www.theartofpressbrake.com

.
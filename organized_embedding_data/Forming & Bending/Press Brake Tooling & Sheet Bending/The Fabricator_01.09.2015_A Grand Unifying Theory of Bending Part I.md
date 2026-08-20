# A Grand Unifying Theory of Bending: Part I

[TARİH: 01.09.2015 The Fabricator]

Bending Basics

Meeting the challenges of the sharp bend

By Steve Benson, Contributing Writer

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

T

he press brake profession has some long-held labels and definitions. We achieve a

sharp bend

when the inside bend radius reaches about 63 percent of the material thickness in 60-KSI cold-rolled steel. We define a

radius bend

as any radius between a sharp bend and an inside bend radius that’s eight to 10 times the material thickness. We call a bend with an inside radius larger than eight to 10 times the material thickness a

profound-radius bend

. We’ve also used a formula to calculate the perfect die opening: Outside radius × 0.7071 × 4.85, 0.7071 being the sine of 45 degrees complementary.

These definitions and formulas, combined with other rules of thumb, allow us to get our calculations close to what really happens at the press brake—but as we’ve discussed over the past few columns, we can get even closer. I’m calling this the "Grand Unifying Theory" of radius, bend deduction, and die selection, and I’ll describe this theory in detail over the next several months.

New Definitions

To begin, we need to change a few fundamental definitions. There are some very good reasons to redefine these, and I’ll make the case for these changes in this column.

First, we will keep our definition of sharp bends, but we’ll now insert new terms. A perfect bend starts at an inside bend radius larger than 63 percent material thickness, extends beyond the point where we have a 1-to-1 inside bend radius-to-material-thickness ratio, and goes up until we reach 125 percent of that 1-to-1 ratio value. Finally, we will now define a

radius bend

as one with an inside radius at or beyond 125 percent of that 1-to-1 value.

We’ll also use new formulas to calculate the optimum die width. For these, we’ll need the outside bend radius, which you can find by adding the inside bend radius to the material thickness. Note that you should not base this die-width calculation on an inside radius-to-material-thickness ratio of less than 1-to-1.

Outside bend radius = Material thickness Inside bend radius

Optimum die width for sharp and perfect bends (in.) = Outside bend radius × 3.29435

Optimum die width for radius bends (in.) = Outside radius × 5

Although sharp and perfect bends share the same die-width formula, sharp bends do require a little extra calculation. That’s due to the nature of bending sharp. Traditionally, once you determine the minimum sharp-bend radius (see "How an air bend turns sharp" at

www.thefabricator.com

), you use that radius in your bend deduction calculation. This works well enough, but here I’m introducing a calculation method that can help you get your inside radius predictions even closer.

For this installment of the Grand Unifying Theory, we will discuss sharp bends and the reasons for these extra calculations—thanks to the parabola effect.

A Review of Sharp Bends

In an air bend, the radius forms as a percentage of the die width. The narrower the die width, the smaller the radius. If the die width is narrower than necessary, the part follows the radius profile of the punch nose. This in turn increases the tonnage, or pressure, placed on the workpiece. Once the pressure builds up enough, the punch nose starts penetrating the workpiece and forms a crease along the bend line. Bends generally turn sharp when the inside bend radius is about 63 percent of the material thickness in 60-KSI-tensile cold-rolled steel; any narrower than this and the punch tip starts to crease the material. Of course, this minimum sharp-bend radius varies depending on the material type and tooling.

It’s best practice to choose a punch nose radius that’s close to the material thickness, if possible. A punch nose radius that’s too narrow concentrates the forming energy onto a small area, making it easy for the punch to penetrate and crease the material. (For more on this, including how to determine the minimum sharp-bend radius, see "Bending soft, not sharp," available at

www.thefabricator.com

.)

A Review of the Bend Functions

These days software handles most bend function calculations. Still, it’s always good to know the math behind it all. Below are bend function formulas long used and well-proven in industry.

Formulas

BA = [(0.017453 × Rp) (0.0078 × Mt)] × Degrees of bend complementary

OSSB = [Tangent (degree of bend angle/2)] × (Mt Rp)

BD = (OSSB × 2) – BA

Key

Rp = Radius of the punch nose (bottoming) or the floated inside radius (air forming)

Mt = Material thickness

BA = Bend allowance

BD = Bend deduction

OSSB = Outside setback

0.017453 = π/180

0.0078 = K factor × π/180

K factor = 0.446

Note: The OSSB formula can have the included or complementary bend angle, depending on how you run your flat-blank calculations. For more on this, see "The basics of applying bend functions," available at

www.thefabricator.com

.

Calculating the Radius for Sharp Bends

We start by calculating the die width as if the relationship between the inside bend radius and material thickness has a 1-to-1 relationship—never smaller than that. Let’s assume we need to achieve a 90-degree bend angle, and we’ll start by using a "perfect" inside bend radius that matches the material thickness of 0.125 in. Knowing this, here’s how to determine the optimum die width:

Outside bend radius = Material thickness (in.) Inside Bend Radius (in.)

Outside bend radius = 0.125 0.125 = 0.250

Optimum die width = Outside bend radius × 3.29435

Optimum die width = 0.250 × 3.29435 = 0.823 in.

Knowing that 0.823 in. is the optimum die width, we choose the closest die width available: 0.866 in.

Punch Nose and the Outside Radius

When using a punch nose that’s less than perfect (that is, less than the desired inside bend radius), you need to take that difference into account. A punch nose with a small radius effectively makes the punch "taller," allowing it to penetrate farther into the die and creating a smaller inside radius when the material is released from the pressure.

Outside radius with sharp punch nose = Material thickness Inside bend radius (Inside radius – Sharp punch nose)

In our current example, if we’re using a 0.062-in.-radius punch tip, the outside radius for our calculations would be the following:

Outside radius with sharp punch nose = 0.125 0.125 (0.125 – 0.062)

Outside radius = 0.250 0.063

Outside radius = 0.313 in.

Calculating the Parabola

When bending sharp, you don’t form a true radius but instead a parabola. Because of the parabola’s conical shape, the distance from one end of the bend to the other changes. In geometric terms, this is called the

arc length

.

Calculating the parabola arc length by hand can get complicated, so instead we can use a few online calculators. Here we’ll use the "Parabolic Segment Calculator" available at

www.had2know.com/academics/parabola-segment-arc-length-area.html

. For the purposes of these calculations, we consider the "Height" variable as the same as the outside bend radius, and the "Width" variable as the same as the die width.

Entered Values

Height (outside radius): 0.313 in.

Width (die width): 0.866 in.

Calculated value

Arc Length: 1.1099 in.

Now that we know the parabola’s arc length, we can uncover what the inside bend radius will be. To keep things simple, we’ll assume there will be 1 degree of springback, our baseline value, so we’ll use a bending angle of 89 degrees included. We first need to convert 89 degrees to radians and then multiply this value by the parabolic arc length. (As you may remember from high school geometry, a radian is a unit of angle in which the arc length equals the radius.)

Converting to Radians

89 degrees × (π/180) = 1.55334303 radians

Next, we multiply this value by the arc length of the parabola, as follows:

Bend angle in radians × Arc length of parabola = Length of arc value

1.55334303 × 1.1099 = 1.724 in. length of arc value

We next take this length of arc measurement and input it, along with our 0.866-in. die width, into the "Complete Circular Arc Calculator" at

www.handymath.com

. After inputting these values, we want to look at the height of arc result.

Entered Values

Length of arc: 1.724 in.

Width of arc (die width): 0.866 in.

Calculated Value

Height of arc: 0.5992 in.

This is pure geometry. To convert this to the "real world," we need to run a few more calculations. The height of arc from the calculator will serve as our initial value for the outside radius.

[Outside radius – (Outside radius)

2

] – Material thickness = Inside radius

[0.5992 – 0.3590] – 0.125 = 0.115-in. inside bend radius

This shows how the sharp bend and parabola effect reduced the inside radius from our "perfect bend" of 0.125 in. to 0.115 in.—a difference of 0.010 in. From here you can use the 0.115 inside bend radius to calculate your bend allowance and bend deductions (see

sidebar

).

Estimating Springback

Just to keep things simple, the previous example assumed 1 degree of springback, following the old rules of thumb. But we can calculate our springback estimate a little more accurately. To calculate the bend angle after springback, convert inches to millimeters (multiply by 25.4) and then use the following formulas.

Springback for perfect and radius bends =

[Punch radius in mm / (Material thickness in mm × 0.9)] /2

Springback for sharp bends =

{{[Punch radius in mm (Material thickness in mm Desired inside radius)] (Material thickness in mm × 2)} / (Punch radius in mm × 0.9)} / 2

These formulas are for 60-KSI cold-rolled steel, our baseline material. For other materials, you multiply the result you get by a material factor. To calculate this factor, divide your material’s tensile strength in PSI by 60,000. For instance, for 120,000-PSI-tensile stainless steel, the material factor would be: 120,000/60,000 = 2. So you’d multiply the springback result by 2. Note also that sharp bends have a different springback formula. That’s because when you’re working with a less than perfect bend, springback increases.

Bend Sharp the Best You Can

Performing sharp bends is never ideal, but if it’s the only choice available, you have to do what you have to do. But for the best results, try following these guidelines:

Never use punch nose radii less than the material’s sharp value; this value may be large if the material is soft.

When possible, use a "perfect radius" relationship by getting the punch radius as close as possible to the 1-to-1 inside bend radius-to-material-thickness ratio.

If you must use a punch radius less than this 1-to-1 ratio, calculate the radius using the parabola radius calculation method, and use the result to calculate the bend deduction.

Know that the bend radius in the part will never be smaller than the radius of the punch nose.

Whenever possible, use the actual material thickness in all of your equations.

Always use the tool sets the bend was calculated for.

The first piece of the Grand Unifying Theory is in place. In future months we’ll tackle tooling selection for radius bends—that is, bends that begin at 125 percent of the 1-to-1 inside radius-to-material-thickness value—as well as aircraft tooling. We’ll end with a step-by-step process that ties the Grand Unifying Theory together.

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
# How to Calculate the Air-Formed Radius of Different Bend Angles

[TARİH: 01.07.2015 The Fabricator]

Bending Basics

Geometry gives you a start, but you’ll need to incorporate real-world bending variables

By Steve Benson, Contributing Writer

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Q:

I have really taken the theory behind your articles to heart, and I have done my best to apply it to the greatest extent I can. I’m always looking for ways to improve my ability to calculate bends more accurately, and I’ve used various rules of thumb that you have provided. Of course, many of these have ranges of values to use. Are there ways to calculate bends more precisely for various angles and radii?

A:

On the shop floor, it’s common to use rules of thumb to get our calculations close, though it’s possible to get your calculations even closer. First, be sure the desired radius isn’t close to the sharp-bend radius. This is the smallest radius you can bend in a part before the punch nose starts creasing the material. For 60,000-PSI cold-rolled steel, this occurs when the radius is about 63 percent of the material thickness. However, various factors come into play for different materials, thicknesses, and punch nose radii. For more on this, see "Bending soft, but not sharp," and "How an air bend turns sharp," available at

www.thefabricator.com

.

A Review of the 20 Percent Rule

During air forming the inside radius forms in proportion to the die width. This is true of all air forms, regardless of the style of tooling you are using. This is the essence of the 20 percent rule. Note that the 20 percent rule really isn’t designed to be used for die selection, but instead is used when calculating your bend deductions. Then again, a good technician can work the information either way. For more on this, see "6 steps to successful die selection for press brakes," available on

thefabricator.com

.

The percentages in the 20 percent rule are based on material tensile strength. The "20 percent" actually comes from the percentage range used for stainless steel. For our baseline material, 60,000-PSI cold-rolled steel, the radius forms as 16 percent of the die width. So, to apply the rule to other materials, we calculate the following:

Material tensile in PSI/60,000 = Tensile difference factor

Tensile difference factor × 0.16 = Die width percentage Die width percentage × Die width = Inside bend radius of an air form

This simple calculation works well in the shop environment, but of course there are plenty of other variables that affect the radius, including the bend angle.

Figure 1

If you know the included bend angle and the die width, you can calculate the inside radius and length of the arc at a specific depth of penetration (Dp), using your graphic calculator or online calculators like

www.handymath.com

. The results give you a starting point for incorporating real-world bending variables such as material type, thickness, springback, and the parabola effect.

Figure 2

When bending sheet metal in a press brake, you actually form a parabola, a conical shape, not a single radius. This affects the bend functions, and for profound-radius bends, the parabola effect can be dramatic.

More Angles

To calculate the radius produced at different bend angles, first find the radius and length of the arc of the bend, and then manipulate these results to factor in tensile and yield strength. This month we’ll cover the geometry behind finding the radius and arc length. In future months we’ll use these measurements and factor in real-world bending conditions.

When calculating the radius and arc length, a graphic calculator or websites like

www.handymath.com

can be extremely helpful. On

handymath.com

, click on "Calculators" and then "The complete circular arc calculator." This calculator uses generic mathematical terms, but they apply to the press brake arena. The "height of arc" on the website’s calculator is the same as the punch’s depth of penetration from the pinch point to the bottom of the stroke (Dp). The "width of arc" is the die width (Dw). If you know the die width and the included bend angle, this online tool will calculate the length of the arc, the depth of penetration, and the inside radius (see

Figure 1

).

Consider an application involving 0.125-in.-thick material being bent over a 0.984-in. die width. Using the online calculator, we get the length of the arc; to find the inside radius, we multiply the length of the arc by the material thickness. (For more about the math behind these calculations, see

Math Behind the Arc Radius and Length

sidebar.)

135 degrees: 1.25476-in. arc length × 0.125 in. = 0.156-in. inside radius

120 degrees: 1.18985-in. arc length × 0.125 in. = 0.148-in. inside radius

90 degrees: 1.09295-in. arc length × 0.125 in. = 0.136-in. inside radius

60 degrees: 1.03044-in. arc length × 0.125 in. = 0.128-in. inside radius

45 degrees: 1.0097-in. arc length × 0.125 in. = 0.126-in. inside radius

Note that all given angles are included

.

Springback and the Parabola Effect

Of course, this doesn’t account for another piece of the puzzle—springback—or, more specifically, the bent/bend multiplier. The angle you bend the part to is the "bent angle," while the "bend angle" is the one measured after pressure is released and the workpiece springs back. If the angle relaxes, so does the radius. For a review on this, see "The hows and whys of springback and springforward," available at

thefabricator.com

. I’ll also be covering the bent/bend multiplier in more detail in a future column.

To really be precise, we need to consider what’s actually happening during an air form. As you begin to push the material into the die, break the material yield, and enter the plastic zone, you actually aren’t forming just one radius.

To explain this, let’s go back to the very basics. A radius is half of a circle’s diameter. Imagine a circle drawn so its curved surface conforms to the bend to get larger to conform to the bend shape; a larger circle, of course, has a larger radius. This is how we measure the inside bend radius in precision sheet metal fabrication. The smaller the radius, the sharper the bend’s curve; the larger the radius, the wider the curve.

On the shop floor, it’s common to use rules of thumb to get our calculations close, though it’s possible to get your calculations even closer.

But this isn’t what exactly happens during an air form. Overlay the circle and the shape of the bend, and you’ll find that, in some cases, they don’t quite match. That’s because the shape of the bend isn’t just one radius, but several.

It goes back to the nature of bending sheet metal. As the punch pushes the material into the die space, it does not always form a simple radius. It in fact creates a parabola, a conical shape (see

Figure 2

). Because you actually form a parabola, the radius does not remain consistent through the bend angle. This parabola affects various bend functions, and the effect on profound-radius bends is great. I’ll have more on this in the coming months.

Math Behind the Radius and Arc Length

Bending at its core is about geometry. To calculate the length of the arc in a bend, you probably will rely on a website such as

www.handymath.com

or a graphic calculator. But if you want to know the math behind it all, refer to the boxed equation in the figure. A is the depth of penetration (Dp), B is half the die width (Dw), and R is the radius. The curved red line represents the bend. Once you calculate the radius, you can find the length of the arc, though you’ll need to convert the degrees of the included bend angle to radians.

Note that this is pure geometry, and the resulting radius does not incorporate the conditions of real-world bending. But it does give you a figure you can work with to factor in variables like material thickness, material type, and springback.

Consider the following application using a die width of 0.984 in., bending to an included angle of 135 degrees. Penetration from the pinch point to the bottom of the stroke (Dp) is 0.328 in.

Radius Calculation

Inside radius = [(Dw/2)

2

Dp

2

] / Dp × 2 Inside radius = (0.492

2

0.3282) / 0.328 × 2 = 0.532 in.

Arc Length Calculation

Degrees to radian conversion: Included angle in degrees × (3.1415/180)

Arc length = Inside radius × Included angle in radians

Radians conversion: 135 × (3.1415 / 180) = 2.35619449

Arc length = 0.532 × 2.35619449

Arc length = 1.253495469

You’re now realizing why we use general rules rather than try to calculate until we’re blue in the face. We have so many variables to deal with. Nonetheless, we can get extremely close if we try. Next month—even closer!

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
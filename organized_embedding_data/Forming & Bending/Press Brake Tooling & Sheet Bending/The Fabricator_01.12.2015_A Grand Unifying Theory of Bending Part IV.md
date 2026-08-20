# A Grand Unifying Theory of Bending: Part IV

[TARİH: 01.12.2015 The Fabricator]

Bending Basics

Tying it all together

By Steve Benson, Contributing Writer

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

F

or the past few months I’ve detailed a new way of predicting the inside bend radius. Instead of the traditional terms such as

radius

and

profound-radius

bends, we’re using some new terminology. I’m calling this the "Grand Unifying Theory" of radius, bend deduction, and die selection, and ultimately it may help you make your bend calculations more accurate than ever.

For this final installment, I’ll review the definitions and bring you through the entire process, from calculating springback to incorporating the bend function calculations. Note that all measurement values—including material thickness, radius, punch nose diameter, and die width—are in inches unless otherwise specified.

The Terms

Types of Bends

Sharp bend: Specified inside bend radius that is generally 63 percent or less of the material thickness of 60-KSI cold-rolled steel. (For more on this, see "How an air bend turns sharp" on

www.thefabricator.com

.)

Perfect bend:

Specified inside bend radius that’s between 63 percent and 125 percent of the material thickness.

Radius bend:

Specified inside bend radius that’s greater than 125 percent of the material thickness.

Bending Methods

Air forming:

Three-point bending in which the material contacts the punch nose and the radius of the die shoulders during the forming cycle. The floated inside radius forms as a percentage of the die width.

Bottoming:

Forced bends, usually at 90 degrees, with angular clearance between the punch and die; the punch descends until the material wraps around the punch nose, after which the ram continues to apply pressure, forcing material against the die face to the desired bend angle. This produces a radius that’s slightly larger than the punch nose, which is why a springback factor still needs to be taken into account. Bottoming occurs at about 20 percent of the material thickness, as measured from the bottom of the V die.

Coining:

Occurs when the tool geometry is stamped into the material at less than the material thickness. It is rarely performed.

Wiping:

Occurs in aircraft tooling during the forming of complementary angles greater than 90 degrees.

Angles

Bend angle:

Angle after springback.

This chart —

Deductio de Diabolus

, or Deductions of the Devil—summarizes the concepts discussed in this series. A perfect bend (in gold) is a bend where the inside bend radius and material thickness are the same. As long as you use the tooling in the manner described in the calculations, a perfect bend will be the result. To the left of the gold spot, the radius-to-material-thickness ratio is less than 1-to-1; to the right, the ratio is greater than 1-to-1.

Bent-to angle:

Angle the press brake overbends to overcome springback.

Included bend angle:

Angle of bend as measured between the two legs.

Complementary bend angle:

180 degrees minus the included bend angle.

Sf:

Springback factor.

Tooling

Punch:

Usually the upper tool, the punch pushes the workpiece into lower die space.

V die:

Angles from 85 to 90 degrees included.

Acute V die:

30 to 85 degrees included.

Relieved V die:

Section of the die faces removed, which allows the punch to overbend for springback without crashing into the die.

Aircraft die:

Channel dies in which the depth is 120 percent of the width

Channel die:

180-degree dies that do not maintain the width-to-depth relationships of aircraft dies.

Forming Variables

Mt:

Material thickness

Dp:

Depth of penetration, the distance the punch tip enters the die space

Ir:

Inside bend radius

Rp:

Radius of punch tip (Note: Ir and Rp sometimes can be interchangeable)

BA:

Bend allowance

BD:

Bend deduction

OSSB:

Outside setback

The Steps

1. Calculate the springback and estimate the bent-to angle.

This is for air forming.

Note that Rp and Mt values are in millimeters

. Also note that the results are approximations at best. There are far too many variables to predict springback with total accuracy.

Springback for perfect and radius bends =

[Rp / (Mt × 0.9]/2

Springback for sharp bends = {{[Rp (Mt Desired Ir)] (Mt × 2)}/(Rp × 0.9)}/2

Springback for 180-degree U bends = {[Rp /(Mt × 0.9)]/2} × 2

2. Select method: Air forming, air forming with backup, bottoming, wiping (aircraft).

3. Select tooling style and calculate optimal die width.

Outside radius for most bends = Desired Ir Mt

Air forming with V die and acute V die

Die width for sharp and perfect bends = Outside radius × 6.85887

Die width for radius bends with standard V tooling = Outside radius × 3.429435

Channel die (not aircraft tooling)

Die width for perfect bends = Outside radius × 6.85887

Die width for radius bends = Outside radius × 5

Aircraft die

For bend angles less than 90 degrees complementary:

Die width for radius bends with standard V tooling = Outside radius × 3.429435

Optimal die width for perfect bends = Outside radius × 6.85887

Optimal die width for radius bends = Outside radius × 5

For bend angles greater than 90 degrees complementary:

Optimal die width = Punch nose diameter (Mt × 2.5)

Note: Aircraft tooling does not allow for sharp or "creased" inside bend radii; therefore, it would be highly uncommon to find tooling used in a sharp bend relationship.

Air forming with relieved V die

Corner offset = [Face length before relieved section ×

Cosine (Die angle/2)] × 2

Relieved die width (dimension A in figure) = Die width – Corner offset

Optimal relieved die width for radius bends = Outside radius × 5

For accurate bend calculations, relieved die widths must be measured by the A dimension.

Bottoming

Outside radius = Mt Rp

Optimal die width = Outside radius × 3.429435

The formulas here give you the perfect die width, but that value rarely will match available standard die widths, so you need to choose the closest die width available.

4. Determine the tonnage requirements.

Forming tonnage per foot = [(575 × Mt

2

) / Die width] ×

Material factor × Method factor

Material factor = New material KSI/60

Method factor = 1.0 for air forming; 5.0 for bottoming, urethane

5. Determine where the bend turns sharp.

Minimum force per foot necessary to pierce the material surface, based on 1-to-1 material-thickness-to-inside-bend relationship.

Land area = Rp × 12

Material factor = New material KSI / 60

Piercing tonnage = Land area × Mt × 25 × Material factor

Piercing tonnage should be greater than forming tonnage. The radius on the nose of the tool should be no less than the calculated "sharp" value of the bend.

6. Determine the springback factor.

Sf = Complementary bent-to angle/

Complementary bend angle

7. Determine the actual radius

Bottoming

Ir = Rp × Sf

Air forming a sharp bend calculated as a parabola

In the online calculator at

http://www.had2know.com/academics/parabola-segment-arc-lengtharea.html

, "Height" equals outside bend radius and "Width" equals the die width. Or, you can perform the following equation:

h = Outside radius

w = Die width

Ln = Natural logarithm

(button available on most scientific calculators)

Arc length of parabola = 0.5√16h

2

w

2

[w

2

/ (8h)]

[Ln(4h √16h

2

w

2

) - Ln(w)]

Included bent-to angle in radians =Included bent-to angle × (π/180)

Length of arc = Included bent-to angle in radians ×

Arc length of parabola

Use this "Length of Arc" value, along with the die width ("Width of Arc"), at

www.handymath.com

’s "Complete Circular Arc Calculator." The result needed is the "Height of Arc" value. The height of arc from the calculator will serve as our initial value for the outside radius. To obtain our final inside radius:

Ir before springback =[Outside radius – (Outside radius)

2

] – Mt

Final Ir after springback = Ir before springback × Sf

Air forming a perfect bend, with the radius calculated as a percentage of the die opening

The inside radius is calculated using the 20 percent rule, a label only. The 20 percent rule refers to the floated radius achieved when bending 304 stainless steel, about 20 percent of the die width. Our baseline percentage, for 60-KSI cold-rolled steel, is 16 percent. This is a median value. Over time you may raise or lower the percentage slightly based on how a certain material forms.

Ir = Chosen die width × Material’s percentage for baseline 60-KSI tensile strength mild cold-rolled steel

Performing a radius bend

If bend angle does not exceed 90 degrees complementary:

Ir = Rp × Sf

If the angle exceeds 90 degrees complementary, you need to account for multibreakage. The larger the radius-to-material thickness, the worse the effect.

Note that this is only an estimate. You may not see this effect in high-tensile-strength material until the bend angle is well past 90 degrees. Nonetheless, the inside radius will get smaller as the included angle gets smaller.

Note that the depth of penetration (Dp) formula below uses the bent-to angle (angle achieved before the bend springs back), not the final bend angle.

b = (Die width/2)

Dp = b / Tan (Bent-to angle/2)

Outside radius = (Dp

2

b

2

) / (2 × Dp)

Ir = Outside radius - Mt

Bending in a die backed up with urethane

Ir = Rp × Sf

8. Calculate the bend functions.

In these formulas, Rp (for bottoming) can be replaced with Ir (for air forming).

BA = [(0.017453 × Rp) (0.0078 × Mt)] × Degrees of bend complementary

OSSB = [Tan (degree of bend angle/2)] × (Mt Rp)

BD = (OSSB × 2) – BA

Note: The OSSB formula can use the included or complementary bend angle, depending on how you run your flat-blank calculations. For more on this, see "The basics of applying bend functions," available at

www.thefabricator.com

.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC, 2952 Doaks Ferry Road NW, Salem, OR 97301,

steve@theartofpressbrake.com

.
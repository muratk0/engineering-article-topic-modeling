# Forming with urethane pads?

[TARİH: 01.07.2025 The Fabricator]

Bending Basics

Be sure to size them correctly

STEVE BENSON

O

ver the last couple of months we have been reviewing urethane press brake tooling, including low-durometer (soft pads) and high-durometer (hard-tool profiles) varieties. If you use a pad, its volume needs to be at least 10 times that of the penetrating punch and material.

Roughly calculating the volume of the penetrating punch and material is straightforward; precisely calculating it is another matter. I’ll cover the rough method here. Practically speaking, most shops don’t run into problems, especially for short production runs, provided they use reasonable pad sizing and avoid excessive compression. In certain circumstances, you might need a more precise approach. Regardless, used correctly, the rough method gives you a workable estimate—as long as you’re not pushing the limits of your urethane pads.

How Urethane Degrades

You might be able to use pads smaller than 10 times the volume of the penetrating punch and material. Doing so, however, is not the best option and may not produce the highest-quality parts. You will overwork the pad, causing hysteresis.

Pronounced "his-tuh-ree-sis,"

hysteresis

is the internal resistance of the urethane to repeated deformation, which causes heat buildup during heavy or continuous forming cycles. The phenomenon refers to the lag between the applied force and the urethane’s elastic recovery after the pad has been released from pressure. Urethane exhibits both elastic (spring-like) and viscous (fluid-like) characteristics.

When urethane is compressed during forming, not all the energy used to deform it is immediately recovered, and some of it is lost as internal friction. That internal friction is what generates heat. Repeated or excessive use without adequate cooling time leads to cumulative heat buildup inside the pad. Over time, this can soften the urethane, degrade its mechanical properties, and shorten its life.

The Rough Approach

Imagine we’re working with a 12-in. bend length in 0.125-in.-thick material. You have a punch with an angle of 90 degrees and a nose radius of 0.125 in. You need to know the

penetrating volume

, or the amount of urethane displaced by the punch tip during forming.

To calculate this, you can use a geometric approximation based on the shape of the punch tip and its depth of penetration into the urethane. The following formula gives you the total penetrating volume in cubic inches. A1 is the nose radius while A2 is the bend length, both measured in inches:

Penetration Volume = 0.25 × π × A1

2

× A2

Penetration Volume = 0.25 × π × (0.125)2 × 12 = 0.1472 cu. in.

So, a 12-in. bend with a 0.125-in. punch nose radius equals 0.1472 cu. in. The minimum pad volume needs to be 10 times that value—or 1.47 cu. in. Notice something missing? Yes, this calculation does not include the material thickness. You would think that all you need to do is add the 0.125-in. punch radius to the 0.125-in.-thick material, right? (In this case, A1 in the formula would be 0.250 in.—punch nose radius plus the material thickness).

This works fine if you’re only roughly estimating displaced volume. So, if you’re performing quick tooling clearance checks or want to check safety margins, or if you have generous design scenarios in which an imprecise volume measurement won’t cause failure, a rough estimate might be enough.

FIGURE 1

For a quick estimate of penetration depth when using a urethane pad, you can add the punch radius (r), material thickness (t), and a safety clearance buffer (tr) added to each side of the radius: r + tr + tr + t. Note that this is not a valid radius substitution. Again, this is a quick estimate, not a precise calculation.

Avoid Bottoming Out

You need to ensure your pad is deep enough for the application. To start, you can estimate the penetration depth with what’s known as the "clearance-stack" concept:

Penetration depth estimate = r + tr +tr + t

where

r

is the punch nose radius;

tr

is a thickness added to each side of the radius, for clearance and safety; and

t

is the material thickness. This isn’t a formal equation. Rather, it is conceptual in nature, helping to illustrate how the material and tooling interact. This quick estimation still can work effectively, especially when that extra clearance (tr) is included.

Note that the tr figure is not literal; it’s just a rule-of-thumb offset that accounts for arc engagement—that is, the curve of the punch tip making contact—and elastic deformation. In most setups,

tr

values between 0.040 to 0.060 in. tend to work well. Doubling the tr value (that is,

tr

+

tr

) ensures clearance on both sides of the punch radius, which can be especially important when estimating worst-case or maximum displacement. The values are based on practical shop floor experience and essentially help keep you out of trouble during quick pad-height estimations.

Figure 1

gives you a visualization of the concept. This isn’t about precise geometry. It’s just a quick method to ensure the punch doesn’t overcompress the pad or bottom out.

Let’s say our punch radius (

r

) is 0.125 in. and the material thickness (

t

) is 0.090 in. In this case, we establish the safety clearance (

tr

) at 0.050 in. (starting at a midpoint between 0.040 and 0.060, to keep the math simple). This gives us the following:

Penetration depth estimate = r + tr +tr + t 0.125 + 0.050 + 0.050 + 0.090 = 0.315 in.

The actual penetration depth may be closer to 0.200 in., but this conservative estimate of 0.315 in. gives you a buffer for safety. Again, this is just a rule of thumb, not precise geometry.

To avoid bottoming out, reduce heat buildup, and extend pad life, your urethane pad should be at least two- to two-and-a-half-times thicker than the estimated penetration depth. If your clearance stack calculates a depth of 0.315 in., you’d want a urethane pad thickness of at least 0.75 to 1.00 in.

This formula overestimates total deformation depth and required pad height. It’s not intended to model real displaced volume. Instead, it gives you a safety zone around the radius and thickness. It can be useful when you want to size a urethane strip quickly.

Where Precision Matters

If you want more exact information on the displaced urethane volume, pad pressure, heat generation, wear patterns in the pad, and the pad’s overall life span, you need to dig deeper. Simply "inflating" the punch radius with the material and clearance buffer doesn’t reflect what’s really going on between the punch tip, material, and urethane pad.

The correct calculation involves modeling the segment of the punch radius corresponding to the urethane compression depth—that is, how far the punch travels beyond the material thickness. I won’t delve into the complete calculations. Your urethane tooling supplier should be able to help determine what you need. Regardless, when you consider how the punch, material and urethane pad interact during bending, you’ll know why the formulas and concepts I’ve provided don’t quite reflect reality.

The punch shape doesn’t change during bending; its radius remains fixed. You’re not increasing the size of the punch; you’re just engaging more of the same arc. The urethane is responding to an increased depth of penetration, not an increased radius.

When the punch radius forms directly into the urethane, the contact zone wraps around the full curvature of the nose. That defines a true geometric penetration shape, a rounded wedge displacing a linear volume. But when you place material beneath the punch, the bottom of the material now becomes the first point of urethane contact.

By adding material thickness under the punch nose, you have changed the punch nose radius in terms of how it engages with the urethane. You’ve altered what we call the

practical engagement geometry

. The nose radius remains physically the same, but its interaction with the urethane pad changes, creating a different effective radius at the urethane interface. That affects both the penetration volume geometry and the stress distribution under the punch.

The volume of penetration scales linearly with the stroke; a deeper stroke results in more volume being displaced. However, the shape of that volume at the contact interface changes. Therefore, the stress field and hysteresis response of the urethane pad begin to reflect nonlinear characteristics. While the total volume may scale linearly, the force distribution and heating characteristics do not scale in a purely linear manner.

If you use a large punch nose radius or add thicker material under the punch, the portion of the punch radius that engages the urethane becomes increasingly flat. Eventually, the pad "sees" only the tangent of the radius (like a flat-bottomed indentation).

So, what happens when you increase the punch radius or use thicker material? You have a more abrupt transition of force into the pad, higher contact pressure at the start of compression, more localized heating, and greater pad wear.

If the compression zone moves beyond the pad’s elastic tolerance, you increase the potential for

punch float

. This refers to the unintended vertical movement—or slight rebound—of the punch during forming, caused by insufficient resistance from the forming material or the forming surface (like urethane). Essentially, the punch doesn’t "seat" firmly into its intended position because the forming medium pushes back or deflects, absorbing and then releasing force. For thin materials and small radii, such detailed analyses will probably result in only minor differences in your setup. For thicker materials or large-radius punches, paying attention to these details becomes crucial if you want to extend pad life and improve process predictability.

More to Learn

Forming with urethane is an excellent addition to your forming toolbox. There is a lot to learn and consider if you want to get the most out of it, and we still have a few more topics to discuss, including the effects of the punch angle, durometer, and shapes other than just a straight radius. Until next time …

Vaya con Dios

.

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

THE TUNGSTEN ELECTRODE EXPERTS

DGP has been industry leader in tungsten and tungsten preparation since 1992. Visit our website to buy online from stock with same day shipping or call us for a free consultation today.

ARC SABER

TUNGSTEN STORAGE

REPLACEMENT

DIAMOND GRINDING WHEELS

PIRANHA

TUNGSTEN GRINDERS

RAW TUNGSTEN

INCLUDING NEW DGP TRI-MIX

WELDING

TORCHES & PARTS

PRE & RE-GROUND

TUNGSTEN ELECTRODES

MONSTER

TIG NOZZLE KITS

DIAMONDGROUND.COM

2661 Lavery Court • Newbury Park, CA • 91320 • 805.498.3837 •

sales@diamondground.com

HYDRAULICINITIAL PINCH PLATE BENDING MACHINES

The K Series from WDM.

Over 40 years of experience with 3 generations working in the business.

Built in USA with American components.

30 gauge to 3″thick, 1′to 26′ wide.

Custom and built to order options available.

Have a rolling question? Call and speak directly to the designer, engineer and manufacturer of WDM machines, right in Tennessee, USA.

From complete custom forming cells to many popular/standard machines in stock.

Waldemar Design & Machine LLC

2748 State Road 55

Moorefield, WV 26836

606-787-8474

sales@wdmrolls.com

www.wcimroiis.com

Contact us direct, or contact your favorite machine tool distributer and ask about WDM Machine Took.

3 & 4 Roll Hydraulic Double Pinch Plate Bending Machines - Initial Pinch Sheet & Plate Bending Rolls Cone Rolling Machines - Bending Systems & Complete Forming Cells
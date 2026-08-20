# Air bending long on the press brake: Part I

[TARİH: 01.09.2024 The Fabricator]

Bending Basics

The bend length can change how the radius forms

Steve Benson

D

o you air form parts in your shop? If so, how much do you know about the 20% rule? It’s a fundamental principle that guides the behaviors involved in air forming sheet metal. It states that when you form sheet metal over a die opening that’s appropriate for the material thickness, the inside radius "floats" as a percentage of the die opening, or the distance between the die shoulders.

For example, 16-ga. A36 cold-rolled steel, with a tensile strength between 55,000 PSI and 60,000 PSI, forms a radius that’s between 15% to 17% of the die opening. (Incidentally, the "20% rule" gets its name for the percentage range for 304 stainless steel, which air forms a radius that’s 20% to 22% of the die opening.) The range of percentages reflects the fact that no two pieces of sheet metal are the same. You’ll see variations in yield strength, tensile strength, and thickness (every gauge has a thickness tolerance). The material’s grain direction also can have an effect. So, as a starting point for mild steel, you start with the median percentage of 16%. For 16-ga. A36 material formed over a 0.472-in. V die, this would be:

0.472 × 0.16 = 0.076-in. inside bend radius

After comparing this with your actual results, you’d fine-tune the percentage value over time. You’d then use this calculated inside bend radius in your bend allowance and bend deduction formulas.

For short bends—those less than 1 ft. long—the measured inside bend radius should match the calculated bend radius beautifully. When you form longer bends, however, you might see your calculations veer off course. In fact, you could find that the longer your bends get, the farther off your calculations tend to be.

How can this be? The material hasn’t changed, and neither have the punch nose radius or die opening. What’s going on? This is where we veer off the beaten path and head into the weeds. Fear not—we have a map and a compass, and I know the way.

Sometimes, the bend radius

actually transitions

during an air bend from a floated inside radius to one that matches the punch nose. Why? It has to do with applied tonnage. To answer this completely, we need to dig deeper and truly understand how applied tonnage relates to the radius during air forming.

The tonnage per foot (or meter) required to bend a piece of sheet metal increases with the length of the bend. This is due to many factors, and what follows are the first four of them that we’ll discuss on this journey. Knowing and understanding these factors, as well as those yet to come, is essential to answering the fundamental question about how the radius progresses during an air bend.

FIGURE 1 Material compresses near the inside bend radius and expands near the outside bend radius. The neutral axis neither expands nor compresses, but it does move inward during bending, a shift described by the k-factor we use to calculate the bend allowance.

FIGURE 2 When analyzing the bending moment, you start with the point of interest, which on a press brake application resides in the middle of the die width, halfway between the die shoulders. Note that the point of interest can be any location along the bend line. The bending moment increases with the length of bend.

FIGURE 3 Multibreakage occurs when the material separates from the punch tip, creating a smaller inside bend radius.

1. Material Behavior

When you bend sheet metal, the material compresses near the inside bend radius and expands near the outside radius. In the middle, we have a neutral axis, an area in which the material undergoes no physical change; that is, it neither compresses nor expands. The neutral axis remains the same length but moves closer to the center of the bend (see

Figure 1

).

As you increase the length of the bend, you also increase the amount of stretching and deformation required from the metal to complete that bend. This increases the applied tonnage.

2. Bending Moment

The

bending moment

relates to the applied forces that cause bending. In sheet metal forming, the bending moment determines the stress distribution across the sheet and the material’s behavior under load. When applied to sheet metal, the bending moment increases with the length of the bend. The longer the bend, the greater the force required to bend the sheet metal, resulting in higher tonnages.

The bending moment is calculated using

M

=

F

×

d

, where

M

is the bending moment,

F

is the

bending force

, and

d

is the measured distance from the shoulder to the

point of interest

, or the bend line at one half the V-die opening. This distance is measured perpendicular to the

line of action

of the bending force. This V-die opening measurement determines how the sheet metal conforms to the radius of the punch nose. Note that the point of interest is

any

location along the bend line where you want to understand the stress, strain, and deformation of sheet metal during the bending operation (see

Figure 2

).

A quick point of caution: The bending moment is often confused with a material’s yield strength, which measures a material’s resistance to permanent deformation. While they are related, they are fundamentally different concepts.

3. Bend Radius

Longer bend lengths generally require a larger bend radius. That’s because a larger bend radius helps prevent material failures from sharp bends and avoid cracking often found on the outside of the bend. A larger tool radius allows for gentler, more gradual bending and reduces localized stress.

A smaller tool radius relative to material thickness induces higher forming pressure and greater stress concentration. These sharp bends, with their greater concentration of load, have a higher bending moment.

The larger the bend radius, the less force (tonnage) is required to deform the sheet metal. The larger radius is effectively "spreading" the bending force over a larger area, which in turn decreases the bending moment. This can result in a smoother transition as the flat material starts to form into the desired bend, reducing stress concentrations.

Larger-radius bends offer more control until they become profound radius bends, at which point the radius and associated springback get so large that multibreakage becomes an issue, when the material separates from the punch nose tip (see

Figure 3

). Multibreakage is expected after the radius exceeds 10 to 12 times the material thickness.

4. Work Hardening

Sheet metal work-hardens during bending. What exactly does that mean and how does that affect the radius transition?

Work hardening in sheet metal bending is where the material becomes stronger and harder as it passes its elastic limit, entering its plastic state where it remains bent. At the beginning of the bending cycle, the material is elastic; this means it will return to its original shape once the load (force) is removed. However, if you continue bending, the stress exceeds the material’s yield strength and plastic deformation occurs.

Once you reach plastic deformation, you change the material’s crystal structure. The crystals dislocate, move, and multiply within a lattice. This makes it more difficult for them to move past each other, creating resistance to further deformation and strengthening the material. This change in the crystal structure increases the hardness, allowing the material to resist wear and tear.

Just Getting Started

Not only do each of these first four factors have their own set of characteristics, but they also interact and affect each other and the resulting inside bend radius. Next month, we will go further into the weeds and review how bending speed, temper, ductility, and annealing affect the bend radius transition. Following that, we’ll look at tool geometry, the isotropic and anisotropic properties of grain direction, the effects of high-tensile-strength materials, and how all this changes when bending softer materials like H-series aluminum.

Finally, we will return to

Tera Ferma

by applying what we have learned to predict what that radius will actually be as the bend transitions from a floated inside bend radius to one that follows the radius of the punch nose.

Remember that all these factors bring their unique properties to the table, but they also interact. This makes it difficult to predict a bend’s inside radius. While a perfect answer will never be completely attainable due to other extenuating variables within the material, we still can get very close. Why is this important? Because the inside bend radius is the heart of any sheet metal project. Predicting it as accurately as possible allows you to calculate the bend allowance and bend deduction with accuracy as well. If you can achieve that radius at the press brake, you will get a perfect part every time, making this trip through the weeds all worthwhile!

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

Revolutionizing Plate Processing

How the PlateLAZER from X-Series Transforms Structural Steel Fabrication

1/2″ - 460 IPM

With years of experience in high-power laser technology, X-Series is a pioneer in the structural steel space. The company stamped its mark on the industry as being known for bringing laser to structural, and the PlateLAZER reflects our commitment to innovation and excellence. The PlateLAZER from X-Series is revolutionizing the industry, delivering unprecedented speed and quality in plate processing with exponentially faster & better :

Hole Quality & Precision

Marking & Part Numbering

Flexibility & Capacity

Throughput & Efficiency

ROI

Unmatched Speed & Precision

2″ Plate -

1.5 × Faster

1″ Plate -

2.5 × Faster

1/2″ Plate-

5 × Faster

1/4″ Plate-

10 × Faster

1″ - 130 IPM

2″ - 25 IPM

WWW.XSERIESUSA.COM

@XSERIESUSA
# Solid isn’t always better

[TARİH: 01.10.2025 The Fabricator]

Bending Basics

Wall and infill considerations for 3D-printed press brake tools

STEVE BENSON

L

ast month, we embarked on a journey into the potential and possibilities that 3D-printed press brake tools offer (see

Figure 1

). We learned about common filament types and the basic 3D printing methods. This included fused deposition modeling, or FDM, the method that’s usually the most applicable and cost-effective for press brake tooling.

This month, we’ll dive deeper into how those tools are printed, including the tool surface (the wall) and the interior (the infill). The wall is the "container," while the infill is what fills that container— that is, the geometric patterns that fill the void up to 100% (solid)—and as we’ll soon discover, 100% isn’t necessarily the best option (see

Figure 2

).

Walls Build Strength

A printed object’s strength and ability to withstand force (including the stress and strain brake tools are subjected to regularly) depends greatly on the number of walls it has. When printing with FDM, the

wall thickness

is usually expressed as a multiple of your nozzle diameter, with 0.4 mm being the most common nozzle diameter filament and nozzle size.

For conventional printed objects (that is, those not subjected to significant force), wall thicknesses usually range between three and six nozzle diameters (often referred to as "walls"), or between 1.2 and 2.4 mm. Printed brake tools usually will have wall thicknesses between 10 to 12 nozzle diameters (or "walls"). When using a conventional 0.4-mm nozzle, brake tool wall thickness of 12 walls would be 4.8 mm (0.4 × 12 = 4.8).

Infill Patterns

Geometric

infill

patterns fill the empty space within the part while providing support, strength, and rigidity—all without making the object completely solid. The infill patterns also reduce the amount of material needed for printing, saving time and money.

Infill

density is usually expressed as a percentage, with 0% being completely hollow and 100% being completely solid.

Different infill patterns offer varying levels of strength and require different amounts of printing time. A grid consists of a basic pattern of intersecting lines. This offers a good balance between strength and printing time. A

gyroid

pattern provides good strength in all directions and is often used for flexible materials. A

lightning pattern

focuses material only where needed for support, minimizing material use and print time. Finally, a

cubic

pattern essentially creates a pattern of stacked cubes. This approach offers good strength and material efficiency.

Each infill pattern collapses under load in different ways: Some crush and some shear away. Cubic, triangle, and gyroid patterns tend to fare best at 25% infill.

Wall Thickness vs. Infill

The outer walls make a big difference regardless of the infill pattern. While 100% infill creates a solid part, it can sometimes be weaker than a part with thicker walls and an interior infill pattern. That’s because the 100% infill can trap air and create stress points.

To create functional press brake tools, prioritizing wall thickness over infill can be more effective. Thicker walls offer better resistance to bending and twisting. Testing has revealed that even gooseneck punches have withstood greater than expected forces—and those punches were not solid.

Certainly, gooseneck tooling by its very nature is a much weaker tool than a standard straight punch. Under testing, the tool deformed before it broke. If you pay close attention, you will see an "overload" coming and be able to back off from the bend before any damage occurs. To overcome the problem, you could find a less tonnage-intensive way to form the part, change to a stronger tool profile, or return to a steel gooseneck punch and save the 3D-printed punch for another time and project.

Deflection

If your shop uses urethane tools, you might have some dies and perhaps some pads you use in a retainer box. You might even have experience with a punch that has urethane components. If so, you’ll know that if you need a small punch nose, you won’t be reaching for a urethane punch. This is because of deflection and the overall elastic properties of urethane (see

Figure 3

). Under a force load, urethane will deflect.

When you exceed the elastic limit of urethane, your 0.032-in. punch nose radius can become a 0.062-in. nose radius.

The amount of deflection will vary depending on the durometer (hardness) of the urethane. Urethane is a much softer material than plastic, with a much higher elastic limit. In many cases, the nose radius will return to its original shape.

FIGURE 1

These tools were printed using fused deposition modeling. Designing tools with the right wall thickness and infill pattern can make a real difference.

FIGURE 2

Note the characteristics of this 3D-printed object, including the interior infill pattern. Solid isn’t always best.

Reflexpixel/iStock/Getty Images Plus

FIGURE 3

This shows the material hardness scales for urethane and the general categories of many 3D-printable materials.

The same can’t be said of polyactic acid (PLA), the material you’ll probably start with if you decide to experiment with 3D-printed tools. PLA will exhibit deflection under a force load, but it won’t behave like urethane in terms of returning to its original shape after pressure is released. PLA is rigid, but it also can deform permanently or even break if the load exceeds its elastic limit. PLA does not have significant enough elastic properties and will not return to its original shape after pressure is released.

PLA is known for being hard and brittle. However, when force is applied

within

its elastic limits, the PLA will deflect and then return to its original shape once the force is removed. PLA does suffer from

creep

, however, meaning that under a constant or repeated load, even at a relatively low stress level, the PLA will deform permanently over time. How much PLA deflects depends on several factors, including the tool design, the number of walls (wall thickness), and the layer thickness.

Nonetheless, sharp punch nose radii should be avoided for several reasons. First, due to force limits, your forming method with 3D-printed tools will be air forming, which develops the least amount of tonnage to form a part. Because you are air forming, your inside bend radius will float as a percentage of the die opening. So, a sharp nose radius adds no benefit. And even though the constant, concentrated, and repeated loads will change that nose radius, you won’t change the inside radius of the part.

Note that because the punch nose deforms slightly under pressure, your overall punch height can change slightly. That’s why, in this case, a punch nose radius change will cause changes in the bend angle. To dial in your bend angle, you might need to adjust the punch’s depth of penetration into the die space.

For the best results, you should have a one-to-one relationship between the punch nose radius and your material thickness. When printing your tools, make sure your die width produces a floated radius in the material that’s as close as possible— and yet does not exceed— your punch nose radius.

If your punch nose radius exceeds the floated radius, the part will take on the larger radius. If your job requires a sharp punch nose radius, in some cases, you could add some metal to your tools. This could be in the form of sheet metal or a small-OD metal tube—elements that can be added right into the printing process. (Look out for future columns about this.)

Next month, we will examine other types of materials and their impact on the printer.

Does the printer need to be enclosed? What kind of build plate do I need? What type of glue or adhesive goes with which material?

We also will look at where to find information about the different materials and whether the printed part needs to be annealed, as well as how and when. Yes, some plastics do need to be annealed for the best results. So, get ready—there is much more to come. Until next time …

Vaya con Dios!

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

.

WHY BUY FROMGRIZZLY?

We buy direct from factories and sell direct to you

High-quality, award-winning machines

Two overseas quality control offices

98% of in-stock orders ship same-day

Over five million parts in stock for instant after-service

Family-owned and operated since inception

Since 1983

14″ 1½ HP Vertical Metal-Cutting Bandsaw

Versatile cutting for any shop

Built-in blade welder and grinder

Annealing station

88–384 FPM blade speeds

Rubber-bonded wheels

Chip blower and work light

Footprint: 16½″ × 31″

Shipping weight: ≈ 926 lbs.

G0806 // ONLY $4150

18″ 2 HP Vertical Metal-Cutting Bandsaw

Engineered for all-day performance

Built-in blade welder and grinder

Annealing station

88–384 FPM blade speeds

Rubber-bonded wheels

Chip blower and work light

Footprint: 16½″ × 34″

Shipping weight: ≈ 999 lbs.

G0807 // ONLY $5350

20″ 2 HP Vertical Metal-Cutting Bandsaw

Power through large-scale production

Built-in blade welder and grinder

Annealing station

83–2100 FPM blade speeds

Digital speed display

Chip blower and work light

Footprint: 413/4″ × 203/4″

Shipping weight: ≈ 842 lbs.

G0668 // ONLY $7875

48″ Pan and Box Brake

Complete heavy-duty box bending

Set an angle in 12-gauge mild steel up to 135°

Make repeatable bends at an exact angle

Adjustable stop collar

Eight removable fingers

Counterweighted, adjustable brake handle

Footprint: 531/4″ × 291/4″

Shipping weight: ≈ 1271 lbs.

G0542 // ONLY $3225

21″ 1½ HP Gearhead Drill Press

Unbeatable power, performance, & precision

Variable frequency drive (VFD) for high-torque variable speed

High/low variable-speed spindle ranges

Spindle speed digital readout

Rack-and-pinion table elevation

Coarse and fine downfeed controls

Footprint: 26″ × 18½″

Shipping weight: ≈ 683 lbs.

SB1115 // ONLY $5175

27″½″ 2 HP Gearhead Drill Press

Tackle extreme drilling applications

60–1740 RPM spindle speeds

2-Speed power downfeed

Recycling coolant system

1″ Powered tapping capacity

Adjustable depth stop

Footprint: 29″ × 20″

Shipping weight: ≈ 1202 lbs.

G0756 // ONLY $6625

52″ Sheet Metal Shear

Cut your work down to size

Rear extension arms with micro-adjusting stops

Spring-activated hold down

Adjustable front stop and angle guide

Convenient foot control

Precision-ground cast-iron body

Footprint: 60″ × 21″

Shipping weight: ≈ 1120 lbs.

T32957 // ONLY $3495

50-Ton Hydraulic Shop Press

Tackle high-tonnage applications

Pneumatic and hand-pump operation

Heavy-duty arbor plates

Winch-adjustable table positioning

Protective front shielding

Pressure gauge

Footprint: 39½″ × 29½″

Shipping weight: ≈ 698 lbs.

T34349 // ONLY $1850

30-Ton Electric Hydraulic Shop Press

Powerful push-button pressing

Motor-driven operation

Heavy-duty arbor plates

Chain-adjustable table positioning

Protective rear shielding

Pressure gauge

Footprint: 40″ × 27″

Shipping weight: ≈ 1232 lbs.

T1242 // ONLY $6195

Please visit

grizzly.com

for up-to-date pricing.

Due to rapidly changing market conditions, our advertised prices may be changed at any time without prior notice.

FINANCING AVAILABLE

WARNING! †1 : Cancer & Reproductive Harm

Some products we sell can expose you to chemicals known to the State of California to cause cancer and/or birth defects or other reproductive harm. For more information go to

www.P65Warnings.ca.gov

.

grizzly.com

800-523-4777
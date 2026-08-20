# How to 3D-print metal press brake tools

[TARİH: 01.03.2026 The Fabricator]

Bending Basics

Debinding and sintering hold everything together

STEVE BENSON

D

ebinding and sintering are the make-orbreak stages of 3D printing with metal powder filament. With a small, tabletop 3D printer, you can print a flawless press brake tool, design it perfectly, scale it correctly, and support it well, but if it isn’t debound and sintered correctly, it will fail.

DEBINDING BASICS

Metal powder filaments contain two primary components: metal particles and polymer binders. A critical postprocessing step in metal additive manufacturing, debinding removes most of the polymer or wax binding material that holds the metal powder together after the initial print. The binder, which exists solely to allow extrusion during printing, represents 10% to 20% of the volume, depending on the filament brand.

Debinding creates open-pore channels throughout the part, preparing it for the final sintering stage in which the remaining binder is burned off and the metal particles fuse into a dense, solid metal object.

Chemical debinding

dissolves certain binders in a solvent, while

thermal debinding

burns off the remaining binder at a controlled temperature.

A part that comes right off the printer is in its

green state

. When it has been fully debound but not yet sintered, it’s considered a

brown-state part

. This is extremely fragile. It retains the exact geometry of the green-state print but will shrink and densify during sintering. If debinding is incomplete, trapped polymer gas will blister or crack the part during sintering.

HOW SINTERING WORKS

Sintering is a high-temperature metallurgical process. The debound part is heated in a controlled-atmosphere furnace—typically between 1,200 and 1,380 degrees C, depending on the alloy type. When sintering occurs, metal particles fuse, porosity collapses, grain boundaries form, and the part densifies and shrinks in a predictable way. This produces a part that is between 94% and 98% as dense as wrought steel.

Certain high-purity applications might use vacuum sintering, but for most printing applications a fabricator might try, sintering will rely on some type of atmosphere. Press brake tooling must be free from oxidation, carbon contamination, and brittleness, and the right sintering atmospheres help achieve this. Even stainless steels require a protective atmosphere to maintain corrosion resistance.

Hydrogen atmospheres are excellent for reducing oxides, while nitrogen/hydrogen mixes are common for stainless steel. Argon is inert and safe but more expensive.

A brake is set up with conventional tooling. Printed tools will never replace steel tools for production, but they have serious potential for certain jobs, including prototyping and light forming work.

funfunphoto/iStock/Getty Images Plus

THE MECHANICS OF SHRINKAGE

Shrinkage is not a defect. It is a necessary process that allows internal voids or hollow pockets to collapse, causing the metal particles to fuse. Shrinkage should occur in a predictable way. Manufacturers even specify shrink values.

Printed parts shrink differently in different dimensions, with X and Y shrinking slightly more than Z. The shrinking happens in a nonlinear fashion, with the greatest amount occurring early in the sintering cycle.

CAD scaling should be able to offset the dimensions accurately for you. For press brake tools, dimensional accuracy is crucial. A punch nose radius or die opening geometry must be predictable after shrinkage. You can use calibration coupons to dial in a perfect compensation.

THE ROLE OF BALLAST

Brown parts need proper support. Sintering occurs at temperatures high enough to cause metal to slump if unsupported, especially in areas with large overhangs, thin vertical features, long unsupported spans, and heavy tops on narrow bases.

You can use ballast to prevent deformation, and common ballast includes more than just sand. The choice varies depending on the material used in the 3D-printed parts.

Alumina setters

work well for flat ceramic plates, while

zirconia

trays are inert and offer high temperature stability. Meanwhile,

ceramic bead beds

can conform to highly complex shapes,

while silicon carbide plates

offer very strong support surfaces.

Which ballast you choose will depend on the application, but whatever ballast you use, ensure that the brown-state tool sits on a stable, inert support that allows uniform heating and prevents sticking and chemical interaction.

The risk of warpage increases with thin features, asymmetric geometry, uneven heating, or incorrect orientation. Choosing the right ballast reduces or eliminates such warpage. To achieve this, you might use a ceramic bead bed, which, again, can conform to and support highly complex shapes.

Warpage is rare in most cases, especially when the part geometry is uniform and properly supported. Nonetheless, preparing the ballast still requires a precise setup. To prevent warping, be sure to support areas prone to sagging. Print with thicker walls, add temporary support ribs if needed (and remove after sintering), and increase chamfers and fillets.

After sintering, the part and ballast go off to the kiln—and not all kilns are alike. While kilns in general are the same in many respects, an older kiln, one that uses a witness cone to regulate the temperature inside, is not accurate enough for sintering. You will be bringing the brown part to a temperature just below the melting point of the metal in the filament. Relying on a witness cone makes it too easy to miss the required temperature.

EXPERIENCE WITH STAINLESS STEEL

Straight from the furnace, sintered stainless steel should have a slight surface texture, good overall hardness, slight porosity, and a fully metallic structure. Depending on the application, optional finishing might include some light sanding and polishing. In certain cases, you might need more aggressive surface grinding and, for critical faces, even some machining. Because the material is slightly less dense than billet steel, machining is slightly easier. And if your part has holes, you might need to ream them to tolerance.

Sintered 316L and 17-4 PH typically achieve 75% to 95% of wrought strength. They have high corrosion resistance, good fatigue behavior, and adequate hardness for prototype tooling. These printed tools shine when you need custom geometry, but not brute force. They work well for air bending and light forming, but I don’t recommend them for bottoming or coining.

WHERE PRINTING METAL TOOLS MAKES SENSE

3D printing metal tools can be ideal when you need a cost-effective way to create custom, complex tool shapes in low quantities and with short lead times. Again, they aren’t ideal for high-tonnage forming or heavy production work, especially when you need tools with a very high surface hardness. And if you’re not machining your tools after printing, you could have problems achieving extremely tight tolerances.

For sheet metal shops in particular, geometric freedom is the biggest benefit. You can print odd-shaped punches, multistage forming inserts, radius transitions, asymmetric die shapes, hemming prototypes, flange locator features, and more—no machine shop required.

Overall, the technology helps reduce tooling cost and downtime. And you can repair or modify tool shapes quickly, iterating the design to dial in the forming process. Testing a new tool shape isn’t a high-risk proposition.

A ROADMAP FOR PRINTED TOOLING

As I discussed in previous columns in this series, printed plastics can work in certain tooling applications, but they have their limits, including creep, warping, and heat sensitivity. For printed polymer tools, proper annealing helps improve strength, thermal stability, and dimensional reliability.

Meanwhile, printing with metal powder filaments, debinding, and sintering represent significant advancements. When used correctly, these tools can be strong, accurate, and reliable for prototype and light-duty forming. For many, they can serve as the bridge between plastic prototypes and full-production steel tooling. They can’t replace hardened steel tooling, but they can be a fast, economical solution for prototyping, short runs, training, and specialty forming.

I wrote this series to introduce you to 3D-printed press brake tooling, to show not only how it works, but

why

it works, where it fails, and when traditional steel tooling remains the correct choice. I intended to give you an experience-based roadmap. Thanks for joining me on the journey. Until next month and a new topic …

Vaya con Dios!

THEFABRICATOR.COM

› AUTHOR › STEVE-BENSON

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s "Bending Basics" book is available at the FMA bookstore,

www.fmamfg.org/store

.

B&B Welding

Next Gen Tech for Next Gen Fab

Dennis McCartney

Vice President/Detailer

Brendan McCartney

CNC Operations Quality Control

On other machines we can get tolerances down to 1/32 or 1/64, but with the laser you’re talking about getting 1/1000 and 10/1000 of accuracy. You don’t have the kerf angle that you have with plasma. The parts are straight. It gives a better fit up on the welded joints. So then welders aren’t trying to fill a gap on one side and tighten the other side. The parts don’t pull and it just creates an overall better end product.

Brendan McCartney

WATCH VIDEO HERE

PeddiSwing 3015 12 kW

Speed of Light

www.peddilaser.com

|

info@peddilaser.com

| (815) 937-3800
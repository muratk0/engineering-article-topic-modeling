# How to anneal a 3D-printed press brake tool

[TARİH: 01.01.2026 The Fabricator]

Bending Basics

And why it matters for the sheet metal shop

By

Steve Benson

T

oday, 3D printing has started to find a home in the modern sheet metal shop. If you need a prototype punch, a test die, a radius form, a soft protective jaw, or a check fixture, you can design a part in CAD and print it immediately. It has changed the way we approach low-quantity forming and process development. While 3D printing is not a replacement for hardened tool steel, it has become a powerful extension of the tooling toolbox, especially when time, cost, or experimentation are the driving factors.

That said, anyone who has used printed tools on a press brake knows the limitations. Printed plastics soften, creep, warp, twist, and sometimes crack on the layer lines. They might look perfect when they come off the printer, but they can distort under the slightest heat from repeated bending cycles. A punch that holds its dimensions today may shrink or curl if left in a warm area of the shop. These problems don’t come from poor printing; they come from the nature of the plastics themselves.

Annealing is the solution. It is one of the easiest, least expensive, and most effective methods for dramatically increasing the strength, heat resistance, and dimensional stability of 3D-printed tooling. Simple enough to perform in most shops, the process reliably turns a fragile printed part into a surprisingly durable workpiece capable of handling real-world use on the press brake. Once you learn how annealing works, how to perform it, and how different printed materials respond, you can use the technique to get the most out of your printed tooling.

WHY 3D-PRINTED TOOLS NEED ANNEALING

Most common 3D printing filaments used in shops—PLA, PLA+, PETG, ABS, ASA, nylon, PC blends, and various composites—are thermoplastics. They soften with heat and stiffen when cooled. During printing, the extruder lays down a hot bead of material on top of a cooler layer. As those layers cool, internal stresses become locked into the part. These internal stresses are harmless when the tool sits idle, but once you use it under load, those stresses begin to reveal themselves.

The symptoms are predictable. You might see the tool warp or curl, or it might twist along its length. You might see weak layer adhesion, especially in Z, as well as creep when holding a heavy load. You could see the tool crack under mechanical load or soften at temperatures far below what you’d expect.

The problem becomes more visible on parts with long dimensions, sharp corners, or insufficient wall thicknesses. Even without mechanical load, simply leaving a PLA tool in a warm car or near a heater can cause significant deformation.

Annealing relieves these internal stresses, allowing polymer chains to reorganize into a more stable, crystalline structure. Heat resistance increases dramatically. Mechanical strength—especially the layer-to-layer bonding—improves. Dimensional drift decreases, and the part becomes far more predictable.

WHAT ANNEALING DOES AT THE MATERIAL LEVEL

To understand why annealing works, imagine the printed part as a bundle of tangled microscopic fibers, each partially aligned in the direction the filament was extruded. These chains are frozen in place as the material cools during printing, locking internal stress into the structure. This disordered internal structure is what makes printed tools weak and unstable.

When a printed part is heated to just below its melting point—typically 158 to 230 degrees F, depending on filament type—the polymer chains loosen and gain the ability to slide into a more ordered formation. This process is called

crystallization

.

One benefit of this microstructural rearrangement is a higher heat-deflection temperature (HDT), or the temperature at which the material begins to soften under load. Annealing can raise HDT for PLA from 131 to 194 degrees F—a dramatic improvement. It also helps strengthen interlayer bonding. Since heat affects the entire volume uniformly, the layers rebond on a microscopic level. The Z axis becomes significantly stronger.

As annealing reduces internal stress, the part becomes more dimensionally stable and far less prone to long-term warping or bending. And as the polymer chains pack more efficiently, density increases slightly, improving rigidity.

Annealing also gives the printed tool better creep resistance, which makes it less likely to deform under constant load. This is why annealed parts behave much more like engineered plastics and much less like brittle printed prototypes.

WHICH FILAMENTS BENEFIT MOST

PLA and PLA+

see the greatest benefit from annealing. Their strength increases, HDT doubles, and brittleness decreases.

PETG

gains good dimensional stability and becomes more scratch resistant, though HDT increases only modestly.

ABS/ASA

benefits only moderately, especially in reducing warp; its heat resistance is already high.

Nylon

gains stability, but moisture content plays a role. Annealing should be done after drying.

PC blends

(polycarbonate mixes) already are strong and heat resistant. These gain stability but require more precise temperature control.

Composites

like carbon fiber and glass-fiber-filled material often benefit less because the fibers already provide structure. However, annealing still makes them more heat resistant.

For printed press brake tooling in particular, PLA+ and PETG are the two most common material choices, and each benefits substantially from annealing.

REQUIRED EQUIPMENT

One of the strengths of annealing is its simplicity. You do not need specialized machinery. Most shops can do it with a convection or toaster oven, along with a flat metal tray or ceramic tile. You also might need fine sand, table salt, or steel plates as ballast, as well as a reliable thermometer, or at least an oven that holds a steady temperature.

Convection ovens are preferred because they ensure even heating. Regular heating elements can cause hot spots that warp the part. And because filaments like nylon, ABS, and PC blends emit fumes, you should never use a household oven that will later be used for cooking.

ANNEALING, STEP BY STEP

The following process works consistently across PLA, PETG, ABS, nylon, and most shop-grade filaments:

1. Preheat the oven

– Bring the oven up to the target annealing temperature before placing the part inside. Never exceed the glass transition point significantly, or the part may sag or collapse.

Typical ranges are:

PLA/PLA+: 158 to 176 degrees F

PETG: 76 to 194 degrees F

ABS/ASA: 203 to 230 degrees F

Nylon: 158 to 194 degrees F (depending on the brand)

2. Prepare the part

– Remove supports used during printing and do any rough sanding beforehand. If the part includes very thin walls or fine features, consider printing a small test coupon to verify shrink rates.

3. Decide whether ballast is needed

– Ballast keeps the part from deforming during the anneal. Options include burying the part in sand; covering it in table salt; placing a flat steel plate on top; and supporting long parts on both ends. You’ll likely need ballast when the part is long and flat, if the part must remain perfectly square, if you’re using PLA or PETG, if your part contains thin elements, or if dimensional accuracy is critical. For thick, dense shapes (like a punch block), ballast may be optional.

4. Heat-soak the part

– Place it in the preheated oven and allow it to soak at the required temperature. Note that "soak" in this context means to keep the part at a temperature for a specific amount of time. The goal is to achieve a uniform internal temperature. Some general guidelines:

Small parts (1- to 3-mm walls): 30 to 45 minutes

Medium parts (4- to 8-mm walls): 45 to 60 minutes

Thick parts (10- to 20-mm walls or thicker): 60 to 120 minutes

5. Control the cooling

– Turn the oven off and let the part cool naturally inside. Rapid cooling—opening the door or removing the part—can cause warping, twisting, or stress cracking. Slow cooling typically takes between 45 and 90 minutes.

COMPENSATE FOR SHRINKAGE

All annealed plastics shrink to some degree. The amount depends on the type of filament:

PLA: 2% to 5%

PLA+: 1.5% to 4%

PETG: 1% to 3%

ABS: 0.5% to 2%

Nylon: 0.5% to 1.5%

Composites: less than 1%

Shrinkage is usually greater in the X/Y plane than it is in Z. On press brake tooling, this may mean that the punch nose width decreases, die openings narrow, and radius blocks shrink slightly in diameter. Note that flat faces tend to contract inward.

To compensate, scale the model slightly larger before printing. You can do this right in your slicer software. You can test with a small cube (about 20 mm across) and anneal it to measure the exact shrinkage percentage for a given filament.

PRACTICAL APPLICATIONS

Sheet metal shops can anneal a variety of printed items: prototype punches, soft dies for preproduction tests, bend radius gauges, check fixtures, go/no-go tools, protective jaws for polished stainless, wiper blocks, radius form blocks—the list goes on.

In these applications, annealing improves durability and reduces wear. For prototypes, annealing means more reliable trials. For protective tools, it means longer service life. For teaching and training, it means tools stay dimensionally accurate over time.

Note that because of deflection, a punch with a small nose radius does not work well under heavy load without a metal insert. Without metal insert support, a printed 1/32-in. punch nose becomes a 1/16-in. nose under load. (We will discuss how to use metal inserts in printed tools next month.)

LIMITS AND BENEFITS

While annealing significantly improves printed-tool performance, the process has some practical limits, one being strength. Annealed PLA or PETG is not steel. These tools are for testing, prototyping, and light forming— not production runs involving high tonnage.

For proper annealing, you need to be able to control temperature precisely. A sloppy oven may cause deformation if it overshoots the target temperature. At least some dimensional change is unavoidable. Shrinkage must be accounted for. Absolute precision may still require CNC machining. Also, thick parts need a longer soak time. Large tooling blocks can take more than an hour to stabilize fully.

Even with these limitations, annealing remains one of the most cost-effective ways to improve the performance of printed tools, bringing them to a new level of usefulness. The process increases heat resistance, improves strength across layer lines, reduces creep, and stabilizes dimensions over time. For press brake work where even temporary tooling must hold shape under load, these improvements are essential.

With minimal equipment and a predictable process, any shop can incorporate annealing into its workflow. The result is stronger, more reliable printed tooling that performs far better than raw prints alone. In a world where speed, cost, prototyping, and adaptability matter, annealing turns a 3D-printed idea into a process you can trust.

Next month, we’ll dive deep into a 3D printing strategy that can make the technology even more useful at the press brake: smart use of metal-infused filaments. Until then …

Vaya Con Dios

.

STEVE BENSON

THEFABRICATOR.COM

› AUTHOR ›

STEVE-BENSON

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

Patent No. US 10,576,588 B2

Patent No. US 11,426,826 B2

Patent No. US 12,017,308 B2

Patent No. US 12,226,858 B2

by Automated Layout Technology™

Precision in Every Line, Power in Every Layout.

For the fabricator looking to maximize their production time and profits, the Lightning Rail is a smart decision. Eliminate the countless manual labor hours involved in laying out handrails, stair stringers, trusses, and more!

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins

Layout complex geometry in seconds

Designed to replace your existing fabrication table

603-402-3055

AutomatedLayout.com

BEVEL-MILL

®

Model 9000

World’s Largest

HAND OPERATED PLATE BEVELERS

Bevel up to 1 3/16″

Model PRO21-G

Up to 10 feet per minute

POWER FEED BEVELERS

Model WS625

WELD BEAD SHAVER

Machines weld beads flush to work piece.

Model BB27

BENCH TOP DEBURRING

Precision finish chamfers.

800-886-5418

Fax 810-632-6640

www.heckind.net
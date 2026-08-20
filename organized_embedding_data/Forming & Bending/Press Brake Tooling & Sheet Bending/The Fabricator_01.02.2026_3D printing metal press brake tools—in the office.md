# 3D printing metal press brake tools—in the office

[TARİH: 01.02.2026 The Fabricator]

Bending Basics

An introduction to 3D printing with metal

THEFABRICATOR.COM

› AUTHOR › STEVE-BENSON

M

etal powder 3D printing is reshaping how small and midsize fabrication shops think about toolmaking. What was once the exclusive domain of large OEMs with metal printers, industrial furnaces, and R&D divisions is now accessible to anyone with a high-quality consumer printer, such as the Bambu X1 Carbon (the one I use the most).

In press brake work, where custom punches, form tools, and test fixtures are part of everyday life, the ability to print metal—including real tool steel, stainless steel, and even bronze and copper—changes the equation. Even small job shops now can prototype small-batch tooling at a fraction of the price and time required for full machining.

WHY PRINT METAL TOOLS?

Tooling often is a bottleneck, especially in the forming department. A brake cannot run a job until the required punches and dies are on hand. For custom and prototype work, tool cost can be substantial, especially if the tooling is a one-off job.

3D printing a custom metal punch or forming insert reduces cost, lead time, risk, and the iterative friction. The final sintered part is strong enough for light to medium forming loads, for most prototype work, and for specialty geometries that would be challenging or expensive to machine.

ABOUT BOUND METAL FILAMENTS

Metal powder filaments

, also called

bound metal filaments

, incorporate stainless steel or other alloys. These metals are reduced to extremely fine powder and mixed with polymer binders.

These binders allow the filament to behave like PLA or PETG during printing, even though the object being printed is mostly metal by mass. Common shop-appropriate filaments include:

BASF Ultrafuse 316L, an austenitic stainless steel like 316L plate.

BASF Ultrafuse 17-4 PH, a precipitationhardening stainless with higher strength.

Markforged ADAM-compatible blends.

Bronze, copper, and tool steel experimental blends (available but less common).

These filaments, printed at the same temperature range as PETG and ABS, do not require expensive hardware and require minor changes to the printer that involve only everyday, off-theshelf items. This can include a hardened-steel nozzle, since metal particles in the filament can wear out standard brass nozzles quickly.

A 3D printer uses bound-metal filaments that, after sintering, create an all-metal part. The technology shows significant promise for press brake tooling, especially for applications with low- to medium-tonnage requirements.

Iloliloli/iStock/Getty Images Plus

DEBINDING AND SINTERING

A metal powder filament prints and looks like PLA, but its internal structure is different. The binder melts; the metal does not. Layer fusion works differently, so print settings must be optimized with sintering in mind.

The final printed object, called a

green part

, contains the full amount of material required to become a metal part after sintering. It’s dimensionally accurate but far weaker than any functional metal. Its strength develops later, after debinding and sintering remove binders and fuse the material to create a metal-only part or tool. For this reason, you will need a kiln with digital controls, or at least access to a debinding and sintering service.

Green parts should be handled like unfired ceramics— dropping one can ruin the print. Support them from underneath, avoid compressive loads, use foam-lined trays, and bag each print individually for transport to sintering. The

brown-state part

, after debinding but before sintering, is even more fragile.

DESIGN AND ORIENTATION

Unlike plastic prints, metal prints should not use an infill pattern, which fills the area inside the printed part, unless they’re specifically engineered for it. Infill collapses during sintering because it lacks an internal structure to support it after binder removal. The safest approach is to use 100% infill (no infill pattern) with solid walls and body. When you need strategic infill for internal reductions, design them intentionally for uniform density and shrink control after printing. Because sintering removes binder and leaves only metal, the geometry must account for a minimum wall thickness, usually between 1.2 and 1.5 mm in the green part, depending on filament. Avoid unsupported, thin vertical walls as well as tall, narrow columns or spindly protrusions. You can add slight tapers (draft) and fillets to reduce warping. Also note that sharp internal corners concentrate stress during sintering and can lead to cracking.

DESIGNING FOR SHRINKAGE

Metal powder prints shrink significantly during debinding and sintering. Printed stainless 316L can shrink between 14% and 20%, 17-4 PH stainless between 12% and 16%, and bronze metal blends between 10% and 14%. This shrinkage is not a defect; it’s part of the densification process. As the binder is removed and metal fuses, the part becomes smaller but much stronger.

Shrinkage is anisotropic. In most formulations, the shrinking in the X and Y directions is slightly more than in the Z direction. Shrinkage is highly predictable once you calibrate your process and tool design to account for it. Sintering companies provide shrink parameters, but the best approach is to print and sinter a calibration block. Simply print a small test cube, measure its green dimensions, then measure its dimensions after sintering.

When designing in CAD, you’ll need to oversize your tools. If a punch tip radius must be exactly 0.500 in., the printed green state may need to be between 0.575 and 0.600 in., depending on shrink rates.

Print orientation influences shrinkage behavior. Long, thin shapes may bow slightly unless supported with setters during sintering. Metal prints shrink more uniformly when layers are aligned with the load path.

For press brake tooling, that often means orienting the punch or die so that layer lines run perpendicular to the forming load. This minimizes your overhangs (unsupported features) during printing. It also makes the strongest axis oriented vertically along the tool body. The Z-axis strength is lower, both for plastic polymer and metal prints.

TOOL DESIGN

Press brake tooling introduces special requirements when designing for bound-metal filament printing. Punches require thick bodies, reinforced shoulders, generous fillet transition, and a smooth load path. Avoid tall, narrow punches unless fully supported during sintering.

Dies are easier to print than punches because they sit flat, can be printed in a natural orientation, and their load paths are predictable. That said, make sure to oversize the critical dimen-sions (again, to account for shrinkage after sintering). This includes the die opening, or V-die width. You also need to ensure the tool remains flat during sintering.

Large-radius tools or custom odd shapes are great candidates for metal powder printing. They can be printed as solid blocks with minimal risk of warpage, if properly supported during sintering. In fact, printing with metal bound filament is great for complex geometries in general. You can create internal channels and organic shapes that couldn’t be milled. The only requirement is that voids

must

be vented for debinding.

During debinding, gases escape as the binder melts or dissolves. If internal cavities are not vented, the part being printed can crack, and even explosive flaking can occur. Surfaces may blister and deep pockets can cause implosions.

Every internal void or recess must have an escape path for the gases leading to the exterior.

PARAMETERS FOR PRINTING METAL

Settings vary for 3D printing software, known as

slicers

, but some general rules apply. First, a hardened steel nozzle, usually with a diameter between 0.4 to 0.6 mm, is best. Extrusion temperatures range from 230 to 260 degrees C, and bed temperatures are between 90 to 100 degrees C.

The wall or perimeter setting is usually between 4 and 6 (with each "perimeter" being equal to the printing nozzle diameter). The top and bottom layers need to be thick enough to prevent porosity, while the flow setting (which controls the volume extruded) needs to be increased slightly to ensure layer adhesion. I also strongly recommend you use what’s known as a

brim

—a flat, single-layer extension added to the base to increase surface, improve bed adhesion, and prevent warping.

Slow printing and high extrusion stability are key. For consistent printing, print at a slow speed, between 20 and 40 mm/s.

COST BENEFITS AND PRACTICAL VALUE

Metal bound filament printing is not meant to replace machining for production tooling, but it fills the gap between plastic prototypes and full machining. Again, it allows you to test first before committing to a steel tool. Used in the right way, metal 3D printing can help reduce costs, especially in prototyping, allowing for rapid design iteration. A metal printer effectively gives you access to real stainless steel tools without a machine shop.

You can design and test punches, experimental profiles, unique and complicated shapes, and short-run tools internally. For production runs, you still would invest in custom punches and dies made out of tool steel, but

only

when you are satisfied with the geometry and are able to create a functional part from the tool.

Next month, at the end of our story, we complete this series with a look at debinding chemistry, sintering temperatures and furnace cycles, ballast and setter plates, warpage on thin tools, dimensional accuracy, and post-sinter finishing and machining. We’ll also discuss realistic load capacities for printed tools, along with the overall pros and cons of adopting the process. Until next time …

Vaya con Dios

.

STEVE BENSON

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s "Bending Basics" book is available at the FMA bookstore,

www.fmamfg.org/store

.

For the fabricator looking to maximize

their production time and profits, the Lightning Rail is a smart decision.

Eliminate the countless manual labor hours involved in laying out handrails, stair stringers, trusses, and more!

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins 9 Lay out complex geometry in seconds

Designed to replace your existing fabrication table

VISIT US AT

NASCC; THE STEEL CONFERENCE EXHIBITOR 2026

Patent No. US 10,576,588 B2

Patent No. US 11,426,826 B2

Patent No. US 12,017,308 B2

Patent No. US 12,226,858 B2

603-402-3055

AutomatedLayout.com

by Automated Layout Technology™

START 2026 STRONG WITH RELIANT

NEW

Features & Options

LOWER

Prices

SHORTER

Lead Times

FREE

Start-Up & Training

LIFETIME

Support

ENGINEERED & AUTOMATED

Solutions Available

PARTS, FILTERS & POWDER GUNS

In Stock

OVER 20 YEARS OF EXPERIENCE

Designing & Manufacturing Powder Coating, Industrial Wet Painting & Thermal Processing Solutions

RELIANT Finishing Systems

888-770-0021

reliantfinishingsystems.com

THE TUNGSTEN ELECTRODE EXPERTS

DGP has been industry leader in tungsten and tungsten preparation since 1992. Visit our website to buy online from stock with same day shipping or call us for a free consultation today.

ARC SABER

TUNGSTEN STORAGE

REPLACEMENT

DIAMOND GRINDING WHEELS

WELDING

TORCHES & PARTS

RAW TUNGSTEN

INCLUDING NEW DGP TRI-MIX

MONSTER

TIG NOZZLE KITS

PRE & RE-GROUND

TUNGSTEN ELECTRODES

PIRANHA

PIRANHA TUNGSTEN GRINDERS

DIAMONDGROUND.COM

2651 Lavery Court • Newbury Park, CA • 91320 • 805.498.3837 •

sales@diamondground.com
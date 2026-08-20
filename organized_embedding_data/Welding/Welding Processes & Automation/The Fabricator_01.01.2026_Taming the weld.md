# Taming the weld

[TARİH: 01.01.2026 The Fabricator]

Fixturing Strategy

Checklists for robotic welding success

By

Santhosh "Sam" Kumar Loganathan

The author reviews a weld program on the teach pendants.

Images: Triple Crown Trailers

O

n Monday morning the gates looked straight. By Wednesday afternoon, they didn’t. Operators at our Ocala, Fla., shop were prying on members with bars, stacking shims in a hurry, and calling for quality control (QC) every other pallet. The rework cart never had time to cool. We’d invested in a new robotic cell for the main gate frames that went on to our car and commercial trailer products. Sure, the cycle time dropped, but geometry drift stayed stubborn, like a bubble under wallpaper.

"Maybe we just need to tweak the program," someone said.

We tried. The bubble moved.

That week taught us something simple and painful: We hadn’t bought a robot problem; we had a system problem. The cell would never be predictable until part presentation, heat, code, and habit worked together. This is the story of how we turned the corner, and the checklists we built so we wouldn’t lose the thread.

WHY ROBOTIC WELDING?

Our management team at Triple Crown Trailers didn’t want to use robotic welding for its own sake. Sure, marketing shots of a robotic weld cell look good on our website as they create our various car- and utility-trailer products. But if they didn’t make the most of our welding talent and increase overall throughput, what would be the point?

We saw an opportunity for robots to weld the frames for the main trailer gates (see

Figures 1

and

2

). The repetitive welds took a lot of time and didn’t make best use of our skilled welders.

For the same reason, we also wanted to avoid relying on fixtures that required tack welds. Our welders wanted to weld, not tack all day. And besides, the cycle time that tack welding added would reduce overall throughput. If robotic welding prolonged the overall cycle time and increased labor requirements, why not weld the frames manually?

On the other hand, if we could design our fixtures and weld processes so that workers could simply load products into the fixture, initiate the program, and offload welded components, throughput would rise—which, of course, is the entire point of process automation.

The rectangular tubes in this application are fixtured in the as-received condition, with no in-house weld prep. Our tube supplier sawcuts them at 90 degrees (no bevel) and sends them to us, which we then inspect, stage, and fixture for robotic welding.

We relied on teach-pendant programming and didn’t have the benefit of offline weld process simulation. In retrospect, we might have benefited from offline simulation, but regardless, after some hard lessons learned, we prevailed.

ESTABLISH THE BASELINE

As a first step, we stopped guessing, tweaking the robot program, and guessing again, only to have QC continually send rework back to the weld cell. Instead, we spent a full week measuring. Sheets and tubes were tagged as they arrived. Joint gaps were mapped with photos and sticky notes. We kept track of the clamp-unclamp times and logged every rework mode: incomplete fusion here, an undercut there.

Two findings changed everything. First, the fixture was arguing with physics; it held parts so perfectly that there was no room for thermal growth. Second, our weld sequence fought our own geometry. We pulled long members toward the hot side and never let them relax.

The robot wasn’t the problem; it was us, faithfully repeating our mistakes. To avoid repeating past mistakes, we developed a checklist to go through before making any changes to the robot program.

We recorded any incoming material variation.

This included the square tube’s straightness, edge prep (the saw cut quality), as well as the radii of the tube’s outside corners. Every tube received from the mill has a tolerance that we needed to account for in the robot cell.

We mapped fit-up tolerance stackup

by joint family and marked where people "made it fit."

We categorized the weld defects,

be it porosity, undercut, incomplete penetration, or anything else.

We timed the non-arc tasks,

including clamping, unclamping, and part repositioning.

We photographed and tagged all the hot spots,

or areas where visual weld examination revealed we had significant heat input.

FIGURE 1

The main trailer gate consisted of a rectangular tube assembly. Each tube was saw-cut and delivered to us in specific lengths.

FIGURE 2

The tube-to-tube connection on the trailer gate created a joint with an open root. Operators inspect components for consistency, including the outside dimension, wall thickness, and the radius of each of the square tube’s four corners. Any change affects the joint geometry.

FIGURE 3

This fixture holds axle components, not the trailer gate frame, but it illustrates the datum logic we use. The blue is the primary datum, which never moves. Every other clamp point (in gray) has a direct path to it. If you find a problem, you relate it back to the primary datum, which helps uncover the root cause of positional error.

All this gave us a baseline. We now had the information we needed to stop guessing and start improving.

FIXTURES THAT RESPECT HEAT

We found that any fixture we used needed to respect the reality of thermal distortion. Our first fixture "improvement" was basically a vise, which really just over-constrained the part. Our welded gate products left the fixture looking perfect, but they curled on the cart 10 minutes later. The fixture hid reality.

Next, we rebuilt around 3-2-1 datum logic. This fundamental fixturing principle involves locating parts on the primary (1), secondary (2), and tertiary (3) planes (see

Figure 3

). The primary locating plane (datum) is your baseline, and every component within the fixture should have a direct relationship to it. A fixture can have dozens of components, and the last thing you want is for one component to become "trapped"—that is, have multiple other components blocking that direct path to the primary datum. This makes it next to impossible to uncover the root cause behind errors.

The bottom line: The welding robot didn’t save us; engineering the system did. The robot just makes the decisions we make repeatable.

On our new fixture, locators forced correct presentation; clamps allowed a controlled slide as heat accumulated. We designed go/no-go features into the fixture, so a wrong load was obvious

before

the arc started. For the entire gate family, we added swappable locators for easy changeovers between different variants in the product family.

The first setup we tested told us we were close—less persuasion with bars, fewer "hold here while I tack that" moments. And from all this, we developed the following checklist:

Call out primary, secondary, and tertiary datums

on the print.

Leave a degree of freedom

where thermal growth needs to go.

Build mistake-proofing

(poka-yoke) and go/no-go points into the fixture.

Plan access

(torch angles, cable sweep, reamer reach).

Standardize wear items;

put replacement intervals on the job traveler.

Use modular locators

for families to shorten changeover time.

SCHEDULE FOR HEAT

With presentation under control, distortion shrank but didn’t vanish. The last mile was heat discipline. We rewrote the weld sequence so the gate breathed. We alternated from one side to the other (see

Figure 4

). The welding gun moved from a point of restraint (that is, certain elements had to remain where they were) to points of freedom, where we accounted for movement from thermal growth.

We also stopped treating a giant fillet as a sign of craftsmanship. Instead, we qualified the

smallest bead

that met the weld requirements (see

Figure 5

) and added interpass windows and dwell times to our digital work instructions. We didn’t want to rely on tribal memory. Everything was on screen.

FIGURE 4

This trailer undercarriage is still manually welded, but it helps illustrate the need for alternating the weld sequence to account for distortion in long members. When a welder finishes a connection on one side of the frame, he then moves to the other side. The same logic applies to robotic welding.

FIGURE 5

We qualified the smallest bead that could meet weld requirements and stopped over-welding.

The next eight-hour run felt unremarkable. The robot welded and parts shipped. No fuss. No drama. That was the point. And from all this, we developed another checklist, this one for controlling distortion and finding the optimal weld sequence.

Balance shrinkage with alternating passes;

plan to move from restraint to freedom.

Qualify the bead size per the weld requirements;

stop oversizing welds.

Set preheat and interpass limits

for critical joints as necessary, and actually measure them.

Build cool-down into the routine

where geometry demands it.

Verify straightness on the cart,

not just in the fixture.

Note that we wrote this (and all of our checklists) to serve as a baseline for current and future robotic welding work. For instance, our gate part family didn’t require any preheating, but we knew that some products could require it, so we documented it for future reference.

We also wrote a "sanity check" list, to ensure we were inspecting and measuring the elements that mattered.

Pull the part hot

and check it on the cart.

Watch for sprung parts,

signs your fixture is masking growth.

Inspect locator wear.

A mushroomed pin is a new datum you didn’t plan for.

PROGRAM FOR THE REAL WORLD

Our first weld programs assumed perfect inputs. The real weld cell needed cushions to account for the real world. We added

fallback routines

where joints drifted most, so the welding gun could find the seam when variation crept in. For instance, we’d know that thermal growth from certain welds would force the assembly to drift in one direction by about one weld-wire diameter (0.045 in.). So at this point, instead of centering the gun position, the programmer would move the gun slightly over. Skilled welders account for this drift naturally; the robot just needs to be taught what to do.

We modeled not just clamps and locators, but also the welding gun dress pack that protects its cables and hoses; we needed the gun to avoid not only the part but also itself. And we tied program revisions to the part drawing and fixture IDs. Everything—the drawing, the robot code, the fixture—"moved" together. From all this, we developed a checklist for our robot weld programming and verification process:

Add joint finding/touch sequences

at known drift points to account for thermal growth.

Include clamps, locators, and cables

when modeling for reach collisions.

Validate angles/approaches

across real tolerance ranges.

Standardize consumables;

change by arc-time, not guesses.

Lock revision controls

across drawings, fixtures, programs, and digital work instructions.

START 2026 STRONG

888-770-0021

reliantfinishingsystems.com

Engineered for the Edge

Where Metal Meets Mastery

SHIPPING SUPPLY SPECIALISTS

QUALITY PRODUCTS YOU CAN TRUST

Huge Selection ALWAYS IN STOCK

Order by 6 PM for SAME DAY SHIPPING

14 North American Locations Mean SHIPPING SAVINGS and FAST DELIVERY

COMPLETE CATALOG

1-800-295-5510

uline.com

PROCEDURES PEOPLE ACTUALLY FOLLOW

We wrote welding procedure specifications (WPSs) and procedure qualification records (PQRs) so that they aligned to common practice, and then trained to the procedure, not to habit.

The first-piece check measured two or three critical datums at the cell using simple, rugged gauges.

Our digital work instructions showed clamp order, safety notes, and rev IDs on the screen next to the work. If a drawing changed, the job traveler changed.

Today, the operator who used to shim quietly to "make the fixture work" now is the person who finds missed locator wear points and other sources of variation.

Nobody asked, "Which version are we on?" From all this, we developed the following checklist for process control, to ensure our smooth operation

remained

a smooth operation.

Create WPSs/PQRs by joint family;

qualify on representative coupons.

Train and re-qualify

on a cadence.

Do first-piece checks at the station;

keep gauges simple.

Use digital work instructions

with clamp order, safety notes, inspection points, and rev ID.

Tie bill of materials, routing, drawing, digital work instructions, and welding robot programs

to one source of truth.

FOLLOW THE PHYSICS

After eight weeks, the data told us we were on the right path. Cycle efficiency climbed into the mid- 80% range—and stayed there. This level gave us the efficiency we needed while still leaving time to account for heat distortion. First-pass yield on critical datums stabilized, and distortion-driven rework fell by more than half.

Once all of our gate product families shared fixture logic and visual work instructions, changeover time dropped significantly. We kept tabs on our KPIs, including cycle time, rework rates, and changeover time measured from the fixture swap to the first good part.

What didn’t change? Steel still moved when heated. People still did what the system allowed.

And we couldn’t beat physics. We

followed

physics and, hence, made the process predictable. Instead of over-constraining the part, the new fixture design left one degree of freedom and let the sequence pull toward the clamps designed to absorb it. Once we let the part talk, it told us what it needed.

Today, the operator who used to shim quietly to "make the fixture work" now is the person who finds missed locator wear points and other sources of variation that the engineering team missed. For safety, maintenance now performs a weekly, 10-minute interlock check. And with comprehensive digital work instructions, a new hire can run the cell after just two days of training. The process details live on screen, not in someone’s head.

The bottom line: The welding robot didn’t save us; engineering the system did. The robot just makes the decisions we make repeatable.

Santhosh "Sam" Kumar Loganathan

is engineering director at Triple Crown Trailers,

www.triplecrowntrailers.com

.

THE TUNGSTEN ELECTRODE EXPERTS

DGP has been industry leader in tungsten and tungsten preparation since 1992. Visit our website to buy online from stock with same day shipping or call us for a free consultation today.

ARC SABER

TUNGSTEN STORAGE

REPLACEMENT

DIAMOND GRINDING WHEELS

PIRANHA

TUNGSTEN GRNDERS

WELDING

TORCHES & PARTS

RAW TUNGSTEN

INCLUDING NEW DGP TRI-MIX

MONSTER

TIG NOZZLE KITS

PRE & RE-GROUND

TUNGSTEN ELECTRODES

DIAMONDGROUND.COM

2651 Lavery Court • Newbury Park, CA • 91320 • 805.498.3837 •

sales@diamondground.com

FXE PERM-ELECTRO LIFT MAGNETS

Safely release with the push of a button

Ideal for lifting applications that require fast cycle times

No battery backup system required

Industrial Magnetics Inc.

imi@magnetics.com

PHONE: 1.888.582.0822

magnetics.com
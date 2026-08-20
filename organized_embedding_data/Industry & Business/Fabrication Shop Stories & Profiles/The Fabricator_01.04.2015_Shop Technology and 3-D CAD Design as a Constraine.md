# Shop Technology and 3-D CAD: Design as a Constrained Process

[TARİH: 01.04.2015 The Fabricator]

Precision Matters

Imagination plays a role in design, but so does practical fabrication

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

"H

ow many of your staff members are dedicated to DFM, design for manufacturability?

"

"Not many. Most are against it."

Hopefully, this dialogue about DFM struck you as a joke. While you’re in a good mood, please take a test. Study

Figure 1

. The challenge is to spot the problems in the design. (

Hint: There are more than a few

.)

Figure 1

This model satisfies many mechanical goals in terms of motion, but it fails when it comes to being buildable. How many problems do you see?

For example, the spring’s inside diameter is too small for the pin it is pressed onto. That is probably an unfair test question because the illustration makes close examination of this model difficult.

A more obvious problem is with the countersunk holes. One of them requires a very long shank on the countersink tool. The other requires an exotic, far-side countersinking whip or fabricating the part with some process other than milling.

Working With What We Have

As we dig through this atrocious example of design, we do so with a kind heart and in a helpful spirit. The pressures that led to this design stage must have been compelling. We do not seek to impugn the capability of the originator of the concept model.

Now is the time to transform a concept piece into a virtual prototype suitable for fabrication. We bring practical fabrication skills to merge with the vision for the product’s function.

Figure 2a

isolates a dowel and a lever. We have learned from our design goals that the dowel is supposed to press-fit into the hole. Interference Detection is a handy CAD tool to verify this.

The dowel and the lever have been selected in the Interference Detection Property Manager, shown to the left of the graphics window in Figure 2a. At the middle left, we see alarming results: There is no interference between the dowel and the lever. The dowel will fall out of the hole.

Figure 2a

The Interference Detection tool can be used to verify how a dowel fits into a hole. In this case, no interference means no press-fit.

A solution is shown in

Figure 2b

. The lever is being edited, and we see the Hole Wizard Property Manager. The hole for the dowel has been changed from a

drilled

hole to a

dowel

hole. All the designer needs to do is select the type of fit. In this case, the designer selects Press for fit with a 5-mm dowel.

The result is shown in

Figure 2c

. Again, the Interference Detection is set to check the dowel and the lever. We are pleased to see that the dowel will stick in the hole.

Figure 2b

If the CAD can do the work, let it! In this case, a wizard can be used for setting the hole size based on the kind of fit desired. Press-fit is our goal.

Figure 2c

The Interference Detection tool reports interference between the dowel and the lever. That’s desirable in a press-fit.

Hardware Captives

Figure 3a

shows the sheet metal bracket with captive hardware. Folks in the sheet metal trade will note at a glance that the stud is too close to the edge of the part. Perhaps more difficult to discover is the shank length of the captive nut. For this gauge of sheet metal, a shorter shank would be better. Editing the model to comply with the hardware manufacturer’s recommendation for sheet thickness and distance-to-edge corrects such design flaws.

Figure 3a

Captive hardware comes with recommendations for proper installation. This design fails to comply with those recommendations.

To goof-proof the captive hardware, one trick is shown in

Figure 3b

. In this example, a circle was sketched in the model to represent the minimum distance center-to-edge of sheet metal. The value of the sketched radius was determined by looking up the manufacturer’s recommendation.

Figure 3b

This sketch represents the minimum distance-to-edge for this fastener. It has been added to the fastener model and can be turned on/off when checking designs.

Returning to the sheet metal, we see in

Figure 3c

how the fastener was located. The good news is that we see the reference circle showing the goal of minimum distance to edge. The bad news is that the dimension to the center of the hole is from the edge of the sheet metal. If we change it now, the hole will move relative to the sheet metal bend. That’s not our goal.

To correct this, we change the dimension so it references the bend, then we change the sheet metal to surround the fastener’s hole correctly. The results are shown in

Figure 3d

. The center of the hole is controlled to match the location of the lever, and the edge of the sheet metal has been moved to extend at least to the reference sketch in the captive hardware.

Sheet Metal Gone Bad

How bad can one piece of sheet metal be? The captive nut shown in

Figure 4a

is hard to reach with tooling for swaging. It may need to be installed before the sheet metal is bent.

Also in Figure 4a we note a slot that appears to be very close to the edge of the sheet metal. This can be done, but probably requires laser cutting instead of stamping.

As optimizers for fabrication, all we can do at this stage is note some cost drivers in this component. Let’s give the sheet metal part a closer look.

Figures 4b

and

4c

reveal a substantial problem with the design. The slot cutout passes through two sheet metal flanges. Only one of those flanges can exist unless this part is welded or 3-D printed. As shown in Figure 4c, this design will not unfold because two tabs intersect.

(CAD hint: Using CAD to test the unfold/fold of the sheet metal model is an important part of DFM.)

Figure 3c

We see the sketched circle from Figure 3b. This shows that more sheet metal is needed. The center of the fastener should be dimensioned to the bend so that it does not move when the sheet metal grows.

Figure 3d

The 23.00 dimension has been changed from Figure 3c. We’ve also increased the size of the sheet metal to 28.588. The reference circle from Figure 3b is now completely in the good zone.

Figure 4a

Captive hardware must be squeezed from both sides for proper installation. This design makes that difficult. If this part is to be fabricated with a stamping process, the slot is too close to the edge of the sheet metal. The distance from the edge of the sheet metal should be at least equal to the material thickness.

Figure 4b

This sheet metal design has several problems. The worst problem is that it won’t unfold. Maybe the slot too close to the bend is just as bad as this overall design?

Figure 4c

When this part unfolds, two tabs unfold into the same space. This happens only in CAD and cannot be produced in metal.

Figure 4d

Instead of the impossible, change the design. Keep holes away from bends, and provide access for assembly tools. Verify that the new design unfolds properly.

Figure 4d

shows an improved version of the bracket. The impossible tab has been replaced with a mortise and tenon for welding.

(CAD hint: Aficionados of the brand of CAD being used here might appreciate the nuances of the tenon. To keep the sheet metal from intersecting itself, the mortise gets cut first, and then the extrude for the tenon passes into the mortise.)

This meets the design goal of stiffness. It turns out that the nasty slot was intended for a stiffening fastener and will no longer be needed.

Figure 4d also shows the relocation of mounting slots away from the bend. This gives the screw head a chance to sit flat. For that same screw, we’ve added a hole so a screw driver can get to the screw head.

The point of this sheet metal exercise is to demonstrate the designer’s need for a combination of 3-D modeling skills and an awareness of constraints of tooling and assembly. With more time and authority, one might improve this further by making more room for swaging the nut into the sheet metal, but that involves changes to the lever and bearings.

Figure 5a

A quick inspection of the machined base reveals several issues. Can you spot them all?

Figure 5b

Let the CAD do the proofreading! Here DFMXpress is used to spot issues with the machined design.

Figure 5c

After the design is changed to eliminate narrow gaps; thin, deep holes; and square blinds, the report card on the design is much better.

Chipmaker’s Blues

The base frame for this mechanism is shown in

Figure 5a

with a variety of easy-to-spot problems. The countersink access issue has been noted previously. The T-slot is modeled with square ends, which should change to allow a spinning cutter to carve the blind slot. For an experienced machinist, these problems are obvious. For someone who has never cleaned oily chips out of a sump, these considerations seem hard to assimilate.

Figure 5b

shows a report generated by the CAD software that automatically identifies design features that violate best practices in machining. This same tool works with sheet metal too. After appropriate edits to the design, fewer "violations" are encountered as shown in

Figure 5c

. Some red warnings remain, but they have to do with the depth of holes as a ratio to their diameter.

We bring practical fabrication skills to merge with the vision for the product’s function.

Purchasing Oddities

The bill of materials table is often used in the process of procuring items for the assembly. The BOM table can be used as a design checker too. In

Figure 6

we see that a 6-32 screw is being installed in an M4 tapped hole. As with the incorrect shank length on the captive nut, the solution is to change either the fastener or the part it is going into.

Figure 6

The design can be checked in many ways. In this ex- ample, a BOM table was used to spot a discrepancy between the threaded hole and screw specification.

It is good to catch these problems now, before the project commits to raw material. By using a combination of tools for visualization, measurement, and detection, we’ve moved this design from concept stage to almost ready for fabrication. What more could be needed?

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop.

Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.
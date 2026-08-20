# Shop Technology and 3-D CAD: Metal Marking

[TARİH: 01.01.2015 The Fabricator]

Precision Matters

A look at alternatives for embossing legends

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

I

n the December 2014 edition of this column, we demonstrated CAD techniques for modeling a set of A to Z-sized straight shank jobber length twist drills. The level of detail that went into

Figure 1

might seem extreme, but consider the future of 3-D printing. Instead of buying a drill bit, simply replicate it. Posterity will bless today’s diligent modeler.

Figure 1

A detailed model of a letter Z jobber length straight shank twist drill is shown.

This month we model a box for holding those bits. It’s called a drill index. But first we ponder why letter drill sizes are on drill charts.

Peter Stubs of Warrington, Lancashire, England, recorded the

Lancashire Round Wire Gauge Standard

around the year 1735. Letter designations were used for the larger sizes and number designations for the smaller sizes. Prior to Peter’s effort, the “number” corresponded to the number of forging draws through a reducing mandrel. Thus, a 6 rod (0.204 in. diameter) is smaller than a 1 rod (0.228 in. diameter) because it has been pulled through five more reducing stages.

Back in the day, each shop’s mandrel set represented a standard set of rods, or wires if you prefer, of copper. Stubs collected what he could find around Birmingham, England, and averaged the results. Today’s letter size straight shank twist drills match Stubs’ wire gauge tables. There’s a factoid to impress your spouse!

Back to the Modeling

We could have modeled a number drill index instead of a letter drill index, but the rebuild time for the model with just 26 bits is lengthy. The 97 twist drill models required for a number size drill index would require a speedy computer system or a very patient CAD jockey. Besides, the larger drill sizes are easier to see on the printed page.

When E.F. Huot patented his Indexed Drill Cabinet in 1933, it was a closed box with tilt-out panels. W.J. Huot improved the method of construction in 1951 and again in 1975. The model shown in

Figure 2

is based largely on his design for the stamped axle hinges and bent-tab assembly of the index cards into the “cabinet.”

Figure 2

Here is a collection of drill bits in an assembly of sheet metal parts.

Having some experience with this product, we know that drill bits are sometimes installed upside down, thus creating sharp edges when a bit is pulled from its hole. We also know that closing the box can be vexing. But the stamping dies are made already. No operator’s manual is required. The design is not perfect, but it works.

As operators of 3-D CAD, we are interested in the CAD challenges this product represents. We note several sheet metal features: extruded round flange holes, embossed lettering, lid snaps, and single-piece hinges.

For the completed 3-D model, we’d like the door to open and the index cards with drills to tilt out. We also would like to examine individual drill bits, perhaps individual pieces of the cabinet. The general approach is to mimic the method of manufacture. It is an assembly of several sheet metal parts.

To spur excitement, for part marking we will use cut-extrude, indent, or forming tool, depending upon how closely we need to reverse-engineer the detail. (The copy editor raised an eyebrow at

excitement

, but let it pass.)

The main enclosure of the cabinet is shown in

Figure 3

. Most of this 24-gauge (0.024-in.) sheet metal is easy to model with base flange, edge flange, and hem tools. A slightly tricky bit is the four spot weld tabs. A slight gap must be kept in the weld interface to allow the sheet metal auto-unfold, even when the real part will have no gap.

The hem tool was used to create the hinge loops. These hinges are only partially formed prior to installing the lid. With the lid in position, the hinges are swaged into the tubes shown.

Similarly, the tabs are shown as

shipped

versus

as stamped

. Off the press, these are simple stamped L tabs. When the hinge frame is assembled into position, these tabs are hammered flat—as in folded over with your pinky—to lock the frame in place. If we were in the business of manufacturing this item, we might create a configuration to show the L tabs and hinge tubes

as stamped

as well as

as assembled

.

Figure 3

Modeling sheet metal features includes use of forming tools for lanced tabs, hems for tube-hinges, and edge-flanges for spot weld tabs.

Making Your Mark

For marking the patent information, the actual item is embossed with a metal stamp. The bulge in the back wall of the cabinet is not modeled here. For expediency, this part marking was modeled as a simple cut-extrude. Here’s a tip: Use a construction line to help locate the sketched text.

Before moving on to the lid, we note that the box features an embossed lid latch. A forming tool was modeled to represent the interior of this stamped feature. When that forming tool is applied to the sheet metal face, the software takes care of updating the opposite surface, much like real sheet metal.

Forming tools have limitations to prevent modeling of impossible sheet metal features. For instance, you can’t have an inside radius smaller than zero.

Figure 4a

The embossed lettering is raised above the exterior of the lid. The lid features edge-snap, radiused corners, and slots for hinges.

Figure 4b

The strike-side of the emboss was modeled with the indent tool. For this simple sheet metal part, a cut-extrude would have served as well.

Figure 5

Forming tools were used to create the extruded flanges.

Figure 6

As shown on the left, three configurations are found in this part file. The A-K configuration is shown. Various features change from configuration to configuration to make it seem like three separate products.

The lid snap emboss is well-suited to a forming tool feature. The emphasis on gauge thickness is because of the impact it has on forming tools. As you may note, several models of forming tools were required for this project.

The lid is 22 gauge (0.030 in.) and, like the box, is pretty straightforward in terms of sheet metal modeling (see

Figure 4a

and

4b

). The corners of the flanges are rounded for safe handling.

Figure 7a

This assembly has six sheet metal components: pivot bracket, box, lid, and three index cards.

Figure 7b

This assembly has four components and three patterns.

To model the embossed “DRILL INDEX,” it was expedient to use a boss-extrude to raise the lettering and then add a slight radius to the faces of the letters to mimic the actual emboss. On the opposite side of the part, an indent feature was used to mimic the striking tool used to coin the lettering. This is not conventional wisdom when it comes to a sheet metal modeling technique, but the result does mimic the coining operation of the real world.

(Here is another caveat: One does not have accurate unfolding of the coined zones with this modeling method. We encourage you to download the model to study the derived sketch and merits of indent offset versus cut-extrude.)

The FMA logo emboss was created using a sketch picture to trace the outline of the logo. That sketch was derived to model the strike side and extruded to model the raised side.

Closing the Lid on this Project

The hinge frame shown in

Figure 5

for the index cards is 24 gauge (0.024 in.) in thickness. The extruded holes are modeled with forming tools; two forming tool models are required. The length of the extruded shanks matches the actual part, although the fractured and jagged edge is shown as perfect and smooth. The index card axles will nest inside these extruded holes.

The index card model has three configurations, one for each version of the panel. That is A-K, L-S, and T-Z. The A-K card is shown in

Figure 6

.

Here is another tip: The features that are unique to each configuration were grouped into folders in the Feature Manager. Many items are suppressed to keep the three index cards distinguished in the single CAD file. A design table is used to manage the suppression, as well as the size of configuration-dependent features.

Equations are used for calculating the size of the stamped flange’s interior. This could have been modeled with a forming tool, but a standard sheet metal flange was near at the time.

Each configuration of the card index has a sketch of points. These points are used to position the drill bit models.

The legends on the index cards were modeled as raised bosses. The necessary de-bosses on the interior to coin the raised lettering were not modeled. We hope you will complete the work on our behalf.

As shown in

Figure 7a

, an assembly is made of index cards, hinge frame, box, and lid. Then, another assembly is made with drill bits (see

Figure 7b

). This mimics the real world and is useful for bill of materials documentation.

For demonstration of kinematic motion, the assembly of the sheet metal is great for tilting cards and closing the lid. To slide drill bits, we either need to make the top-level assembly flexible or edit-in-place the sheet metal assembly.

Rather than insert the drill bit model into the assembly 26 times, it is inserted once for each of the three index cards. Each card is populated to match the configuration-dependent pattern of

sockets

.

Figure 8a

Create a sketch with one point for each copy and then create a pattern.

Figure 8b

Make each instance of the pattern unique by changing its specific configuration.

Figure 9

The model is useful for illustrations and demonstrations. Maybe someday you’ll send the author a printed version.

To demonstrate, in order to populate the T-Z index card with drill bits, one drill bit model was inserted into the assembly and mated in place. Its properties were set to select its proper size. Then a sketch-driven pattern of that drill bit was created (see

Figure 8a

). Recall the configuration-specific sketch pattern created in the index card model.

The members of that pattern were then edited to set their properties to select the correct drill bit size. The process is simple: Click on component, select configuration, and click OK (see

Figure 8b

). The rebuild time for the drill bit slows the process, however. Be patient or get a fast computer. Perhaps a selling point of this technique is that the sketch-driven pattern allows you to resize the index card and have the drill bits remain in their holes.

Keep in mind that there are many ways to model. The techniques demonstrated here might be useful for reference.

The result is a model—

Figure 9

—that might be handy in a dramatic design presentation. Perhaps in a short while it will be fodder for replication.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. Please send your questions and comments to

dand@thefabricator.com

.
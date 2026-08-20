# Design for function before design for manufacturability

[TARİH: 01.09.2025 The Fabricator]

Precision Matters

The best design results occur with clear understanding of the design goals

GERALD DAVIS

T

he CAD model shown in

Figure 1

is an example of a design for mounting components in an electronic assembly. An exploded view is shown to the left of the completed assembly. This project is offered for review of the confluence between design for function (DFF) and design for manufacturability (DFM).

The lower sheet metal bracket has four captive threaded spacers. A critical design goal is to have their location match the mounting holes in the printed circuit board (an SD card reader). This lower sheet metal bracket also features an edge-flange with a pair of mounting slots.

The purpose of the upper sheet metal bracket is to mount an off-the-shelf cable. Not only must it match the mounting holes in the cable, the location of the captive fasteners in the lower sheet metal bracket are also a critical constraint. In other words, the mounting holes in the SD card reader control the location of the screws.

An Automatic BOM Is the Bomb

Figure 2

shows a 2D drawing that lists procurement information for each of the items in the assembly. Mainstream 3D CAD uses the 3D model to automatically populate such 2D documents and tables. Some data entry (typing of text) is required for description, tolerance, and other product manufacturing information. However, once that typing is finished, the completion of the BOM table is handled by the software.

Reviewers may note that the exploded view on this 2D drawing has helpful lines showing the connection path for screws, as well as balloons in the exploded view that correspond to the item in the bill of materials (BOM) table. For example, the upper bracket is identified with balloon No. 3 and is the third item in the BOM table.

In overall appearance, the drafting on this sheet is well done. The components in the exploded view are not overlapping and are positioned in a logical manner. This drawing passes review.

Figure 3

presents the 2D drawing file for the upper sheet metal bracket as it appears on a CAD monitor—in full color—whereas Figure 2 is showing a black and white PDF. Our CAD shop uses layers in drawings to control colors. Dimensions are on the DIM layer, and all things on that layer are blue, simply to make it easier to scan. As part of the review, we note that all dimensions and text appear to be in the correct layers, per our internal standard.

The Best Modeling Technique: Get It Done

Let’s take a peek at what the CAD jockey was thinking during the design of the upper bracket. The layout of the illustration in

Figure 4

shows the Feature Manager to the left and the Graphics Window to the right. The 3D model is presented within the Graphics Window.

As the 3D model progresses (as the roll-back bar is moved forward), existing CAD features in the Feature Manager are added to the 3D model. The roll-back bar controls the end-of-time for the Feature Manager.

Figure 4 has the list of CAD features rolled back in time so that only the first few modeling events have occurred. At this point, holes are modeled in a flat flange to match the mounting features on the cable. This may not be the best place to start this model, but it gets the job done. It is often easier to see a better way to model a project once some way has been found. That’s a reason to postpone until the DFF is completed.

In

Figure 5

, more of the required sheet metal design activities have occurred. A sheet metal flange is added to the starting flange; the sketch for that flange was edited to create the profile shown. The Hole Wizard is used to add clearance holes for an M3 screw (pattern aligned with the mounting standoffs in the lower sheet metal).

The connector would now mount in an OK manner, but its body would interfere with the SD card. So, in

Figure 6

, a jog bend has been added to move connector mounting away from the SD card.

As a sheet metal modeling CAD tool, jog bends are named after actual tooling found in a sheet metal production line—jog tooling—which creates a pair of bends (a Z jog) with one machine stroke cycle.

Fold-Unfold Are Flat-Out Handy

The design problem now is that the cable on the connector is obstructed by the vertical wall of the jog bend. In

Figure 7

, the Unfold tool has been applied to flatten the part. All of the bends are unfolded. This unfolding operation is in preparation for adding a cut to clear the cable that will span across a sheet metal bend.

FIGURE 1

An assembly is shown exploded (to the left) and collapsed (to the right). The red arrow indicates where a screwdriver will need access.

FIGURE 2

A black and white PDF—a 2D drawing—for the 3D assembly includes a BOM table that lists the procurement of the required components. The exploded view has balloons that correspond to rows in the BOM table.

FIGURE 3

A 2D drawing for the upper bracket is shown. On a CAD monitor, layers and colors can be used to make it easier to distinguish the part being made from the detailing of it.

FIGURE 4

The Feature Manager has a roll-back bar that sets the end-of-time for the 3D model shown in the Graphics Window. Here, the model is rolled back to the starting point—the mounting for the connector.

Sidebar: Sheet metal in 3D CAD behaves similarly to actual sheet metal—bending causes a change in length. Outside dimensions will stretch, and inside dimensions will compress. There are well-known k-factors used by the CAD software that accurately predict that behavior. Here, the bends in our model are accurately unfolded.

With the part in the flat condition (see

Figure 8

), a slot to clear the connector cable is added. The slot was chosen and sized simply for gentle radius in close contact with the plastic cable. Some material also was removed to gain screwdriver access. See the right-hand view in Figure 1.

Stress-Free PMI

After refolding the part—

Figure 9

—the sharp corners on the part are radiused. This is both for safe handling and to remove stress risers that might (should the bracket be subject to vibration or heavy stress) cause cracking.

We also note, to the right in Figure 9, that data entry has been completed. Product manufacturing information—material, finish, revision, and so forth—is added using the Custom Properties Tab that we set up for our CAD department. This information appears in the title block on the 2D drawing.

FIGURE 5

An edge-flange is added to the starting flange. The sketch for the new flange has been edited to include the slots and profile shown.

FIGURE 6

A jog bend is added to move the connector away from the SD card, but there is a problem. The connector has a cable that must pass through the jog.

FIGURE 7

In preparation for cutting a hole for the cable pass-through, the part is flattened. This makes it easier to cut across a bend.

FIGURE 8

Cuts are added to the flattened part for the cable and for screwdriver access (see Figure 1).

FIGURE 9

The part is refolded. Then the sharp corners get treatment for safe handling and to remove stress risers that might crack during vibration.

It is often easier to see a better way to model a project once some way has been found. That’s a reason to postpone design for manufacturability until the design for function is completed.

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Multi-articulated spot welder

,

Perfect for fabricating Cabinets

Clean

Easy

No Training

MYSPOT makes it possible for anyone to perform welding with the same high quality, no burn marks or distortion. MYSPOT saves our operators from manhandling bulky items - the copper tabletop acts as a work bench whilst welding. This process requires far less man-hours than traditional welding and is very effective in high volume production applications.

Visit us #A3202(International Technologies, Inc.) at FABTECH2025

BETENBENDER Manufacturing, Inc.

MADE IN THE USA WITH PRIDE & DURABILITY

Family Owned & Operated Since 1972 Hydraulic Shears, Press Brakes & C-Frame Presses

VISIT US AT

BOOTH #A3113 Sept 8-11th, 2025 Chicago, IL

Hydraulic Shears:

1/8″ (10GA), 3/16″, 1/4″, 3/8″, 1/2″, 5/8″, 1″, & 1-1/4″

Press Brakes:

50-Ton to 550-Ton

C-Frame Presses:

40-Ton to 200-Ton

Retrofit Backguages:

for Shears & Press Brakes, Made to fit most machines with minimum modifications

Precision Knife Sharpening:

up to 12″

Custom Designs:

for custom applications

WWW.BETENBENDER.COM

Phone: 319-435-2378 Fax: 319-435-2262

sales@betenbender.com
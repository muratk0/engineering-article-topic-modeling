# Shop technology and 3-D CAD: Technique and ramifications

[TARİH: 01.02.2014 The Fabricator]

PRECISION MATTERS

Sometimes taking the basic approach to design might make sense

By Gerald Davis, Contributing Writer

Gerald Davis is a job shop consultant and chairman of the board of DSM Manufacturing Co.,

gerald@glddesigns.com

.

In this edition of Precision Matters, our example design goal is to model a flat metal cover with six holes in it. The holes are to be in a symmetrical pattern around the cover’s perimeter. Consider a CAD technique that uses sketch relations in preference over dimensions.

Figure 1a is a screen shot of a completely constrained sketch that will become the pattern of holes in the cover. Only one dimension is found in the sketch, and it sets the diameter of a circle. That circle has a sketch point that is coincident with its center. Wherever the circle goes, that sketch point will travel with it. Note that the circle serves as construction geometry in this sketch. It may be hard to see in the illustration, but the circle is drawn with a dashed line.

Figure 1a This sketch has only one dimension to control—the location of all six sketch points. Sketch relationships are used to fully constrain the sketch.

The circle has sketch relationships that make it tangent to two lines—one horizontal and one vertical. The result is that the circle is fully defined; that is to say, it cannot accidentally move in 3-D space. The other five sketch points also have sketch relationships relative to the circle’s center. If the circle’s diameter is changed, the six sketch points will be adjusted relative to the part’s edge.

The construction line in the middle of the sketch plays a major role in eliminating the need for dimensions in this sketch. The construction line’s midpoint is constrained to the cover’s center. (In this case it happens also to be the origin of the model.) This construction line also is constrained to be horizontal. To fully define this line, its right endpoint is constrained as vertical to the circle’s center at the top right corner of Figure 1a.

Two sketch points are constrained to be coincident with one on each end of the construction line. This completes the description of how three of the six holes are fully located. The sketch point at the top left corner in Figure 1a is constrained horizontally to the center of the circle and vertically to the endpoint of the construction line.

The remaining two sketch points at the bottom are mirrored copies using the horizontal construction line and the top two sketch points. That fully defines all six sketch points. The resulting pattern of holes is shown in Figure 1b.

Figure 1b The sketch from Figure 1a was used to create this pattern of holes.

Use of sketch tools (for example, Dynamic Mirror) will both speed the drawing effort and automatically create the sketch relationships. Going a step further, saving commonly used patterns of holes as library features could both speed the future modeling and standardize the techniques used.

How Good Is Dimensionless CAD?

What are the merits of this “dimensionless” CAD approach? We’d like to emphasize two possibilities.

Sketch relationships (horizontal, vertical, tangent, coincident, parallel, etc.) within the sketch are faster for the CPU to solve than dimensioned relationships. Minimizing the number of entities in the sketch also helps the CPU. If this model is used once, then that bit of elegance is only a trifle of goodness. On the other hand, if it appears many times in a complex assembly, then CPU cycles begin to add up.

Second, this sketch is both faithful to the design intent and is easy to edit. While it may have taken a few moments longer to set up initially, the future CAD edits to this model could benefit from double-click to edit and click to rebuild; the revision is then complete.

Perhaps not all is swell with this tricky bit of “hidden” magic. On one hand, the future CAD jockey who looks at Figure 1a might not be familiar with the meaning of all of the little green icons in the sketch. On the other hand, dimensions are intuitive for almost all CAD jockeys. Figure 1c shows a similar sketch that has no sketch relationships other than dimensions. It should not require much study to understand how each of the six points is constrained; that could be of great benefit to the next person to edit this model.

Figure 1c Dimensions are used exclusively to fully constrain this sketch. No “hidden” sketch relationships are used. To do it this way is a simple but laborious process.

Stay in Formation

Changing subjects slightly, sketch relationships can be made with features that exist outside of the sketch. Consider the assembly shown in Figure 2a. The design goal is for the three holes in the side bracket to align with the three holes in the cover.

Figure 2a The location of the holes in the side bracket can be constrained with sketch relationships to the location of the holes in the cover. The side bracket and cover parts are located (mated) relative to each other in an assembly file. All three files (assembly, cover, and side bracket) are required for reliable CAD editing.

A common CAD technique is to create parametric features. In other words, edit the side bracket in the context of the assembly with the cover. In this example, while editing the sketch for the pattern of three holes, the CAD jockey constrains the sketch points to be concentric with the corresponding holes in the cover. The diameter of the construction circle in Figure 1a also would control the location of the three holes in the side bracket.

The obvious merits of the parametric technique are:

1. Certainty that the holes will always be modeled in alignment.

2. Convenience of editing in the future.

The ramifications include the need for three files in order to edit the side bracket in a reliable environment. If the CAD jockey has only the side bracket part available for editing, the external relationships to the holes in the cover will be dangling. Even if the CAD jockey has both the cover and the side bracket, without the assembly file that constrains the cover to the side bracket, the sketch relationships continue to dangle. If the CAD jockey creates a new assembly of the cover and side bracket, the sketch relationships will dangle because they are looking for the original assembly context in which they were created.

Which Is Better: Faster or Slower?

As a side note, the use of sketch-driven patterns of features is a great time-saver for the CAD jockey. The pattern of countersunk holes in the side bracket shown in Figure 2b was created from Figure 2a with just a few mouse clicks.

Figure 2b A sketch of sketch points can be used to drive a pattern of features. This pattern of countersunk holes is driven by a sketch. This example was created using a Hole Wizard tool in the software. This approach makes it easy to switch among tapped, countersunk, counterbored, and simple holes.

The ramifications of using patterns of holes include convenience of editing and a handy pattern feature when adding models of bolts and nuts to the assembly, which helps to save time. The CAD system used in support of this article includes a built-in Hole Wizard that makes patterns of holes in a quick and convenient process.

Figure 3a shows a pattern of slots. The CAD technique used is a three-step process:

Figure 3a This pattern of slots was made by modeling a single slot as well as creating a sketch containing sketch points located where the slots are to be. This approach is similar to the Hole Wizard in results, but allows you to model a pattern of any shape cutout.

1. Create a sketch that has sketch points in it.

2. Create the feature to pattern.

3. Create a sketch-driven pattern of that feature.

While this is somewhat more laborious than using the built-in Hole Wizard, it allows you to model a pattern of almost any shape feature (not just round cutouts) and still gives you a handy pattern feature for use in assemblies.

Figure 3b shows one set of fasteners installed in our example assembly. The design goal is to populate all three locations with this hardware. The most laborious CAD method would be to repeat the same process two more times. That process involves a lot of mouse clicks: Insert a washer, mate the washer coincident with the side bracket, mate the washer concentric with the hole in the cover, insert a nut, mate it (twice), and insert a screw and mate it (twice). That’s a lot of tedious work!

Figure 3b This illustration shows an assembly of a nut, washer, and screw. The design goal is to install this hardware in every slot.

Figure 3c shows a pattern of the hardware items based on the sketch-driven pattern of slots. The location of the slots is driven by the location of the holes in the lid. The holes in the lid are controlled with a single dimension adjustment, which controls the distance from the edge of the cover.

Figure 3c This pattern of hardware was easy to create: Select the hardware, select the feature-driven pattern tool, click on one of the patterned slots, and wow! All of the hardware is installed. Also, it will follow any edits to the location of the slots (in this example).

Looking back at Figure 3b, note that the slot in the side bracket has one end centered on the hole in the lid. That limits the range of adjustment of the slot. In Figure 4a the end of the slot in the side bracket has been dimensioned relative to the hole’s center in the cover. The side bracket can now move ±0.25 in. relative to the cover. As a CAD technique, parametric links can be made with dimensions as well as constraints to points and edges. This is a handy technique for building manufacturing tolerances into the design.

Figure 4a External relations include dimensions as well as hard constraints like coincident, horizontal, and tangent. This is a handy method of building in tolerances for manufacturing.

Design for Manufacturing—Don’t Keep Secrets

Here’s some “pierceless” advice: Compare the cutouts shown in Figure 3a to the holes shown in Figure 2a. If the side bracket was to be fabricated using a laser or waterjet, which design would be “better” for manufacturing? To the extent that piercing is slow and messy, Figure 2a has a lot more piercing than Figure 3a.

Figure 4b shows the benefits of captured-by-the-bolt when piercing is eliminated. Figure 4c shows the idea in an example assembly. This is a design-for-manufacturing tip that not all product designers are aware of. It is OK with us if you pass this article around to your customers.

Figure 4c This example assembly shows a feature-driven pattern of hardware installed in process-optimized cutouts that are parametrically driven within an assembly. Oh, this is so engineered!

Figure 4b Patterns can include shapes like this one. Not a hole and not a slot, it is faster for a laser to cut than a simple hole. Design for manufacturing includes tips for time-savers like this one.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

.

Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

dand@thefabricator.com

.
# Mind the gap when modeling interlocking features

[TARİH: 01.05.2026 The Fabricator]

Precision Matters

Exploring ways to create a gap for fabrication tolerance

By

Gerald Davis

FIGURE 1

Interlocking fingers allow two panels to be joined with a friction fit. A sketch can be used in different ways to model the trapezoidal tabs.

FIGURE 2

Just three steps are needed to create a sketch of a wiggly line. In doing so, a sketch block is patterned and constrained so the edges of interlocked panels align.

FIGURE 3

Insert>Features>Split is a tool that splits a single body into several (or two in this example). Here, the Split tool is also saving the bodies into files. Note that this trick results in zero gap between parts. It’s a very snug fit.

FIGURE 4

A gap allows for easier fit between panels. The tolerance gap can be made with a Cut-Extrude (on the left) and by offsetting the sketch used earlier for Split, or the gap could be made with Insert>Face>Move (shown on the right). The result is mechanically the same.

I

n the process of modeling the interlocking fingers in

Figure 1

, a variety of CAD tools were used, including Make Block, Sketch Pattern, and Split. To create a gap for fabrication tolerance, we will compare the merits of using a Cut-Extrude rather than a Face-Move.

Figure 2

shows a sequence of three steps used to create the wiggly sketch. The first step is to sketch one of the fingers and then make a block from that sketch. Note that two of the dimensions in that sketch (the trapezoid’s wide and narrow size) will be useful in creating a linear pattern.

With the sketch block completed, the second step is to add a linear pattern of blocks. The interval distance for the pattern is the sum of the previously mentioned pair of dimensions from the trapezoid. By checking the Dimension Y spacing box, the accidental dragging of the pattern with the mouse is avoided.

The third step is driven by the desire to print two of these panels and lock them together. Symmetry in the wiggly line is key to keeping the edges of the assembly looking nice. Here, a horizontal construction line is attached to the midpoint of the panel, and two points that are vertical to each other are made to be symmetric about the construction line.

To verify the symmetry (or as an alternative to adding the sketch relationship), a pair of dimensions were added—in this example, 17.25 mm. Because of the symmetric relationship, these dimensions are set to be driven and are for show and tell only. The wiggly sketch now can be used to separate the panel into useful pieces. For those who read the previous episode of this column ("A conversation about sketches in 3D modeling," The Fabricator, April 2026, p. 24), the use of Insert>Features>Split will be familiar. Split uses a sketch to create multiple bodies. In

Figure 3

, it also is creating files from the bodies created. Only one of the two bodies is needed (if the symmetry trick worked), but saving them both turned out to be handy.

Note the inset of the wiggly line in Figure 3. There is zero gap between the two bodies. That might work for very soft materials, but a zero gap would be impractical in general because of tolerance requirements.

Instead of using the sketch to split the part, we modify the sketch for use in a Cut-Extrude. That will result in two bodies in the part. Right click on one of the bodies and select Insert into new part. The left-most view in

Figure 4

shows an assembly of two of those parts and their resulting gap. The CAD trick is to offset the wiggly line on both sides and cap it to create a loop. The amount of offset is half the amount of tolerance desired.

MOVING FACE FOR GAP

Instead of using a Cut-Extrude, let’s repurpose one of the pair of parts created earlier with the Split tool. With the zero-gap part open, use Insert>-Face>Move, select the tangent faces, and offset them 0.08 mm. The resulting gap from Face-Move is shown in the right-most view in Figure 4. It’s a result indistinguishable from the left-view’s use of the Cut-Extrude.

GERALD DAVIS

THEFABRICATOR.COM

› AUTHOR ›

GERALD-DAVIS

Gerald

would love for you to send him your comments and questions. Please send them to

ddavis@fmamfg.org

.
# A conversation about sketches in 3D modeling

[TARİH: 01.04.2026 The Fabricator]

Precision Matters

What makes sense? Re-use of existing work with derived sketches or re-use of consumed sketches?

By

Gerald Davis

FIGURE 1 A plan for the generation of a 3D STEP file from a 2D sketch. For this demonstration, a centerline sketch will control the shape of a 3D model. How that model is chopped (or not) controls what will be in the STEP file.

FIGURE 2 Insert reference geometry (a plane) at the endpoint of a segment of a path. Sketch a profile on that plane. Insert a sweep using the profile and selected segments for path. Repeat the following for all remaining sweeps: insert a plane as before, insert a derived sketch onto that plane, center the profile on the path, insert a sweep.

FIGURE 3 Replace Face is a way to fill in missing curves. Insert a surface where the curve should stop, replace the face (end of the sweep) with the surface. Then hide and ignore the surface body.

FIGURE 4 The sweeps resulted in bodies that need some DFM. A solution is to chop the intersecting bodies and re-combine them into useful bodies.

B

oba Fett needs help. He has a 2D sketch but needs a frame for a new range finder. For fabrication, a 3D STEP file would be more useful than a 2D centerline sketch. Export as STEP AP214, and you can include face properties and appearances.

Figure 1

presents our plan to create a 3D CAD model for easy export of a STEP file. On the left, we see Mr. Fett’s centerline path for raw material. The imagined raw material is to have a square profile. This led the author to the notion of modeling the raw material with sweeps instead of base extrudes.

A side note regarding the sketching of squares in general: The Shift key during mouse drag will (as of 2025) allow a square to be sketched instead of a rectangle.

In the middle of Figure 1, we see a 3D solid model of the frame. At this stage of modeling, it could be exported as a single-body 3D STEP file.

To the right in Figure 1 is an exploded view of a multibody version. This level of refinement allows export as multiple bodies—perhaps in a single STEP file.

The CAD model shown in Figure 1 has two configurations. One suppresses the combination of the bodies; the other does not. This distinguishes between single- or multibody versions when exporting the STEP file.

PLANNING MAINLY ON THE PLANES

It bears repeating: Minimize the redundant.

Here, we apply that rule to sketches. Mr. Fett’s sketch will be used for defining paths for several sweeps. As a result of our behavior, various line segments in that one sketch will be consumed by several modeled features.

Not only that, our sketch for the profile will be reconsumed by deriving other sketches from it. Not really tricky, but derived sketches are convenient for sweeping, as we shall see.

What is a consumed sketch? When a feature, such as a sweep, is created, the necessary pair of sketches for profile and path are consumed by the sweep feature as it appears in the Feature Manager. That is to say, the Feature Manager organizes the consumed sketches as children of the sweep, visible only when the sweep’s feature history is expanded.

The consumed sketches remain available for creating other features. Here, we take advantage of that. Each time a path for a sweep is needed, the Selection Manager is used to select an appropriate group of lines found in Mr. Fett’s sketch. That sketch is consumed by the first sweep created.

A disadvantage of using one sketch in many features is that it may take another CAD jockey a moment to assimilate where the controlling sketch is and how many children it has, in case it needs editing.

An advantage of having only one sketch is that it makes sweeping changes to all of its children. (We just had to take the opportunity to make that swipe at punning!)

To prevent distortion due to odd projection, the profile sketch should be perpendicular to the path for the sweep. We do this by giving the profile sketch of each sweep its own plane located perfectly at the end of the path. We note that some of our paths start with curves; perpendicular is what a plane can do every time.

THE PLANE PLAN IN ACTION

Figure 2

illustrates a series of modeling events. The first event is insertion of a reference plane. Just the path and an endpoint of that path are required to create a new plane (Insert>Reference Geometry>Plane). The plane for a profile will have to exist before that profile’s sketch can exist. With the new plane selected, sketch the profile. In Figure 2, a dimensioned square is revealed. With the sketches for path and profile complete, the first sweep can be inserted.

A similar process (insert a plane at the endpoint of a path, make a profile on that plane, and then insert a sweep) is repeated for each of the other members of this design. The qualified difference in process is in how the profile sketch is derived.

Here’s a CAD tip: Expand the Feature Manager and show the sketches for the first sweep. That makes it easier to select line segments found in Mr. Fett’s drawing, as well as to see the dimensioned profile sketch for selection (reconsumption).

To derive a sketch, use the mouse to CTRL-select both the consumed profile sketch (found as a child of the first sweep) and the newly created profile plane. You can then select Insert>Derived Sketch (found within the menu system).

While inserting the derived sketch, use the mouse to position the sketch origin to be coincident with the path (or, in other words, center the profile on the endpoint of the path), and constrain its angle of orientation.

With the derived sketch for the profile fully constrained, the next sweep can be inserted. Please note: Do not merge these sweeps; uncheck the merge checkbox as these sweeps are created.

At the far left in

Figure 3

, we see the result of creating all required sweeps: a collection of bodies. The curved sweeps are incomplete because they share endpoints with neighbors.

To the right in Figure 3, Replace Face is just the right CAD tool to fix the problem. All it needs is a surface as destination and a face that wants to be there. The trick is Insert>Surface with an offset of zero. This action— insert surface, replace face—is repeated for the other missing curves.

Replace Face also is used to get rid of the extra horizontal bar artifact. The result is shown to the right in

Figure 4

: a collection of better bodies, but not quite ready for fabrication.

From left to right in Figure 4, there is a progressive shuffle of the perimeter of the bodies. The spoon intersects with the horizontal bar in the wrong direction. The bottom point should be on the vertical bar, not the curved one.

In the middle of Figure 4, the Intersect tool (Insert>Features>Intersect) is used to chop bodies wherever they intersect. The tool also has the option to remove bodies, so we do so. This leaves us about half done—with lots of little bodies.

The next step is to use the Combine tool (Insert>Feature>Combine) to merge the bitty bodies with design for manufacturing in mind.

Finally, the bodies are mirrored and given a final pass of Combine to get the finished fabricated brassy appearance (to the right in Figure 4).

To get better contrast between the welded bits, the Face Move tool was applied to the spoon. But you’d only notice that if you download the native CAD model.

GERALD DAVIS

THEFABRICATOR.COM

› AUTHOR ›

GERALD-DAVIS

Gerald

would love to hear your comments and questions. Please send them to

ddavis@fmamfg.org

.

A Business Built on Partnerships

Profile & Angle Roll Benders

Finishing Machines

Mandrel Tube Benders

J&S Machine, Inc.

Ph: 715-273-3376

E-mail:

sales@jsmachine.com

www.jsmachine.com

Machine Sales & Service

Since 1998

Tube Bending & Finishing Solutions

INTRODUCING TECOI SORTEC

LS Series Large

TECOI SORTEC

STOCKTEC LOADTEC ROBOTEC

IS Series Large Format Laser

THOR Thermal Cutting & Machining

FULLY AUTOMATED PLATE-TO-PALLET TECHNOLOGY

When you combine Sortec, Tecoi’s fully automated plate-to-pallet technology with either our LS Series Laser or THOR, both large format plate processing systems, you’ll elevate automated productivity to an entirely new level. Cont act Tecoi Advanced Plate Processing Systems today.

Tecoi USA, Longview, TX 75605

Call: (833) 878-3264

Web:

www.tecoiusa.com

Email:

sales@tecoiusa.com

Visit Us: NASCC Booth #3141

Service Centers Wind Power Machinery Oil & Gas Ship Yards Steel

Construction THERMA-TRON-X, INC.

Reverse Osmosis | Wastewater Treatment | Industrial Pretreatment Systems

ADVANCED WATER RECOVERY TECHNOLOGIES
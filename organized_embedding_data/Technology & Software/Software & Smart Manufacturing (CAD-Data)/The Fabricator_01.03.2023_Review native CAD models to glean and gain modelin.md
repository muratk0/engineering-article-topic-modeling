# Review native CAD models to glean and gain modeling technique

[TARİH: 01.03.2023 The Fabricator]

Precision Matters

A downloadable native CAD file offers learning opportunities not available in STEP files

By

Gerald Davis

For more content from

Gerald Davis

, visit

www.thefabricator.com/author/gerald-davis

.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

W

hen presenting and reviewing a design, props are often used to convey scale, operation, and feel. We introduced a tote box design using such props (hand tools) in August 2020 (see

Figure 1

).

To avoid excess labor on the part of the CAD jockey, such visual actors are often downloaded from sources such as

mcmaster.com

,

3dcontentcentral.com

, and

grabcad.com

. The author is familiar with these resources and values them greatly.

The model for aviation tin snips shown in

Figure 2A

was provided by Mark Gunn. He posted it way back in 2014 on

grabcad.com

. The 3D model is a faithful representation of an actual tool.

Figure 2B

shows the curved shape of the jaws. The same sldprt is used for both jaws, just as an actual product might.

FIGURE 1

Props help to convey the use and scale of a design. For example, this tote box for hand tools was created for a prop discussion in 2020.

FIGURE 2A

Fellow CAD jockey Mark Gunn posted this model for aviation tin snips on

grabcad.com

. It is very realistic and useful as a prop.

FIGURE 2B

The jaws are modeled with realistic curves, very faithful to an actual set of tin snips.

FIGURE 2C

The jaws are fully detailed, including a serrated edge.

FIGURE 2D

To add to the realism, Gunn modeled a torque spring. The CAD model includes mates to allow the lock and jaws to be positioned.

Figure 2C

is a close-up of the serrated cutting edge. Gunn made the effort to add nearly complete detail to the model—not just with the jaws and handles, but with the torque spring as well. The spring appears in

Figure 2D

.

Gunn’s tin snip model could be downloaded as a STEP file and imported as a dumb model into Solid-Works or other brands of 3D CAD. Textures and kinematics would be lost. Thus, here’s the part of the pitch for native CAD files.

The imported STEP might serve immediately as a prop, albeit gray and stiff. With just a little extra work, textures (see Figure 2C) and kinematics could be added to the import. In contrast to importing STEP or IGS files, downloading the native CAD is sometimes advantageous.

Gunn’s tin snips are lovely, and as inspiration for this article,

grabcad.com

doesn’t mind offering native CAD files for any (old or new) version. In contrast, some other download libraries restrict the downloads to current versions of the CAD.

Gunn’s aviation tin snip model, when opened in the SolidWorks, arrives with its components mated. These mates allow a mouse-drag to open the lock and operate the jaw mechanism—full kinematic motion. As a prop model being used to illustrate a design, realistic posing is part of its charm.

FIGURE 3

A Boundary-Cut is used to form the outside curve of the jaw. The profile sketch has the critical curve; the line segments simply close the loop. An existing edge is available in the model, so Gunn didn’t have to create a separate sketch for a path.

FIGURE 4

The Cut-Loft tool is used to create a clearance pocket on the blade side of the jaw.

FIGURE 5

The 100 teeth along the serrated edge are from a Curve-Driven pattern. An available edge in the model was used for the curve-path, avoiding the need for a separately sketched path.

FIGURE 6A

The torque spring is modeled using an Extruded-Sweep. The path for the sweep is created with a helical curve and two 2D sketches.

FIGURE 6B

To create a path for the Extruded-Sweep, three sketches are combined into one curve with the Composite-Curve tool.

To avoid excess labor on the part of the CAD jockey, such visual actors are often downloaded from sources such as

mcmaster.com

,

3dcontentcentral.com

, and

grabcad.com

. The author is familiar with these resources and values them greatly.

Perhaps as a study in overmolded plastic or as an example of a levered hand tool mechanism, this downloaded model has other uses to the designer-jockey. As a CAD jockey, the model is useful as a training exercise: It demonstrates several efficient modeling techniques.

In

Figure 3

, we see Gunn’s use of the Boundary-Cut tool. Similar to a Swept-Cut, the Boundary-Cut uses a profile sketch and a path. In this example, an available edge is used as the path. The profile has the curve that defines the outside of the jaw.

The jaw’s casting has a relief pocket on the cutting side of the blade. To model that, Gunn used a Cut-Loft (see

Figure 4

). The profiles, as sketched, match the draft of the casting intended for mold release.

To create the 100 teeth along the serrated edge, a Curve-Driven pattern of a single Cut-Extrude does the job (see

Figure 5

). A separate sketch could have been used for the curve, but when a curve in a feature is available, skipping the sketch is an efficient technique.

We spring to the topic of a bent wire in

Figure 6A

. Gunn created a model of a torque spring by sketching a circle and using the Helix-Spiral tool to define a curve for the centerline path of the coil.

The endpoints of that helical curve serve two purposes:

They are used to define a plane for a 2D sketch of a leg.

They provide external references for the starting points of the 2D sketches for the centerline paths of the legs.

With sketches for the coil and two legs complete, Gunn combined the three into a single curve using the Composite-Curve tool (see

Figure 6B

). The result is used as a path in an Extruded-Sweep.

In preparation for sketching the profile of the spring, the right plane was offset to a vertex—an endpoint of the leg sketch (see

Figure 6C

). A circle was then sketched on that new plane, and with the path and profile sketches complete, the Extruded-Sweep tool was applied. The result is Figure 6A.

We could embellish Gunn’s work slightly. Note the ends of the spring in Figure 6A. They are nipped off at an angle. That angle is actually parallel to the right plane, not quite "faithful" as the rest of the model.

We edit Mark’s definition of the plane (see

Figure 6D

) to use a line segment and the end of that segment. The resulting sweep, in

Figure 6E

, has the ends of the spring perpendicular (i.e., normal) to the centerline of the wire.

I believe the wisdom and effort that goes into CAD modeling should be a legacy offered to peers. Gunn’s CAD technique of nearly a decade ago is still relevant, efficient, and worthy of emulation. The STEP file import workflow is speedy, but it strips away legacy. Huzzah to

grabcad.com

!

FIGURE 6C

The profile for the Extruded-Sweep needs a plane. That plane was created as an offset from the right plane and a vertex—a point in the sketch for the leg.

FIGURE 6D

As an alternative to Figure 6C, use a line segment and the endpoint of the segment to define a plane. This keeps the profile sketch for the Extruded-Sweep normal to the centerline path.

FIGURE 6E

Compared to Figure 6A, the ends of this Extruded-Sweep are more normal. (Pun intended!)

THERMA-TRON-X, INC.

Industrial Paint Finishing Systems

Your Best Finish Starts With Us!

Turn-Key Supplier

Material Handling Innovations

Heat Processing Solutions

Water and Wastewater Treatment Equipment

Customer Service and Spare Parts

www.ttxinc.com

I

sales@ttxinc.com

Drill All Day, Every Day

HMD920 Mag Drill

2.3/8″ Diameter × 3″ Depth

Hidden Motor Cord

3 Speed - 250 / 450 / 700 RPM

Use HSS or Carbide Cutters

100% Hougen Reliability

Available Accessories

Two Year Warranty

800-426-7818 SERVICE • INTEGRITY • RELIABILITY

HOUGEN.COM
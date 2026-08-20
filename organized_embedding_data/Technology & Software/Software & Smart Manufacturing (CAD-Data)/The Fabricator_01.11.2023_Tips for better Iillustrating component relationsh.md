# Tips for better Iillustrating component relationships in a 3D model

[TARİH: 01.11.2023 The Fabricator]

Precision Matters

Excellent Exploded Views lead to clearer drawings and warm feelings from the design team

Gerald Davis

E

xploded Views are useful for illustrating how components are related. To demonstrate the process of adding an Exploded View to an assembly and then adding Explode Steps to it, the assembly in

Figure 1

will be used.

Figure 1 shows our assembly after a new Exploded View is first added. An Explode Step is ready to be added.

Figure 2

shows the setup for the first Explode Step.

Here’s a CAD tip: Select various related items so they reposition as a group. In later steps, separate the parts in that group. This can be handy later when refining the Exploded Steps, as we shall see.

In Figure 2, a cover and two screws have been repositioned as a group.

Figure 3

shows the cover after it has been repositioned away from the group. Good progress is being made. The next step is to move the just-exposed O-ring.

The Joy of Repositioned Groups

In

Figure 4A

, the O-ring is easily positioned away from the machined block. Sadly, the cover obscures the O-ring’s best position. The cover must move, and the screws are in the way of the cover.

FIGURE 1 Exploded Views reside in an assembly and consist of Explode Steps. When a new Exploded View is created, it has no steps. No components have been repositioned.

FIGURE 2 As a CAD technique, create Explode Steps with groups of related parts. This will be useful later when refining the repositioning.

FIGURE 3 To separate the group—the cover from its screws—add a step to reposition the cover and leave the screws alone.

In

Figure 4B

, the first Explode Step is edited to reposition the entire group to properly reveal the O-ring. This is the end of the CAD tip regarding grouped Explode Steps. For this demonstration, five Explode Steps will almost complete the creation of an Exploded View.

Sometimes it is easier to select components for repositioning after rotating the view. In

Figure 5

, the model has been rotated for convenient selection and repositioning of a couple of O-rings.

Connecting the Dots

To complete the Exploded View, after the components are in the desired position, the addition of an Exploded Line Sketch helps the audience make the connection.

Figure 6A

shows the drop-down menu selection for an Exploded Line Sketch. Use this tool to create a 3D sketch of lines that connect the exploded components.

Figure 6B

shows the result of adding an Exploded Line Sketch. Use the tool to select components (and the direction of the lines). Please also note the custom point of view in Figure 6B. The model is currently viewed so that the components are all visible. The standard isometric projection of this model doesn’t do that.

Remembering the View

When a desired custom view should be the memory of your current view, tap the space bar and select New View from the popup. Give your new view a memorable name, perhaps DWG ISO.

Figure 6C

presents a 2D drawing that is using such a named custom view—DWG ISO, in this example.

As we conclude this tour of Exploded View creation, we note that:

FIGURE 4A Adding a step to reposition the O-ring is easy, but the cover is now in the way. Master the domino effect when creating Explode Steps.

FIGURE 4B Want to move the covers and screws in one easy move? Edit the group.

FIGURE 5 To make component selection and repositioning easier, rotate the view as needed.

• Motion Studies can use Exploded Views.

• Exploded Steps can be rearranged in the Exploded View so that covers go on before the screws go in.

• Multiple Exploded Views can be created for various purposes.

FIGURE 6A An Exploded Line Sketch starts with a menu selection.

FIGURE 6B The Explode Line Sketch connects the selected components with dashed lines in the direction selected. Oh, by the way, saving a custom view is easy—hit the space bar and give it a name.

FIGURE 6C Here’s an example of using a named custom view in a 2D drawing. In this instance, DWG-ISO is in use.

Gland Skill Bonus Round

O-ring glands and Exploded Views don’t have much in common. However, the specification of grooves and pockets for O-rings is a useful design skill. Here’s a career

tip: When collaborating on a team, contributing clear illustrations and well-specified seals are among the skills that will make you welcome.

I’m not affiliated with Apple Rubber, but I am a fan of its online gland calculator tool (

www.applerubber.com/oring-gland-calculator

). Similarly, I’m not affiliated with McMaster-Carr, but its website is useful for O-ring cross-sectional measurements (its DASH size) and offers downloads and (at least preliminary) answers for where to find things.

In general, an O-ring is used for creating a face seal against its cover. The O-ring is sealing against internal pressure.

Figure 7A

features a sketch for a Cut-Revolve for that O-ring’s gland. The dimensions and tolerances used were discovered online using Apple Rubber’s gland calculator (see

Figure 7B

). Tell the calculator that it is a face seal for a DASH-012 size O-ring against internal pressure. The calculator returns a starting suite of dimensions that can be tuned to optimize the squeeze.

FIGURE 7A The sketch for an O-ring’s gland can use a dimension name and layout method that matches the results from a gland calculator tool (see Figure 7B). This makes review and verification easier. In this screen shot, a dimension is being renamed to H. Note that dimension A has already been renamed.

FIGURE 7B Set up the gland calculator with type of seal (face) and the size of O-ring (DASH-12), and it gives you a starting set of dimensions. The tool shows a preview cross-section of the gland, with dimensions labeled to match the data table above.

FIGURE 7C Here, the calculator is set up for a rod seal for a DASH-206 O-ring. The dimensions will be used in Figure 8A.

Here’s another CAD tip: Make the dimension scheme in the sketch match the dimensions on the calculator. You can even rename the dimensions to match the ABCs. The people reviewing and editing the gland will appreciate the clarity.

For the O-rings that are sealing against the rod, change the calculator’s application from axial to radial, and update the DASH size desired. (In

Figure 7C

, it is DASH-206).

Disclaimer: There is more to gland design than this starting point calculator.

When collaborating on a team, contributing clear illustrations and well-specified seals are among the skills that will make you welcome.

See the Seal

As mentioned, downloads for O-rings are easy to find. However, it doesn’t take much to model an O-ring from scratch—a dashed line and a slot or circle. In

Figure 8A

, a Revolved Sketch shows the deflected O-ring for the rod seal. The dimensions for deflection are borrowed from the gland calculator. Similarly, in

Figure 8B

, the face seal O-ring is modeled to show its squeezed flatness.

Figure 9

is the encore shot showing the deflected O-rings doing their duty. Deflection is a small thing to show but is sometimes a way to spot an error.

FIGURE 8A An O-ring can be modeled (using configurations) to show a deflected condition as well as the as-purchased condition.

FIGURE 8B The face seal O-ring deflects in a different manner from the rod seal type. Visual accuracy can help engineers spot design errors and bolster illustrations for training materials.

FIGURE 9 Virtual prototypes sometimes benefit from little details like deflected O-rings. They always benefit from well-grounded guesswork.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

ddavis@fmamfg.org

.
# Shop Technology and 3-D CAD: Modeling a Cable Harness

[TARİH: 01.10.2016 The Fabricator]

Precision Matters

Here’s how to get those model wires, cables, and hoses to where they need to go

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

M

odels of wires may be required for a variety of reasons: to create a faithful visual prototype or perhaps for the task of planning physical cable routes. A 3-D CAD feature—the sweep—is useful for modeling items such as wires and hoses.

Parametric links add some "intelligence" to the model. The properly modeled wires will follow the components as the design evolves.

Figure 1

illustrates a fan and a plug that do not yet have a wire harness connecting them. For purposes of context for our CAD modeling scenario, this 3-D CAD model has several nested subassemblies. The fan and the plug are both in the same subassembly. Here is the scenario: Several cable models are required for this project, and we’re starting with the fan power harness.

Here is the outline for the CAD technique being recommended:

A 3-D sketch will define the path or route for the wire.

A 2-D sketch will define the profile of the wire to be modeled.

One end of the 3-D sketch of the path will be fully constrained to the parent model.

The other end of the 3-D sketch will be parametrically constrained to an external component.

Figure 2a

highlights a generic technique for a cable harness’s 3-D sketch. This type of sketch can be the foundation for many types of wires and hoses. Of note are three sketch entities: two line segments and one spline. The spline is constrained to be tangent to the line segments. The line segments are convenient for adding constraints to other components. Their length represents the stiffness of the harness being modeled. The spline handles are convenient for changing the route of the wires.

Figure 1 Here’s the starting point: The fan is missing wires that should connect it to a plug.

Looking Farther Down the Path

Thus far in this CAD technique, only one end of one 3-D path is fully constrained. For the fan cable in this scenario, the 3-D sketch is referencing features found in the fan model to achieve that starting anchor constraint.

Here’s a CAD tip: Use the path to define the sketch plane for the profile. This consistent work flow habit makes it easier to edit your CAD work in the future.

After creating the semiconstrained 3-D path, the next step is to create a sketch plane for the profile of the harness.

Figure 2b

illustrates the selection of a line segment and a point on the path to define the location of a plane.

Figure 2c

illustrates the sketch setup for the profile of the harness. In this example, the fan has two 1-mm-diameter wires connected to it.

Here’s a CAD tip: Use the path to define the sketch plane for the profile. This consistent work flow habit makes it easier to edit your CAD work in the future. The blessing and curse of 3-D CAD is that there are many ways to model a similar solution. We opine that it is not always a blessing to use all possible modeling techniques in the same project.

In

Figure 2d

the sketches for the profile and path are used to set up a sweep. In this example, the profile twist-along-path setting is used to represent a twisted pair of wires.

With only one end of the path constrained, the twisted pair is heading in an arbitrary and undesirable direction (see

Figure 3a

). Instead, the wires should bend to terminate in a plug on a circuit board. Fortunately, all that is needed is to edit the path to constrain the floating end of the 3-D sketch to that plug.

Figure 2a This is a 3-D sketch that has two line segments connected with a spline. At each of its ends, the spline is made tangent and coincident with the line segment. Only one end of the path is fully constrained at this time; the other end "floats" in 3-D space.

Figure 2b A plane is defined using a point and a line segment from the 3-D sketch for the path. This plane will be used for the sketch for the profile of the wire harness.

Figure 2c The path defines the plane. The plane helps to define the profile. In this example, two circles represent a twisted-pair profile.

Figure 2d The profile and path are used to define a sweep. In this example, the option for a twist-along-path is used to create a twisted pair of wires. The appearance of the sweep was changed to distinguish the black and red wires.

Figure 3b

illustrates the result of editing the 3-D sketch to properly constrain it. The length of the line segments and the position of the spline’s tangent handles control the shape of the resulting wire path (see

Figure 3c

). If a more exotic path for the harness is required, spline control points may be added to the 3-D sketch to add control points for the path.

Good news! If either the fan or the plug is relocated, the constrained 3-D sketch for the wires will rebuild to follow the components.

In other news, the constrained 3-D sketches can be ill-mannered. Unconstrained lines sometimes project in unexpected directions. Be prepared to edit the path for cable harnesses when making dramatic component moves. Fully constraining the 3-D path sketch might improve the robustness of the path. (In other words, make it able to withstand more dramatic component moves.) However, more constraints take more computer resources to solve.

Figure 3a These are bad wires. In the context of the top-level assembly, the wires in the fan model are not connecting to the pins in the plug.

Figure 3b This makes for good wires. In the context of the toplevel assembly, the 3-D sketch in the fan model is constrained to the back of the plug on the computer board.

Figure 3c After we edit the bad wires shown in Figure 3a, the fan’s cable harness now connects to the board in a credible path.

Now, here’s the bad news. This model for an off-the-shelf 40-mm fan is now dedicated to this particular chassis. If the same fan model’s wire harness is reconstrained to work in a different chassis, a conflict between product lines will arise.

The next column will address a solution to this CAD conflict. Here’s a hint as to what’s coming: Create a subassembly for each product line that contains the common fan and plug, along with a unique wire model for each product line. We’ll probably demonstrate that with the cable harness for the camera.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop. Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

dand@thefabricator.com

.
# Shop Technology and 3-D CAD: Cap-Offs, Springs, and Threads

[TARİH: 01.11.2014 The Fabricator]

Precision Matters

Solid modeling tools are versatile, but not always intuitive

By Gerald Davis, Contributing Writer

Gerald Davis

is a job shop consultant and chairman of the board of DSM Manufacturing Co.,

gerald@glddesigns.com

.

W

hen modeling curved objects, we often create unwanted byproducts such as a flat end face that should be hidden under a rounded end. An example is shown in the upper model in

Figure 1

. To put a name to this problem, we borrow the term

cap-off

from Matt Lombard’s

SolidWorks Surfacing and Complex Shape Modeling Bible

.

One solution to the cap-off is shown in the lower model in Figure 1. This example uses a Loft between the profile of the flat face and a point on a plane some distance from the face. To control the shape, we use a Guide curve.

The result of this loft-as-cap-off has some benefits as well as some drawbacks. The main drawback is demonstrated in the lower model shown in

Figure 2

. The face of the cap-off does not match the curvature of the handle body, even though it is tangent and in contact with the handle. The consequence is that there is a distinct line around the cap-off.

The upper model in Figure 2 demonstrates a different solution to the problem—use of a Surface-fill feature instead of a Loft. This cap-off was inspired by an idea in Lombard’s book. The ability to match the curvature of the main handle body results in an excellent blend. Additionally, the setup is somewhat easier than that for the Loft solution. To compare these cap-offs, we’ll dig into some of the details of the loft-cap-off first.

Figure 1

The upper model shows an unwanted flat end. The lower model shows a solution modeled using a loft feature.

Figure 2

Surface-fill works better than Loft for cap-off of this handle.

Figure 3

This cap-off was designed with a Loft. The CAD jockey uses a Guide curve to loft a profile to a point.

Looking Into the Loft

Figure 3

is a screen shot of the Property Manager for the Loft feature. This specific loft is defined between two sketches. The sketch that starts the loft is an exact match of the face to cap-off. The other sketch contains a sketched point that controls where the loft ends. An experienced CAD jockey can construct these sketches and define these lofts in several different ways. All CAD methods have merits. The prevailing design constraints generally help to select the best method.

A CAD trick used here is to multipurpose the sketch with the point. That sketch (3DSketch7) also has an arc that controls the shape of the loft. Without this guide curve, the loft would try to form a cone to a sharp point. With the guide curve, the loft blends in a more pleasing manner.

Of note at the bottom of the Property Manager shown in Figure 3 is the option to Merge result. If this option were not checked, this loft would create a solid body separate from the solid body of the handle. Multibody versus single body is a concept that is often regarded as mundane in solid modeling, as it should be.

In review, to set up this loft we needed a sketched profile to start, a sketched profile to end, and a sketched guide curve. We used a 3-D sketch to create both the guide curve and the end point sketch.

As a side note, using a sketch for multiple purposes like this might be efficient, but the next CAD jockey that comes along to edit this model will have to spend some time sorting out where the required setup items are hidden. A similar sin of this nature is the trick of using a temporary axis to constrain a sketch. When the axis is invisible, the sketch remains constrained. You know why, but will the next person who edits this model think to turn on invisible things?

Focusing on the Surface-fill

Turning to our example of a cap-off solution using a Surface-fill feature,

Figure 4a

is a screen shot of our setup of a plane some distance from the end of the handle. We use that plane to sketch the guide curve for the Surface-fill feature-to-be.

Figure 4b

shows the sketched guide curve. This is where we pause in awe of Lombard’s insight: Anything can be a guide curve—even a straight line!

In our example, we are modeling the little bit of flatness that results, as this end of the casting would be sanded and polished. Myriad possibilities for guide curves are possible; Lombard’s cap-off solution, however, is versatile.

Figure 5

shows the Property Manager for Surface-fill, whereas Figure 3 shows that for the Loft. As shown in Figure 5, our Surface-fill needs a Boundary. The edges around the end of the handle were selected.

Figure 4a

This cap-off was designed with a Surface-fill. The first step is to create a plane for the guide curve.

Figure 4b

The second step is to sketch a line on a plane. The Guide curve for this Surface-fill is just a little pink line!

Figure 5

The Curvature option is used for all edges of the patch boundary.

Figure 6

This bill of materials table shows the various parts of the hair clipper. Most of these items were reviewed in last month’s article. What remains to be seen is shown in Figure 7.

Figure 7

Not counting the handle shown in outline, four parts make up the spring action: cap, spring, actuator, and ball pin.

Note that all edges match Curvature, not simple Tangency. This curvature option results in a very good-looking cap-off.

As with the Loft in Figure 3, the Surface-fill in Figure 5 has an option for Merge result. In the case of the Surface-fill, this option is merging a surface into a body—a wonderful bit of convenience. To accomplish this otherwise, we would need to knit surfaces and try to form a solid body from the result. Knitting surfaces and forming solids is a topic for another day.

In keeping with the nonintuitive straight-line guide curve, the CAD jockey can use the option for Reverse in the Surface-fill, as shown at the bottom of Figure 5. The author believes this should be labeled “Hail Mary!” instead. If the Surface-fill fails, try the other setting of Reverse, and it might work. Reverse probably makes more sense if one were to study the math that is underlying this very useful surfacing tool.

Examining the Bill of Materials

The model for the handle we’ve been reviewing so far is part of a hair clipper design as shown in

Figure 6

. The table that appears below the model is a preview of the Bill of Materials. Note that this table corresponds to the components inserted into the assembly as shown in the Feature Manager to the left of the graphics window.

Last month (“Shop technology and 3-D CAD: Some boundaries in solid modeling,” Precision Matters,

The FABRICATOR

, October 2014, p. 66), we began working our way through the bill of materials to examine the models for each line item. Not following any particular order, we reviewed the models for the blades and wing nut and noted that conventional solid modeling techniques achieved good results. The blade cover was best modeled using a combination of surface modeling and solid modeling techniques. We called that

hybrid

modeling.

To complete our tour of parts,

Figure 7

shows the four components that give spring action to the handle: spring cap, spring, spring actuator, and ball pin.

The ball pin model shown in

Figure 8

is modeled as a Revolve of a Sketched profile. The merits of Revolve, rather than an alternative technique such as a stack of extruded cylinders with fillets and chamfers, include:

Faster rebuild time

Shorter feature history

All features in a single, easy-to-edit sketch

Suitable for the goal of the model, which is a spherical push-end

Fewer mouse clicks and thus a speedier CAD jockey

Figure 8

A Revolve is a good CAD method for modeling this ball pin. The spring actuator shown in Figure 7 is also a good candidate for a Revolve.

Figure 9a

The spring is modeled using a Sweep along a helical path. A Variable pitch Helix feature is handy for flat-ended spring models.

Figure 9b

The round wire is represented by a circular profile—called Sketch3—and the pitch of the spring is controlled by the helix from Figure 9a.

Figure 10

Instead of a helix, this thread path was defined using a twisted surface loft and an interference curve between that twist and the thread’s outer diameter.

There is not much difference in terms of the CAD methods used to create the ball pin and the spring actuator. Both are easy to model as Revolves. The spring actuator is visible in Figure 7 and presses into the end of the spring to provide an engagement socket for the ball pin.

Should the ball pin and the swing handle be modeled as an assembly instead of as stand-alone parts? This is a rhetorical question with a dichotomy of answers.

Yes. And those two parts and their assembly should be given part numbers. Assembly documentation will include an exploded view and instructions for pressing the pin into the casting.

No. A subassembly of these two components is not really needed. They can co-exist at the top level of the BOM for the purposes of a visual prototype. Of course, when creating Motion Studies, it is sometimes handier to select subassemblies instead of groups of parts.

Regarding the modeling methods used for the spring, it is basically a Sweep with Cut-extrudes to flatten the ends. The cute trick is with the helix that drives the sweep.

The Property Manager for the sweep’s helix is show in

Figure 9a

. Of particular note in Figure 9a is the Variable Pitch of the helix as used in manufacturing a flat-ended spring.

The spring’s Sweep feature setup is shown in

Figure 9b

. In this example, the spring’s wire is round, so the profile sketch is a simple circle noted as Sketch3. The helix was defined to match the outside diameter of the finished spring. This decision was made for the convenience of matching the spring’s size to the bore in the handle.

Last, we visit another method of modeling swept-cut threads.

Figure 10

shows the model for the spring cap. Instead of using a helix to create the path for the cut, this model uses a path that is defined by an interference curve between the outside diameter of the thread and a swept surface.

The swept surface feature has an option to twist along its path. In this example, the path is a line along the axis of the cap. It is easy to set the number of twists to match the target thread pitch.

This twisted swept surface trick has a slightly faster rebuild time than the helix. The helix has the convenience of variable pitch setup. Let us know which you feel is better.
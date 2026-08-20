# Analysis can help when working with sheet metal

[TARİH: 01.01.2025 The Fabricator]

Precision Matters

Simulation gets you closer to a part design that can function

GERALD DAVIS

One of the limitations with the SimulationXpress is that it does not work with assemblies, but it does work with a single body part. We could model the captive fasteners as simple extrudes. Instead of trying to analyze representative studs, we’ll just run the simulation on the sheet metal part.

T

he sheet metal bracket shown in

Figure 1

has been the topic of discussion in the past couple of columns. In particular, we’ve considered modeling the project as either a multibody or an assembly, as well as the nuances of modeling for manufacturing. Efficient CAD practices add merit, but all that really matters is the suitability of the design.

FIGURE 1

A sheet metal bracket is shown. It has been evaluated for technique and speed of invention. Is it suitable for function?

FIGURE 2A

Material, fixtures, and loads have been assigned in SimulationXpress. The simulation study reports problems with Factor of Safety in red. This design is too weak.

FIGURE 2B

The open corners of the bracket have been closed to improve the strength. The study now shows that the holes are too weak. Perhaps the holes are not good choices as fixtures for simulation.

FIGURE 2C

The fixture has been changed. The entire back wall of the bracket (cyan arrows) acts as the fixture. The load is indicated by red arrows. The resulting Factor of Safety is greater than 1.4. Success! But can we eliminate material? Do we need more mounting screws.

FIGURE 3A

Material has been removed. The study still shows a Factor of Safety greater than 1.2. The design is improving.

FIGURE 3B

A plot of stress is shown. Fatigue is likely in the corners and along the horizontal bend (red). This design is barely strong enough, perhaps ideal.

FIGURE 3C

A plot of displacement predicts that the front edge of the bracket will experience permanent deformation with this load and fixture.

FIGURE 3D

An optimized design is based on understanding the behavior of the material under load. Compared to Figure 1, this bracket design has more welding and less raw material involved.

The professional license of the CAD software used in this column includes simulation tools that can help predict the suitability of a design for an intended application. Granted, the included SimulationXpress add-ins are limited, but they can provide a strong hint. The need for a full license might become evident if those limitations become obstacles to completing the prediction.

To paraphrase SimulationXpress’ help documentation, accuracy of simulation depends on fixtures, loads, and material properties. The user interface for this simulation tool makes entry of those three data points very intuitive. As foreshadowing, the fixtures must accurately represent the part working conditions.

One of the limitations with the SimulationXpress is that it does not work with assemblies, but it does work with a single body part. We could model the captive fasteners as simple extrudes. Instead of trying to analyze representative studs, we’ll just run the simulation on the sheet metal part.

For this project, suitability means that it supports a 250-lb. static load, and it does so with minimum mass. We are to prevent the load from slipping off either side of the bracket, so we need side flanges to serve as bumpers. Size requirements (4 in. wide by 2 in. high by 3 in. projection) along with thread specifications for mounting also are required. We’ve selected 0.062-in. 5052-H32 aluminum for the material.

The simulation software features a Factor of Safety (FOS) Wizard, which is one of several analysis reports. The FOS is based on stress and shear calculations. The material is failing where the FOS is less than 1. It is just starting to fail where the FOS equals 1. Where the FOS is greater than 1, no material failure occurs. (Perhaps there is an opportunity to save material.)

Figure 2A

shows FOS results. As criterion for the study, the holes are fixtured as stationary, and a load is placed on the horizontal surface. We see red as a warning. The bracket is too weak along the horizontal bend. The FOS is only 0.10 and should be greater than 1!

To improve the design for strength, we will weld the open corners closed. We’ll model these new welds as simple extrudes. Simple can be good (or necessary) for the purposes of ballpark analysis!

In

Figure 2B

, the simulation is re-run to show that the welds improved the FOS. However, red areas are still showing problems around the mounting holes. As fixtures, these holes are in severe shear and are tearing out as points of failure.

The use of the holes’ walls as fixture points can be misleading. In reality, the captive screws have larger engagement with the sheet metal than mere contact with the holes’ walls.

In lieu of trying to model the bodies of the studs, we’re going to tell the software that the entire back wall of the bracket is anchored. We’ll keep in mind that the design for three-point mounting might not be suitable.

We seem to be keeping a lot of things in mind as our setup for the simulation deviates from ideal. We could improve the situation with a more extensive license and more patience in modeling. The biggest problem so far is with the mounting.

In

Figure 2C

, the fixture has been changed. The entire back wall of the bracket is now the fixture (as indicated by the cyan arrows). The direction of load is indicated with red arrows.

The simulation now predicts an FOS of 1.49, which is not failure, although it might be excessively heavy. In

Figure 3A

, mass has been removed from the design by cutting away the unnecessary corners.

The side bends have become flanges. Their intersections are still modeled as if they are welded closed. This results in an FOS of 1.27, above failure and acceptable, keeping in mind the things we’re keeping in mind.

As mentioned earlier, in addition to plotting the FOS study, plots for stress and displacement are available. In

Figure 3B

, we see the von Mises stress predictions. This bracket is in danger of permanent deformation near the corners and along the horizontal bend, as predicted in red.

The displacement of the material is predicted in

Figure 3C

. The front lip seems to be flappy. Animations don’t play well on paper, but in addition to creating the static plots, the software generates animations to help visualize the stress and displacement.

Figure 3D

shows an assembly that incorporates the stronger bracket with the (suspect) mounting hardware. In contrast to Figure 1, welds have been added, and material has been removed.

These changes were made with some confidence. If it turns out that the prediction is incorrect, it is at least under control. The parameters can be adjusted to achieve accurate simulations in very few iterations.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

ddavis@fmamfg.org

.

DISCOVER OUR DRY DEBURRING TUMBLER

DEBURRING

EDGE ROUNDING

DESCALING

DEGREASING DESLAGGING

SPK SOLUTIONS

www.spk-solutions.com

832-302-7766

@spk.solutions

spksolutions

Transforming challenges into opportunities, and opportunities into successes.

Laser Automation

Press Brake Automation

Shear Automation

e-ci.com/transform

Trusted Support | Reliable Service

Proudly USA Owned and Operated since 1898

Add CIberDash to your operations OWN IT. and unlock even more potential.

www.e-ci.com
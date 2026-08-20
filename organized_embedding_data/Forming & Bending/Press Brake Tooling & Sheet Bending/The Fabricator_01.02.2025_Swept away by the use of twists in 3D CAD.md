# Swept away by the use of twists in 3D CAD

[TARİH: 01.02.2025 The Fabricator]

Precision Matters

Two sketches might look similar, but a twist reveals how different they are

GERALD DAVIS

F

igure 1A

shows a sketched profile. The dimensions and shape are arbitrary. It is simply an example of a routine 2D sketch in 3D CAD.

Figure 1B

shows that same sketch being used to create a solid body. In this example, the body is 1 in. tall. This could have been accomplished using a Base-Extrude, but in Figure 1B the solid body is created as a sweep along a path.

The sweep relies on two sketches: Sketch1 is the profile we saw in Figure 1A, and our new Sketch2 is the path. This path is a straight line, simply to illustrate the similarity to a simple Base-Extrude.

A Base-Extrude only requires a single sketch. We celebrate that. Simultaneously, note that it takes only a moment of CAD labor to create the sketch for the sweep’s path. The CAD jockey must draw a line usefully related to the profile sketch and save it for use as the path. Perhaps the CAD jockey should rename the sketch for the purposes of documentation.

FIGURE 1A As an example of a routine 2D sketch in 3D modeling, a dimensioned profile is shown.

FIGURE 1B A sweep along a path is shown. Sketch1 is the profile, and Sketch2 is the path. In passing, we note that this resembles a Base-Extrude so far.

FIGURE 2A The same sketches for profile and path are used, with a 360-degree twist option to create a spiraling body. This is an advantage over a simple Base-Extrude.

FIGURE 2B Instead of multiplying five by 360 to arrive at a degree setting, the user interface for the sweep allows convenient selection of a number of twists. Here, we show five complete twists. Note that we’re using a multibody part for this demo.

We note that Sketch1 and Sketch2, as names, mean profile and path for as long as memory lasts.

The benefit of the extra effort of a sweep rather than a Base-Extrude might be a hard sell. Perhaps the sketched path, as a result of being explicit, somehow helps convey the design intent to the team. Perhaps the path sketch is easier to relate to other features in the model.

While it is good to be enthusiastic about the power of sketched paths, don’t be distracted. The twist is the intended benefit here—as shown in

Figure 2A

.

The difference between Figure 1B and Figure 2A is very small, just one twist. Literally the same sketches and tools are being used to create these separate bodies.

We’re getting CAD fancy! Sketch1 and Sketch2 from Sweep1 are being re-used to create Sweep2. (Cheers to the labor savings!) The trick is to CTRL-select the two sketches in the Feature Manager as part of inserting a sweep feature. Beyond labor savings, sharing a sketch between multiple bodies allows their common features to be edited and controlled without redundancy.

For this demo, the resulting 3D bodies are not being merged (although there is an option for that). Configurations are being created to manage the display states (hide or show) for the various bodies used in this demo. The use of configurations to hide or show modeled bodies is perhaps best savored by downloading the 3D model.

The sweep tool has options that allow specification of twist along the path. In Figure 2A, the twist is set to 360 degrees along the entire path. One twist per inch is the result.

Figure 2B

demonstrates a different but similar sweep setting to achieve five twists along the entire 1-in. path. Could a CAD jockey model 20 twists per inch, as in ¼-20 thread? Try it. After a bit of delay, you’ll see why maybe that’s not speedy modeling.

In

Figure 3

, the path for the sweep is now a 3D sketch. Note that the profile sketch is again borrowed from Sweep1 for this demo. It is the same Sketch1 from Figure 1A. The number of twists in this longer sweep is 20, which coincidently resembles the pitch in Figure 2B. If the sketched profile had been a pair of circles, we would have a model for a pair of twisted wires.

Could all Base-Extrudes be modeled as sweeps? Yes, but it’s not recommended. It’s better to add twist to the plot if needed. A twistless twist, like a pun, is a gift to the giver.

FIGURE 3 The sketch for the path of our sweep is now a 3D sketch, just to show off. The profile remains the same Sketch1 from Figure 1A. Of course, more twists (20 with this longer path) are required to maintain five twists per inch.

Gerald

would love for you to send him your comments and questions. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.
# How to 3D-print PLA press brake tools

[TARİH: 01.11.2025 The Fabricator]

Bending Basics

Insights on filaments, printer programming, and annealing

STEVE BENSON

F

or the past few months, I’ve been introducing what’s probably a new concept to most people in the bending department: Using a 3D printer to make press brake tooling (see

Figure 1

).

This month, let’s start with the drawings for the tool you intend to develop. At the CAD level, you will design tools, fixtures, gauges, and other components in the same way you always have, except that you may save them in a different file format, such as STL, 3MF, or STEP—any format that your slicer can use for 3D printing. In the additive world, the "slicer" is a software application that converts a 3D model into machine instructions.

You have many different slicers to choose from; some are machine-specific while others are not. After opening or importing the file, the fun begins. At this point, you will be presented with your first parameters regarding quality, including linear and angular deflection. The smaller the value, the slower the print and the higher the quality. For press brake tooling, I recommend the smaller values.

Once you ensure your printer is properly calibrated, you can set the print parameters. This includes the filament diameter, type, and (if you have a multifilament feed) location.

You then inform the slicer about the type of build plate you are using. Different materials require special build plates. Some are smooth while others are textured; some are made of spring steel, others are glass. You will need to research the specifics for the type of filament you will be using. For this discussion, we will be using a PLA (polylactic acid) filament, so we will be using a standard spring-steel build plate with a light texture.

Basic Parameters

The first parameter is

quality

. Here, you can set your wall thickness and infill. You also set the print precision, ironing settings, wall settings, and advanced options. "Ironing," as the name suggests, makes the surface appear smoother. The

strength

parameter includes the number of wall loops, infill type, and percentage of infill, along with many advanced options.

You next determine the

support

needed to print your part. Some elements of an object, external or internal, might be incapable of supporting themselves.

FIGURE 1

The idea of 3D-printing press brake tools isn’t new. These were printed for a tradeshow in 2018. Still, the process hasn’t pervaded the industry—at least not yet.

You next set the

speed

; this includes speeds when you’re printing the part as well as the speed of printing when bridging (that is, printing on air between two points) and building supports. You also can set the speed of travel and acceleration between printing passes. Finally, you can specify special modes, print sequences, and G-code output. Yes, the slicer and printer use G-codes just like everything else.

Annealing and Stress Relief

Metal annealing aims to soften and relieve stress, while metal tempering aims to reduce brittleness and increase toughness in a hardened metal. For PLA, tempering isn’t a standard process. It can, however, be annealed.

Every PLA filament type has precise settings, including the print bed temperature, extruder head temperature, and cabinet temperature. Rapid cooling as the printer deposits material layer by layer can introduce internal stresses within the part (see

Figure 2

). That’s why many of these materials require annealing to increase their mechanical strength, improve thermal stability, and reduce internal stress locked in from the printing process.

Annealing involves heating the part to just below its melting point. This encourages its molecules to transition into a more stable, crystalline structure, making the part harder and more resistant to deformation.

To anneal your PLA part, gently heat it in a controlled environment, such as an oven, to a temperature above its glass transition temperature but below its melting point. For PLA, this is typically between 60 degrees C and 70 degrees C. Hold the part at this temperature for a specified time—usually somewhere between 30 and 60 minutes—to allow molecular rearrangement to occur.

Finally, slowly cool the part to allow the new, stable structure to form. Dialing in the correct temperature and time is crucial. Overheating can cause the part to melt or deform, while insufficient time may not allow for proper crystallization.

Also, check the part’s opacity. Although this might not affect the creation of press brake tooling, a change in a part’s opacity is a familiar visual cue indicating successful annealing. The crystallization process often makes the part less transparent.

Uncontrolled cooling or improper heating can cause the part to warp. Using a stable medium, such as sand (also called "ballast"), can help keep the part in position and prevent deformation. The type of ballast medium will vary depending on the material being annealed. The ballast needs to be packed firmly into all internal voids and completely encase the entire piece.

FIGURE 2

A spool of PLA filament is fed into a 3D printer head. Printers deposit PLA layer by layer. This process can create some internal stresses within the part.

Szakalikus/iStock/Getty Images Plus

Part Orientation and Bed Adhesion

Just as steel can have a grain, so can the PLA parts you’re printing. You will be able to rotate your tool on the build plate so that you will be printing "across the grain" of the tool rather than "with" the grain induced by the printer.

Depending on the type of build plate you use, you may or may not require an adhesive to improve

bed adhesion

, or the ability of the first layer of the printed plastic to stick to the build plate during the printing process. For PLA, I’ve used a simple Elmer’s glue stick. However, some materials require a specific adhesive to function properly, much of which is designed to work at a particular plate temperature.

Moisture Content

With a few exceptions, your filament needs to have very low moisture content. The problem is that most filaments are very

hygroscopic

, meaning they absorb moisture from the air. The higher the moisture content, the more difficult it is to print and build acceptable parts or tools. I have a dedicated drying unit that I use for my filaments, but if you need to, you can dry your filaments in a standard kitchen oven.

Store your filaments in an airtight container with a desiccant bag to absorb any moisture that might be present. This will keep your filaments dry and ready to use when needed.

Plastic Body, Metal Nose

All this was just a quick overview of 3D printing. Trust me, learning the process will take some time. Then again, it is no more complicated to learn than any other CNC machine in a sheet metal shop.

If you have a 3D printer already, do a Google search for press brake tooling, punches, or dies, and include STEP or STL files in the prompt, and you will find quite a few downloads of press brake tooling designs. You can find files from places like Bambu Lab, Maker Lab, Thingiverse, Printables, Cults 3D, and numerous other websites.

Every PLA filament type has precise settings, including the print bed temperature, extruder head temperature, and cabinet temperature. As the printer deposits material layer by layer, rapid cooling can introduce internal stress into the part. Annealing helps improve the part’s strength and thermal stability characteristics. It also helps reduce internal stress locked in from the printing process.

Next month, we will conclude this series by examining the insertion of metal into a 3D print at the nose of the punch. This build strategy helps address issues with wear and deflection.

We also will explore 3D-printing metal using a small, home-sized 3D printer. Yes, it’s possible, but it does require a special extruder head, a build plate, and another specialized piece of equipment: a sintering kiln. To produce high-quality, tight-tolerance tools or parts, you also will need to calculate a shrinking percentage. There’s more to learn—so, until next month, Vaya con Dios, my friends.

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

PRODUCTION CONTROL, REINVENTED.

Integrated Task Management

Barcode Scanning

MRP Integration

BOOK A DEMO

(866)979-0453

sales@fabstation.com

www.fabstation.com

Jackson, MN Sioux Falls, SD

From Prototype to Production TrusT HiTcHDoc To Deliver

Flame and Plasma Cutting

Tube & Sheet Laser Cutting

Metal Forming

Metal Rolling

Machining

Manual & Robotic Welding

Powder Coat Painting

Assembly

Contact us Today to Learn More!

507-847-4049

Marketing@HitchDoc.com
# Shop Technology and 3-D CAD: One Part, Multiple Modeling Techniques

[TARİH: 01.12.2016 The Fabricator]

Precision Matters

CAD techniques for modeling flanges, inserted bends, converted sheet metal, and flat layouts

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

Figure 1

These are seven 3-D model variations of the same part. The best one is the one that allows you to get a part fastest to market. A model that is easy for others to edit and understand is also good. In some cases, however, the most important goal is a model that allows for the fastest rebuild time.

T

he versatility of 3-D modeling software allows for many possible solutions to the same problem. To emphasize the nuances among sheet metal modeling techniques, we pre–sent seven variations on the same part, as illustrated in

Figure 1

.

Here’s a disclaimer: This article does not cover all possible ways to model this example. Let us know as you find others. Further, much of the terminology applies to a specific brand of CAD. The general concepts apply, nonetheless

.

First, we consider a conventional modeling technique without regard to sheet metal, and then use a tool to convert that model to include sheet metal behaviors. The reasons for the conversion include the ability to flatten the part, the ability to tune the flat layout calculations to match physical tooling, the ease of adjusting bend radii, and the convenience of having the bends and thickness modeled automatically.

Figure 2a

Use simple Boss-Extrudes—all the same thickness—to model the part without bends.

Figure 2b

The Convert to Sheet Metal tool adds the bends and the ability to unfold.

Figure 2a

demonstrates a CAD technique using three Boss-Extrudes to model the basic features desired. In

Figure 2b,

the Convert to Sheet Metal tool has been applied—and part marking added—to complete the part. The only sheet metal-specific skills required are:

1. To keep the thickness of all extrudes the same.

2. To set up the Convert tool with matching thickness and appropriate inside bend radius.

Those settings are editable, which is a compelling reason to use the Convert to Sheet Metal tool.

Figure 3a

demonstrates modeling the part as it will be manufactured, starting with a flat layout. This requires knowing how to calculate flat layouts. This technique is demonstrated only for comparison and contrast to other—perhaps better—techniques.

The sheet metal CAD tool used in Figure 3a is the Insert Bends tool. Even though the modeled flat does not have bends, the Insert Bends trick makes it possible to add sketched bends to the flat layout.

In

Figure 3b

the Sketched Bend tool has been used to model the first of two bends. To complete the part, we add a second sketched bend (see

Figure 3c

). Note that the dimensions for locating the bend line also require skill in sheet metal flat layout calculation. As a CAD technique, this is perhaps the most difficult to edit and understand for sustaining engineers.

Figure 4a

illustrates a method that is very similar to that shown in Figure 3a. Start with a flat layout, but this time use the Convert to Sheet Metal tool. In addition to a preference one might have in using one tool over the other, a CAD jockey also should know that the Insert Bends tool rebuilds slightly faster than the Convert to Sheet Metal tool does. (The Insert Bends tool takes 0.34 seconds compared to 0.36 seconds for the Convert to Sheet Metal tool in this model.)

A Sketched Bend is added in

Figure 4b

. As with all sketched bends, it helps to have sheet metal skill in locating the bend line. The second bend is added separately (see

Figure 4c

), and part marking is added to complete the model.

Figure 3a

This technique starts with a model of the flat layout extruded to the correct thickness. The Insert Bends tool adds the ability to have bends, even though there aren’t any yet.

Figure 3b

The Sketched Bend tool uses a single sketched line to add a bend to a sheet metal part.

Figure 3c

A second sketched bend is required to complete the part.

Figure 4a

A flat pattern is extruded to represent a piece of sheet metal.

Figure 4b

The Sketched Bend tool adds the first bend to the flat part.

Figure 4c

The Sketched Bend tool adds a second bend to the flat part. Now that it is complete, the flat part we started with can be flattened.

If flat layout is not a design goal, then the modeling technique shown in

Figure 5a

is pretty straightforward. Sketch a pair of lines, fillet, offset them with end caps to create a closed profile, and then extrude it. An Extrude-Cut is required to prepare for the flange. In

Figure 5b

the flange is modeled as an extrude, and to make it "look" finished, the part marking is added in

Figure 5c

. Note, however, that this model does not have the ability to unfold.

The model in

Figure 6a

was created as sheet metal from the get-go. A pair of lines were sketched as the L, and then a Sheet Metal Base Flange was applied to that sketch to model the bend and thickness. An Edge Flange with bend relief settings completes the sheet metal. Part marking completes the model in

Figure 6b

.

Figure 7a

shows a neat trick with a Miter Flange feature. The model is nearly identical to

Figure 6a

except that a Miter Flange is used instead of an Edge Flange. The Miter Flange has the ability to offset its start and end. In this example, the end is offset to create the bend relief. Note that Plane 1 shown in

Figure 7b

was automatically created by the Miter Flange feature.

Making the File Transition

To convert a STEP file, or any other imported 3-D geometry, to sheet metal, the first step is to run Import Diagnostics to clean up the import as shown in

Figure 8a

. Then in

Figure 8b

Insert Bends is applied to add sheet metal functionality to the model. This is very similar to the method used in

Figure 3a

. As with the other techniques demonstrated, part marking is added (see

Figure 8c

).

Figure 8d

shows a flat pattern that was generated from an imported STEP file. Adding bends to STEP files is a reliable method of sending files from design to fabrication. The

Figure 8d

model also has the best rebuild time—0.31 seconds.

The techniques demonstrated in

Figures 6a

and

7a

are suitable when the design is likely to be edited as well as for final release to fabrication.

Figure 5a

This screen shows a simple extrude of a closed profile to model the bracket.

Figure 5b

A simple extrude of a closed profile is used to model the flange.

Figure 5c

This is a perfectly good model, but it will not automatically unfold. Note that this model was used to create the demo in Figure 8a.

Figure 6a

An Edge Flange feature is added to a sheet metal part. The bend relief and bend sketch require a bit of planning and setup.

Figure 6b

Modeling sheet metal parts as sheet metal from the get-go saves labor and is fairly easy to edit. This model has a 0.37-second rebuild time.

Figure 7a

A Miter Flange is added to a sheet metal part. The bend relief is easy to create with settings in the Miter Flange tool.

Figure 7b

Miter Flange offers versatility that the Edge Flange lacks. The choice depends on design intent. This model has a 0.41-second rebuild time.

Figure 8a

A STEP file has been imported and the Import Diagnostics tool has been launched. All faulty faces and gaps will be healed.

Figure 8b

As with any model, the Insert Bends tool is a way to add sheet metal functionality to the model.

Figure 8c

After importing, making it sheet metal, and part marking, this model is as good as any other. It is just missing some of the design history of its features. This has the best rebuild time of all—0.31 seconds.

Figure 8d

When it comes to fabrication, STEP files are great for sheet metal. It is very easy to Insert Bends so that the part will unfold.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop. Please send your questions and comments to

dand@thefabricator.com

.
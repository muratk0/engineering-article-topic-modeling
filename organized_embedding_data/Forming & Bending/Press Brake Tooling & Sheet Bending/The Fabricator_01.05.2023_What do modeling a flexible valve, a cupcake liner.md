# What do modeling a flexible valve, a cupcake liner, and a coffee filter have in common?

[TARİH: 01.05.2023 The Fabricator]

Precision Matters

Using a Design Table to control size and shape of models

By

Gerald Davis

FIGURE 1

The flat pattern for a pleated cup is not magically unfolded. It was modeled with links between the flat and formed configurations.

R

eader Joshua Raimond of Denver wrote to ask about a filter in CAD that was covered in a June 2016 column ("Shop Technology and 3-D CAD: Modeling items for visualization but maybe not for manufacturing," Precision Matters,

The FABRICATOR

, p. 60). The question: How is its flat layout modeled?

The item in question—a cupcake filter—is shown in

Figure 1

. There’s no magic here. The flat paper disk was created separately from the formed cup. The configurations determine which of two bodies to display—pleated or flat.

Short of an automatic flat-layout tool for pleated paper, there is nonetheless a CAD connection between the flat layout sketch and the formed cup. In this model, the size of the formed filter and flat layout are constrained parametrically.

As a brief review of the cited article,

Figure 2A

shows the 3D filter with corresponding flat layout dimensions. The colors and symbols employed by the brand of mainstream 3D CAD being demonstrated indicate that the R 56-mm flat radius is controlled by a Design Table and the 30-mm wall length is controlled by an Equation. The Design Table that is doing the controlling is shown in

Figure 2B

, and the Equation Table is shown in

Figure 2C

. The intent of creating the global variables was to use them in subsequent sketches in the model. However, that is another story.

To review the CAD technique employed, configurations were created for both a big coffee filter and a smaller cupcake liner shown in

Figure 3

. Thus, both the Design Table and the Equation Table have entries for each configuration. (The original article, which can be found on

TheFabricator.com

, goes into more detail regarding the surface modeling techniques used.)

FIGURE 2A

The flat dimensions (R 56 mm and E 30 mm) are linked to the formed shape.

FIGURE 2B

A Design Table sets the radius (used in Sketch2) at 56 mm. Also note that the floor diameter in Sketch1 is set to 52 mm.

FIGURE 2C

This table shows the equations used to control features in various sketches in the model.

FIGURE 3

The model for the filter has two configurations—one for a coffee filter and another for a cupcake liner. The sizes and number of pleats are controlled with equations and a Design Table.

FIGURE 4

A flexible valve is modeled using a revolved sketch. The sketch has a dimension named OpenGap@Sketch1. As that dimension changes, the rest of the sketch is constrained to adjust. A Design Table controls the open gap dimension—0.4 mm when open and 0 mm as default.

FIGURE 5

Section views of the valve assembly show a gap in the open configuration and no gap in the closed configuration. Design Tables can be useful.

Maslow’s Hammer

Paper filters and flexible valves—what might such things have in common?

To paraphrase Abraham Maslow’s famous quote from 1966 about having a hammer and seeing every problem as a nail, let’s just say, "If the tool you have is a Design Table, it is tempting to treat everything as if it were Configured."

Recently, this CAD jockey needed a flexible valve. To model it, a revolved sketch is used. (This was done, of course, for minimum rebuild time.) The sketch for the valve is constrained so that the valve’s shape will adjust with the gap distance (between 0 mm and 0.4 mm in

Figure 4

).

Also shown in Figure 4 is a Design Table that sets up two configurations—default and open. In the open configuration, the gap is 0.4 mm; closed it is 0.0 mm.

Figure 5

shows an assembly of the valve and a valve seat in cross-section. The assembly has configurations for open and closed. Those configurations select the valve’s open or default status, respectively.

FAB

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. SPlease send your questions and comments to

dand@thefabricator.com

.

For more content from Gerald Davis, visit

www.thefabricator.com/author/gerald-davis

.
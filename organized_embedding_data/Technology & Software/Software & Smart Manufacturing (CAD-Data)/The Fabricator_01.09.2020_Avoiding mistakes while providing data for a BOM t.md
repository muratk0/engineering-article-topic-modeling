# Avoiding mistakes while providing data for a BOM table

[TARİH: 01.09.2020 The Fabricator]

Expertise » Precision Matters

A hinge model reveals how to ensure the information remains correct, even as new models are made

By

Gerald Davis

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

F

igure 1

shows a tote box assembly’s bill of materials (BOM) table. The 3D model was introduced in the previous episode of this column. A frequent reader of

The FABRICATOR

has asked about inclusion of cut length and cut width in the BOM. It is possible to do so. (See the highlighted portion of Figure 1.) But data entry errors have created a sense of sadness. This is a case of garbage in, garbage out.

As we look to goof-proof the data entry, we’ll be covering specific procedures that are specific to a major CAD so—ware brand. First let’s cover some bad news, and then we can jump into how to do it.

CAD jockeys with experience from the early days may remember how the value of a dimension and the length of a line that that dimension points to could be controlled separately. This made for low overhead for the computer graphics, but also made for great confusion among humans trying to scale or visualize the drawing. Modern CAD so—ware links the line length to the dimension value for less confusion over scale versus shape.

Manually entering information such as cut length and cut width creates real danger that the BOM table will display incorrect data if future edits are not made correctly because the modeled length is controlled separately from the displayed cut length. Linking values to modeled features is one technique to goof-proof the data entry for BOM table information. But even with that in place, the meaning of "cut" and "length" can be an exercise in enforced policy and procedure.

FIGURE 1 A BOM table for a tote box is shown. Columns for cut length and cut width show flat blank size, finished saw cut, or bounding box size depending on the type of component.

Consider the hinges that are welded to the lids of the tote box assembly.

Figure 2

highlights the hinges’ BOM entry. We are interested in line item No. 16. The cut length is shown as 18.75 in.

Suppose that the purchasing department orders 18.75-in.-long hinges per the BOM table. Without knowing the tolerance or how to stake and split the knuckle during cut, or how to deburr it, the result could still be OK.

More consistent production will result if purchasing understands that "cut length" is informational, but not sufficient for manufacturing. The folks on the shop floor somehow must know that raw hinge stock is 6 —. or so long, and purchasing has to round the cut length to the nearest foot to get three finished hinges per raw stick. (In this example, 18.75 in. becomes 24 in.) Eliminating "somehow" is a matter of policy and procedure that accompanies the decision to include cut length in the BOM table.

While pondering Figure 2, please take a peek at line item No. 15—the tray divider. This sheet metal part has a flat blank size of 18.25 in. by 1.464 in. Is that the final cut size? If this is farmed out to job shops, will they all use the same flat blank layout? Probably not.

Is the flat blank size supposed to be the cut size for the raw blank? Should the cut size be some nesting in the sheet size, which is 48 by 96 in.? These questions are answered by policy and procedure and, in turn, influence the CAD technique implemented.

In this scenario, it is desirable to display the modeled (finished) size as the "cut size." For sheet metal parts, the flat blank size—also known as the cut size—is modeled using an approved bend deduction and bend radius.

For parts made from sticks of raw material, the "cut length" shall be the modeled/finished length. The cut width is the unfolded hinge or finished dimension of the part.

For purchased parts, such as handles, rivets, and latches, the cut length and width are not linked to the model. They represent a bounding box that would contain the component.

Now, for the Next Act …

With such policy and procedure in mind, we turn to the mechanics of linking dimensions to product manufacturing information (PMI).

The general procedural plan is to use the BOM table to display PMI stored in the components of the assembly. By "components," we mean parts or subassemblies of parts. In

Figure 3

the sheet metal frame and its end pieces are examples of components that provide PMI for line items in the BOM table.

Figure 4

is a Cut-List properties table in the sheet metal frame. This table is created by the so—ware when a flat layout configuration is created.

FIGURE 2 The hinge is line item No. 16 in the BOM table. The cut length of 18.75 in. is the finished size. A limitation of the BOM table is that it does not show tolerance or how to cut between the knuckles on the hinge. Perhaps another drawing is required. Perhaps policy and procedure is required to define how many parts come out of a raw stick of material.

FIGURE 3 The components of the tote box include a frame and frame ends. These components drive line items displayed in the BOM table.

FIGURE 4 Sheet metal parts, which have a bounding box in their flat layout, also have a Cut-List property table that shows the length and width of the bounding box. The trick is to copy the value—for example, "SW-Bounding Box Length@@@Cut-List-Item1@FMA Tote Box Frame. sldprt"—so it can be pasted into another table.

FIGURE 5 Paste the values from Figure 4 and create your own properties for PMI. Cut Length and Cut Width are shown as examples. The BOM table requires that every component have these two properties. If you’re looking closely, you’ll notice that the file name (FMA TOTE BOX FRAME END.SLDPRT) changed between Figure 4 and Figure 5. These custom property lines (Nos. 18 and 19) can be copied and pasted between components to speed typing. The file name updates itself if it can find a sheet metal flat layout bounding box. To help with this exercise, create the bounding box before pasting these new properties in from another completed component.

FIGURE 6 The PMI for the hinge comes from the extruded length of the pin (18.75 in.) that is defined in an Equation (also known as "Length") that is used to set the value for the property "Cut Length." The model for the hinge has three configurations—two for leaves and one for the pin. The leaves are excluded from the BOM. Only the PMI in the pin configuration matters to the BOM.

Linking values to modeled features is one such technique to goof-proof the data entry for BOM table information. But even with that in place, the meaning of "cut" and "length" can be an exercise in enforced policy and procedure.

Here’s a CAD tip: The flat layout configuration, bounding box, and Cut-List properties are automatically created by inserting a part as a flat pattern into a slddrw file.

The sheet metal flat layout displays a bounding box that includes just the flat part. The bounding box has properties for size in the Cut-List table that do not appear in the PMI table. The trick is to copy "SW-Bounding Box Length@@@Cut-List-Item1@FMA Tote Box Frame.sldprt" and paste it into the File Properties Table (see

Figure 5

).

In Figure 5 we see policy and procedure in action. The name of the property "Cut Length" matches what our BOM table template is looking for in order to display our Cut Length. Note the pasted value of the Cut Length property from the Cut-List property table.

The hinge—see

Figure 6

—represents a few additional CAD tricks. The hinge model has three configurations—pin, leaf1, and leaf2. Only the pin is included in the BOM table. The leaf models are excluded from BOM. The pin has an extruded length of 18.75 in. It has an equation that is set to the extruded length. The equation value, which is the length, is used to set the value of the property known as Cut Length.

The hinge leaf configurations derive their length from patterns of cuts and extrudes that are not as easy to link to an equation as the extruded length of the pin is. That’s the entire motive in this hinge PMI demonstration.

Congratulations! You made it through a convoluted topic. Now for the problem of 18.75 versus 18.750, also referred to as the case of the trailing zeros in the BOM table. The newest version of this so—ware is required to display trailing zeros. The Detailed Cut list is the secret check box, but you can’t forget the document property to show trailing zeros.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

Reliable Leveling and Deburring.

Metal quality at its best. Deburring and edge rounding, double-sided in a single pass. Precision leveling for flat and stress-relieved parts and sheets. Optimize your downstream processing with ARKU.

www.arku.com
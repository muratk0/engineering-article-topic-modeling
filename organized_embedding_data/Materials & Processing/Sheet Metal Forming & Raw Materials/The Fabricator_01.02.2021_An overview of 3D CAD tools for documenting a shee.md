# An overview of 3D CAD tools for documenting a sheet metal design

[TARİH: 01.02.2021 The Fabricator]

Expertise » Precision Matters

Drop-down lists help with data entry, flat layouts, gauge selection, and bend radius selection

By

Gerald Davis

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

F

igure 1A

shows a 3D CAD model for a weldment. This one happens to be a tray for a tote box. The Feature Manager, which appears to the left of the graphics window, lists the components in this assembly. To the right of the graphics window, the Custom Properties form is shown. It is used to collect information that is otherwise difficult to model. Drop-down lists restrict what the CAD jockey can do; they also reduce typing mistakes.

For context in the suite of documents that we are preparing,

Figure 1B

shows step-by-step instructions for welding the tray together. Creation of this illustration was a topic in the previous episode of this column.

Figure 1C

shows a single component of the weldment—the tray’s frame. The task at hand is to create documentation for the fabrication of this single item.

As a CAD tip, the Feature Manager to the left in Figure 1C reveals how this tray frame was modeled. A design goal for this tray is symmetry. Thus, the Mirror tool works well. Just model half of the part and let the software do the rest of the work. Sheet metal modeling tools allow for automatic creation of a flat layout.

A subtle modeling tip is to locate the Base Flange sketch on the front plane. This Base Flange feature is extruded as a midplane feature. In combination with the mirroring technique, these actions put the world origin of the tray smack in the middle and are handy for creating

intuitive

mates in upper-level assemblies.

The general theme in any recommended modeling technique is to first satisfy the design goal and then consider the next person who will have to edit or maintain this model. Mating all of the right planes together requires premeditation.

Yes, the hems could be created in one step by selecting two edges. We postulate that the mirroring of the hem emphasizes the symmetry of the overall part. In this case, your method is the best method. We’re just kibitzing.

FIGURE 1A

A tray weldment is shown in the graphics window (center). To the left, the Feature Manager lists the eight components that go into this weldment. To the right, the Custom Properties form is used for data entry and retrieval.

FIGURE 1B

As a review, in the previous Precision Matters column in the January 2021 issue of The FABRICATOR, the weldment assembly was used to create step-by-step welding instructions.

FIGURE 1C

The frame for the weldment is shown in the graphics window. It’s almost the same as Figure 1A, but this is for a part, not an assembly. To the left, the Feature Manager shows the modeling history. To the right, the Custom Properties form presents appropriate dropdown lists to speed data entry.

Goof-proofing via Drop-downs

Drop-down lists speed and goof-proof the data entry chore. Custom Properties forms are created (by administrator-type people) with well-thought-out drop-down lists.

The Custom Properties tab in Figure 1C is similar to, but not the same as, that shown in Figure 1A. The software presents the data entry form associated with the file in view—part, assembly, or drawing. The difference, as far as the drop-down lists presented here, is that Figure 1A is an assembly and Figure 1C is a part.

This data entry drama has been in preparation for creating the drawing. Our drawing template has been designed to use the information that has been entered into the form (the data shown to the right in Figure 1C).

As we work through the preparation for making a drawing, the data entry task includes information such as the part number, description, material, tolerance, and finish.

Figure 2A

shows early and rapid progress in making the final 2D drawing. The title block has filled in instantly with the product manufacturing information. (Hurray for preparation!)

After we add a few dimensions, making sure solid and dashed lines are correctly shown, the 2D drawing starts to become useful. Please see progress in

Figure 2B.

Flat QA or Not

For sheet metal designs, flat layouts are foundational to fabrication. The CAD software makes it easy to verify that the part unfolds. That is an important design evaluation to be completed before releasing the 3D model to drafting and subsequent fabrication.

Including a flat layout view on the final drawing, an example of which is shown in Figure 2B, is a matter of policy and procedure for the CAD department. If the flat layout is something that will be inspected and subject to accept/reject decisions, then the flat layout should be on the control drawing.

On the other hand, if the finished part—the folded part—is all that will be subjected to quality assurance, then show only the folded part. Less is more when it comes to detail on a control drawing. Just enough is just right.

With that said, a specific business network could be efficient—faster estimating and quicker time in and out of CNC programming—with flats on the drawing.

This FMA tote box, as part of an apprenticeship program, may benefit from having the flats on the drawings. Reader suggestions are appreciated.

The crew on the production line probably knows more about current flat layout technology than the design team does. To help the production staff automate the unfolding of the part for production engineering, a recommended CAD process is to provide production with the 2D PDF drawing along with a 3D STEP file that shows the part you want to receive.

FIGURE 2A

After a view of the part has been created in the drawing, the data entered in Figure 1C fills in the title block automatically. The drawing template and the Custom Properties form are designed to work in concert.

FIGURE 2B

Progress! Dimensions and a flat layout view have been added to the 2D drawing. The dimensions shown within parentheses (11.028) are for reference and not to be inspected. If not to be inspected, why do they appear on a quality control drawing? The flat layout should not be on a production drawing, unless the flat clarifies, expedites, or is otherwise of value.

If the flat layout is something that will be inspected and subject to accept/reject decisions, then the flat layout should be on the control drawing.

Goof-proofing via Gauge Tables

If the accuracy of the flat layout matters to your design work, the use of a gauge table can goof-proof and speed the production of flat layouts. A gauge table exists in a dedicated folder as a spreadsheet. A gauge table is selected during the setup of the Sheet-Metal feature. It presents the CAD jockey with a list of allowed gauges and corresponding inside bend radii to choose from.

In our example, a gauge table for cold-roll steel was selected way back when

Figure 1C

was being created. Figure 2C shows what that selection of the gauge table looked like.

If you want to create perfect gauge tables for your production line, the help system that comes with the software is your best resource. A gauge table can be set up for each alloy, such as aluminum, steel, and stainless sheet, that is acceptable to production.

Figure 2D

shows the contents of an example coldroll steel gauge table spreadsheet. Selecting the table selects the K-factor. The K-factor that appears in the gauge table is specific to alloy and tooling.

The K-factor value shown in cell B4 in Figure 2D (0.4780) could be established by test bending coupons to prove the tooling’s behavior. Formulas also exist that can be used to predict the K-factor based on a known bend deduction.

The K-factor in the selected gauge table will be used by the system to unfold the entire range of gauges shown in rows 8 through 20.

The goal is to have rows 8 and beyond to list all of the gauges that the production line is likely to process. These rows will be used by the system to create a drop-down list for the convenience (i.e., goof-proofing) of the CAD jockey. The administrator that creates such tables will delete (or add) rows to ensure that only reasonable combinations of gauge and radius are selected.

Column C lists inside bend radii that the production line has tooling for. The radii separated by ";" will be used to create drop-down selection lists to make it harder for the CAD jockey to model with an unrealistic inside radius. Again, if the radius does not apply (i.e., should never be selected), simply delete it from this table.

Once you have the ideal gauge table for your production line, share it with collaborators so that their parts will unfold in ready-to-burn perfection. Our favorite gauge tables are available for download.

FIGURE 2C

Selecting a gauge table from a drop-down is easy once the workstation’s file-path settings are established. Once the table is selected, the system knows the K-factor to use for flat patterns. Drop-down lists present selections for gauge, radius, and relief type to use for modeling the sheet metal features.

FIGURE 2D

A gauge table is a spreadsheet with a specific format as shown. Selecting the table selects the K-factor to use. The rows that list gauges create the selection dropdown for gauges, and the available bend radii create the selection lists for inside bend radius.
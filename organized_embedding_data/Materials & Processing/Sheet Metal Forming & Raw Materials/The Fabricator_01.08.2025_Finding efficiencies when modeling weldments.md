# Finding efficiencies when modeling weldments

[TARİH: 01.08.2025 The Fabricator]

Precision Matters

Parametric links can simplify the process of design revision

GERALD DAVIS

FIGURE 1

A before and after of a two-sheet drawing is shown for comparison’s sake. Across the top is the short version, REV B, and across the bottom is REV C. Rev C is taller than Rev B. To make the change, the first thing we did was move a plane.

FIGURE 2

In the model to the left, the system comes with a top plane. We’re using that as the top of the surface that supports our design. A custom plane is created at a distance that is easy to control. In the model to the right, a 3D sketch is constrained to follow the new plane. Structural members follow the 3D sketch.

FIGURE 3

The model to the right shows how structural members are added using line segments in the 3D sketch. On the right, the Trim feature is used to resolve incorrect mitering problems.

T

he evolution of a two-sheet drawing is shown in a before-and-after format in

Figure 1

. Please don’t strain your eyesight. The details on these example drawings are offered to give an impression of how mainstream 3D CAD contributes to revising a typical 2D drawing.

This is pretty close to a real-world project. The drawing in Figure 1 specifies the welding requirements and the final overall size of the completed stand. The dimensional details for cutting and trimming of the structural components are found on separate drawings, as identified by the bill of materials (BOM).

For purposes of this demonstration, the revision from B to C was specified by an engineering change order (ECO), which calls for more height for the welded stand. In Figure 1, the highlighted section emphasizes that the stand was stretched to about twice its height, while no change was made to the overall footprint.

Administrator Jockey

As a CAD department effort, the task involves:

Retrieving the existing suite of CAD files

Saving those CAD files as the starting point for the next revision

Obtaining a change-order serial number

Editing the starting point 3D model to become the completed revision

Completing the revised 2D drawings (ECO, revision, tidy up the dimensions, etc.)

Releasing the production documents—PDF, STEP, CAD, etc.

The most time-consuming part of this process is administrative work—updating the change logs and completing the file management. After 3D editing was completed (changing one single dimension from 42 to 70), the 2D drawings updated automatically, just by opening them. It took about a minute of keyboard work on each drawing to update the revision notes and to adjust the layout of dimensions.

Parametric Secret Sauce

Parametric modeling is the secret sauce that contributes to the ease of revision. The CAD tricks shown in

Figure 2

include a 3D sketch that is constrained to a geometric reference plane (named LID SHELF), which in turn is constrained to control where the top of the stand is. The structural members of the stand are controlled by the 3D sketch.

CAD terminology uses Weldment to mean a suite of tools that are useful when modeling something to be made from intersecting sticks of raw material—metal tubing or wood, as examples. For this presentation, the sticks of raw material are rectangular steel tubing. Another loaded term is structural member, which means stick of raw material.

Modeling a weldment does not require the use of Weldment tools. As with sheet metal, the CAD system’s sheet metal tools are entirely optional. However, the use of the Weldment tools can be expeditious by way of automatic mitering, intuitive trimming, easy revision to material shapes, convenient generation of cut lists, and better weld symbols and callouts.

Trim and Extend

With the 3D sketch complete, the structural members can be added. The process involves selecting the raw material’s profile along with the line segments in the 3D sketch that the profile should follow. Here, a profile for 2-in. square tubing is in use, as shown to the left in

Figure 3

. To the right, the Feature Manager has been rolled forward to demonstrate how the Trim has been applied to resolve ambiguous intersections.

The Weldment feature automatically creates a Cut List that specifies the raw material lengths needed. For this demonstration, a BOM is used instead of a Cut List.

Parametric modeling is the secret sauce that contributes to the ease of revision.

FIGURE 4

After all of the structural members have been added and trimmed, the Save Bodies feature is used to create an assembly of parts (as shown in the model on the left). One of the parts created by the Save Bodies command is shown in the model on the right. That part file can be given product manufacturing information that will be used by the 2D drawing template.

FIGURE 5

The 2D drawing for a structural member is shown. The revision has been bumped. The revision table has been updated. The dimensions have been updated. This is repeated—by opening the document and updating the revision—for the other drawing that changed as part of this engineering change order.

BOMs Away

To set up for the use of the automatic BOM table, the bodies in the weldment are saved as part files that are, in turn, components in an assembly file. To the left in

Figure 4

, the Feature Manager has been rolled all the way forward. All of the structural members have been trimmed. The last feature in the multibody 3D weldment model is Save Bodies. The reason to do this is so that product manufacturing information (part number, description, revision, material, finish, etc.) can be saved with the part files in a manner compatible with the drawing templates and custom properties in use in our theoretical shop.

To the right, in Figure 4, one of the parts created by the Save Bodies feature is shown. Its Feature Manager history shows that it is parametrically linked to the multibody weldment.

The product manufacturing information stored in the part file (M00842. SLDPRT in this demonstration) is used by the drawing template to create the final 2D drawing in

Figure 5

.

Here’s a final CAD tip: Copy the prior-revision product manufacturing information from the old version of the part file before overwriting it with the Save Bodies feature.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Webinar Series

Tuesday, August 26

2 PM ET 1 PM CT

Lights Out Machining

Discover the Future of Waterjet Automation with Biesse

Optimized Cutting Performance:

Cut up to 46% faster than traditional 60-kPSI systems at 78 kPSI, using 30% less abrasive. See how optimized parameters drive measurable gains.

Minimize Downtime with Predictive Maintenance:

Integrated oil circuit sensors, temperature monitors, dump valves, and intelligent alerts detect potential failures before they disrupt production.

Advanced Diagnostics System for Smarter Operation:

An intuitive on-pump HMI and WHMI remote support provides real-time system visibility and remote troubleshooting —freeing up skilled labor.

Whether you’re managing a production floor, making capital investment decisions, or preparing the next generation of technicians—this session is for you.

Don’t miss out! Scan here to register today!

About the Speaker

With decades of technical experience in advanced cutting systems,

Jim Fields

will share practical insights on implementing automation, maximizing ROI, and staying competitive in a fast-evolving market.
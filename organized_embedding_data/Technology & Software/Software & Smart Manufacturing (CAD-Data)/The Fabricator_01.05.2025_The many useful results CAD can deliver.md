# The many useful results CAD can deliver

[TARİH: 01.05.2025 The Fabricator]

Precision Matters

Choose the design tools that meet your needs

GERALD DAVIS

F

igure 1

presents a screenshot of a fabrication drawing. Such 2D drawings are often one of the deliverables (aka useful results) from CAD effort. As part of a quality control program, part number and revision control of specification help to minimize random outcomes.

FIGURE 1 A 2D drawing is a quality assurance document. It only takes a few clicks to create such a drawing, largely because of the prior CAD work required. If you’re selecting CAD software, drafting standards, tolerancing, revision control, and tradition might refine the selection.

Most importantly, the revision control/document control process assures that improvements are implemented without surprise. The specifications in this example drawing include a bill of materials table (BOM) with corresponding balloons in an exploded view.

If the goal in your CAD project is the finished 3D object, you don’t really need a part number or revision. You also don’t really need CAD software that supports drafting and tolerancing standards.

The brand of CAD used here presents the 3D model as a projection on a video screen. It’s very useful for development and prediction. Once that 3D object exists, the video screen can be replaced with paper or a PDF to document the expectation.

A workflow to produce such a quality assurance document begins with decision-making regarding design commitments. Before even launching the CAD, a statement is made regarding the desired functionality and ideal capability, along with a general description of look and feel.

Here’s a side note about architectural versus mechanical habits: Decades of legacy exist in CAD libraries, and other organizations have some tradition when it comes to CAD software. If you are selecting software, be compatible with customers and with your suppliers. Ask them what they prefer.

Getting Down to Business

The actual CAD work—the production of a virtual prototype—starts with gathering models for the various components. Downloaded CAD models can be time-saving. As a CAD format, STEP is simply ASCII text and zips into a small size nicely.

The advantage of native CAD formats is support of parametric modeling (the holes and bolts constrained to always align as the design evolves). Other CAD formats are dumb models.

The advantage of an exchange CAD format (STEP, DXF, IGS, or STL) is that they strip all of the development history and result in a clean (aka dumb) model.

Downloaded models also can burn some of the time they save. They might arrive with too much detail; helical threads on screws, for example, might be extraneous detail. Or they can arrive with too little detail, like the door on the box being stuck in the closed position. Accordingly, the CAD workflow includes massaging of the imported models.

In this example, the box is imported as a multibody part. That multibody was edited to feature two configurations—open and closed. An angle mate was configured to position the door body at 0 degrees relative to the box when closed and at 95 degrees when open. Selecting the right configuration of the multibody part opens or closes the door.

Virtual prototyping includes assembly work—putting the components together so that they look and behave in a realistic manner. With the box inserted into the assembly as a starting point, the other components are positioned relative to it. The various images in

Figure 2

are the result.

With the components appropriately constrained, Assembly-Cut features are applied to create holes. In this example, the sketch to cut the holes is used to constrain the location of the switch and conduit. As an alternative, the holes could have been constrained to follow the location of the switch or conduit.

FIGURE 2 The prior work required for the drawing in Figure 1 is shown. As part of design refinement, the model can be animated and posed to demonstrate the feature and function.

As mentioned, the imported model for the box was massaged to allow the door to be positioned. That change to the model did not change any of its provenance or sourcing. The part number, description, and physical characteristics remain the same.

Cutting holes (for the conduit and switch) makes the box unique to this project. It alters the physical and thus the part number and description. By using an Assembly-Cut, the off-the-shelf import remains pristine for use in other projects.

We’re building a virtual prototype, and the mates we add to constrain motion provide realism and help with posing the model. In this case, the door swings. To pose the model’s components for the exploded view, the CAD software offers a tool for that purpose.

The production of an animation—or a movie—for design review is a matter of a few mouse clicks once the constraining mates have been added.

Further realism is gained by adding material and finishes to the component models. Information about the mass or weight of the assembly can be surprisingly useful during design review.

With the model posed, exploded, and looking good, it is a good time to verify that the physical design and function are tracking well. Review of the 3D model might reveal substantial changes before moving ahead.

To help with the review of the design, animations and glam shots are prepared. Figure 2 presents a collection of views of the project. The 3D model has been assembled, posed, and reviewed.

Time for the Unveiling

Behind the scenes, data entry has been completed. The part number and description have been assigned. We’re ready to create a 2D drawing. Fortunately, the process of adding views and dimensions to the drawing is largely automatic. All that’s needed is a drag-and-drop process with a bit of typing.

The main deliverable is a feature-rich 2D drawing that can be fully revision controlled. It’s very easy to produce once the other deliverables—glamour shots, animations, BOM table, and a library of CAD models for future projects—are completed.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.
# A quick overview of three CAD modeling techniques

[TARİH: 01.07.2026 The Fabricator]

Precision Matters

Sometimes it’s a choice between opportunity cost and elegant modeling

By

Gerald Davis

M

ainstream 3D CAD offers many alternative modeling techniques that can be combined to arrive at about the same ending point. The "best" modeling technique is a moving target, but completing the model without delay is a bonus. Opportunity cost (time to completion) always should be minimized.

To that end, it is good to have in mind the advantages of various modeling techniques—useful combinations of CAD tools. Here, we review three: a revolved body, several extrudes, and a surface model.

FIGURE 1 A sketch of the cross section of a revolved body might show a best way to model the part. All of the information is contained in a single sketch. However, the history of the design’s evolution is not evident.

FIGURE 2 A series of modeling steps (boss-extrudes) creates a model similar to Figure 1, but with more history on how the design evolved. This might take a bit longer to invent, but it might also be easier to revise and perfect. The notes (see yellow highlight) help with assimilation.

Useful implies several merits: ease of design development, ease of revision, speed of rotation under the mouse, speed of completion of the project, and perhaps, ease of collaboration with other CAD jockeys.

THE REVOLVED SOLID IS SIMPLE

Figure 1

shows a design for an axle hub. From the viewpoint of the computer (that is to say, software execution time), a revolved body is reasonably speedy. Most of the information required by the software to create the body is contained in a single sketch. If this component were to be used many times in a larger assembly, the rebuild time might be an important consideration, although the freeze tool can make modeling for rebuild time irrelevant. (The freeze tool is a performance-boosting tool that locks specific features in the Feature Manager design tree to exclude them from model rebuilds. It speeds rebuilds because it excludes complex surfaces, intricate patterns, or heavy features from the rebuilding process.)

It is good to have in mind the advantages of various modeling techniques—useful combinations of CAD tools. Useful implies several merits: ease of design development, ease of revision, speed of rotation under the mouse, speed of completion of the project, and perhaps, ease of collaboration with other CAD jockeys.

FIGURE 3 Surface modeling (as a technique) allows control over each face of the model. When curvy swoops are needed, modeled surfaces can be the solution. Here, surface modeling is more entertainment than important to mission. The yellow highlight emphasizes notes that were added to explain the modeling intent.

Is a revolved body an efficient technique from the point of view of the CAD jockey? Perhaps having the controlling dimensions in a single sketch is more important than merely convenient. The sketch for the revolved body, however, is a cross-section, not entirely intuitive during design review.

In the example in Figure 1, the revolved sketch reflects the entirety of the finished design. All of that information about the finished design may not have been available when the sketch was started. Perhaps the sketch was edited and revised in several stages; however, the sketch does not give much of a hint about how the design evolved.

THE BOSS-EXTRUDE IS BOSS

Figure 2

shows a similar solid body, but this one has a more detailed history (more modeling steps, or in this case boss-extrudes) that appears in the Feature Manager. Each modeling step captures an aspect of design exploration.

It requires a bit of typing, but the meaningful naming of the features in the Feature Manager makes it easier for your future self (and others) to assimilate the model. Notes and comments can make later design revisions more efficient.

A glance at the feature history reveals that the design started with a hollow cylinder. (Rolling back the time bar is sometimes fun!) That starting point reveals design constraints and intent (inside and outside diameters).

The length of the hub was at one point a design consideration. As the design evolved, a stopping face was added. A centering hub was then needed. A relief groove was then added to avoid interference with the mating part.

To eliminate the need for support structures when 3D-printing the part, a chamber was added to the nonworking side of the stopping flange. The design history ends with the addition of chamfers to help with assembly in the final installation.

BEAUTY JUST BENEATH THE SURFACE

Figure 3

is a demonstration of surface modeling. This example mostly serves as a reminder of what goes on behind the scenes when modeling with solids. The surfaces of this design are prismatic—not much need for curves and swoops that surface models are useful for.

The inside and outside cylindrical surfaces of the hub serve as the starting point. These surfaces were extruded from a sketch, very much like extruding a solid body. The outer face of the cylinder was split and offset to create the flange. Several modeling steps were used to create the surfaces of the groove. A boundary surface takes care of the chamfer for 3D printing.

Planar surfaces close off the ends of the hub to form a closed volume. After deleting a few overlapping features, the surface body was knitted into a solid body. The solid body is convenient for the addition of the little chamfers.

If you have any comments or questions, please send them to

ddavis@fmamfg.org

.

Editor’s Note: Supporting CAD files for this column are available for download at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.

GERALD DAVIS

THEFABRICATOR.COM

› AUTHOR ›

GERALD-DAVIS

EXPERIENCED: Thousands of Successful Projects

DEPENDABLE: Free Lifetime Customer Support

REPUTABLE: 5-Star Reviews + Extensive Reference List

ACCOUNTABLE: Sold, Designed & Supported Factory-Direct

STABLE: Same Ownership for Over 20 Years

888-770-0021

reliantfinishingsystems.com

Patent No. US 10, 576, 588 B2

Patent No. US 11, 426, 826 B2

Patent No. US 12, 017, 308 B2

Patent No. US 12, 226, 858 B2

Precision in Every Line, Power in Every Layout.

For the fabricator looking to maximize their production time and profits, the Lightning Rail is a smart decision. Eliminate the countless manual labor hours involved in laying out handrails, stair stringers, trusses, and more!

Cut fabrication time by more than 50%

Ensure the highest level of accuracy

Boost your profit margins

Layout complex geometry in seconds

Designed to replace your existing fabrication table

603-402-3055

AutomatedLayout.com

OCTOBER 2026: EXPERIENCE THE MACHINERY THAT JUST WORKS

AND WE’LL BE AT FABTECH TO PROVE IT.

DEMO THIS PRESS BRAKE LIVE AT

#C4610

AUTOMATION-READY

FAST SUPPORT

EASY TO USE

BUILT TO LAST

NO SURPRISE FEES

Simple transparent pricing.

USA Made Since 1898

READY FOR AN EQUIPMENT PARTNER WHO GETS IT?

SCAN TO SEE THE LATEST DEALS

Talk with our team today!

www.e-ci.com
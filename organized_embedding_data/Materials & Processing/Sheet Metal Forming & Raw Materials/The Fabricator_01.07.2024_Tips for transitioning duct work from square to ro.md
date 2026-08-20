# Tips for transitioning duct work from square to round

[TARİH: 01.07.2024 The Fabricator]

Precision Matters

Modeling the part the way it is built makes the CAD easier to understand

Gerald Davis

W

e start at the end with a sheet metal project as presented in

Figure 1A.

The purpose of this bit of transition is to duct from square, approximately 36 in., to round, approximately 12 in., in the span of about 18 in.

This funnel is to be stout. It will be banged about by things as big as baseballs. The material and finish are proven (borrowed from related equipment). It will be 14-ga. mild steel with a powder coat finish to slow down the rust.

The CAD planning for this project considered three modeling techniques: a single part with multibody features, an assembly of individual parts, or as a part with a single body.

FIGURE 1A To transition a duct from square to round in four pieces in CAD modeling, the CAD jockey mimics the way the part would be fabricated—four identical corners welded into a funnel.

FIGURE 1B The drawing for the funnel takes advantage of the things an assembly can do, such as offer an Exploded View. An assembly also can populate a BOM table and catch item balloons. This is sheet one of three.

FIGURE 1C This drawing provides size specifications for quality control and instructions to welders regarding weld bead requirements. This is sheet two of three.

FIGURE 1D A drawing for a sheet metal part uses Section A-A to show the size of the bend (0.60 in.) that will get welded. It is implied that this is typical of both bends in the flat layout.

Multibody parts are excellent for parametric modeling—making sure all components behave well as the dimensions are edited. The drawbacks to multibody, if any, are with the behavior of the resulting virtual prototype.

The animation, the bill of materials (BOM) table, and the Exploded View features are subtly different between multibody parts and assemblies of parts. It’s basically a static-vs.-kinematic utility. Assemblies are great for moving inventions; multibody parts are great for the stationary.

How subtly different? Looking at a multibody, you might wonder what is wrong with your mouse until you remember that it is not an assembly. The multibody does not have a BOM; it has a Cut List. These nits being picked are part of the learning curve and overhead for project maintenance.

The merit of a single-body part is a short learning curve for anyone doing the editing. The demerits include massive amounts of detail as a stream of consciousness exists in the Feature Manager, laboriously created BOM tables, and pseudo-animation by stop-motion freezeframe edits. This project is not suitable for a single-body model.

Even though this project is relatively simple, the sheet metal aspect, which requires a flat layout and bending instructions, calls for an assembly as the modeling technique. In this example, all four of the sheet metal parts are the same item.

The CAD technique chosen here mimics how the funnel would actually be fabricated, as an assembly of four identical corners. Welding is the planned method of assembly.

Duct Migration

Figure 1B

shows a 2D drawing featuring an Exploded View of the 3D model. The convenience of exploding reveals part of the reason why an assembly of parts was chosen as a modeling method. Huzzah to the convenience of automatically generating a table that lists the parts required for the assembly. The BOM table, in this example, has only one item with a quantity required of four.

FIGURE 2A A lofted bend sheet metal feature requires two sketches. This is Sketch1. An arc centered on the origin defines the round end of the lofted transition.

FIGURE 2B This is Sketch2. A 90-degree corner centered on the origin defines the square end of the lofted transition.

FIGURE 2C This is a screenshot of a lofted bend feature configured with four bends. It is using Sketch1 and Sketch2 seen in Figures 2A and 2B, respectively.

FIGURE 2D Holes are punched in the flat. The use of CAD tools Unfold and Fold is demonstrated in the Feature Manager’s list. Unfold the model, add holes with the Hole Wizard, and then Fold the model.

Within the title border in the lower right corner of Figure 1B, sheet one of three indicates that this is a multisheet drawing. Sure enough,

Figure 1C

reveals sheet two of three. Here, target dimensions for the welded funnel are shown along with welding notes. The fabricator using this drawing has the option of either stitch welds (1 in. long every 3 in.) along the edge of the seams or spot welding on 3-in. intervals.

Drilling down to further detail, we turn to

Figure 1D

, the individual corner piece. This is sheet three of three for this drawing. The drafting technique is suitable for use in a sheet metal shop.

The CAD system automatically generated the isometric and thirdangle projection views, with dashed lines to show bend direction. This is very routine sheet metal activity. Perhaps the fancy drafting trick is to use Section View A-A to show the size (0.60 in.) of the 90-degree bend that becomes the welded seam.

The flat layout is generated by the CAD system and gives the press brake crew a hint about the goals for bending. This is an exception to a rule. Flat layouts on production drawings imply that the flat is as important as the formed product; don’t specify if you don’t want people to take time to verify.

Turning from drafting to sheet metal modeling, it is just a few steps to model this round-to-square loft. All we need to create it is a pair of sketches—one to show the round and the other to show the square size. Each sketch is on its own plane. Their separation is how we control the 18-in. distance for the transition.

An arc sketched on a plane does the job for the 11.5-in.-dia. end (see

Figure 2A

). Note that the arc is centered on the origin as a convenience. This becomes Sketch1, the default name the software gave to this sketch as it was created. In this case, it is a suitable name.

Unlike the default sketch name, the default Top Plane used by Sketch1 was renamed from Top Plane to Top Plane – ROUND END OF FUNNEL to remind our future selves of intent.

Figure 2B

shows Sketch2, the square end of the funnel. We could get by with just sketching two straight lines (one-fourth of the square). However, the addition of a radius between the lines helps the sheet metal fold more like the real deal. As with the arc in Sketch1, this sketch is centered about the origin.

The CAD magic is happening in

Figure 2C.

This is where we are setting up a sheet metal lofted bend to use the two sketches along with our decision regarding the number of bends. Four bends are just right for this project. More steps would make a smoother transition, but they also add expense and difficulty at the small end.

Next, we add a few sheet metal flanges to finish out what the lofted bend started. Mounting flanges are modeled as a separate feature from the seam flanges, rather similar to the reality of setting up a press brake. That is to say, all of the same-size flanges happen at the same time.

Our inner CAD jockey is showing off in Figure 2D. A close study of the Feature Manager in

Figure 2D

shows the use of Fold and Unfold in a sheet metal model.

After the Unfold, a Hole Wizard drills a couple of 0.5-in. holes. Then Fold restores all of the bends. The result is holes on different planes from a 2D sketch. Now you know how eight holes in Figure 1A were modeled—one little sketch with two points. There are times when Fold and Unfold can be a significant time-saving trick.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.

Gerald

would love for you to send him your comments and questions. Please send your questions and comments to

ddavis@fmamfg.org

.

Discover the World of High-Productivity Double-Articulated Weld Booms

Complete Area Coverage - No Dead Zones!

Effortlessly More from Weld to Weld

Integrated Fume Extraction (option)

Robust Design-Buit to Perform

Increased Productivity

Increased Safety

Andersen Industries •

www.andersonmp.com/veicpro

• 160 760-246-8766

One Stop For All Your Needs

Metal Fabricating, Machining & Robotic Welding

30KW Laser Cutting with Bevel

Specialty and Production Machining and Fabrication

Wire EDM, Waterjet Cutting and Robotic Welding

Locations: Jackson, Dyersburg & Camden, TN

WE ARE A FAB40 COMPANY

cupplesjandj.com

Cupples’ & Co. Inc.

Contact us today for a quote:

rfq@cupplesjandj.com

• 731-424-3621

For employment send resume to:

jobs@cupplesjandj.com
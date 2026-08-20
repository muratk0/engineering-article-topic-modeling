# Working with flat patterns of coined corners

[TARİH: 01.01.2026 The Fabricator]

Precision Matters

CAD can unfold coined corners if they are modeled using a Swept Flange

By

Gerald Davis

T

he previous episode ("Sheet metal CAD skills applied to leather," The Fabricator, December 2025, p. 24) presented a CAD technique that allows coined sheet metal corners to seem to be unfolded. For demonstration, leather was the target material instead of sheet metal. Although effective, the tip was more of a trick than a practical workflow.

That is to say, the merit of using configurations to suppress or unsuppress flattened sheet stock does not require a professional-level license of CAD software. With an adequate license, the following workflow is recommended for more intuitive modeling.

The brand of software being used for this episode includes a CAD sheet metal tool called Swept Flange. As the name suggests, a Swept Flange is very much like any sweep in terms of modeling requirements. It involves a profile and path. That aspect of modeling the Swept Flange works regardless of license. The resulting sweep behaves like a flange in that it can unfold if you have a fancy license.

The CAD’s help system shows examples of sheet metal items (in the style of HVAC) that would be easy to fabricate using a sheet metal folding brake as opposed to discovering impossible-to-fab corners using a V-die setup in a press brake. Going beyond the help system, let’s consider using the Swept Flange to replace the CAD trick from the previous episode.

To stretch the meaning of design for manufacturing (DFM), we continue the theme in leather craft. The manufacturing process we’re designing for is entirely manual using paper patterns, hammers, punches, and needles.

SWEPT FLANGE FOR FLATS

Figure 1A

shows the setup for a Swept Flange.The profile sketch represents only the inside edge of the bent target flange. The path for the sweep is made by selecting the edges of the base flange in this example.

The addition of a top flap and needle holes completes the model (see

Figure 1B

). Compared to the complex workflow in the previous episode, the Swept Flange is a blessing, both in terms of time to completion and accuracy of result.

A fillet is added to the inside corners. As a DFM consideration, the tool on hand is 5/32-in. radius, so the modeled fillet radius is 5/32 in. Sadly, this 3D fillet will not unfold, so it is configured to be suppressed in the flat. Similarly, a 2D fillet is added to the flat to be suppressed in 3D.

FIGURE 1A

The Swept Flange requires a sketch for the profile and edges to select for the path of the sweep. The resulting flange can be unfolded.

FIGURE 1B

The model from Figure 1A has additional details added—a flap and needle holes. Fillets also are added to stress-relieve the corners. In the Default configuration, the 3D fillet is active. In the flat configuration, a 2D fillet is active instead.

FIGURE 1C

In the spirit of design for manufacturing, the target fabrication process has a six-prong tool, so the design tries to needle things in multiples of six. The distance between the tool’s prongs leads to adjusting the size of the box to maintain convenien needle hole spacing. Symmetry works for left and right ends of the box.

Figure 1C

shows the end panel in the flat configuration. As part of the DFM, a six-prong punching fork will be used to make needle holes.

NEEDLING THE DESIGN

The stitching around the top flap is merely to reinforce the glued sandwich of inner liner and outer leather. Since we have some artistic liberty, the decorative layout for stitching around the flap tries to minimize the number of punch strikes. Note that there are multiples of six holes along each vertical side. DFM helps prevent strokes (with the hammer, at least).

As mentioned in the previous episode, the size of the box was adjusted to accommodate the straight-line punching distance between the prongs in the fork. Going around the corners, the distance between holes changes based on how the material compresses during forming.The design goal is to maintain equal spacing and symmetry so that the same one-to-one pattern works for the left and right end panels.

There are a few CAD tricks going on in Figure 1C. Note that many of the features listed in the Feature Manager have been renamed (for example, Cut-Extrude5 stiff) to give a stronger hint of the feature’s function in the model. This CAD tip might help the future-self reassimilate the model when editing the model.

The rectangle appearing in the middle of the part is merely for transferring the location of a stiffening panel during the gluing stage. The location was modeled as a pocket so that the outline would show up in this flat pattern for transfer to the leather.

AIM WELL FOR BETTER BOXING

Figure 2A

shows an available tool being aimed using a fillet in the flat pattern. As noted in Figure 1B and shown in Figure 1C, the inside corner fillets in the flat pattern will not fold.

FIGURE 2A

The fabrication process uses transfer punching. An accurate flat layout helps ensure accurate punching.

FIGURE 2B

The punching tool has sharp points on each diamond-shaped prong. Aiming the points at small dots is relatively easy. Design for realism is not always DFM.

Similarly, the 3D fillet in the formed condition will not flatten. The fancy CAD trick is to use configurations to control which fillet appears when.

Figure 2B

shows the fork being aimed at the needle-hole dots on the paper pattern. The alignment of the paper with the leather is an important tolerance variable.

Figure 2C

shows the aiming opportunity for the punching tool when the dots are replaced with diamonds. The thought was that diamonds on the flat layout help with planning the decorative layout. In practice, aiming is more important than decorative imagination.

FIGURE 2C

To be more realistic, diamonds on the flat pattern can show where to place the punch. However, the aim at the interior of a box isn’t as easy as aiming at a dot. Groping for realism can interfere with production.

FIGURE 2D

It is possible to mirror the diamond shape, resulting in a backwards target. From practical experience, this makes aiming even more difficult. Again, DFM says dots are dandy for the aiming of a hand-held punch.

FIGURE 2E

The one-to-one flat pattern for the frame of the box is larger than the printer’s sheet size. This requires printing a sheet, moving the view on the sheet, printing a sheet, and then splicing and trimming the paper template. A larger-format printer would improve the accuracy of the process. DFM reveals opportunities for future improvement.

FIGURE 2F

Several boxes were produced using copies of the same paper templates to test the accuracy of CAD’s prediction. The worst box is within two material thicknesses, and the best box is within 1/32 in. Transfer punching is the main contributor to error.

The prongs on the tool are diamond shaped to lance a slit for the convenience of passing two needles through from opposite directions. The needles end up in the long end of the slits. If one is consistent with the "leading" needle in the slit, the resulting zig-zag of the stitches is part of the charm of the saddle stitching process.

Even though they are evocative of what the finished part will resemble, hitting the center of a diamond with a lancing punch tip isn’t as easy as hitting the center of a small dot. The author planned to present the CAD tip of using the Hole Wizard to create a pattern of diamonds but had a change of heart. The dots are dandy.

To critique the excessively fancy, we note that the diamonds are directional. It is possible to print diamonds that are going in the opposite direction from the punching tool’s imprint (see

Figure 2D

). The backward diamonds should not be any more difficult to aim at than the forward diamonds, but from practical experience, they create uncertainty.

In

Figure 2E

, the flat pattern for the main frame of the box is shown to be larger than the sheet size in the printer. The printer in the shop only handles A-series paper, so the one-to-one paper template process includes printing a sheet, dragging the drawing view of the flat to the other end of the paper, printing that sheet, and then splicing the two sheets together. That’s another tolerance variable (opportunity for improvement) in the process being presented.

For this hobby project, the use of CAD to predict and plan for the behavior of leather proved to be reliable. The sewing process benefited from the planning. The final product proved to be reasonably accurate.

Figure 2F

shows six samples that were produced using copies of the same paper templates—all finished dimensions range within a couple of material thicknesses. The main variables are due to errors in transfer punching. The best box is very close (with 1/32-in. tolerance) to the designed intent.

GERALD DAVIS

THEFABRICATOR.COM

› AUTHOR ›

GERALD-DAVIS

Gerald Davis

would love for you to send him your comments and questions. Please send them to

ddavis@fmamfg.org

.

Trust the leaders in Dust and Fume Extraction

Superior performance. Proper engineering. Sensible pricing.

Get your dust and fume extraction solutions from one of Canada’s most trusted manufacturers with over 30 years of experience.

Industrial Vacuums

Dust Collectors

Wet Collectors

Downdraft Tables

Fume Aims

Vac Ready Welding/Tools

Contact us for a quote

1-800-365-DUST (3878)

info@eurovac.com

www.eurovac.com
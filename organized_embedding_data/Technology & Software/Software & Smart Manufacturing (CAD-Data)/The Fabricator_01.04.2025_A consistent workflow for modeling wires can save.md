# A consistent workflow for modeling wires can save time

[TARİH: 01.04.2025 The Fabricator]

Precision Matters

There’s no need to create that model of a wire from scratch every time

GERALD DAVIS

F

igure 1

presents a switch with wires posing as a CAD model. Most of the components were downloaded from an online hardware store. The wires are the task at hand. They need to be modeled as individual parts.

This brand of CAD software offers an add-in to make the routing and modeling of such path-driven objects more menu-driven and controllable. In a team environment where any model can be edited by anyone, the add-in brings discipline and routine that is a definite benefit.

For the occasional virtual prototype, several tools and workflows are available to model wires. The recommendation here is to establish a routine for modeling them. You’ll thank yourself later when you are tasked with decoding the workflow that made sense at the time.

In the brand of CAD used here, these wires are modeled with a menu selection titled Sweep. These sweeps are defined with a pair of sketches—one sketch for the profile and one for the path.

The profile demonstrated is a 2D sketch of a circle with a diameter of 1.29 mm (16-AWG copper wire). As part of the routine, the sketch is on the wire’s front plane and is centered on the wire’s origin.

Here’s a workflow tip: When mating the wire in an assembly, reference to the wire’s origin or a sketch feature is likely to persist (compared to a face or edge) as the model is edited and rebuilt.

The wire’s path, unlike the 2D profile, is a 3D sketch. One end of the 3D sketch is constrained in the center of and perpendicular to the profile sketch.

These required sketches take a few mouse clicks to set up, so it could be done from scratch for every wire model. Yeah, that should be a last resort. Embrace the idea of a template part, instead.

For this demonstration, an existing model for the wire serves as a starting point. When that template model was created (with the Save-As command), all external and dangling relationships were removed. Not all templates are created equal; some dangles might require attention.

Our workflow is to edit the 3D path in the context of the assembly. The model for the wire is mated to constrain the end with the profile sketch.

Figure 2

presents the evolution of the 3D path. Straight-line segments are added as needed to allow for sufficient bend radius. Then the fillets are added to "bend" the wire.

To be fancy, the insulation is modeled using the same path as the copper. The profile sketch for the insulation is offset from the diameter of the copper. It follows the gauge of the wire. As a finishing touch, the insulation can be stripped using the Move-Face command (see

Figure 3

).

To create a trace-color in the insulation, twist the profile along the path. The profile will need line segments to create a surface that can receive color treatment.

For the occasional virtual prototype, several tools and workflows are available to model wires. The recommendation here is to establish a routine for modeling them. You’ll thank yourself later when you are tasked with decoding the workflow that made sense at the time.

FIGURE 1

A model of a switch is posed and exploded to show the connection of a few wires. These wires were modeled as sweeps. The workflow for mating and modeling such sweeps is yours to make into a routine.

FIGURE 2

The path for the wires starts as straight-line segments. The vertices are filleted to represent bends in the wire. Note that one end of the wire is constrained with mates, which coincidentally aligns the end of the 3D sketch.

FIGURE 3

Insulation profile is offset from the copper to give it thickness. The profile can be twisted along the path for fancy traces. The path is the same 3D sketch as used for the copper. Move-Face works to strip the insulation.

FIGURE 4

"First in, last out" is the rule when it comes to deleting fillets. As long as the controlling fillet is present, its children can retain their vertex as they get deleted. If the controlling fillet is gone, the children are deleted as arcs, leaving gaps in the path.

In Figure 2, the fillets were added to replace the sharp vertices of the 3D line segments. These fillets represent the bends in the wire. Create all of these bends in one step using the Fillet command. The goal is that they be equal and dependent upon the controlling fillet. That’s the first one and shows the radius dimension.

Safe and credible wire bends are necessary. However, when editing the location of line segments in the path, these fillets may (more like will) flip tangency and become a nuisance.

Here’s a CAD tip: When deleting 3D fillets, delete the controlling fillet last. First in, last out.

Figure 4

shows the pop-up message that appears when the control is being deleted. The warning appears because, once the controlling fillet is gone, any orphaned fillets will be deleted without retaining the vertex they were based upon. This leaves a gap in the path. That’s extra mouse clicks. Gnar.

Gerald would

love for you to send him your comments and questions. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: The CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.
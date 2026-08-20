# CAD shortcuts for a weldment

[TARİH: 01.07.2021 The Fabricator]

Expertise » Precision Matters

Pulling together a BOM table and adding holes to a cart frame

By

Gerald Davis

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

dand@thefabricator.com

.

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

T

he cart shown in

Figure 1

was rolled about in the previous episode. The four little casters skate nicely. Fortunately for this episode, the design needs to evolve. It lacks a vise. Out of concern for load and impact, two of the casters are to be replaced with hard wheels.

Here’s a CAD tip: A familiar object gives scale and lends meaning when presenting a design. The myriad tools on the cart in this example are perhaps distracting clutter. Moderation in all things.

Virtual Prototype

The cart, without the clutter of accessories, is shown in

Figure 2A

. In the real world, this is how the cart would be assembled.

To prioritize CAD labor, the casters and wheels, axle caps, and vise are off-the-shelf items. They will get the minimum amount of effort. The 0.5-in.-diameter axle is cut to length but is otherwise common steel rod. The documentation for these items is primarily textual information to support procurement. Downloaded or representative models work expeditiously.

The thrill, in terms of design fidelity, is the welded frame.

Figure 2B

picks up where the previous episode left off. We now know where the missing holes should be. Modeling holes in a weldment is not difficult, but many paths can be taken through the CAD menu of tools, all delivering alternative outcomes. Here we contrast assembly with multibody modeling.

FIGURE 1 Weldment CAD techniques used to design this cart with four casters were discussed in the previous episode of Precision Matters.

FIGURE 2A The connected components of the cart are modeled as an assembly of frame weldment, casters and sockets, wheels, axle and axle caps, and vise.

FIGURE 2B The weldment does not have holes for mounting the vise, venting the braces, or installing the axle. The Hole Wizard is a recommended solution to this problem.

Let’s pause for a moment to discuss terminology: In the brand of CAD being demonstrated, CAD assemblies are like matryoshka nested dolls. Components that make up assemblies can be assemblies or parts. CAD weldments start out life as multibody parts, a different way to represent a real-world assembly.

As with any multibody part, the bodies in a weldment can be saved to external files to create an assembly of parts. This results in components that are parametrically linked to the weldment part.

BOM Table Versus Cut List

Figure 3

shows a drawing for a multibody weldment. The table shown is an inserted Cut List. It is generated from the bodies in the part. Cut List tables have power that bill of materials (BOM) tables lack—an automatically generated list of lengths.

The Cut List table displays information from solid bodies found in a part. This is distinctly different from a BOM table, which displays information from the components found in an assembly. As a matter of drafting standard/style, the BOM table and assembly method are perhaps more familiar than Cut List and multibody documentation.

We have a choice between Cut List and BOM table. Either way, the weldment needs holes.

Do these holes get drilled before or after welding? The CAD brand being discussed has a system setting that makes a distinction between as welded and as machined. If automatic is preferred, when a weldment is created, the CAD will create two configurations. The idea is that features that are added after welding are suppressed in the as welded configuration and are revealed only in the as machined configuration.

As Welded or Machined

In

Figure 4A,

the Default <As Welded> configuration has been selected. As foreshadowing, in yellow highlight, the features that create holes postwelding have been suppressed. They never happened but could. Time traveling in CAD is fun.

In

Figure 4B

, the Default <As Machined> configuration has been selected. The holes not in Figure 4A are no longer suppressed. The CAD trick inspiration for this episode has been revealed: The Hole Wizard is a recommended tool for modeling holes. In the author’s opinion, the Hole Wizard reduces mystery in future edits. As a bonus, and the pattern of holes that the Hole Wizard creates might prove to be unexpectedly useful for patterning of related hardware—snap caps to hide vent holes, perhaps.

Saved Bodies: The Path to BOM

If the Cut List table approach to documentation will suffice in your shop, then the sldprt as multibody weldment cut list technique in Figure 3 is perhaps the end of this episode. Not shown are the several drawing sheets to show the completed size of the frame with hole locations.

FIGURE 3 This drawing sports a Cut List table that automatically lists the required lengths for each item. This may be preferable to a BOM table.

FIGURE 4A When weldments are created, the software makes configurations named as machined and as welded. This demonstrates use of those configurations to show before and after welding. Here the holes are suppressed in the as welded configuration.

FIGURE 4B This is the as machined version of Figure 4A. Use configurations to show before and after welding. Here the holes are unsuppressed in the as machined configuration.

If a BOM table is needed instead of a Cut List, the bodies in the weldment can be "exported"—saved as external part files and used in an assembly. Then that assembly can be used to make a BOM to replace the Cut List.

The tool that saves bodies can be commanded to create an assembly of the parts it creates as it creates them.

Figure 5A

is a screen shot of the setup used to create the assembly. The setup includes assigning names to all of the sldprt files that will be created. Of particular usefulness in the Save Bodies tool is the checkbox that recognizes identical components. When checked, the resulting BOM is tidy. The same item is used twice instead of as two individuals that are twins.

Figure 5B

shows the newly created assembly. Features in the as machined configuration have been inherited from the weldment’s bodies. If we squint really hard at Figure 4B, we see a Save Bodies feature in the as machined configuration. The as welded configuration doesn’t save bodies or create assemblies in this example.

The action of the Save Bodies means that any change made to the solid bodies in this part will be propagated into the saved components. Caution: Save Bodies will replace existing part files and might be a nuisance to PMI that gets overwritten with blanks.

If the method of documentation using a BOM is good, with the exception of missing drawings for hole locations, this episode has ended. However, we didn’t answer the question. Does the documentation need to show the holes in the parts that are welded, or should it show the holes after the parts are welded?

In Figure 5B, the holes exist in the parts before welding. The piece part drawings will show holes. Maybe that is good. Maybe not. If holes happen after welding, the answer perhaps gets punted to the new assembly.

Hole Punting

The CAD brand being discussed features a suite of tools called Assembly Features. To demonstrate one of these tools, we have used the Hole Wizard as an Assembly Feature in

Figure 6A

to drill a vent hole in the brace.

The intent is pressure relief to make closed-seam welding of this tube easier. When set up, the vent hole was not propagated to the part. It exists only at the assembly level. The hole will not show up in the part’s drawing.

Note in Figure 6A that as a consequence of nonpropagation, only one of the two braces has a vent hole. The Hole Wizard’s sketch could be edited to add that cutout.

In this scenario it is desirable to show the holes on the piece part drawings. The Assembly Cut shall be set to propagate to the target part(s).

Figure 6B

shows the result of that propagation setting. Since the same part is used twice in the assembly, when the cut propagates to the part, all copies of that part will show the propagation too.

FIGURE 5A To make a BOM table, we save the bodies in the weldment to create parts in an assembly. File names are specified by the operator for each of the parts.

FIGURE 5 This assembly was created by the Save Bodies feature in the weldment part in Figure 5A.

FIGURE 6A Assembly Features like the Hole Wizard are useful for cutting holes in assemblies. Here, a vent hole has been cut in a brace. The hole is not propagated into the part; it exists only in the assembly. For this reason, the brace right next to it does not have a hole. The sketch pattern for the Hole Wizard could be edited to add that missing cut.

FIGURE 6B In this example, the Assembly Feature—the Hole Wizard—does propagate into the part. The hole automatically shows up wherever the part is used.

FIGURE 7 This frame is an assembly of parts that were created from Saved Bodies in the weldment shown in Figure 2B. The weldment part parametrically defines the component parts in this weldment assembly. Not shown, and excluded from the BOM, is the weldment part. The author included it in the assembly to keep its file from getting separated from its children parts.

Drumroll for the Cart Roll

The difference between Figure 2B and

Figure 7

is that 2B shows a part (weldment) and the other shows an assembly (weldment) that is parametrically linked to a part (weldment).

One final CAD tip: To keep the master part file from getting separated from its children, include the master part weldment as a hidden component in the assembly weldment (and exclude it from the BOM to keep this our little secret).
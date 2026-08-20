# Shop Technology and 3-D CAD: Organizing Tips for CAD Assemblies

[TARİH: 01.09.2016 The Fabricator]

Precision Matters

CAD techniques for organizing and renaming models

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

T

he CAD model that emerges during product development is often a creature of opportunity rather than foresight. It was made quickly and is ill-suited to long-term product support.

The names and locations of models evolve and clarity emerges during the product development. They change to address the gaps between as-modeled and as-desired at any state of that development process. For instance, the alignment of axle and bearing once commanded where a wandering pocket might be located, but a well-designed pocket might insist on a location, with the bearing more than pleased to follow.

Perhaps most important is the organization and reorganization of the model for collaboration in a team environment. The goal of modular CAD hierarchy is to allow parallel development—separate ownership—of functionally related aspects of the project.

The project shown in

Figure 1

was introduced in the August 2016 edition of this column. This screen shot reveals issues with file names and CAD organization.

What’s in a Name?

"O, be some other name!" rues Juliet, an early pioneer in fragile relationships.

The CAD modeling software we are describing is based on Windows

®

and uses file types for specific purposes. Parts are represented by the SLDPRT file type, and assemblies of components by SLDASM. Assemblies can contain assemblies. We use the word

component

to mean either a part or an assembly.

That which we call a rose, for example, could be modeled as an assembly of stem and bloom, the bloom as an assembly of petals, and the stem as an assembly of leaves and twigs.

Figure 1

The early model has a cluttered Feature Manager, bad file names, and missing information.

Figure 2a

The Windows Explorer Rename tool does not have the ability to preserve parametric links embedded in CAD models.

Figure 2b

The CAD software includes extensions to Windows Explorer that are designed for preserving parametric links. These tools work without requiring the CAD workstation to open each file.

The CAD jockey can establish relationships between components. The bloom is patterned around the stem, for example. Those relationships then can span multiple files. Those files can be found in folders in Windows Internet Explorer

®

, but the CAD relationships are invisible. The CAD software uses the file names and their locations on disk to create and recall the external relationships modeled in the CAD.

Danger! It is possible to use Windows Explorer to rename and move CAD files (see

Figure 2a

). The external links embedded by the CAD software are broken using this Windows Explorer process. Broken links are not the end of the world, but it does make for tedious and needless do-over work to repair the broken links in CAD.

The preferred method is to use any of several CAD tools to rename or move CAD files. When these tools are used, the goal is to protect the links embedded in the CAD. A stem.SLDPRT by any other name will literally lose the rose’s bloom in rose.SLDASM, for example.

Two Bills Revered: Shakespeare and Gates

Windows Explorer offers convenience for moving or renaming files. It offers independent operation from the CAD software. That’s good news for the parametric links. When the CAD software is installed, it adds tools to Windows Explorer that make Windows Explorer safer to use (see

Figure 2b

). To find those tools, right-click on a file name, and the pop-up menu includes CAD tools for Pack and Go as well as Rename, Replace, and Move.

These tools for Rename, Replace, Move, and Pack and Go have the smarts to search and update parametric links in CAD files, regardless of their state in RAM, and can preserve the revised parametric data in those related files. Because of its ability to be thorough, this tool suite is easy to use. Be advised that it can be slow if it has to scan many files across many folders. Simple, uncluttered folders are a blessing.

As an alternative to using the Windows Explorer/CAD tools, use the CAD software itself. Perhaps the most straightforward renaming technique is to use the CAD’s File>Save As command:

Open the parent assembly.

Open the component to be renamed in a new window.

Use Save As to a new file name.

Close the window to return to the upper-level assembly.

In the process of saving the component to the new file name, the CAD jockey also is updating the other CAD files open in RAM. This preserves any parametric data. The main problem with the Save As method is the requirement that

all relevant files be open

during the Save As. They must also be saved to preserve the new information.

CAD’s Pack and Go was alluded to earlier. A screen shot is shown in

Figure 3

. It is a Swiss army knife compared to Save As. From Windows Explorer or from within the CAD itself, Pack and Go is a fine tool for moving, naming, and zipping CAD files. As a ZIP file maker, Pack and Go has the smarts to include drawings as well as toolbox parts, which is very important when making a comprehensive ZIP of the project.

The Pack and Go interface presents the file names and folders in a table. Double-click in a cell to edit—that is, change the file name or folder—or select a column and use the Select/Replace tool. Such column operations are a quick way to change all or part of a name in all occurrences in the assembly.

Figure 3

This screen shot of the Pack and Go user interface was made while creating the CAD model used for the illustrations in this article.

Like Save As, Pack and Go can be used to create new files and even to create new folders. Similar to Save As, Pack and Go updates all of the parametric data

in the files that it is creating

. Unlike Save As, Pack and Go has no effect on links in open files. This nuance matters if a new file is to replace an existing component in an assembly.

Pack and Go is very useful for creating a "branch" in a CAD design when a product line must diverge. In this discussion, the branch is the end of one stage of the development model—a snapshot—and the start of the next stage with improved file names and better internal hierarchy.

If a better component model exists, but it isn’t in the current assembly, use a CAD tool for performing component replacement. For example, in the Feature Manager’s presentation of components, select the component that is to be replaced and then right-click to replace this component with another. Replacement represents a method for reorganizing components in a project.

With the challenges of Windows Explorer danger in mind, the CAD software offers what it calls

virtual

components. Very little difference is introduced by being virtual. Virtual components behave in almost every way like ordinary models.

Virtual components, however, don’t exist in files as they relate to Windows files or folders. They exist only because the assembly that contains them exists. Thus, their names can be changed at any time without Windows danger. When the virtual file name is deemed to be satisfactory, the virtual component can be converted to be Windows faithful.

Pack and Go is very useful for creating a "branch" in a CAD design when a product line must diverge. In this discussion, the branch is the end of one stage of the development model—a snapshot—and the start of the next stage with improved file names and better internal hierarchy.

Virtual Safety Isn’t

The reason to convert, or to save, virtual components as Windows files is to eliminate their dependence upon a parent assembly for existence. If a parent gets deleted, its virtual children disappear with it.

A recent innovation in the CAD software is the ability to toggle any component between virtual and Windows. Consider what can be done with a component with an improper file name:

Make the problem component virtual.

Change the name by double-clicking.

Save the renamed virtual as a properly named Windows file.

Figure 4a

The model shown in Figure 1 has been changed. A folder "hides" the off-the-shelf hardware. Drag-drop was used to move components into a better order. Also, the components were made virtual for renaming.

Figure 4b

By adding metadata and updating what information the Feature Manager’s Tree Display shows, a CAD jockey can make it so that anyone can easily scan and interpret the design intent behind the model.

This process is similar to Save As. The benefit of making many components virtual at the same time is that it allows a more batch-centric work flow in CAD. One can iterate the names of the virtual parts into a matched set. When the names are satisfactory, in a group-selected step, all of the virtual parts can be converted to their Windows files.

PDMS: The Better Work Environment

The ultimate solution to the Windows parametric hazard is prevention. Use the document manager or vault known as PDMS (Project Data Management System) to prevent problems with broken links. PDMS eliminates all of the Windows danger and allows the CAD jockey to rename files without parametric worry and still operate quickly in a Windows Explorer environment.

Unlike the venerable WPDM, the data management tool that is based entirely on Windows, models in a PDMS vault don’t use the Windows file system and thus can be renamed, searched, and moved with great speed and reliability. The PDMS CAD vault is functionally virtual. The process of getting the model out of the PDMS vault essentially converts the model into a Windows-based CAD file.

The delightful aspect of PDMS is that it uses Windows Explorer as its user interface. That is to say, drag-drop, double-click, copy, and paste pretty much look and behave like ordinary Windows Explorer commands when you are working on files within the vault.

Yes, migration from WPDM to PDMS requires some planning, software installation, training, and work flow changes. In this author’s opinion, novault requires parametric sensitivity and team discipline in all things Windows. WPDM goof-proofs collaboration and revision control, but requires a distinct work flow. PDMS accomplishes everything WPDM does, requires little user-interface training, and adds better tools for recording the evolution of design and for controlling how the evolution proceeds.

The Hierarchy Shuffle

Clearly, many CAD tools are available for changing the names as well as the storage locations of components. Within the CAD model, the grouping of components into assemblies or into folders represents another aspect of CAD organization.

In the CAD’s Feature Manager, folders reduce the clutter. Folders serve to group components without creating new subassemblies. Compare the list of components in Figure 1 to that shown in

Figure 4a

. Folders and file names are getting better.

Figure 4b

shows the result of converting the virtual.

As mentioned earlier, the Replace Component tool is useful for changing that which is contained by an assembly. We drolly note that the consequences of such a component replacement include changing how the CAD model is organized.

Another CAD tool for grouping components into subassemblies is to form new subassemblies. Use the Feature Manager. Group-select the components that should be in a single assembly, right-click, and select Form New Subassembly.

To move components from one assembly to another or to move a component into an existing folder, drag and drop within the Feature Manager is very convenient. While dragging, observe how the mouse pointer changes to indicate where the component will drop. Alt-drag prevents the component from dropping into a subassembly. That’s handy when you are moving something from a subassembly up to the top-level assembly.

To dissolve a subassembly and retain all of its components within the current assembly, right-click and select the eponymous Dissolve Subassembly command.

Here’s a CAD tip: Parametric links, derived patterns, assembly cuts, equations, explode steps, and mates are sensitive to how subassemblies contain components. Awareness is advised when dissolving or dragging components out of one context and into another

.

The CAD’s help system describes how drag/drop/dissolve effects mates. (Check out Effects of Assembly Structure Editing within the SolidWorks help results for more details.)

Here’s another CAD tip: Add derived patterns of components after the component hierarchy/organization is complete. Otherwise, the derived patterns have to be re-created after the drag-drop is complete

.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop. Please send your questions and comments to

dand@thefabricator.com

.
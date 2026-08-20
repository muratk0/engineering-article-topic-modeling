# With changes in CAD hierarchy, don’t forget the pointers

[TARİH: 01.11.2025 The Fabricator]

Precision Matters

Design revisions can alter the relationship between related files

GERALD DAVIS

D

esigns change. As a result, revisions to documentation are required. When the design change involves the hierarchy of files in the CAD database—that is to say, which is the parent of what—a few pointers come to mind.

To illustrate what the CAD workflow can involve, we present the assembly shown in

Figure 1A

. Our tank lid assembly features a sheet metal lid, which is a subassembly. (It’s to confuse tank lid with just the lid.) Changing that sheet metal lid subassembly into a sheet metal lid part is our task at hand.

In review of this CAD model’s history, captive nuts were once swaged into the sheet metal lid. Mounting bolts are aligned with the nuts for various items. The current design replaces the nuts with tapped holes.

The current drawings in this project are just fine. They show the change from nuts to tapped holes adequately. All views on the 2D drawings and BOMs are acceptable.

The only reason to change this CAD model is to maintain closer fidelity to the real-world production item. The policy in our CAD shop is to maintain fidelity—keep the model tidy so the next CAD jockey doesn’t have to wonder why.

FIGURE 1A

The CAD task is to change the subassembly into a part. The drawing for this assembly will be affected. The drawing for the lid will change as well.

FIGURE 1B

The task is to replace this unrealistic assembly-of-one with a more realistic single part and to rename the part. The -1 no longer belongs in the filename.

FIGURE 1C

The drawing for the lid references a subassembly. We want to rename the SM-0127-1 to SM-0127 and replace the SLDASM with the newly renamed SLDPRT.

FIGURE 1D

The drawing for the top-level assembly—the tank lid assembly—is pointing to a subassembly for the lid. It should point to a part for the lid instead.

As we conclude the review, we note that the assembly for the sheet metal lid has only one component in it—

Figure 1B

. In other words, the lid’s subassembly is an unnecessary bit of legacy in the CAD model.

Heads Up

Our task involves changing pointers and at least one filename. There are internal Custom Properties for Part Number and Revision that will be affected, as well.

One to-do is to manage pointers in the drawing for the sheet metal lid. The drawing currently references (has a pointer to) the sheet metal lid assembly. We want the slddrw to point to a sldprt, not a sldasm.

Figure 1C

shows the results of File>Find References.

That’s not the only thing we want to do. We want to change the filename (and internal part number) of the sheet metal lid, as well. By an arbitrary standard, the -1 in the filename (and part number) implies that it is a component of an assembly, not a stand-alone item. In effect, we’re renaming the lid-as-a-part to be what the lid-as-an-assembly was.

FIGURE 2A

First step in this task is to rename the part. Use Solidworks>Rename to preserve file pointers.

FIGURE 2B

The drawing for the lid is pointing to the assembly, not the part. Replace the component in all view to correct this.

FIGURE 2C

The top-level assembly needs to point to our new lid-as-a-part, instead of the obsolete assembly for the lid. Use Replace Model and navigate to the new sldprt.

FIGURE 2D

Dangling patterns are easy to correct by isolating the seed component and the component with the hole pattern (the lid). Edit the pattern and select the corresponding hole pattern. The dangle goes away.

Designs change. As a result, revisions to documentation are required. When the design change involves the hierarchy of files in the CAD database—that is to say, which is the parent of what—a few pointers come to mind.

Note that this desire regarding the meaning of punctuation in filenames is entirely arbitrary and not a CAD operational requirement, per se. We include the renaming task here for completeness.

Another to-do is that the tank lid assembly (see

Figure 1D

), which currently references the obsolete lid assembly and should point to the (renamed) sheet metal part instead. When that pointer change is completed, the drawing for the tank lid assembly will be out of date until it is opened and re-saved.

Rename the Part

In

Figure 2A

, the CAD software tool for renaming CAD files that preserves pointers is used. The sheet metal part is renamed from SM-0027-1 to SM-0027. In Figure 2A, you might be able to see that the file SM-0027.SLDDRW is updated because it is pointing to an assembly that has a renamed component. We still need to inform the drawing that it should point to a part, not the obsolete assembly.

We’re using Windows Explorer in Figure 2A. Right-click on the filename, select see more options, select Solidworks, select Rename. Note that on Windows 10, skip the see more options.

Point the Drawing to the Part

In

Figure 2B

, the SLDDRW is updated to reference the new sldprt instead of the old sldasm. With the slddrw open, right-mouse-click on any view in the drawing. Select Replace Model. Then navigate to select the desire file.

Point the Assembly to the Part

In

Figure 2C

, the top level tank lid SLDASM is updated in a manner similar to that used on the lid’s SLDDRW. Right-mouse-click on the assembly to be replaced, select Replace Component. Then navigate to select our newly renamed sheet metal tank lid.

Point the Patterns to the Part

The tank lid assembly uses hole patterns in the sheet metal lid to align models for the bolts with the tapped holes. When the sheet metal lid changed from an assembly to a part, the hole patterns went into dangle. It’s a small nuisance.

To repair the dangles, a handy workflow is to isolate the seed component and the item that has the hole pattern, which happens to be the lid (see

Figure 2D

). Edit the pattern, select one of the desired holes in the lid, and the pattern no longer dangles. Repeat for the other two patterns, in this example.

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

SAVE!

End of Year Specials and 179 Tax Benefits

80+ IN-STOCK

METAL FABRICATING MACHINES

Ironworkers, Plate & Angle Bending Rolls, Horizontal Benders,

and more!

Explore our exclusive brands:

TrilogyMachinery.com

• 888.988.7655
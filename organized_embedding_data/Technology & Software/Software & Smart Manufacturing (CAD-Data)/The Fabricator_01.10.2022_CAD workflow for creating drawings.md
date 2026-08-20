# CAD workflow for creating drawings

[TARİH: 01.10.2022 The Fabricator]

Expertise Precision Matters

Learn when to choose a clutter-free starting point or lean on an existing drawing

By

Gerald Davis

www.thefabricator.com/author/gerald-davis

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

FIGURE 1 The Sheet Format for this drawing has several problems including crazy fonts and a missing third-angle projection in the title block.

FIGURE 2 By changing the path to the drawing’s Sheet Format to use an improved Sheet Format, a few problems are solved. The thirdangle projection designation now appears in the title block, and the company logo is updated.

FIGURE 3 This CAD project will require several drawings. At least one of the drawings will be created from templates. Perhaps several of the drawings will be created by using that first drawing as a functional template.

T

emplates are useful when creating drawings for fabrication. An existing drawing could be used as a template—a starting point. Look at it as a clone, albeit with legacy data.

Alternatively, starting with a Drawing Template is the equivalent of starting with a blank form.

A conventional Drawing Template might have several other templates nested within it. Recent episodes of this column have discussed templates for a Sheet Format, a BOM table, revision table, title block, and general table.

From practical experience, templates are in constant need of improvement. That is to say, the templates in use are flawed but not that flawed; some set of errors must be corrected as routine workflow.

Figure 1

shows a drawing created from a template that has several problems. Among other errors and omissions are a wide range of font sizes, an out-ofdate ASME standard (cited in Note 2), and a missing third-angle projection note. The effort of refining a template is often a procrastinator’s call to inaction.

With the brand of CAD that I’m using, the Sheet Format is frequently the source and solution to tedious flaws. The Sheet Format contains the title block, links to custom properties used in the title block, standard notes, and the drawing border. The Sheet Format is entirely user definable. It can be completely blank or completely exotic.

When a drawing file is opened, it loads its designated Sheet Format. When a drawing is saved, it saves the path to the Sheet Format that it last had in use. While a drawing is open, the path to the Sheet Format can be changed. In

Figure 2

, the Sheet Format has been updated to show the third-angle projection information. This CAD trick of changing the Sheet Format in use is a means to update existing drawings to new company standards.

An existing drawing is powerful in at least two ways:

1. It can be saved as a copy to create a starting point for another drawing.

2. It can be used to create a both a Drawing Template and a Sheet Format template to update existing drawings.

As a side note regarding multisheet drawings and Drawing Templates, it would be clearer to use the term Sheet Template instead of Drawing Template because separate templates are used for the first and the subsequent sheets on a multisheet drawing. A first Sheet Format would be used by the first Sheet Template. Likewise, the nth Sheet Format would use a nth Sheet Template.

Compared to using an existing drawing as a starting point, the CAD workflow of saving an existing drawing as a copy to serve as a starting point for a new drawing is particularly appealing when a batch of drawings has more in common than just their drafting standard.

As an example of a CAD project that could feature the drafting of several drawings in a batch, we offer the FMA shop cart, seen in

Figure 3

. In addition to complying with company standards, its initial batch of drawings is likely to share the same revision history—same ECO#, date of release, approval, and author.

Our design of templates tries to anticipate the workflow of their use. Accordingly, a sequence of CAD operations might be the following: use a Sheet Template as a starting point and refine it to complete a good drawing (with a good Sheet Format, revision table history, and updates to the dates and authors, the views, and dimensions).

Save that good first drawing. Then, with the Save-As command, create the starting point for the next drawing with a new file name. That new drawing file is slightly dangerous. It has a meaningful name but is presenting the legacy 3D model (as its Component In View).

To correct this dangerous drawing, open it and use the Replace Model command to update the model shown (in all views). The result of replacing the model likely will be dangling dimensions and perhaps some obsolete views. The good news is that redundant data entry is reduced.

As an alternative workflow to Replace Model, a button called References that appears on the CAD system’s File Open dialog can be used. Clicking on the References button allows one to change the referenced components that the drawing file opens. This allows the use of Windows Explorer to make a copy of the good file and then change the references while opening that copy.

If all goes well, the views in the new drawing now show the correct model. The main task at hand is to update the dimensions in the views. The data entry for history of revision and authorship is inherited and is a time saver.

Pack&Go is an alternative to Save-As. Pack&Go eliminates the need to replace the model. When only one filename needs to be changed for the new drawing, Save-As or replacing the model is efficient workflow.

If several file names must change as the template is created, then Pack&Go is the efficient tool. Its user interface is table-oriented with useful tools for editing the data shown in the cells of the table.

Going back to the CAD tip for creating Sheet Templates from drawings, templates shine without the legacy clutter of obsolete dimensions and incorrect views. The command Save Sheet Format creates a file that can be used by other existing drawings including existing Sheet Templates. This is a means to update the Sheet Format of those drawings to current company standards.
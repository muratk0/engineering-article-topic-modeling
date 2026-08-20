# A neat trick to keep product information with the drawing file

[TARİH: 01.08.2022 The Fabricator]

Expertise Precision Matters

Title Block functionality in drawing templates aids user navigation

By

Gerald Davis

FIGURE 1A Here’s how to add Title Block functionality to a title block in a sequence of steps: No. 1, sketch a title block frame; No. 2, add notes; No. 3, select those notes and add them to a Title Block Table, add tool tips, and surround the notes with a hot spot rectangle; No. 4, save the Sheet Format. To see how things went, test the Sheet Format with a drawing.

T

itle blocks on drawings are defined as part of the company’s drafting standard. With the CAD software being discussed, templates are created to capture that company standard. The customized drawing templates then can be used as a good start in creating production drawings.

This (ongoing) discussion of the design of templates will emphasize Title Block functionality, a somewhat simpler approach than using custom properties. The idea is that the drawing file stores the product manufacturing information (PMI). With the custom properties approach from previous episodes, the PMI is stored in the part or assembly files and then is simply displayed by the drawing’s Sheet Format. As foreshadowing, the simpler approach may end up with less convenience.

The CAD software has special functionality that can be applied for title block design and data entry. The PMI stored in the Title Block travels with the drawing file and does not change the 3D model file in any way.

Title Block has a double meaning. We will capitalize in the context of CAD functionality and use lower case when using it as common drafting terminology.

The Sheet Format, another CAD term, of the drawing defines what the title block looks like and where the Title Block fields are located on the drawing.

Customized Sheet Formats are as easy to create as Save Sheet Format. Sheet Formats are used to update existing drawing templates and existing drawings.

In this demonstration, an existing drawing is being edited to design a revised Sheet Format. That Sheet Format will be used by an updated Drawing Template. With the starting point drawing open, the Edit Sheet Format tool is used.

Figure 1A

shows the three steps involved in setting up a Title Block.

Step No. 1 calls for sketching the title block’s frame and adding titles. In this example, the sheet is 11 by 17 in. (B size). The sketched size of the title block and its fonts are adjusted for legibility on hardcopy.

Step No. 2 is where notes are added to each of the fields desired in the title block. (A note is a CAD term for an item that contains text.) The fields (notes) in this example are Description, Material, Tolerance, Finish, and Deburr. Because we’re editing an existing drawing, we might be tempted to make notes meaningful as they are added. However, keep in mind how the template will be used. Help the user understand what data needs to be changed from default. For example, the note for description "ASSEMBLY, BASE, FMA CART" might be better as "ENTER DESCRIPTION" in the finished template.

FIGURE 1B To test the Title Block, open a drawing using the Sheet Format from Figure 1A. Move your mouse over the title block on the drawing. The cursor should change to Title Block Table. When it does, right-mouse-button click and select Enter Title Block Data from the pop menu. Tab through the fields, make changes as needed, and click the green checkmark when completed.

With the fields positioned in the title block, we are now at Step No. 3, where the Title Block is defined. While editing the Sheet Format, click the rightmouse button to pop up a menu and select "Title Block Fields … "

The Title Block has a hot spot that appears as a rectangle with handles. The users of the template will have to position the mouse within the hot spot to access the menu to get to the data entry fields.

Set the size of the hot spot accordingly. Keep in mind that a right-mousebutton click in the hot spot is needed to access the Title Block. Because the rightmouse button has other uses in other locations on the drawing, keep the hot spot just around data entry fields.

To add fields to the Title Block, select available notes. In this example, there are five notes to select.

Each field in the Title Block table has a Tooltip entry that can be filled in. This helps the user understand what is to be entered as they arrive in the field.

The fields in the Title Block can be reordered for the convenience of the user when tabbing through the fields.

Step No. 4 calls for saving the Title Block (embedded in this Sheet Format) so others can use it. Edit the Sheet (as opposed to editing the Sheet Format). Save the Sheet Format with a meaningful name. In this example "sheet formatdumb title block" was used. The "smart title block" version is promised later.

Here’s a CAD tip: To create a Drawing Template, copy an existing drawing template to a new name and update the copy. (Open the copy, edit the Sheet Properties, browse to select the new Sheet Format, and apply the change.) Save the new Drawing Template.

To test the Title Block, create a new drawing using the new Drawing Template or update an existing drawing with the new Sheet Format (see

Figure 1B

). Hover the mouse over the hot spot and click the right-mouse button to select Enter Title Block Data.

With Title Block functionality, the use of fancy custom properties and flyout data entry forms is not required but is allowed. The Title Block functionality is relatively quick and easy to set up. It also is difficult for end users to accidentally move fields around—an improvement over independent notes on a drawing.

Title Block functionality is useful for guiding the user through what information is expected. Tab key navigation in the context of the title block is helpful.

However easy to set up, the use of dumb data entry fields puts a burden on the end user. To relieve that burden, a Custom Property data entry form with drop-down selection lists, presented in previous episodes of this column, makes it much easier to be consistent and speedy.

Title Blocks, when used in conjunction with Custom Properties (Hint: Link text to property!), could allow the PMI stored in the component file to be edited via the Title Block, much like data in a BOM table can update the data stored in the component file.

www.thefabricator.com/author/gerald-davis

Gerald

would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.

"THE ADIRA GAVE ME CONSISTENCY AND ACCURACY. IT WAS EXACTLY WHAT I NEEDED".

MILAN POPIK

. OWNER

METAL TRONICS INC

. ONTARIO. CANADA

Proven machines. Unmatched service.

For more info, call

630-616-5920

or visit us at

mcmachinery.com

Scan

to see our Case Study!
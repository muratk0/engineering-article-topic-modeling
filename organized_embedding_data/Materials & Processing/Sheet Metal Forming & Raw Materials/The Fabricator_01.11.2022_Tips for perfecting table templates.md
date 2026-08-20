# Tips for perfecting table templates

[TARİH: 01.11.2022 The Fabricator]

Expertise Precision Matters

Only a little effort is needed to create a template that’s easy to use

By

Gerald Davis

T

he creation of fabrication drawings usually involves tables, such as revision tables, bills of materials, and hole location tables.

As mentioned in the discussion of template design in the September edition of this column, tables have anchor points to help with drag-and-drop location snapping. Tables have additional features that might be useful when designing and refining templates. For example, one particular setting forces uppercase display for all the entries in the table.

Each type of table can be assigned a unique font. To assign a font, select the table to see a pop-up menu displaying a button/icon for controlling the font. The font control button either enables use of the document font or a font to be selected from a list.

To help with correcting font errors, the Design Checker is a tool that is built into the CAD system. The Design Checker can be used to scan a drawing document for fonts that are in use by the drawing.

Design Checker is helpful for complying with many aspects of an in-house drafting standard, including proper spelling. As part of the scan, the Design Checker can replace or update the fonts for various tables, notes, and dimensions.

Sadly, Design Checker cannot correct all types of errors. Column width, for example, requires something other than Design Checker to repair.

Disclaimer: In the following discussion, an "in-house drafting standard" is alluded to as if it were an existing document. It is a work in progress. At this stage of development, the in-house drafting standard actually is just a collection of suggestions.

Among those suggestions, the in-house drafting standard will address the issue of which fonts and sizes are to be used. For this demo, all tables are to use 14-point Arial font.

Our in-house standard also specifies that tables will use the document font. To help with the creation of new drawings, the drawing template being designed assigns the correct 14-point Arial font to each type of table. To bring existing drawings into compliance, a few mouse clicks can correct the settings of the various table fonts in the document’s properties.

Our in-house standard prohibits the manual assignment of font to a table. The document properties are where the assignment is made. The Design Checker’s role is limited to verifying that table fonts have been correctly assigned in the document’s settings. If an error exists, it will be corrected in the document’s properties with mouse clicks, not by changing the table’s font with Design Checker.

Here’s a CAD tip: Tables sometimes are reluctant to update their displayed font. That is to say, a table’s appearance isn’t always updated. To force the table to update, select the table and toggle its font button to not use then to use the document’s font. If the table’s font was stuck in limbo, then the table’s appearance is likely to change when it finally does update.

As mentioned, our in-house drafting standard specifies a table’s column widths. To help with this effort, our table templates are prepared with the correct column widths and fonts. A two-step process (set and save) is shown in

Figure 1.

To set the width, mouse drag or type a value for the width. Once the widths are set, the column widths are locked. When the table’s properties are correct, the table is saved as a template.

When that saved template is used in the process of inserting a new table, its imported column widths will be correct (and locked). The font will be correct because of the inheritance of font size from the drawing’s file. In the example of the revision table, its rows will be imported if they are saved as part of the table template. Those rows might or might not be a blessing.

Make the table template your way. For context, the FMA Cart is presented in

Figure 2

as a typical startup project. It has a legacy of several drafting styles, collections of templates, and levels of implementation.

As a demonstration of a process for correcting the font and column spacing of a revision table, please consider

Figure 3

. As a before-and-after comparison, the table we have (at the top in Figure 3) has wrong font and wrong size and incorrect column widths.

The compliant table is the lower table in Figure 3. Note that this good table has a larger font (14 point Arial). The column widths of the table allow it to align with the tick mark on the drawing border. (The orange arrow is pointing where the top left corner should be).

A few options are available for correcting the obsolete table fonts. One is to require that fonts be manually assigned at the time of creation. It’s simply a matter of a few mouse clicks (and remembering to perform those clicks).

FIGURE 1 Column widths are lockable. This helps with standardizing the widths of table columns. When preparing a table template, set the fonts, font sizes, and column widths, and then save the table as a template.

FIGURE 2 The FMA cart is a CAD project that will be merging several templates and drafting standards.

FIGURE 3 The revision table we have (the upper table) has the incorrect font, incorrect font size, and incorrect column widths. The lower table is good. We want the table to align its top left corner with the 3½ tick mark on the drawing border.

A second drafting option is a variation of the first. A workflow that is easy to repeat (and remember) is to rely upon Design Checker to detect and correct problems with table fonts. It is more reliable than scanning for errors by eye.

A third alternative is to require (as a matter of policy) that all tables use the use document font button-setting for their font. This workflow works best when most of the drawings are being created from scratch. Design Checker might be better for correcting existing drawings.

Once the table templates are set up, creating new drawings is a breeze. Getting the templates into perfect working order is one of those "Do as I say, not as I do" endeavors.

▸

www.thefabricator.com/author/gerald-davis

Gerald

would love for you to send him your comments and questions. Please send your questions and comments to

dand@thefabricator.com

.
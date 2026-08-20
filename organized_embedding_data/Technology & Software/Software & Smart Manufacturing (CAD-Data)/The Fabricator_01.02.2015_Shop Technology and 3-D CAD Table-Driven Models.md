# Shop Technology and 3-D CAD: Table-Driven Models

[TARİH: 01.02.2015 The Fabricator]

Precision Matters

One model can take many shapes given instructions in a design table

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

R

ecent editions of this column have featured table-driven models.

Figure 1

shows drill bits A through Z in a matching drill index cabinet. The table-driven drill bit model allowed one CAD file to represent 26 individual drill bits.

(Disclaimer: The technical details in this column apply to specific brands of software. If you don’t have access to Microsoft Excel

®

, the following tips and tricks for SolidWorks

®

won’t be of much use.)

Figure 2

shows the design table for the drill bit model. Creating a design table takes a few mouse clicks and some understanding of syntax for the column headings, but it is otherwise a routine and brief chore.

Figure 1

A detailed model of 26 drill bits and a cabinet with three index cards for holding drill bits is the model to be explored.

Figure 2

The 26 rows in this spreadsheet create 26 configurations of the drill bit model. The columns identify the dimensions and other features that change from one bit to the next.

Drilling Into a Design Table

The design table in Figure 2 is controlling eight dimensions and suppressing a few features. If you know how to use a spreadsheet, you are well on your way to using design tables.

Note that, in this example, the description for each bit is created with an Excel string concatenation function. The rows represent the different configurations of the drill bit and related values for dimensions. The columns identify the dimensions or features being controlled.

Figure 3

Compared to Figure 2, this is a relatively simply design table—just three rows. The complexity and labor involve swapping out (suppress and unsuppress) of six different features.

Here is a quick CAD tip: Dimensions with meaningful names are easier to comprehend when working with design tables.)

The trade-off between model complexity and convenience of use—easy to search for and easy to install any letter size drill bit into an assembly—make the table-driven technique seem prudent for drill bits. Little bits are shaped just like big bits; only a few (as in eight) dimensions change from one bit to the next. To extend the drill bit model to include other drill bit sizes, we merely add rows to this table.

Working Hard to Make It Easy

The index cabinet shown in Figure 1 features three hinged index cards. In a manner similar to the drill bit, those three panels were modeled in a single CAD file and controlled with a design table. If you winced when you read that, you are probably well studied in the art of design tables.

To explain why it would probably have been better to simply create three separate CAD files, consider the spreadsheet shown in

Figure 3.

Maybe it’s a blessing because only 3 rows are present. (That’s a lot easier than working with 26 versions of a drill bit.) In this example I did not use elaborate Excel functions; the configuration names are just simple text strings: A-K, L-S, and T-Z. The table is controlling six features and five dimensions. The major labor in setting up this table is the swapping out of the legends for the embossing. It would have required less brain drain to create three files and skip the suppress/unsuppress activity altogether.

In the author’s defense, the thought behind selecting a table-driven modeling technique rather than creating three separate CAD files was that the panels had a great deal in common. They were all painted the same color and fit into the same box. They differed from one another only in terms of overall length, window size, and quantity of holes. The legends embossed near the holes to show sizes were unique to each panel. Each panel featured unique hinge points and hinge diameters. Not only did dimensions change, but entire sets of features were functionally deleted and replaced from one panel to the next.

In retrospect, about the only thing the panels had in common were the sheet metal thickness and the width to fit into the cabinet’s hinge clip. For the design intent behind this model, this example has two things going for it:

It is a good bad example.

Having fewer files to share with you is a blessing.

Figure 4a

As the modeling is completed, dimensions are renamed to give them meaningful names.

ChassisWidth@sketch1

gives a better hint than

D2@sketch1

.

Figure 4b

Insert>Tables>Design Tables brings you to the Property Manager for the design table. Here you select the dimensions or other features to include in the design table. You don’t have to select; you can type it all by hand, but it is easier to just click.

Figure 4c

After inserting the design table, we see it has only one row for Default. This screen shot shows the table after new rows have been edited or added to include sizes and descriptions for other configurations of the chassis.

Figure 5

In this example, the front cover is modeled in place after the chassis is completed. The front cover will resize to match the chassis because of parametric links between the models.

(Here’s another CAD tip: Table-driven design makes sense when dimensions change from one configuration to the next. If more than simple changes are needed, the CAD jockey then begins to feel exponential pressure to create separate files for the variations on the theme.)

A Table-driven Product Line

Armed with some wisdom regarding the limitations of table-driven design, we consider the following scenario. Our product line features a sheet metal enclosure that has various lengths, widths, and heights depending on the end user’s selection of options. Our task is to model an enclosure assembly that is controlled with a design table.

To be more specific, our sheet metal chassis is controlled with a design table. The front panel and covers are parametrically linked to the chassis, so their size follows the chassis.

Figure 4a

highlights some dimensions in the model of the sheet metal chassis. Of particular note are the width (10 in.) and the depth (4 in.). They are controlled with the design table and are renamed for clarity.

Figure 4b

shows the initial steps in creating a design table. At this point, the selection of dimensions to include in the design table occurs. This is where properly named dimensions prove to be invaluable.

In

Figure 4c

we see the completed data entry in the new design table. The default row is automatically created. The other rows were inserted using routine spreadsheet copy/paste/edit functions. To create new sizes of this box, we merely enter a new row with values for the length, width, and height, along with the proper description and part number.

Figure 5

shows that the front cover is "modeled in place" within the assembly and is parametrically linked to the chassis model. This is accomplished using sketch constraints and dimensions. If the size of the chassis changes, the size of the front cover changes to match.

Connecting the Controls

At this point the CAD jockey has no convenient way to switch between sizes of chassis. The only control available is to select a different chassis configuration.

To make this assembly easier to use—and to assign part numbers to the various configurations of the enclosure assembly—we need to add configurations to the assembly that is holding our components—the chassis and front cover. Our eventual goal is to click on a configuration in the assembly and have all of the components adjust to match that configuration.

We’ll create those configurations in the assembly by inserting a design table. It can be helpful to keep matching configuration names in the assembly as well as in the components. We have only the configurations in the chassis at this point, and those are the configurations we want to create in the assembly as well.

To speed the process, we make a copy of the design table in the chassis and edit that copy with Excel to delete columns that used to control dimensions in the chassis. Those dimensions won’t be controlled by the assembly in the assembly’s design table.

All that we keep in this "design table template" are the configuration names in column A, the configuration description in column B, and a part number in column C. The result is shown in

Figure 6a.

Next we insert that spreadsheet into the assembly as a design table. The only difference between creating a new design table from an existing file and creating one from scratch is the selection of From File instead of Auto-create.

After the design table is inserted into the assembly, it creates the configurations for us. We then have a start on assuming convenient control over the model. We repeat the "Insert Design Table From File process" to create configurations in the front cover component.

Figure 6a

This spreadsheet was created from the design table in the chassis. As a time saver, we’ll use this spreadsheet to add configurations to the front cover and assembly models. We could manually create all of the configurations in all of the parts, but who likes to type?

Figure 6b

We tricked the software into creating new columns to control the configuration of the chassis and front cover components. We now use copy and paste to make all of the configuration names match in columns A, D, and E.

Figure 7

These four enclosures are of different sizes. That’s eight different parts and four different assemblies. We modeled it with three files—an assembly and two part files.

However, the components—the chassis and the front cover—are not controlled by the new design table in the assembly yet. Our next one-time step is to select configurations of the chassis and front cover. That’s done in the Feature Manager. We select configurations to match the current configuration of the assembly—for example, 10 × 4 × 3.

We’re closer, but only one of the five configurations works. The other four configurations all revert to the default size at this point.

We now edit the design table in the assembly. The software recognizes that the components have been configured manually and gives us the opportunity to include their configuration in the design table. We want that. The result is shown in

Figure 6b.

The software created columns D and E with the configuration controls set for the chassis and front cover.

We use Excel tools to copy the configuration names from column A to both columns D and E. This forces the assembly, the front cover, and the chassis to all assume the same configuration at the same time.

Fewer Files, Efficient Enclosures

Figure 7

is a demonstration of four different sizes of the enclosure. An assembly was made of the enclosure parts, and then the configuration for each enclosure in the pattern was set with a few mouse clicks. The benefits of using design tables include ease of extending new sizes to the product line in a standardized procedure. Editing rows in a spreadsheet can be much easier than editing a copy of a solid model.

By linking the configurations to the design table spreadsheet, we can use Excel macro functions to control the design table, which controls the assembly, which selects the right configuration of components to display. We’ll leave it to your imagination as to what can control spreadsheets in order to control models. You might be on the way to an interactive product selection tool for your customers.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop. Please send your questions and comments for Gerald to

dand@thefabricator.com

.
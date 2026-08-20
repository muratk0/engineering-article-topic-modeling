# Shop technology and 3-D CAD: Workflow with PDM

[TARİH: 01.06.2015 The Fabricator]

Precision Matters

To be useful, the design’s CAD must be both secure and available

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

E

xpert operators of 3-D CAD software know how to delegate tedium and thereby goof-proof routine chores.

They have an abundance of such tricks. They start with nearly complete models or templates. Their bill-of-material tables auto-populate themselves. User-friendly data entry forms speed routine typing.

At a more esoteric level, they use tools available in the CAD software for speeding the completion of 3-D features as well as for placing dimensions on 2-D drawings.

The result: A CAD jockey on a workstation can generate documents very quickly. A fabricator who is operating both CAD and CAM knows that the CAM system produces a similar flood of files.

Like most PC software, CAD projects are burdened with named files, which can lead to dangerous conflicts. One sees files with the same name, but different meanings, when dealing with multiple projects, product lines, customers, or revisions.

If that weren’t enough, organizations merge. Their combined CAD and CAM data is a valuable inventory. It is vital to the success of the business to maintain that inventory of intellectual property in a useful state. "Useful" in this context means wellorganized and ready when you need it.

Useful Documents

To delegate the filing and organization of CAD documents, the CAD jockey needs something to delegate to. To that extent, this article is a pitch for software. The good news is that there are several brands of document management systems that work great with CAD. Our theme here is focus on function; you can pick your preferred method or brand of implementation.

For the purposes of conversation, we’ll use an acronym, PDM, which stands for product document management. Our emphasis is on designing or refining a product, and our goal is to produce

useful

documentation, as alluded to earlier. In terms of function, it would make just as much sense to use DM, or document management, and omit the emphasis on product. Keep that in mind if you’re shopping for software.

When it comes to protecting files with PDM, the file types we’re talking about include CAD data. Let’s include the image files that make up the artwork for logos and legends. It might make sense to include CAM and CNC data. Some PDM products are capable of capturing all of the documents that the business generates, but that good idea is beyond the range of this article. Our PDM needs to be a CAD jockey’s friend.

A DIY PDM

Suppose that Windows Explorer™ is the software to use for a do-it-yourself product document management (DIY PDM) as shown in

Figure 1a

.

Explorer has handy tools for searching and controlling access. It is stable in terms of function and operation. And there’s a lot to like about free.

In our scenario we are a job shop with dozens of customers. The CAM/CNC department has network folders for each customer with subfolders for each product. CNC programs are stored in subfolders by part number. The CNC operators download the programs from those part number folders.

When it comes to revisions, our DIY PDM work-flow is to create a new subfolder with the revision (REV) appended to the folder name—/PartNumber/REV A/CAD/, for example. Figure 1a shows two revisions of the same part number. It takes a moment of study to spot the most current revision. In

Figure 1b

, the same folder is displayed in a task pane—on the right—in the CAD workstation. This makes the DIY PDM convenient for CAD work, but it is still easy to fetch the incorrect revision.

Figure 1a

Windows Explorer software can be used for product document management. This screenshot shows folders for two revisions of the same part.

Figure 1b

The CAD workstation can be set up to display Windows folders in a task pane, as shown on the right. This is slightly more convenient that using Explorer in a separate window from the CAD.

To avoid confusion, our DIY PDM procedure should have a rule to hide the obsolete subfolders. Don’t delete them. You never know when an old revision will want to rev again.

(CAD warning: It can be a performance and stability issue to use network folders from a CAD workstation. Network drives tend to be slow and Internetreliable.)

(CAD tip: Make a local hard drive folder on the CAD workstation for active CAD work, and when the design edit is completed, copy the files to the network for safekeeping. This "local copy" method is much safer than editing directly in the network folder. Be sure to keep in mind a couple of questions, however: Who else has access to the network folder? and Should they be able to see the in-process edit?)

Here’s a memo for the do-it-yourselfer: Remember to include an "edit a local copy" rule into our DIY PDM system.

Our DIY PDM system is almost complete. It would be nice to prevent accidental edits of work that has been released for production. That can be accomplished by making the subfolder read-only. We just have to remember to turn that setting on and off in Explorer.

The main drawback to our DIY PDM system is enforcement. We have rules that must be followed: Properly create and name subfolders, toggle read/write access, keep old revisions hidden, and so forth.

It is tedious to remember all—and dangerous to forget any—of the rules that go with DIY PDM. Let’s find a way to delegate and goofproof the document management.

The Friendly Enforcer

Professionally designed document management systems do all that our DIY PDM system does. However, they do it better by making adherence to the rules nearly effortless and automatic.

The concept of a "document vault" is nearly synonymous with PDM. We check documents into the vault for safekeeping. We check the document out of the vault when the document requires editing.

The CAD workflow in a PDM environment is straightforward:

Log into the vault.

Check a document out of the vault.

Take ownership of that document.

Save changes to the document.

Check the document into the vault.

Release ownership of that document.

Log out of the vault.

Figure 2

This screen shot shows a view into a PDM vault (shown on the right). PDM is easy for the CAD operator to access. It is just a fly-out pane similar to many others.

Figure 2

is a screen shot of an example CAD workstation with the PDM vault view expanded. In addition to the read/write access for the document being edited, you can also see the revision level and status (e.g., released, prototype, engineering change order, or obsolete) of the document.

In reviewing the benefits of PDM workflow, we first see privacy benefits from the addition of a PDM service. The log-in/log-out requirement controls the ability of anyone to even know that a document exists.

Then we notice that the PDM workflow requires authority, or ownership of files. A formal PDM system is designed with collaboration in mind and makes it easy to know who has a document checked out. This prevents accidental editing and minimizes conflicts between authors.

A fully featured PDM system administers the revision level of the document. That is, every time a document is checked into the vault, the new edition is stored with a unique revision. The PDM system controls the revision sequence. This provides the opportunity to roll back to any previous copy stored in the vault.

The vault’s revision of the document is typically shown as the revision of the design. With our DIY PDM system, the CAD jockey had to remember to manually change the revision level. The vault makes the process automatic. Goofproof that tedium!

When you are first starting out in a PDM environment, loss of control over the revision level can be a culture shock. The vault’s revision changes just because you fixed a little spelling error and checked the document back in.

(CAD tip: Resist the temptation to cheat the vault’s revision manager. Embrace the change—and the record thereof. It is beneficial that the vault keeps a diary of all edits.)

For CAD work, PDM systems include the ability to tailor the revision scheme to the needs of your organization. For example, we might use an alphanumeric revision code. To deal with minor revisions such as spelling errors—that is, no change to

function

of the part—increment a numeric field in the revision level. When function changes, bump the alpha field to the next letter.

Some enterprising document management systems offer more versatile revision systems as well as the ability to route the document for approval before release to fabrication and otherwise apply business rules to scheduling, authorizing, and making design changes.

Queries to Solve Quandaries

Typically, a commercial PDM vault has search tools that Explorer lacks. The vault can see and allow you to search all data fields, not just file names. Not only that, it can answer the query, Where is this part used?

Figure 3

is an example that shows this motor is used in five different assemblies in our scenario.

The ability to answer the question—Where is this part used?—can be a compelling motivation for implementing a PDM system. Your PDM vault has a complete snapshot of all the products you make. It can identify all of the product lines that are affected by a design change, possibly preventing unintended consequences.

Figure 3

With a couple of clicks in the vault, you can learn everywhere that this component is used. The motor shown in Figure 2 is used in five different assemblies, according to this report.

The vault is precious. Not only is it the enforcer of rules, but it also is the container of knowledge. The vault by its very nature captures corporate knowledge. It is the digital encapsulation of intellectual property. A secure backup system is a critical piece of the PDM installation.

If you don’t yet have PDM as part of your current workflow, check your software license; some brands of CAD software ship with PDM tools built-in. You may already have a PDM system at your call, waiting—nay, pleading—for some documents to manage.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Please send your questions and comments to

dand@thefabricator.com

.
# What a review of a CAD model says about its creator

[TARİH: 01.11.2024 The Fabricator]

Precision Matters

Tools used provide a glimpse into the CAD jockey’s logic and technique

Gerald Davis

T

his is a review of the CAD techniques used in the sheet metal project shown in

Figure 1.

The product is functionally a three-sided socket (0.090-in.-thick 5052-H32 aluminum), featuring captive studs. The bracket is to be 4 in. by 2 in. by 2 in. on the inside and mounted with three ¼-20- by ⅝-in.-long studs.

With not much more information than that, the project is imagined as part of a job application for a position as a CAD jockey. Many tools are available in CAD. Seldom is there a single right or best way to model. We’re looking for efficiency as well as clarity. As part of the reviewing team, your opinions are solicited.

Disclaimer: A specific brand of CAD and its terminology are referenced in this column.

Good Reviews From First Impression

The exploded view (top left in Figure 1) makes it easy to distinguish between the sheet metal and the captive studs. The bill of materials table (lower right on the drawing) clearly indicates part numbers, quantities, and sources for all required items.

Also pleasing but of questionable value, the rendered view (to the right in Figure 1) is lovely. The image strongly resembles an aluminum bracket with swaged-in studs.

Less pleasing so far: The drawing is incomplete. Fonts, colors, and general legibility of the sheet format could be improved.

Returning to the exploded view, at the software level, its Component-in-View defines how the subcomponents are positioned when the model is exploded. By right-clicking on the view, the reviewer can discover what the name of that component is as well as open it for editing.

In this example, the CAD model used by the drawing is

November_Assembly.SLDAM

, shown in

Figure 2

. We now know that assembly modeling was employed as the core CAD technique.

In review of technique, this project could have been modeled as a multibody part (sldprt), instead of as an assembly (sldasm). There is file clutter associated with assemblies. Multibody is contained in a single file, which is friendly to the disk drive.

Because a CAD file for the captive stud exists, the multibody technique would duplicate existing work. That’s great for efficiency. Demerits are warranted, however, for not explaining the modeling challenge very well.

In the theme of efficiency, this CAD jockey remembers a time when a computer’s central processing unit was slow and its graphics processing unit could be counted on one hand. The overhead of setup for sweeping threads, as well as the burden of rendering helical spirals, taxed patience to the point of avoidance.

Today, Insert>Feature>Thread is a tool that makes modeling helical threads easy and takes advantage of the GPU’s multicore and arrays. However, there is an existing model. Is it worth updating it with the Thread tool?

FIGURE 1 A drawing for a sheet metal project is shown on the left, and a rendered image of the product is shown on the right. The exploded view and bill of materials table help to explain how the bracket is fabricated. Is the CAD technique used assembly or multibody? The reviewer wonders.

FIGURE 2 On the CAD workstation, the Feature Manager appears on the left, the Graphics Window in the middle, and the Properties Pane on the right. In review, the data entry for properties seems to be complete. This is an assembly of a sheet metal component and studs (not a multibody part).

FIGURE 3 To ease the burden on the CPU that comes with using a helix, a thread can be simulated by cutting a raccoon’s tail. Cut a single ring and pattern it. This creates the illusion of threads with less CPU burden. If CPU is not a concern, use the Insert>Features> Thread tool to model threads.

FIGURE 4 Virtual components are similar to multibody in that they are contained in the parent file (efficient disk storage). Mating the origins of components fully constrains them in one step. Concentric mates can be fully constrained (no rotation). Hole wizard is efficient for creating patterns and avoiding the tedium of mates.

Many tools are available in CAD. Seldom is there a single right or best way to model. We’re looking for efficiency as well as clarity.

One can have the appearance of threads without the spiraling overhead. To wit, various stages of the model for the captive stud are shown in

Figure 3

.

From top to bottom, if threads are not needed for fabrication of the product, don’t model them. If threads are useful for visualization of the function of the model, avoid using a helix. Apply an appearance instead of creating a physical surface.

If a simple decal or appearance won’t do, simulate the thread with a raccoon’s tail. Cut a single ring and pattern it to create the illusion. The camera can only reveal one side of the stack of rings. It could be a helix to the casual observer.

Because the boomer’s model for the stud already exists, use it. Otherwise, create a fresh model from scratch and employ the Thread tool. Tricky models almost always grow raspberries.

Returning to the assembly,

Figure 4

reveals some further details about the assembly. In the Feature Manager, the braces around the component’s name show that the sheet metal part is a virtual component, (i.e., [Virtual Component]).

The Feature Manager is expanded to show the mates for the sheet metal part. Its origin is mated to the origin of the assembly; this fully constrains it in 3D space. Like a multibody part, the virtual component is friendly to the disk drive. The virtual component is easy to save as a conventional file if desired.

A concentric mate between the stud and the sheet metal is also shown in the Feature Manager in Figure 4. This concentric mate has been set to not rotate. This fully constrains the stud to match the reality of this application. This might be important when doing ki kinematic studies. For this model, the few seconds that it took to make it real might be spent elsewhere. If this were a job applicant, a bit of show-off is in play.

The Hole Wizard was used to make the holes for the studs. The resulting pattern of holes is useful for creating a pattern of studs. As a matter of efficiency, it is quicker to mate one component and pattern it than it is to mate three copies of the component individually.

This pleases the reviewer and brings up another tip. When admiring one’s own work, it is easy to see the nicely pruned tree and not the forest of peril. A buddy check is a blessing, even if your work is perfect.

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.

March 11, 2025

Hyatt Regency Schaumburg

1800 E. Golf Road, Schaumburg, IL

Reserve Your Exhibit Space Today!

Connect With Buyers and Boost Your Business

Join The Fabricator for a one-day tabletop event to showcase your latest equipment and technologies to the local manufacturing community. It’s the perfect forum for buyers and influencers to view your products and services.

Sponsorship opportunities are available. Contact your sales rep for details!

Co-located with GIE Media’s Industry & Innovation Conference
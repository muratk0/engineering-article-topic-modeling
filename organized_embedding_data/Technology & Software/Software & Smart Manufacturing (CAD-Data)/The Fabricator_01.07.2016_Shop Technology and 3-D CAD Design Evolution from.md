# Shop Technology and 3-D CAD: Design Evolution from Invention to Manufacturing

[TARİH: 01.07.2016 The Fabricator]

Precision Matters

CAD techniques should evolve as designs move from invention to final release

By Gerald Davis, Contributing Writer

Read more from Gerald Davis at

www.thefabricator.com/author/gerald-davis

Figure 1

An assembly of electronic equipment is shown. The fan is mounted with studs and nuts. The studs are located with a Hole Wizard pattern. The pattern is parametrically linked to the fan. If the fan’s location changes, the studs and nuts will follow.

Figure 2

Here is a derived pattern of components—in this case, a screw. The seed component is fully mated into position. The other four screws do not have any mates; their location is controlled by a sketch. The sketch was created with the Hole Wizard and also locates the standoffs that receive the screws.

M

ainstream 3-D CAD software is versatile in that it offers tools that can be applied in many combinations to achieve similar results. There is seldom a single "right" way to go about creating the model. Nonetheless, the benefits and penalties of some general CAD techniques are worthy of consideration.

Product development with CAD often progresses through stages of evolution. The invention stage is followed by initial manufacturing, which hopefully leads to mass production aimed at capturing and supporting market share.

Inventing a Stage

CAD techniques that are useful during the invention stage include virtual parts, extensive use of parametric links, direct editing of "dumb" models, patterns and mirrors of components, and use of CAD tools that apply at an assembly level to propagate to components found in the assembly.

The theme of the invention stage is speed: Develop a digital prototype for visualizing what the finished product will look like in record time. Elegance in 3-D CAD technique and detail for procurement are back-burner issues. The goal is to get something on the screen to look at—quickly.

An ideal research and development model would be easy to stretch and modify. Exploration is an important activity during the invention stage. Parametric links (see

Figure 1

) help to keep critical features in alignment as the shape of the product emerges. As a CAD technique, patterns of components based on features in the assembly speed the modeling process.

These patterns of components may persist all the way through mass production. However, as the design matures, components are often reorganized from one subassembly to another. Derived patterns often fail and must be remodeled.

Here are a pair of CAD tips: In general, add fillets to the model as the finishing touch. You’ll end up with fewer dangling references in sketches. Similarly, add patterns of components after the general organization of subassemblies is completed. You’ll end up with fewer busted component patterns. An example of a derived pattern of screws is shown in

Figure 2

.

The organization of the invention-stage CAD model reflects the timeline of inspiration. As opposed to subassemblies that are useful for production and field support, the components at the invention stage are organized—if they are organized at all—simply for visualization.

Initial Fabrication

Details related to product support become important when the CAD model matures from the invention stage to the initial manufacturing stage. When considering how to actually build what the model represents, purchasing wants to know who, what, why, when, and how many for each component. Quality control wants to know how to inspect it. Manufacturing needs to know material, finish, and size.

Generically termed as

metadata

, this information is related to product support and can be retained in the CAD files. That requires data entry, or simple typing on the part of the CAD jockey. To speed and standardize this task, the Custom Property panel is an excellent tool.

Figure 3

The Custom Property panel is very useful for data entry. This metadata can be used to populate a bill of materials table. Standardized data entry forms with dropdown lists speed the typing chore.

Figure 4

To prevent accidental edits, it is possible to lock all external references. If the model requires revision, they can be unlocked with a click. This preserves the design intent. Simply deleting the external references effectively burns a bridge, and some information is lost.

During the invention stage, the Custom Property panel is a distraction at best and wasted effort at worst. A rapidly evolving design may obsolete the component by the time the metadata is entered.

To the contrary, during the manufacturing stage, the Custom Property panel is both a timesaver and a nag when it comes to data entry.

Figure 3

is a screen shot of data being entered for a CCD camera that is present in the example assembly.

It should be acknowledged that some effort is required to set up the Custom Property panel. The effort is heartily recommended.

Mass Production Stage

When the product is in the manufacturing stage, the virtual parts start to lose their charm. Virtual parts have charm in that their file names are very easy to edit; that’s why they are so handy during the invention stage.

Here is a bit of CAD trivia: A 3-D CAD assembly file contains pointers to other files that represent components in the assembly. If the file name of a pointedto file is changed without 3-D CAD’s involvement, the assembly will point to things that do not exist. Virtual parts, as a modeling technique, help the CAD jockey focus on the invention; then as time permits, the CAD jockey can address topics such as proper spelling of the file name

.

When the design moves out of the CAD shop and into the wide world of procurement, things that are easy to change become hazards. It is often desirable to have indelible file names when communicating online with suppliers, vendors, and assemblers.

As a prototype, and even as a mass production item, a product design is subject to revisions. The CAD techniques that were useful during invention continue to be handy as the product is refined. As a technique, parametric links have great power.

This should get the Spidey sense tingling. When the location of a cutout follows the position of some other component, the editing of the model is wonderfully automatic and nearly instantaneous.

"With great power comes great responsibility," Uncle Ben told our friendly neighborhood wall crawler. If the component is moved "accidentally" during revision for manufacturability, the consequences can be dire. CAD techniques that rely on opening the entire model are less wonderful when you want to edit only a single item. The good tools from the invention stage can complicate and slow the process of revision management in the manufacturing stage. Locking or instead deleting parametric links is often a major activity in transforming a research-and-development model into a ready-for-fabrication model. A screen shot of locking external links is shown in

Figure 4

.

Details related to product support become important when the CAD model matures from the invention stage to the initial manufacturing stage. When considering how to actually build what the model represents, purchasing wants to know who, what, why, when, and how many for each component. Quality control wants to know how to inspect it. Manufacturing needs to know material, finish, and size.

As the manufacturing and distribution of the product matures, revision

management

seems more like revision

prevention

. Each individual component in the product grows its own form of inertia to resist change. Derived sketches, propagated cuts, and multibody splits were slick when the model needed to behave like putty. The industrial designer likes easy change and instant gratification.

The product manager wants to control exactly how the changes take place. Production management wants reliable communication among purchasing, manufacturing, and product support. That means no accidental edits. CAD models that are fragile—too easy to edit—are undesirable when prices and schedules are involved.

The basic CAD technique for preventing revision scope creep is to remove dependencies on other files—or remove all link-based features and patterns.

Stage Craft

We’ve discussed the stages of design evolution as though entirely different models are involved. CAD tricks appropriate during invention are abandoned, and the model is re-created in a different way as a manufacturing model. With planning, less abandoning and more revising of models can be the better use of time.

In many cases, entirely different teams of people are involved. The teams should still be able to look at each other’s work and quickly isolate the difference between the essential design and the CAD techniques used to portray that essence.

From "invention" through "owners’ manual," the experienced CAD jockey will launch a design using techniques that anticipate the future use of the model. The transition from invention to production is thereby less dramatic. Some tools and methods are grand for product life cycle support. Other tools are just right for speedy evolution of a vision.

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

. From 1984 to 2004 he owned and operated a job shop.

Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.
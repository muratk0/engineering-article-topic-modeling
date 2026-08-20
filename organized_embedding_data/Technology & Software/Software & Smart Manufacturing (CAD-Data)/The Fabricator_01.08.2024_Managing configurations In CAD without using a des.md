# Managing configurations In CAD without using a design table

[TARİH: 01.08.2024 The Fabricator]

Precision Matters

Configurations are a handy way to create variations on shape without changing the underlying CAD technique—a boon to sustaining engineers

Gerald Davis

O

ne of my favorite tricks while showing off at CAD user group meetings is the "Rebuild All Configurations" button. Rebuilding has special meaning in CAD. It is the software’s process of calculating where the 3D surfaces should be, based on the constraining 2D sketches.

Rebuilding is time-consuming, so the software can be told to rebuild only when commanded. Sometimes this approach gives incomplete results. We can allow a full rebuild after every change to avoid the hazard of incomplete rebuilds, but that rebuild wait time is boring. Thus, any technique that reduces the headaches associated with rebuilding is nerdly exciting news.

To add drama and excitement, the prelude to my rebuild demo is the theme of configuring a dimension without using a design table. If configurations as a CAD topic fails to make your heart go pitter-pat, then perhaps it will pitter after we consider the conduct of conduit in the assembly shown in

Figure 1A.

FIGURE 1A A modeled assembly is shown—a box with a conduit elbow mounted with an adapter nut. This model was created to pose a reason to configure the conduit’s model.

FIGURE 1B A cross-section view of the assembly reveals fine detail in the downloaded models. The utility box includes a subpanel. A close-up of the adapter nut reveals the threads, nut, and gasket. Perhaps some of this detail is extraneous, but it came free with the download.

FIGURE 2A A pattern of elbows follows a pattern of holes drilled in the box. The impossible intersection of the elbows is a problem to solve.

Figure 2B The solution is to configure the patterned elbows so they are the correct size for their location.

This model of conduit elbow represents an off-the-shelf, liquid-tight, UL-rated item fabricated with zinc-plated steel armor in ¾ trade size— very common. It is bent here on its minimum 5-in. radius, the smallest radius recommended for this style of conduit.

Figure 1B

shows a cross-section view passing through the conduit. It also shows a detailed view of an adapter nut. An adapter nut screws into the spiral armor at each end of the conduit to form a weather-tight connection. The threaded end of the adapter is gasketed to seal to the face of the box (or panel). (As a side note, these nuts are excluded from the cross section in this illustration.)

The CAD models for both the box and the adapter nut were downloaded as STEP files and then imported into the 3D mainstream CAD system used here. The large amount of detail inherited (see Figure 1B) from those STEP files is largely extraneous to this project but at the same time useful both for visual presentation and for trustworthy virtual prototyping.

However, extraneous CAD detail is a burden to the computer system’s performance and perhaps distracts from the mission. For example, the pitch and profile of the thread for the ¾ NPT panel connection is not vital to our mission. We are not going to manufacture the adapters; we are only going to drill holes so we can put them where needed.

As efficient CAD personnel, we eschew the extraneous detail. CAD’s Delete Face tool is our friend for the purpose of simplifying CAD imports. However, the labor to delete what can be easily ignored may be labor wasted. We wag our finger (officially, anyway) at labor expended that is not mission critical. Officially wag, anyway. From practical experience, accurate detail helps us anticipate actual experience and perhaps perceive an opportunity for improvement that might otherwise be missed.

In the spirit of showing detail without going overboard, the model for the spiral armor in the conduit is not full length as it would be in reality. Only a few inches of the spiral are modeled to reduce the computer’s rebuild burden.

We’ll take a closer look at the conduit modeling techniques used, but let’s first consider shape and how to shift it.

Figure 2A

is a variation on Figure 1A with an added driven pattern of four conduit elbows—a physical impossibility, but very easy to model. The pattern follows an Assembly Feature—a Hole Wizard pattern of four holes drilled into the side the box.

As an improvement over the impossibility of Figure 2A,

Figure 2B

shows the desired CAD model. How do we get from A to B with minimum fuss and bother?

We could create four separate CAD files for these elbows. Instead, we will create four shape-shifting configurations of the elbow in one CAD file. The advantages of configured parts include fewer file names on the disk and intuitive editing for the CAD jockey. The drawbacks include larger file size and possibly the burden of unused (extraneous) configuration data that the computer has to take time to ignore.

To manage our configurations, we could use a design table, as discussed in the July 2015 edition of this column. Instead, we shall configure dimensions by merely using right/left mouse gestures and a bit of typing.

Behold the mouse gestures 1 and 2 in

Figure 3A

. Before those two clicky gestures happened, a double-click on the conduit’s outer jacket revealed the path sketch for the jacket. Then, a right-click (1) on a dimension in that path pops up a menu (look for Configure Dimension in that menu). After that, a left-click (2) on Configure Dimension leads to

Figure 3B

. Note that, in this example, we’ve right-clicked on a dimension that has the internal CAD tag of D1@3DSketch1.

In Figure 3B, we see a user interface (UI) window titled Modify Configurations. This UI window presents a table for data entry and some control buttons. In this screen shot, we’ve already added rows for the needed four configurations. Each row was added by clicking on the row showing < Creates a new configuration >.

As each row was added, a configuration name was entered. Background information: The intended function of each of these conduits is to guard a leg in an electrical circuit (hence the Leg 1 through 4 names used here).

FIGURE 3A To add a configuration to the elbow, double-click on the elbow to show its path sketch, right-click on a dimension, and then left-click on Configure Dimension and proceed to Figure 3B.

FIGURE 3B Add configurations by clicking on <Creates a new configuration>. Here, four configurations have been set up for the legs: Leg 1, Leg 2, Leg 3, and Leg 4. The value of the dimension in the path (D1@3DSketch1) is unique to each configuration (2.0, 3.5, 5.0, and 6.5 respectively). The buttons control how the table is displayed and what it includes.

FIGURE 3C The configuration rebuild button has two options: Rebuild Active Configuration or Rebuild All Configurations. Sometimes, Rebuild All Configurations is a real labor saver. Rebuild Active Configuration is handy too.

FIGURE 3D Each patterned component is individually configured to use the appropriate configuration for its location in the pattern.

As the new configuration name was completed, a value was entered for the configured dimension (D1@3DSketch1). In this example, each subsequent leg grows by 11/2 in. As a result, the leg’s path changes to a unique shape for each configuration. We actually configured two dimensions in the path, but we’re skipping that for brevity here.

Those experienced with creating configurations know that the model must be rebuilt after adding and editing a configuration to fully translate sketch changes into Parasolid changes. But that’s foreshadowing.

Returning to Figure 3B, the first row in the table shows 7127K68. That is a legacy configuration left over from the original download of a native CAD model. This configuration probably should be deleted, and that’s easy to do from this UI— just right-click on a row and delete it.

It remains here as homage to the originator of the spiral armor model. Master’s version is not bent, and it’s 12 in. long and has the armor spiral exposed, but it’s otherwise an efficient model of liquid-tight conduit.

While we have the Modify Configurations UI open in Figure 3B, please note the row of mouse-able controls across the bottom of the window. From left to right, there is a button to swap rows and columns in the table—fun, but not "wow." For the moment, please skip the red/green button and arrive at a button to show the Custom Properties; it gives you properties ready to edit in a neat table– that’s "wow-ish."And there is a button to include more properties for review. Too much fun!

In

Figure 3C

, the red/green Rebuild button’s option arrow has been clicked—options for Rebuild All or Rebuild Active now await a mere click.

<Gasp, then applause>

At least in the user group meetings, this click to Rebuild All Configurations prompts a slow eye blink and some joy. I attribute the happy reaction to their workflow experience. It is sometimes necessary to verify that a change made to one configuration does not cause errors in other configurations during and after a rebuild. It can be tedious to click through each configuration to force a rebuild to verify adequacy. The Rebuild All button eases that tedium.

In

Figure 3D

, we take advantage of our four new leg configurations now present in the conduit elbow by right-clicking on a patterned elbow and then selecting a desired configuration for it. To try to hint at the process, in Figure 3D, the last of the four elbows is being configured; the others have been completed.

We turn from configurations to sweeping techniques (yes, that is punny).

Figure 4A

shows a cross section through the insulating jacket of our conduit elbow. We note that the armor spiral is of a computer-friendly length suitable for our virtual prototype—avoiding the extraneous detail, as it were.

The spiral body of the armor was modeled using a sweep. The resulting body was move-body/copied to create the second end of the conduit as opposed to remodeling a second helix and sweep. This technique was chosen to reduce error during redundant modeling operations.

In

Figure 4B

, we see cross-section details of the spiral armor. The profile sketch (in blue) was used in a Sweep feature to create the spiral armor. This profile sketch was borrowed from an online resource. We appreciate the detailed information available online from several sources, including Anaconda.

Not much effort was made to make the profile sketch suitable for tooling; just enough effort was made to make it visually credible.

Deep background: A feature of liquid-tight conduit that helps keep it watertight is a gasket that spirals between the flexing engagement of the armor. It didn’t take much effort to add that hidden gasket to the model, but "not much" can be a hard sell.

We could, of course, edit the sketch of the gasket’s profile. Instead of a simple circle, we could sketch flats to show how the gasket compresses against the surrounding steel spiral. If this were a pressure-critical project, where custom fabricated conduit is a possibility, that might be appropriate. It wouldn’t take much effort.

However, the finger wags. There are levels of descent into detail that practically make nonsense.

FIGURE 4A The conduit elbow is modeled to minimize computer overhead. Only a short segment of spiral armor is modeled. That body is copied to represent the armor at the other end of the cable, because copying is easier than redundant modeling of helix and sweep.

FIGURE 4B The spiral armor is modeled with a sweep of a sketched profile along a helical curve. The sketched profile is borrowing heavily from information found online. The profile includes a sealing gasket that is a design feature of liquid-tight conduit. This gasket model could be considered extraneous.

FAB

Please send your questions and comments for

Gerald Davis

to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-caddownloads

.
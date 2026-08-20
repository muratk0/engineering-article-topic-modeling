# A review of tricks to animate downloaded models

[TARİH: 01.07.2025 The Fabricator]

Precision Matters

Configurations to control mates help with animation of mechanisms

I

n

Figure 1

, the door to an enclosure is positioned to indicate the range of door motion and access available for service. A glance is enough to get an understanding of the mechanism.

In this (imaginary) project, screwdriver access is limited to the terminal blocks, which must be tightened before being snapped onto the switch actuator. But there might be alternatives. Perhaps the enclosure could be rotated 90 degrees, or a different terminal could be used?

Our purpose here is to demonstrate methods of adding kinematics to a CAD model utilizing a workflow suitable for mainstream 3D CAD.

For this example, the model for the enclosure is available as a download in a variety of CAD formats. If we were intending to fabricate the enclosure, a fully featured native CAD file might be the best starting point. That would facilitate parametric control over features ranging from material thickness, weld seams, fastener sizes, and other design considerations.

Going With What’s Commonly Available

Our scenario is instead to use generic off-the-shelf items wherever practical. The model is to represent what is routinely available. This CAD effort will result in:

A credible virtual prototype

Support for live review

The production of animations

A variety of illustrated documents, such bills of materials, dimensioned drawings, and glam shots

We anticipate that the review meetings will keep progress focused. The model might evolve extensively. Detail is added when it is likely to stick. Product manufacturing information, like tolerance, finish, and description, might be among the last details to be addressed.

Getting Down to Business

During a review meeting, actuating the mechanism (fancy talk for this demo of swinging the door) could help with progress in optimizing the design. A Limit Angle mate is the CAD technique we’ll use to set this up.

A Limit Angle mate does the trick by constraining the degree of freedom about an axis. (Here’s a quick CAD note: There are nine degrees of freedom and many types of mates with which to constrain them.)

Credible animation (a virtual prototype swinging like the real thing) is not necessary for the static glam shots. A freely movable component might even be a nuisance. Changes to the model’s position would propagate to the 2D drawing when it is opened. Unintentional edits waste time.

FIGURE 1

A design presented for review: We see how the door is opened for access. We also see that screwdriver access to wiring terminals is problematic. This is an example of how animation can help with problem identification and subsequent design improvement.

FIGURE 2A

The STEP file imports as a multibody part. Multibody parts are stationary critters. We prefer assemblies for dynamic animation. Because of this, we select the bodies for the box and choose "Insert into a New Part." We repeat this step to create a part file for the bodies that make up the door.

FIGURE 2B

The parts created in Figure 2A are added to an assembly. The box is fixed in location. The door just happens to float in a good-looking spot at this time.

During a review meeting, actuating the mechanism (fancy talk for this demo of swinging the door) could help with progress in optimizing the design.

For predictable, repeatable positioning, Fixed Angle mates are the cat’s meow. A set of configurations can control such positioning mates. That is to say, the value of the angle can be specified to change depending upon which configuration is active.

To open the door, the open configuration sets the value to 90 degrees. Closed is set to 0 degrees. To allow the door to swing, a third configuration enables the Limit Angle mate and suppresses the Fixed Angle mate.

Returning to the download, the STEP file for this enclosure imports as a multibody part (see

Figure 2A

). For a dynamic (i.e., swinging) mechanism, an assembly is more fun than a multibody.

To create an assembly from the multibody, bodies are saved as part files, and then those parts can become components in an assembly (see

Figure 2B

).

Within the assembly, the box is to be stationary. It should not move with the mouse. This can be accomplished several ways: fixing the component in place, mating origin to origin, or mating planes to planes. For this example, the box is fixed in position, as indicated by the (f) in

Figure 3

.

FIGURE 3

To make the door move realistically, a concentric mate aligns a hinge pin, and a coincident mate aligns the hinge knuckle. It now swings, but it can swing in an impossible 360-degree range.

FIGURE 4

A conflict between Limit Angle and Fixed Angle mates exists. We need to suppress one or the other. Adding a configuration is the next step.

FIGURE 5

A right-mouse-button click on Angle2 allows us to configure the feature using the table shown. Here, Angle2 is suppressed in the Swing configuration. At 145 degrees, Angle2 is open, and at 0 degrees, it is a closed case. We now have a well-behaved mechanism for drawings and a dynamic mechanism for entertainment—and review.

A concentric mate will center a hinge-pin on a door hinge. A coincident mate will keep the hinge assembled properly. With those mates as features of the assembly, a mouse-drag will swing the door. However, the door can swing unrealistically into the box.

The addition of a Limit Mate (with appropriate limit values of between 0 and 145 degrees) makes dragging the door realistically much easier.

As we proceed to add the Fixed Angle mates, a problem emerges as shown in

Figure 4

. The addition of a Fixed Angle mate overdefines the assembly with mates in conflict.

The remedy to the conflict between mates is the addition of a configuration (or few) to control what is constrained.

Figure 5

shows how Angle2 was configured to avoid such conflict.

The 2D drawing view will specify which configuration it uses (Open or Closed) to gain the desired repeatability. The Swing configuration could be handy during review.

For predictable, repeatable positioning, Fixed Angle mates are the cat’s meow. A set of configurations can control such positioning mates. That is to say, the value of the angle can be specified to change depending upon which configuration is active.

Gerald would

love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

ddavis@fmamfg.org

.

Editor’s Note: CAD files associated with this column can be downloaded at

www.thefabricator.com/page/shop-technology-and-3-d-cad-downloads

.

UNITOWER

Whether

standardized

or

customized

– our

tower storage

systems for

long goods

and

sheet metal

deliver the ideal solution for

boosting productivity

and

maximizing efficiency

.

kasto.com/storage-heroes
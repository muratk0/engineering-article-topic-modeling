# Automating an abrasive process

[TARİH: 01.04.2014 The Fabricator]

Quantifying the “feel” of deburring, edge finishing

By Robert J. McNamee

Manufacturing automation is becoming an integral part in maintaining revenues in an increasingly competitive market. Six-axis robots are a popular option for tasks such as material handling, painting, and spot welding. With the advancements in offline programming, vision systems, and sophisticated end-of-arm tooling, the capabilities of these industrial robots far exceed just pick-and-place tasks.

Another area where robots can excel is in deburring and edge finishing. The nature of this type of metal finishing is labor-intensive. The operator has to introduce the workpiece to an abrasive media, or in other instances, portable tools incorporating the abrasive media are brought to the workpiece.

Abrasive media, typically seen in deburring, fall into three categories and are available in various shapes:

1. Coated abrasives, such as belts, discs, flap wheels, and specialty shapes

2. Nonwoven abrasives, such as wheels, belts, and discs

3. Abrasive brushes, such as radial wheels and cup wheels

Coated abrasives are made of a resin and abrasive mix applied to a backing, generally a cotton or polyester cloth (see Figure 1). Nonwoven abrasives are also a mixture of resin and abrasive grains, but they are applied to a fibrous material that can then be formed (see Figure 2). In wheel form, the fiber acts as a bonding system that wears away with product use. In belt or disc form, a backing, or scrim, is used in a similar fashion as a coated abrasive. Abrasive brushes utilize abrasive-impregnated nylon filaments configured to a wheel (see Figure 3).

Figure 1 An example of a coated abrasive belt is shown.

Photos courtesy of Norton Abrasives.

Figure 2 These nonwoven abrasives have been formed into wheel shapes.

Figure 3 These types of brushes have abrasive-impregnated nylon filaments that act as the material removal medium.

Most of these tools are used for manual operations. These manual processes are commonplace because they are easy to implement and human operators are inherently flexible. However, any manual operation runs the risk of possible operator injury. In addition, manual operations can prove to be time-consuming and involve costly labor.

For these reasons, a growing shift in manufacturing to automate is being seen—even though each application has its own unique set of circumstances. Because many of these operations are based on an operator’s interpretation of the feel of the abrasive against the part, it can be difficult to make this transition. Fortunately, the feel of an abrasive media is quantifiable in terms of cut rate, wear rate, compliance, and conformability, and it is important to have a good understanding of these attributes as you take steps toward automating your process.

Material Removal Rates

In the abrasives industry, the cut rate of an abrasive is also known as

material removal rate (MRR)

and can be used in terms of volume (cubic centimeters per minute) or weight (grams per minute). For any given abrasive, this value will vary with material, the amount of force in the cutting zone, and the speed of the abrasive (which affects the forces in the cutting zone).

MRR is the key piece of information used in determining achievable cycle times for processing a given part. One simple test commonly used is to record the workpiece weight before and after grinding, and the total grind time—or contact time. Material removed divided by grind time gives the rate at which material is removed: MRR. Variations of this simple test method can provide valuable insight for feasibility studies when determining how to process a particular component.

It is also helpful to quantify the amount of material to be removed from the workpiece. The schematic in Figure 4 shows an approach that can be taken to define the volume of material to be removed to generate a 0.075-in. radius. Once this volume is determined, an abrasive or sequence of abrasives can be chosen based on their MRRs and the allowable cycle time. Figure 5 demonstrates an example of product mapping that compares the MRR of four nonwoven discs of different aggressiveness, with coarse being the most aggressive and producing the roughest surface finish and very fine being the least aggressive and producing the finest surface finish. This data can then be used to make informed decisions when selecting a product for the process.

Figure 4 This shows the volume of a 0.075-in. radius over a 10-in. length.

Figure 5 The MRRs of these four nonwoven abrasive discs with different levels of aggressiveness can be used to determine which is most suitable for an automated abrasives application.

One of the most significant variables that will affect MRR is the type of grain in the abrasive product. Speaking in general terms, three major types of conventional abrasives are used for deburring: aluminum oxide, silicon carbide, and ceramic alumina.

In these general terms, ceramic alumina grain has better MRR and longevity characteristics than its silicon carbide and aluminum oxide counterparts. It is important to take this into consideration when selecting a product for the automated system. Maximizing efficiency and reducing overall costs in the operation may require a premium grain. Though the products may be more expensive, the abrasive costs are negligible in comparison to the savings associated with reduced cycle times.

Wear Rates

The

wear rate

is an indication of how quickly an abrasive media reaches its so-called “end-of-life,” which varies depending on the abrasive and the workpiece. Some examples that characterize the end of the abrasive’s usable life are:

• Significant reduction in MRR and unachieved geometric tolerance requirements

• Unachievable surface finish requirements

• Wheel reaches stub size

One simple test commonly used is to record the workpiece weight before and after grinding, and the total grind time—or contact time. Material removed divided by grind time gives the rate at which material is removed.

How quickly these conditions are reached and at what rate are important factors to take into consideration when developing an automated system. When these are determined, you can put programming or feedback measurements into place to account for these changes.

For example, software programming can be used to increase the penetration into an abrasive brush face by 2 percent after 10 cycles to maintain a required cut rate, or simple counting programs based on the number of cycles an abrasive media can maintain a surface finish can be relied upon to signal an abrasive media change. In another example, probing or vision devices can account for the reduced diameter of an abrasive wheel.

When compensating for wear characteristics, pay attention to the abrasive’s cut consistency, especially for tight tolerances.

Magnified views show a conventional abrasive structure in Figure 6 and an engineered abrasive structure in Figure 7. These are both classified as coated abrasives.

Figure 6 In a conventional abrasive, the grains are dispersed randomly based on the coating method.

Figure 7 Controlled placement of abrasive patterns is the hallmark of engineered abrasives.

The controlled pattern of the engineered structure allows for a consistent cut rate as well as surface finish. Understanding that wear rates of engineered coated abrasive follow a more consistent trend will increase the controllability of the automated process.

Compliance and Conformability

Compliance and conformability are two attributes that are similar in nature, but refer to different parts of the automated system.

Compliance

, normally used when describing fixturing or tooling, refers to the ability to control the amount of force between the workpiece and the tool. It is common to achieve compliance with a combination of pneumatic cylinders or mechanical-electrical controls that regulate the air pressure or electrical current and, as a result, the force at the grinding interface.

To better illustrate this, picture a robot carrying a workpiece to an abrasive belt grinder outfitted with a constant-force pneumatic cylinder, which allows the grinder to “give” when force is applied. This give, or compliance, allows the force to be nearly constant at the area of contact between the workpiece and the belt, assuming the area of contact does not change. Even if the robot’s position accuracy or repeatability is ±0.002 in., the compliance can help account for this variation by allowing an interference to be programmed at the contact area. This is also true for situations where the tool is compliant and brought to the workpiece.

Overall, it helps to increase the accuracy and consistency of the results of the robot by allowing for positioning error at the tool center point while maintaining an acceptable force. In terms of abrasives, this allows the system to control the MRR. Compliance fixturing and tooling are well-known among robotic manufacturers and integrators.

Conformability

refers to the ability of the abrasive to match, or reach, the various contours and intricacies of the workpiece. A good example of this is a nylon abrasive brush conforming to a corner, edge, or complex geometry (see Figure 8). Each filament has the flexibility to bend and pull across the workpiece and introduce the abrasive grains, taking small repeated cuts until the edge finish condition is reached. These two attributes are especially important when finishing irregular features.

Figure 8 Notice how the brush conforms to the workpiece edge.

A turbine blade is an example of a component with several areas that may present difficulties for automation and will require the right combination of compliance and conformability. Generally, the more complex the features are to deburr, the more conformability and compliance will be required in the system.

Automating a manual operation can pose several unique difficulties, but the benefits of reduced costs and increased safety for operators may prove to be attractive to some fabricators. By keeping an eye on the key elements of material removal rate, wear rate, compliance, and conformability, you can successfully transition from an offhand operation to an automated abrasive process.

Robert J. McNamee is an application engineer, Norton Abrasives/Saint-Gobain, 1 New Bond St., Worcester, MA 01615, 800-962-9379,

www.nortonabrasives.com

.
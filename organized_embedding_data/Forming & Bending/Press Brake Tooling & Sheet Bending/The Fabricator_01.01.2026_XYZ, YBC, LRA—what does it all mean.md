# XYZ, YBC, LRA—what does it all mean?

[TARİH: 01.01.2026 The Fabricator]

Exploring Tube Benders

Getting from print to part

By

Jay Robinson

T

o bend tubular parts on a CNC bender, you have to use some kind of coordinate system to give the machine the data it needs to produce the part. The data governs how the machine moves to create the bent part from a straight tube. This data can take different forms, including XYZ, YBC, and LRA.

XYZ DATA

Sometimes referred to as Cartesian coordinates, XYZ data is the most common kind found on engineering and manufacturing prints. However, it also can be the hardest to understand, especially when it relates to tubing.

Point in Space.

An XYZ coordinate can be any point in space. Defining it requires a point of reference—its origin. The origin also can be any point in space, but it is the point from which all other points are measured in three dimensions.

X

is a horizontal distance left or right. As you move from origin to the left, the distance is represented as a negative value. As you move to the right, the distance is represented as a positive value.

Y

is a horizontal measurement away from or toward you. The distance moved away from origin is represented as a positive number, and a move from origin toward you is represented as negative.

Z

is a vertical measurement, up being represented as a positive distance from origin and down being a negative distance from origin.

Making It Work for Tube.

In this way, any point can be defined. But how do you make a point in space relate to the shape of a tube?

Imagine you have a straight piece of tubing with a string exactly through the center of it. Now, imagine the tube is bent to 45 degrees, but the string remains perfectly straight. So one end of the tube has a string in the center that continues straight on through the bend to infinity.

Now imagine a second string that starts at the opposite end of the tube and continues exactly down the center but also stays straight at the bend, continuing on to infinity. Because they are exactly in the center of the same piece of tubing with one 45-degree bend in the center, those strings will eventually cross. If you have an origin to measure from, the point where the strings cross can be defined using XYZ coordinates.

Now imagine the same piece of tubing with multiple bends in all directions, but with a straight piece of string down the center of every straight section of the tube. Every place the strings cross, a new point can be defined using XYZ coordinates.

When all the points in the bends are defined, you need to represent the tube ends by defining the point where the string passes exactly through the center at the ends of the tube. One end of the tube gets its own origin point, and the opposite end gets an end point.

While most drawings of an individual tube define the "A" or beginning end of the tube as the origin-XYZ coordinates (0,0,0), that is not required. The tube may be part of a larger assembly, and the origin point of the drawing may be far removed from the end of the tube you are trying to produce.

Working in Three Dimensions.

Representing the tube, or any part, on a piece of paper as a drawing is challenging because the part is three dimensional, but the drawing is two dimensional. Because of this, most drawings will have the part drawn twice or even three times, with each drawing presenting a different perspective. In this way, all three coordinates for each point can be displayed effectively.

The coordinates of the part often are listed on the print in a chart, but you may have to make your own. Starting from one end of the tube, list all three coordinates:

1. At the center where the tube originates

2. Where the centerlines (the strings you imagined) cross

3. At the center where the tube terminates

So, an XYZ chart of a bent tube will always have at least two more points than the number of bends in the part.

Limitations.

There is a limitation in using XYZ coordinate data when the bend in the tube is 180 degrees. When this happens, the two straight legs are parallel to each other, so the strings never cross.

To overcome this, you must define at least one extra point. The most common is noted as if there are two 90-degree bends and a straight line through the center of the tube at the apex. In this case, the XYZ chart will have three more points than there are actual bends because the 180-degree bend is represented as two 90-degree bends plus the two end points.

Some tubes have additional details—like holes, fittings, or other information—the location of which may be called out in the same XYZ chart with the bends. You may have to eliminate these additional details from the chart, as a feature like a hole will be away from the center of the tube.

YBC AND LRA DATA

YBC data represents the same data as XYZ coordinates, but it is listed in a way that is easier to understand when adjusting on the machine. Y, B, and C relate to the axis names most manufacturers use on CNC tube benders. LRA stands for length, rotation, and angle, so YBC and LRA values are interchangeable. Some bender manufacturers that use different designations for their axis names will use LRA to program or adjust the tube in their software.

Y

is the axis that moves the tube away from or toward the bending axis using a carriage. This movement defines the straight

length

of the tubing, including from the first end of the tube to the first bend, the straight length between the bends, and from the last bend to the end of the tube.

B

is the axis that can

rotate

the tube and so can change the plane in which the tube is bent relative to the other bends.

C

is the axis that forms the tube into a bent shape to a defined

angle

.

Think back to the XYZ coordinates and imagine the tube with a single bend in it. The length of the section of tube that is straight will change if the radius it is bent around changes, even though the XYZ coordinates will stay the same. That straight length is measured tangent to tangent, with tangent defined as a straight line perpendicular to the linear direction of the tube, originating at the center of the circle being formed by the bend die.

The angle of the bend is defined by the difference in direction of the intersecting lines. (They are unaffected by differences in bending radius.) If you had just lengths and angles and the tube stayed in one plane, you would need only X and Y coordinates, and there would be no need for rotation.

The rotation of the tube changes the plane of the bend, moving the intersecting points in the vertical direction. Imagine that the origin point of the tube (a point at the perfect center of the end of the tube) never moves. When the tube is bent, instead of the tube being moved, the machine and the rest of the tube are moved. Instead of the tube being rotated, the machine is rotated around the tube, changing the plane the part will be bent in. The bend will now make the machine move up and down, as well as left or right. So, as each bend is made, the intersecting lines of two bends will be in the correct XYZ position relative to the origin point of the tube.

Most modern control systems will let you enter the coordinate data using either XYZ or LRA coordinates and convert to the other—or import, analyze, and create coordinate data from a solid model, such as a STEP, IGES, or Ship Constructor file.

Several software products are available that can convert XYZ data to LRA data, adjust the part design to accommodate additional needed lengths or features, generate reports and part views for the operator, and even transfer the data directly to the bender’s control system.

Jay Robinson

is owner of RbSA Industrial,

rbsaindustrial.com

.

Tower’s Tube Bending Lubricants

CONTACT TOWER TODAY & LEARN ABOUT OUR

FREE

SAMPLES!

Engineered For Every Bend

SAF-T-VANISH

Hazard-free evaporative lubricant for throughmandrel bending of 3″ stainless steel on 1.5D bends.

Bend-All Heavy Duty Paste & Oil-Free Gels

From 1.5″ handrails to 10″ process pipe, engineered for strength and consistency.

Halogen & Chelator-Free Fluids

Designed for Aerospace, Nuclear & Defense critical applications.

Trusted Worldwide.

Engineered for Excellence.

For over 40 years, New-Form Tools has been a trusted partner to the tube and pipe industry, delivering

Carbide-Tip (TCT) Circular Saw Blades

and Shear Blades that help operations run smoother, last longer, and cut cleaner.

Engineered for precision and durability, our blades are designed to keep your production

a cut above.

Get the Blades that Go the Distance!

LONGER BLADE LIFE.

LOWER COST PER CUT.

LESS DOWNTIME, MORE PRODUCTIVITY.

www.newformtools.com

| 519 -272-0921 |

tjantzi@newformtools.com
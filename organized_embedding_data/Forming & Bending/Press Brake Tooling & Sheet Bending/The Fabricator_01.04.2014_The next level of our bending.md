# The next level of our bending

[TARİH: 01.04.2014 The Fabricator]

Adaptive forming helps to improve the quality of bends in a press brake

By Wim Serruys

Editor’s Note: This is an edited excerpt from

Sheet Metalworking: State of the Art

, published by LVD Group.

Air bending (also known as free bending) is the most common way for bending sheet metal because of its flexibility.

In air bending, a bend angle is formed by driving the punch into the sheet metal to a specific position within the die opening. Different bend angles can be obtained using the same set of tools. The sheet thickness and the behavior of the material determine the angle that can be achieved by the position of the punch.

As the punch drives down into the sheet metal, plastic deformation of the material occurs—not the fracturing of the material that occurs with cutting and punching. In fact, tensile strength of the material has little effect on the bending process. (After the bending occurs is another story.) Bending is mainly affected by strain hardening, the property by which a material becomes stronger the more it is deformed.

Looking at the bending of material with low strain hardening, a press brake operator finds that the resistance to yield remains virtually the same even until deformation. As bending occurs, the material first yields where the bending stress is highest: in the middle of the die under the punch. There is no reason that surrounding material should yield, and the deformation continues where it started. The material bends around the punch, and the radius of the bend will be equal to the punch radius.

In materials with high strain hardening, the yield point increases as the material deforms. The material will yield first where the bending moment is highest: in the middle. However, upon deformation, the material becomes stronger, so the surrounding material is given an opportunity to deform, which means the internal bend radius becomes larger. Because the radius is not determined by the radius of the punch, it is referred to as the natural bend radius.

Material variations present a challenge to accurate air bending. Variations in material thickness are frequently found in a batch of sheet metal. Even within a sheet, the thickness can vary from the edge of the sheet to the center, which is caused by the rolling process used to size the sheet at the rolling mill. Material properties also differ depending on whether the material is rolled parallel to or perpendicular to the rolling direction, which is called anisotropy. As a result, the accuracy of the bend angle using air bending is limited to ±1 degree.

The discussion to this point, however, has focused only on the bend angle under a load. As soon as the load is taken away, the induced stresses cause the material to spring back, which affects the formation of the desired angle. (Springback increases proportionally with a material’s tensile strength.)

Better Accuracy in Air Bending

As can be seen, many variables can affect the air bending process. Sophisticated control software can dictate the punch position recommended for a material type and thickness, but the nature of the material ultimately has an influence over whether that material is bent accurately the first time. Adaptive forming technology can help to ensure the first piece and every piece thereafter is bent to specified angles.

Adaptive forming is a special form of air bending. The same tool setup is used as in air bending, except that the punch position is not preset to a particular value. The position of the punch is controlled through the press brake’s in-process angle measurement system. In contrast to air bending, the bend angle obtained is no longer influenced by the sheet thickness or the strain hardening of the material. As a result, adaptive forming has better accuracy with a tolerance of 0.3 degrees on the bend angle.

Two methods stand out in the adaptive forming process: One measures the amount of springback and the other does not. The fastest and most commonly used method does not measure the spring-back during the forming process. As the punch closes in the die, the angle of the material is measured to equal the desired angle minus the spring-back angle. When the punch retracts, the material will spring back to a known springback position relative to the desired angle.

During adpative forming of steel to an angle of 90 degrees, the control forms an angle of 88 degrees knowing that the springback is 2 degrees. The springback angles for all known materials are stored in the control database. Neither variations in material or thickness have much effect on the springback angle. Even with the tolerances caused by the steel manufacturing process, a bending tolerance of 0.3 degrees is achievable.

This method of adaptive forming takes the same amount of production time as air bending.

When springback is measured during the bending process (see Figure 1), three sequences take place. If the bend angle required is 90 degrees, the movement of the punch into the die is adaptively controlled to 90 degrees. When the bend angle of the material is achieved, the movement of the punch is reversed, and it is raised until the bending force is removed. At that moment, the bend angle is measured again.

Figure 1 When springback is measured during the forming process, the press brake bends the workpiece to the correct angle, releases the pressure on the workpiece, measures it to determine the amount of springback, and then applies the necessary pressure to achieve the desired bend angle. All of this takes place in one operation.

If this is 92 degrees, for example, then it is concluded that the springback angle is 2 degrees. In a third movement, the sheet is then adaptively formed to 88 degrees. This method is slow and is used only if the springback angle is unknown. After applying this method once, the springback angle is known and adaptive forming subsequently can be used without measuring the springback.

Making Adaptive Forming Work

Before adaptive forming can be employed, the bend angle must be accurately measured. However, to be useful in an industrial environment, additional conditions need to be met.

First, the values measured must be transferred quickly to the CNC so that the bending process is not delayed because of slow measurement. Typically, the frequency of the data stream is 100 samples per second.

In addition, the angle measuring system must be set up so that it does not obstruct the bending process. It should be capable of measuring the bend angle of small flanges and Z profiles.

Figure 2 explains the principle of an angle measuring system. Located on the front and back of the press brake bed are two measuring systems that measure the angle between the die and the workpiece. A laser beam is projected against both sides of the die and the workpiece, creating within the range of the cameras two lines of laser points. One line is the projection of the workpiece; the other is the projection of the die. The difference between the slope of the two lines is the angle B. This is completely independent of the position of the measuring system. The bend angle A = 360 degrees -B1 -B2.

Figure 2 This is how an angle measurement system might look installed on a press brake.

Setup time must be short, and changing measuring systems for different tools or bending angles is neither practical nor efficient. Many angle measuring systems waste time because they must be calibrated when the tools are changed because the geometry between the dies and the measuring system changes during the setup. The system shown in Figure 2 does not have this disadvantage because the measured variables are independent of the setup.

Finally, the working environment must not affect the function of a good angle measuring system. Machine tolerances and the deflection of the press during the bending cycle interferes with the reference between the workpiece and the measuring system.

When long parts are formed, particularly on a machine with long beds, the bend may be out of the center. The angle still needs to be measured correctly. Figure 3 shows that the alignment between the punch and die does not influence the measurement of the bend angle.

Figure 3 Angle measurement systems are flexible enough to accommodate out-of-alignment bends and still deliver the correct measurement information.

Deformation of tools is another condition that should not affect the function of the measuring system. Therefore, the projection on the tool will be calculated prior to the bending load (see Figure 4).

Figure 4 Angle measurement systems calculate bend angles before bending loads can deform tooling.

Adaptive forming systems that take material springback into account also require that the spring-back is accurately determined when the workpiece is completely relaxed; that is, when the force is no longer being exerted between the workpiece and the tool. Defining this point can be accomplished by using the same measurement system.

During the bending process, the legs of the die will open by a couple hundredths of a millimeter. This movement is detected by the angle measuring system as a small change in the slope of the line projected on the die. In the adaptive springback system, the punch is raised until the measuring system recognizes that the die is back in its original position.

Wim Serruys is director of engineering, LVD Group, Nijverheidslaan 2, B-8560 Gullegem, Belgium, 32- 56-43-05-11,

info@lvd.be

,

www.lvdgroup.com

.
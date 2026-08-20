# Angle adjustment fundamentals

[TARİH: 01.12.2022 The Fabricator]

Expertise Bending Basics

Difficult to grasp for novices, such adjustments get easier with experience

By

Steve Benson

www.thefabricator.com/author/steve-benson

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association Intl. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book,

Bending Basics

, is now available at the FMA bookstore,

www.fmamfg.org/store

.

Question:

I am new to the press brake world, and I need help understanding how to change my numbers when measuring a piece. For example, let’s say that the piece requires a 90-degree angle, and my part is at 88.5 degrees. I know I need to add 1.5, but I’m not sure which way to move my number (up or down) when I’m starting with a negative or positive number.

Answer:

How to adjust an angle is a great question, one that I have not addressed before. To help you understand the nature of angle adjustment, we will begin by looking at the modes of operation in a press brake controller.

A press brake generally has two and sometimes three modes of operation. These include

manual data input

(MDI, also known as

depth mode

),

angle mode

, and graphics mode. Graphics mode often is combined with angle mode into a single option. Note that your press brake may use different names for these modes or options, but the functionality is the same.

When working in MDI mode, assuming the press brake zeros at the bottom of the stroke under a small load, the technician enters data that says to the press brake controller, "Go to a position X number of thousandths above 0 to achieve a given bend angle when the operating pedal of the press brake is engaged." Those adjustments are made in thousandths of an inch or millimeters.

In an angle-mode program, the technician tells the controller what the desired bend angle is, the tooling being used, and information about the material to be formed. The controller then takes that information and calculates the punch descent into the die space and the total depth required to achieve the bend angle. The controller sets the initial penetration depth into the die space based on the operator’s initial inputs. The operator then adjusts the angle at the press brake. Rather than using a direct numerical value, adjustments are made in degrees of bend angle.

Graphics mode operates similarly to angle mode while displaying pictures on the controller’s screen showing how the flange will progress throughout the bending process.

How Controllers Read the Angle

Angle and graphics adjustments differ entirely from depth mode. This is where bend angle adjustment becomes hard to follow, especially for an inexperienced operator, because of how different controllers reference themselves and how they convey the angular measurement of the bend.

FIGURE 1 Bends can be described by their complementary or included angle. Note that these naming conventions differ from those used in geometry, but since "included" and "complementary" are widely used on the shop floor, I’ll use the terms here.

To understand how the controller views things, we need to look how we label angles. As shown in

Figure 1

, external angles are called

complementary angles

while internal angles are

included angles

. Add the included and complementary angle measurements together, and you should get 180 degrees. So, a 135-degree complementary angle is a 45-degree included angle. It’s the same angle, just a different way of defining it.

Note that these naming conventions differ from those used in geometry. That said, "included" and "complementary" are commonly used on the shop floor, so that’s how I’ll describe bend angles here. Also note that most callouts on prints use the complementary angle.

You must understand how your press brake controller makes the measurement to adjust the bend angle. During air bending, as the punch moves downward into the die space, the included angle decreases while the complementary angle increases (see

Figure 2

).

Angle Mode

If your press brake controller sees the angle as complementary, an underbent flange needs an increase in bend angle. So, if you need a 45-degree complementary angle and your current bent angle is 42.5 degrees complementary, you need to change the value in the controller using one of two methods. The first is to change the initial value of 45 degrees to 47.5 (2.5 degrees greater). The second method is to use the angle-adjustment function on your controller and input a positive 2.5 degrees (see

Figure 3

).

FIGURE 2 During air bending, as the punch descends into the die space, the complementary angle increases while the included angle decreases.

FIGURE 3 In this case, the controller programmed to bend to 45 degrees complementary resulted in an actual angle of 42.5 degrees. To increase the complementary angle by 2.5 degrees, in angle mode, you can tell the controller to bend to 47.5 degrees complementary or input a positive 2.5 degrees using the angle-adjustment function.

FIGURE 4 Say your controller reads the included angle and is programmed to bend 135 degrees. Your initial bent angle is too large (137.5 degrees), so you adjust by decreasing the included angle by 2.5 degrees.

If, on the other hand, your press brake controller reads the included bend angle, then the angle adjustment will be the opposite. That is, the angle value will get smaller. Take the same 45-degree complementary bend, which has an included bend angle of 135 degrees (see

Figure 4

). Your machine is programmed to bend a 135-degree included bend angle, but your initial bent included angle is 137.5 degrees. So, you change the primary controller angle input to 132.5 degrees, representing a decrease of 2.5 degrees in the measured included bend angle. You could also make 2.5 degrees of negative bend-angle adjustment at the angle-adjustment input.

FIGURE 5 Sometimes, the origin point is set at the bottom of the die, but other times, the origin point is set at the top surface of the material, as shown here.

Depth Mode

To adjust the angle in depth mode, you’ll need to input a direct increase at the controller in either inches or millimeters, depending on the preferences you have set for the controller. Angle adjustments are direct; if you need to go from a complementary angle of 88.5 degrees to 90 degrees, the operator will tell the controller to move down, say, 0.005 in., from a penetration depth of 0.074 in. to 0.069 in., which will, with any luck, bring the next bend to the desired bend angle of 90 degrees (please note that the 0.005-in. value is arbitrary).

Returning to the 45-degree complementary bend angle example, let’s say your initial bend is only 42.5 degrees complementary. If 0.005 in. equals 1 degree of angular change, and you need a complementary angle that’s 2.5 degrees greater, you would simply tell the controller to drive the ram 0.0125 in. deeper (0.0125 is 2.5 multiplied by 0.005). So, rather than the initially called depth of 0.074 in., as measured from the bottom of the die, you would tell it to go to 0.0615 in. from the bottom (0.074 – 0.0125 = 0.0615).

The explanation I just gave works fine if you are originating the press brake at the bottom of the die. But what if you use the depth mode and you originate the system on top of the die plus the material thickness (see

Figure 5

)? Chances are the controller is reading the included bend angle, but guess what? The new input depth will get larger.

Confused Yet?

While experienced technicians and operators are familiar with these concepts, some will still find them difficult to grasp, even after years of experience. It is even more confusing if you are new to the press brake.

Over time you will get comfortable with the machine you operate daily, but your chances of running the same machine every day are pretty slim, given a long enough timeline.

If your shop uses just one brand of press brake, switching and adjusting won’t be too much of an issue. But again, the chances of that are slim, and you will be switched to another press brake at some point. But have no fear. With experience, you’ll be able to handle the adjustments just fine.

Up to 6-inch O.D. | Short Lead Times

Pipe and Tube.

Bending.

Laser Cutting.

End Forming.

Sharpe Products specializes in custom tube and pipe bending, laser cutting and related fabrication, up to 6-inch O.D. With the latest machine technology and a large selection of tooling, we are known for short lead times and quality results. Whatever your tube bending or laser cutting needs, we’d value the opportunity to work with you.

Visit us at

sharpeproducts.com

.

sharpeproducts.com

ISO 9001:2015 | Over 30 Years in Business

NO MATTER WHAT YOU’RE WELDING, BLUCO

®

HELPS YOU MAKE IT BETTER

®

Ships, tractors, equipment … no matter what you weld, overcoming fixturing obstacles takes more than hardware. It takes collaboration, experience, and hard work. And that’s exactly what Blucoe provides. We’ve solved problems alongside thousands of customers in countless industries. From

big picture issues

like improving efficiency and ensuring repeatable accuracy, to

targeted details

like welding mitered corners flawlessly or eliminating heavy lifting. From

prototype to production

, the key to success isn’t a fixture — it’s a modular fixturing solution. Visit

bluco.com/request-a-proposal

today to get started on your solution.

MODULAR FIXTURING SOLUTIONS FOR

WELDING MACHINING POSITIONING ROBOTICS

Call 800.535.0135 for Solutions

33 YEARS Of EXCELLENCE |

BLUCO.COM

VISIT US AT FABTECH, BOOTH #C12417
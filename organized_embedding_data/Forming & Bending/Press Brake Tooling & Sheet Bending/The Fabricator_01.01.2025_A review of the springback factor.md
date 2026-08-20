# A review of the springback factor

[TARİH: 01.01.2025 The Fabricator]

Bending Basics

What is it, and how can it help?

STEVE BENSON

A

lbert Einstein once said, "The more I learn, the more I realize how much I don’t know." This is known as the paradox of knowledge. It reminds us of the vastness of the unknown and the never-ending nature of the pursuit of knowledge.

For the past several months, we have been discussing the inside radius of the bend, including its importance in design and manufacturing. So, what’s next? How about a look at the springback factor? What is it, and what does it have to do with the inside bend radius? Well, as you might have already guessed, you’re about to find out.

What Is Springback?

You probably know what springback is, but if you’re new to bending or need a refresher, here are the basics: When you form sheet metal (or anything else that will bend, for that matter), you will see varying amounts of springback. The nature of springback varies with the bending method, but for this discussion, we’ll focus on air bending. Also know that I’ll be referring to outside angles, as measured from the outside of the bend (see

Figure 1

).

When you release material from the load (force), the bend relaxes as the material tries to return to its original flat position. It doesn’t make it all the way back to flat, but the angle does spring back open a certain amount. The press brake air-bends to the

bending angle

, which is the required angle plus the necessary degrees of overbend for springback. When sheet metal is released from the load, it releases the energy put into the bend and the angle relaxes to the

bent angle

, the angle that the material achieves once the springback has been released (see

Figure 2

).

Springback is part of the final developed bend radius. When the bending angle relaxes, so does the inside radius of the bend. It relaxes a small amount, just like the bend angle. Can you calculate it? Yes. Can it be used? Sure. And here’s how.

Calculate the Springback Factor

Divide the bending angle by the bent angle and we get a multiplier value known as the

springback factor (Sf)

, which we use to calculate the actual inside radius of the bend. For example, if you are working with a material that has 2 degrees of springback, and you need to make a bend with a final angle of 90 degrees, you know you need to overbend to an outside angle of 92 degrees:

Sf = 92 degrees/90 degrees = 1.0222

FIGURE 1

Outside bend angles are measured from the outside of the bend.

FIGURE 2

The press brake overbends to the bending angle, then releases pressure and allows the bend to relax and spring back to the bent angle. The bend radius relaxes too—not by much, but enough to affect your bend allowances and bend deductions.

What do you do with that number? You use it as a multiplier, which is then applied to the original expected inside bend radius. If the inside bend radius is 0.062 in., you multiply the beginning inside radius value by Sf to find the actual inside bend radius after the bend relaxes: 0.062 × 1.0222 = 0.063. This gives you your relaxed inside bend radius, which you then use to calculate the bend allowances (BAs), bend deductions (BDs), and outside setbacks.

Springback isn’t limited to 2 degrees, of course. Depending on the material type, the springback could be less or even a lot more. We need to calculate Sf using the actual angles involved, which often requires bending a few test pieces before making any calculations.

For the last few months, I have been hammering the importance of the inside bend radius to any project that requires bending. It is the heart of anything you are trying to accomplish. If you get that incorrect, guess what? You get finished parts that also are incorrect.

Two Degrees Is Not Two Degrees

You might be asking, is this one of those situations where two plus two equals five? No, it is not. That kind of math only works in politics. I’m referring to the fact that simply knowing a bend springs back by 2 degrees doesn’t give us our springback factor. The Sf changes depending on what the bending and bent angles are:

Again, even though each of these angle pairs is 2 degrees apart, the value for Sf varies with the angle of bend, which also affects the BA, BD, and setback calculations. As we all know, flawed calculations equal bad parts.

Imagine a job in which we achieve a 0.063-in. radius in 0.063-in.-thick material at the bending angle, before springback. When the angle springs back 2 degrees, the radius opens slightly. Assuming a k-factor of 0.446, how does this affect our bending calculations? Check out the below examples:

We’re talking changes of just a thousandth or two. The changes are minimal, but they’re still there.

Do We Really Need to Worry?

That depends on your part tolerances and just how accurate your parts need to be. It also will depend on how many bends you have in one workpiece.

If you have a tolerance of ±0.020 in. and multiple bends, then the springback factor would be worth considering, as every additional bend compounds the amount of error you will see in that part. If your tolerances are just ±0.010 in., then it is a pretty good idea to incorporate the springback factor in your calculations.

Measuring the Radius

A different level of springback changes your inside bend radius. For precision work involving multiple bends, even the smallest change can throw everything off. So, if you want to be accurate, how do check for such minute changes?

Pin gauges work great but are expensive, and people tend to lose them. I recommend making your own radius gauge set. Create a single DXF file for a single gauge, then, at the laser or waterjet, scale it up or down for the radius you need to measure.

You can create a single gauge and let it travel with the work folder. Alternatively, you can create two complete sets, one for the forming department and another in quality control. Make a set for everyone working in the press brake area.

Small Numbers, Big Impact

For the last few months, I have been hammering the importance of the inside bend radius to any project that requires bending. It is the heart of anything you are trying to accomplish. If you get that incorrect, guess what? You get finished parts that also are incorrect.

Tight tolerances in precision bending are like bacteria. They may be very small, but they have a big impact.

Small numbers matter. A thousandths error on one bend might not sound like a big deal, but what about a part that has a dozen bends or more? Before you know it, a tiny error can snowball into a major problem.

Like multiplying bacteria, the tolerances stack up, and before you know it, you’ve scrapped a complicated, and probably very expensive, part.

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

FORNEY INTRODUCES

VERSATILITY AND POWER IN TWO NEW MACHINES

Designed to offer exceptional versatility, power and reliability for professionals and hobbyists alike.

190 AC/DC MP:

Ultimate versatility with AC/DC TIG, MIG and Stick capabilities

Suitable for professionals and skilled hobbyists

Handles welding on various metals like aluminum, steel and stainless steel

Designed for versatility in multiple welding applications

250 MP PRO:

Portable and powerful, delivering high amperage and extended duty cycles

Designed for professional use with MIG, Flux-Core, Stick and TIG capabilities

Dual-voltage and generator compatibility for adaptability on job sites, including remote locations

Trilingual LCD screen

To learn more about our new machines, call your Forney sales rep, or go to

Forneyind.com

We shape the conversation around metal

Hosted by The Fabricator’s Dan Davis and co-hosted by a rotating cast of editors and contributors, The Fabricator Podcast welcomes people who are either working in metal fabricating or working to attract more talent to the industry.

Find the Fabricator Podcast on any major podcast platform, including Apple Podcasts, Spotify, and YouTube.

The Fabricator Podcast is presented by the Fabricators and Manufacturers Association.

Find us wherever you get your podcasts
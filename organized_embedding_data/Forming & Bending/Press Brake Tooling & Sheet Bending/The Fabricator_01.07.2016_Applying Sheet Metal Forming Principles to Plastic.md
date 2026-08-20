# Applying Sheet Metal Forming Principles to Plastic

[TARİH: 01.07.2016 The Fabricator]

Bending Basics

As in metal, results depend on the plastic’s material properties, thickness, and radius

By Steve Benson

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Figure 1

Every bend has tensile stresses on the outside surface and compressive stresses on the inside surface. Material on the inside of the bend has reached its plastic state while the outside of the bend has not; this elastic state on the inside of the bend forces the bend to spring open. The neutral axis does not remain at 50 percent of the material thickness during bending. Instead, without going through any physical change, it simply moves toward the inside surface of the material, causing elongation in the bend.

Figure 2

According to

Machinery’s Handbook

, the K factor, or multiplier value, ranges from 0.40 to 0.50 for mild cold-rolled steel with 60,000-PSI tensile strength, depending on the forming method.

Question:

I am forming plastic, not metal, but I am applying metal bending principles to my application. After a few years of iteration, we have developed an accurate flat-pattern method for our tank bending operations. Our tanks are formed from sheet stock typically 0.25 in. thick, thinned in the bent areas along the circumference and wrapped into a rectangle with radiused corners. I have an accurate K factor for this bend condition. The inside radius for these bends is 0.75 in., and all along the radius the material thins to 0.078 in.

We also do sharp bending from sheet stock that is thinned in the bent areas, but V-cut with a small flat bottom. It’s thinned at the flat bottom to 0.063 to 0.078 in. Based on the same K factor as the large-radius condition, the flat pattern here produces a part that is too long. So I conclude from this that the K factor for this condition is less than for the large-radius condition.

What do you have to say about K factor versus the type of bend in plastic material? It seems if the K factor for the first condition is 0.4, the K factor for the second condition is 0.2 or less. Is there a known relationship for metals when dealing with the same comparison? Any information would be appreciated.

Answer:

Unfortunately, my experience with plastic is limited to forming Lexan™ on a press brake within a sheet metal manufacturing environment. While my plastic forming experience is limited, I have had reasonably good luck producing good parts by applying sheet metal theories and layout calculations for the flat-pattern development.

Though I did find that springback in Lexan was much greater than for sheet metal, the time it took for the springback to fully relax in plastic was quite long—hours versus immediately after bending, as with sheet metal. Also, heating your punch can help eliminate much of the springback encountered in many plastics.

Terminology

To answer your question, I need to define the terms we are going to use for the discussion. Although those who study and work regularly with plastic may use different terminology, in sheet metal bending,

K factor

is a multiplier used to determine where the neutral axis lies within the bend. That value is determined by both material type and forming method: air forming, bottom bending, and coining.

When a bend is made in sheet metal or plastic, the outside of the material structure expands while the inside compresses. All this occurs on a molecular level. You can see this in the "fogging" of some clear plastics on the outside surface.

There is also a theoretical area within the bend that is referred to as the

neutral axis

, where material does not expand or compress. When the material is flat, its neutral axis is at 50 percent of the thickness. During forming, this axis remains neutral—that is, it is neither expanding nor compressing—but it does move within the bend toward the inside surface of the material (see

Figure 1

).

Because the neutral axis does not change in length, its movement toward the inside surface causes the material toward the outside surface to elongate; that is, it appears to grow or get larger. The movement of the neutral axis is an integral part of determining the total amount of elongation a bend will have.

If you refer to

Machinery’s Handbook

, you will find that the K factor, or multiplier value, ranges from 0.40 to 0.50 for mild cold-rolled steel with 60,000-PSI tensile strength, depending on the forming method, with 0.446 being the average default value (see

Figure 2

).

For example, if you took a piece of 0.060-in.-thick material and multiplied it by the K factor of 0.446, you would find that the neutral axis has moved from 0.030 to 0.02676. This means that the neutral axis has moved only 0.00324 in. closer to the inside surface. That does not seem like much, but it is enough to cause the material to elongate. This is why the flat blank is always smaller than the sum total of the outside dimensions.

A Review of the Basic Formulas

I believe that the K factor you refer to is actually a

bend deduction (BD)

, or the total elongation for each bend in a part. To find the BD, you first need to find the bend allowance (BA), or the distance around the bend radius. The K factor is applied within the BA formula, which reads:

BA = [(0.017453 × Inside radius) (0.0078 × Material thickness)] × Degrees of bend angle complementary, on the outside of the bend

Figure 3

To calculate the bend deduction (BD), double the outside setback (OSSB) and subtract the bend allowance (BA).

The value 0.017453 is simply pi over 180, and the 0.0078 is pi over 180 times the K factor. The second part of calculating the BD is the outside setback (OSSB), as defined in

Figure 3

. You calculate it as follows:

OSSB = [Tangent (Degree of bend angle/2)] × (Inside bend radius Material thickness)

You calculate the BD by doubling the OSSB and subtracting the BA from that value:

BD = (OSSB × 2) – BA

This gives you the elongation value, or the amount of material that needs to be removed for each bend from the sum total of the outside dimensions. (For more on this, see "The basics of applying bend functions," archived at

thefabricator.com

.)

Regarding your question, you can see how variations in both material thickness and the bend’s inside radius affect the final results. The larger the radius, the greater the amount of elongation.

Your radius is being produced as a percentage of the die width, as determined by the 20 percent rule. Note that "20 percent" is only a title; the actual percentage is based on material type and tensile strength. For example, for cold-rolled steel, that percentage is between 15 and 17 percent of the die width.

Because the neutral axis does not change in length, its movement toward the inside surface causes the material toward the outside surface to elongate.

Not knowing for sure what the punch radius is or the die width, it is safe to say that the smaller the inside radius, the smaller the BD.

Regardless, checking the radius is easy; just use your basic radius gauge set or gauge pins. If you match the radius to the calculated values, and measure only after the springback has settled out, it should work perfectly.

Thinning Material on the Bend Line

The material thinning that you cite at the point of the bend would affect the final results as well. I have used this trick of thinning the material at the bend line in extremely thin parts that have been produced using a Chen or photo-etch process. In sheet metal work, this is called a

half-etch line

, and it’s used to establish the bend line and direction of forming.

Anytime the material thickness changes, so will the BD. The elongation will be different just by changing the material thickness in the thinned area from 0.078 to 0.063 in., and the radius will be slightly different as well. The BD will also change based on the width of the thinned area.

Back to Forming Basics

While forming plastics is not my specialty, I hope I have shed a little light on your question. Your question did present me with a vehicle to elaborate on the topics of radius, BD, and a few unique practices involved in forming sheet metal.

Steve Benson is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC, Salem, Ore.,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmanet.org/training

, or call 888-394-4362. For more information on bending, check out Benson’s book,

The Art of Press Brake: the Digital Handbook for Precision Sheet Metal Fabrication

, © 2014, available at

www.theartofpressbrake.com

.
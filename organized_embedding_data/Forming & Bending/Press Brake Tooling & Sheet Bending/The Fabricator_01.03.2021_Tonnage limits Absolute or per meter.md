# Tonnage limits: Absolute or per meter?

[TARİH: 01.03.2021 The Fabricator]

Expertise » Bending Basics

Terminology matters, especially when safety is at stake

By

Steve Benson

Read more from Steve Benson at

www.thefabricator.com/author/steve-benson

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators & Manufacturers Association International

®

. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book,

Bending Basics

, is now available at the FMA bookstore,

www.fmamfg.org/store

.

Question:

I was designing a new tool and needed to calculate its strength. The toolset included a very deep gooseneck to accommodate a deep return flange (see

Figure 1

).

I referred to your previous column, "The 4 pillars of press brake tonnage limits" (archived on

thefabricator.com

), in which you explain how to estimate tool strength. I’m encountering a discrepancy when I calculate for a gooseneck punch’s full length (3,100 mm) and the tonnage limit per meter (1,000 mm).

I used the punch illustration from that column (see

Figure 2

)

and the associated formula for calculating the punch’s load limits:

P = Punch’s resistance to pressure, in tons per square meter

l = Distance from tool nose to the tangent point between the neck and the inside radius of the tool, in millimeters

T = Width of the tool neck at the tangent point, in millimeters

b = Tool length in millimeters

(Editor’s note: If you wish to apply this formula, please first refer back to "The 4 pillars of press brake tonnage" on

thefabricator.com

for more information.)

For the tool I was designing, T was 33.6 mm and l was 295.1 mm. For length (b in the formula), when I calculated the load over the tool’s full length (3,100 mm) as well as per meter (1,000 mm), the results were quite different. When I calculate with 3,100 mm, I get 281 tons, which I divide by 3.1 to get 90.66 per meter. When I use 1,000 mm, I get 150 tons per meter. Have I applied these formulas incorrectly?

Answer:

Considering you’re designing a very deep gooseneck punch, I understand why you are concerned about the tonnage required and the total tonnage load of the tool.

To answer your question, the first thing that jumps out at me is the discrepancy in your units of measure. And no, my American readers, I am not talking about the metric system here. I’m referring to the difference between

absolute tonnage and tonnage per meter or tonnage per foot.

FIGURE 1

These very deep gooseneck punches, designed to accommodate deep return flanges, exemplify why knowing the required forming tonnage for a job, as well as the tonnage limits of your tools, is so important. The deeper the gooseneck, the weaker the tool becomes.

FIGURE 2

If a punch has no specified tonnage limit from the manufacturer, you can estimate it with a formula that incorporates the dimensions specified by l, b, and T.

I will refer you back to the column you cited. In that article, I start with the following statement: "Like many aspects of the sheet metal trade, the terms can be confusing, how they are applied can be confusing, and the worst part, not understanding how tonnage is calculated and applied can lead to some disastrous consequences."

We all need to be fluent in the terminology. This is especially true when it comes to press brake tooling load limits. Miscalculations can create extreme dangers for the crasperson, not to mention the added costs of replacing the tool or damage to the press brake itself. Whether you are designing tooling or using the tooling at the press brake, keep safety in mind.

When you push a press brake tool past its tonnage or force limit, bad things will happen. You can bend or destroy the punch, damage the press brake by upsetting the ram (exceeding the centerline load limit), and maybe even destroy the die. Vintage precision-ground tools have been known to throw shrapnel when overloaded. They can explode and sometimes hurl pieces a very long way.

So, what are you calculating, absolute tonnage or tonnage per meter? How do you know what to calculate? That, my friends, all depends on what you need to know. For the tool designer, it is absolute tonnage. For job shop engineering departments or technicians at the press brake, it is the tonnage per meter or foot that matters.

In your case, as a tool designer, you need to calculate the absolute tonnage limit. The equation asks for "length of the tool." So the answer we can assume is an "absolute tonnage" value and not a "tons per meter" value. You’re not calculating the amount of tonnage per meter a specific job requires (the forming tonnage), but how much tonnage, in absolute terms, your punch can withstand.

When you input a tool length (b in the formula) of 3,100 mm, your result shows an estimate of the absolute tonnage limit your 3,100-mm-long tool can withstand. Similarly, when you input a length of 1,000 mm, your result shows not the tonnage limit per meter, but what your absolute tonnage limit would be if the tool were only 1,000 mm long.

Press brake technicians calculate the tons per inch (or foot or meter) that a specific job requires. They then multiply the result by the bend length to get the job’s forming tonnage, which should never exceed (and, ideally, should be well below) the absolute tonnage limit of the tools and the machine.

Forming tonnage is calculated based on air forming 60,000-PSI-tensile mild cold-rolled steel. When you change the material type, you have a different tensile strength, and you change the force required to make the bend. This means you will have to factor the tonnage load based on the material type.

A 120,000-PSI stainless material is twice as strong as 60,000-PSI mild steel, so you’d need to multiply your result by 2. A 30,000-PSI aluminum is half as strong as 60,000-PSI mild steel, so you’d multiply your forming tonnage result by 0.5. Also know that material strength values vary, which is why tonnage calculations are only estimates. For this reason you should never push your tools or machines close to their tonnage limits. (For specific forming tonnage formulas, you can refer to "The 4 pillars of press brake tonnage" archived on

thefabricator.com

.)

These materials and other forming factors illustrate another key concept: The absolute tonnage does not factor in material thickness, tensile strength, or even the die opening—all factors that change the amount of force required to bend (forming tonnage), which, again, cannot exceed the absolute tool pressure rating (or absolute tonnage).

Safety and Forming Methods

Be sure to consider the part length and the gooseneck punch’s profile depth. Note that the formula in your question addresses the gooseneck profile depth

only indirectly

. As I noted in my previous column, the comprehensive formulas tool designers use get pretty deep into the weeds, incorporating material type, heat treatments, yield point coefficients, and other factors. The formula I presented is intended for press brake technicians who use tools that don’t have documented load limits specified by the tool manufacturer. It simply gives a quick estimate of a punch’s ability to withstand a load.

Regardless, in any situation you need to take the time to consider the method of forming and how you intend the punch to be used. Are you coining, bottom bending, or air bending (air forming)? You also need to consider part length and the gooseneck punch’s profile depth.

Considering the deep gooseneck profile you’re designing, your only option is probably air bending. Air forming requires the least amount of force to bend the material, and the tonnage requirement is calculated at the point the yield is broken in the material. If you were to try bottoming or coining with your punch profile, odds are you would "spring" the punch (bend it), perhaps even break it. Bottom bending takes five times the tonnage of air forming, while coining can take 10 times as much force. (Note that calculating bottoming and coining pressures are, at best, just educated guesses.)

Die Opening and Tonnage

Because you need to air form, which keeps the forming tonnage low, the die opening becomes an important player. As I am sure you already know, the wider the die opening, the lower the bend’s tonnage requirement. Of course, because you’re air bending, the wider you make your die, the greater the part’s inside bend radius becomes. This changes your bend allowance, setbacks, and bend deduction.

Consider reviewing the print to determine the largest inside bend radius allowed by the print tolerance, then pick your die opening (width) based on the 20% rule. Per this rule, stainless steel forms at about 20% of the die opening (which is where the name comes from), while 60-KSI mild steel—our baseline material—air forms a radius that’s about 16% of the die opening. A 120-KSI material is twice the strength of 60-KSI mild steel, so you’d multiply 16% by 2 and find that your radius will be about 32% of your die opening.

To reduce forming tonnage, use the largest floated radius the customer will allow. Calculate your inside bend radius and bend functions for air forming in the largest possible die opening.

If the customer specifies a tight inside radius, it might be worth your time to discuss with them the possibility of using a larger radius. Using a larger radius will help you make better, more consistent parts while at the same time add life to your tool and press brake.

Use a punch nose radius equal to or just slightly smaller than the naturally floated inside radius of an air-formed bend. If the customer insists on a sharp bend with a small inside bend radius, when you can, avoid using a punch nose radius that’s less than the calculated sharp-bend value—that is, the point at which the bend becomes "sharp." A bend turns sharp when a narrow punch nose radius forms a crease at the bend, causing it to be far less stable and predictable (For more on this, search for "How to avoid a sharp bend" on

thefabricator.com

.)

For the best results and most consistent bend angles and dimensions in air bending, try using tooling that creates a one-to-one relationship between the floated inside bend radius and the material thickness—a "perfect" bend radius.

Consider a Single-stroke, Two-bend Tool

If you need to form a deep return flange, and you can create a setup with the necessary clearance, you might consider making both bends at once with a single-stroke, two-bend tool that forms both inside flanges simultaneously.

True, the forming tonnage would be more significant, considering you’d be forming two bends with every stroke. But a two-bend tool wouldn’t require the deep gooseneck shape, so you’d likely have a more robust toolset with a higher absolute tonnage limit.

Do the Due Diligence

Challenging parts require a good understanding of the terminology and how to apply it. This includes what to calculate for, such as "absolute" or "per meter." Whatever route you take—involving a deep gooseneck punch, a two-bend tool, or anything else—you need to perform a tremendous amount of due diligence to make sure that your calculated values are correct.

THERE’S ONLY ONE…

HMD904 MAGNETIC DRILL

When it comes to mag drills, there are many choices but there is only one HMD904 The drill that has produced more holes and helped build & fabricate more than any other. The drill from which all others are judged. And now… It just keeps getting better.

NEW Hidden Motor Cord

NEW Ergonomic Design

Safer Product

Less Maintenance

1-1/2″ Dia × 2″ Depth

Pilot Light

Wide Range of Accessories

100% Hougen Reliability

Now Includes Two Year Warranty!

Patent Pending

800-426-7818 SERVICE • INTEGRITY • RELIABILITY

HOUGEN.COM